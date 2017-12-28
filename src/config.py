from configparser import ConfigParser


class config:

    def __init__(self):
        cfg_file = "config.ini"
        self.cfg_dict = {}
        self.cfg = ConfigParser()
        self.cfg.read(cfg_file)

    def generate(self):
        for section in self.cfg.sections():
            self.cfg_dict[section] = {}

            for (key,val) in self.cfg.items(section):
                self.cfg_dict[section][key] = val

        return self.cfg_dict
