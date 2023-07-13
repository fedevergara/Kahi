import yaml
from importlib import import_module
import pkgutil
from collections import OrderedDict
from pymongo import MongoClient
from time import time

class OrderedLoader(yaml.SafeLoader):
    def __init__(self, *args, **kwargs):
        super(OrderedLoader, self).__init__(*args, **kwargs)
        construct_dict_order = lambda self, data: OrderedDict(self.construct_pairs(data))
        self.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_dict_order)

class Kahi:
    def __init__(self,workflow_file,verbose=0):
        self.plugin_prefix = "kahi_"
        self.workflow_file = workflow_file
        self.workflow = None
        self.config = None
        self.plugins = {}

        self.client = None
        
        self.log_db = None
        self.log = None
        self.verbose = verbose

    def load_workflow(self):
        """
        Loads the workflow from file
        """
        with open(self.workflow_file,"r") as stream:
            data=yaml.load(stream,Loader=OrderedLoader)
            self.workflow=data["workflow"]
            self.config=data["config"]
            self.client = MongoClient(self.config["mongodb_url"])

    def load_plugins(self,verbose=0):
        """
        Loads all plugins available in the system
        """
        discovered_plugins = {
            name : import_module(name)
            for finder, name, ispkg
            in pkgutil.iter_modules()
            if name.startswith(self.plugin_prefix+"_")
        }
        self.discovered_plugins = discovered_plugins

    def retrieve_logs(self):
        """
        Retrieves the logs from the database
        """
        
        self.log_db = self.client[self.config["log_db"]]
        log = list(self.log_db[self.config["log_collection"]].find())
        if log:
            self.log=log
        
        if self.verbose>1:
            print("Log retrieved from database")
        if self.verbose>4:
            print(log)

    def run(self):
        if not self.workflow:
            self.load_workflow()
        if not self.log:
            self.retrieve_logs()

        #import modules
        for module_name in self.workflow.keys():
            if self.verbose>4:
                print("loading plugin: "+self.plugin_prefix+module_name)
            try:
                self.plugins[module_name]=import_module(
                    self.plugin_prefix+module_name+
                    "."+
                    self.plugin_prefix.capitalize()+module_name
                )
            except ModuleNotFoundError as e:
                if self.verbose>0 and self.verbose<5:
                    print(e)
                    print("Plugin {} not found.\nTry\n\tpip install {}".format(
                        module_name,
                        self.plugin_prefix+module_name
                    ))
                    return None
                if self.verbose>4:
                    raise

        #run workflow
        for module_name,params in self.workflow.items():
            if self.verbose>4:
                print("running plugin: "+self.plugin_prefix+module_name)

            plugin_class = getattr(
                self.plugins[module_name],self.plugin_prefix.capitalize()+module_name
            )
                
            plugin_instance = plugin_class(
                config=self.config
            )

            run = getattr(plugin_instance,"run")
            try:
                time_start = time()
                status=run()
                time_elapsed = time()-time_start

                if self.log_db[self.config["log_collection"]].find_one({"id":module_name}):
                    self.log_db[self.config["log_collection"]].update_one(
                        {
                            "id":module_name
                        },
                        {"$set":
                            {
                                "time":int(time_start),
                                "status":0,
                                "message":"",
                                "time_elapsed":int(time_elapsed)
                            }
                        }
                    )
                else:
                    self.log_db[self.config["log_collection"]].insert_one(
                        {
                            "id":module_name,
                            "time":int(time_start),
                            "status":0,
                            "message":"",
                            "time_elapsed":int(time_elapsed)
                        }
                    )
            except Exception as e:
                if self.log_db[self.config["log_collection"]].find_one({"id":module_name}):
                    self.log_db[self.config["log_collection"]].update_one(
                        {
                            "id":module_name
                        },
                        {"$set":
                            {
                                "time":int(time()),
                                "status":1,
                                "message":e,
                                "time_elapsed":0
                            }
                        }
                    )
                else:
                    self.log_db[self.config["log_collection"]].insert_one(
                        {
                            "id":module_name,
                            "time":int(time()),
                            "status":1,
                            "message":e,
                            "time_elapsed":0
                        }
                    )
                raise

        #exit status
                


