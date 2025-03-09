import configparser
from configparser import ConfigParser
import os

# https://wiki.python.org/moin/ConfigParserExamples
# JSON viewer: https://jsonviewer.stack.hu/

class ConfigReader(ConfigParser):
    """ <sections_list> contains all sections and options in ini-file """
    def __init__(self, file_name):
        super().__init__()
        self.sections_list = []
        self.file_name = file_name
        self.read_config_file()


    def read_config_file(self):
        if self.check_if_file_exists():
            self.read(self.file_name)
            sections = self.sections()

            for section in sections:
                # option_dict_list = []
                option_dict = self.read_options(section)
                # option_dict_list.append(option_dict) # Puts the option_dict in a List

                dict = {
                    section: option_dict
                    # Alternative: section: option_dict_list
                }
                self.sections_list.append(dict)



    def check_if_file_exists(self):
        if os.path.isfile(self.file_name):
            return True
        else:
            # TODO: Create new file
            return False



    def read_options(self, section):
        options_dict = {}
        all_options = self.options(section)
        for option in all_options:
            try:
                options_dict[option] = self.get(section, option)
                if options_dict[option] == -1:
                    print("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                options_dict[option] = None
        # print("Options dict", options_dict)
        return options_dict





if __name__ == "__main__":
    c = ConfigReader("config.ini")
    print(c.sections_list[0]["Telegram"]["bot_token"] )
