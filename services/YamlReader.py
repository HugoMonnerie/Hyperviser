import yaml


class YamlReader:
    def __init__(self, path):
        self.yaml_path = path
        self.yaml_data = self.readerYaml(path)

    def readerYaml(self, path):
        data = None
        try:
            with open(path) as f:
                data = yaml.load(f, Loader=yaml.FullLoader)
        except ImportError:
            print(ImportError)
        return data
