
class KahiBase:
    def __init__(self):
        pass

    def run(self):
        """
        entry point for the execution of the plugin, this method must be implemented
        """
        raise NotImplementedError(
            self.__class__.__name__ + '.run() not implemented')
