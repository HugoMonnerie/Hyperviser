"""Yaml reader script

Copyright (c) 2021 Marion Meurant, Francesco Hart, Hugo Monnerie
All Rights Reserved.
Released under the MIT license

"""

import yaml


class YamlReader:
    """
    class Yaml reader
    """
    def __init__(self, path):
        self.yaml_path = path
        self.yaml_data = self.readerYaml(path)

    def readerYaml(self, path):
        """
        read yaml
        :param path: path's yaml
        :return: data
        """
        data = None
        try:
            with open(path) as f:
                data = yaml.load(f, Loader=yaml.FullLoader)
        except ImportError:
            print(ImportError)
        return data
