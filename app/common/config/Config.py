import yaml
import os

class YamlLoader:
    __name = "application.yml"
    __root = os.environ.get("config_root", ".")
    __path = os.environ.get("config_path", "/conf/")
    def __init__(self, file_name, file_path):
        if (file_name == None):
            file_name = self.__name

        if (file_path == None):
            file_path = f"{self.__root}{self.__path}"
            
        full_path = f"{file_path}{file_name}"
        
        with open(full_path, "r", encoding="utf8") as f:
            self.yaml = yaml.load(f, Loader=yaml.FullLoader)

class ServerConfig(YamlLoader):
    def __init__(self, file_name = None, file_path = None):
        super().__init__(file_name, file_path)
        self.__config = self.yaml["server"]
    def get_host(self):
        return self.__config["host"]
    def get_port(self):
        return self.__config["port"]
    def get_debug(self):
        return self.__config["debug"]