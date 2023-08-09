
class KahiBase:
    def __init__(self):
        pass

    def empty_affiliation(self):
        entry = {
            "updated":[],
            "names":[],
            "aliases":[],
            "abbreviations":[],
            "types":[],
            "year_established":None,
            "status":[],
            "relations":[],
            "addresses":[],
            "external_urls":[],
            "external_ids":[],
            "subjects":[],
            "ranking":[],
            "description":[]
        }
        return entry

    def empty_source(self):
        return {
            "updated": [],
            "names": [],
            "abbreviations": [],
            "types": [],
            "keywords": [],
            "languages": [],
            "publisher": "",
            "relations": [],
            "addresses": [],
            "external_ids": [],
            "external_urls": [],
            "review_processes": [],
            "waiver": {},
            "plagiarism_detection": False,
            "open_access_start_year": None,
            "publication_time_weeks": None,
            "apc": {},
            "copyright": {},
            "licenses": [],
            "subjects": [],
            "ranking": []
        }

    def empty_subjects(self):
        return {
            "updated": [],
            "names": [],
            "abbreviations": [],
            "descriptions": [],
            "external_ids": [],
            "external_urls": [],
            "level": None,
            "relations": []
        }

    def run(self):
        """
        entry point for the execution of the plugin, this method must be implemented
        """
        raise NotImplementedError(
            self.__class__.__name__ + '.run() not implemented')
