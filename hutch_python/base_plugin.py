class Plugin:
    """
    Interface for each top-level entry in the conf.yaml file.
    """
    # Plugins with high priority numbers will be created first.
    # Plugins with equal priority numbers will be created in sequence.
    priority = 0

    def __init__(self, info):
        """
        Parameters
        ----------
        info: str, list, or dict
            The full entry from the yaml file, not including the top-level
            dictionary key.
        """
        self.info = info

    def get_objects(self):
        """
        Build the Python objects specified by the plugin and config.

        Returns
        -------
        objects: dict{str: object}
            Mapping from final global reference name to object
        """
        pass

    def future_object_hook(self, name, obj):
        """
        This method will be called on every object that is created afterwards
        by other plugins. Please do not mutate the incoming objects.

        Parameters
        ----------
        name: str
            Global reference name
        obj: object
            Any object
        """
        pass

    def future_plugin_hook(self, source, objs):
        """
        Provided to be overridden if the plugin needs to treat the incoming
        objects as a group.

        Parameters
        ----------
        source: str
            Top-level yaml config string that built the objs
        objs: dict{str: object}
            The return value from a previous plugin's get_objects call
        """
        for key, value in objs.items():
            self.future_object_hook(key, value)
