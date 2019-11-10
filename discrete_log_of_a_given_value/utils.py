# -*- coding: utf-8 -*-

import json
import sys


class Config:
    def __init__(self, config_path):
        self.config_path = config_path

    def get_json_data(self):
        try:
            with open(self.config_path) as f:
                data = json.load(f)
            return data
        except ValueError:
            print('В файле содержатся данные в неправильном формате.')
            sys.exit()

    def write_json_data(self, data):
        with open(self.config_path, 'w') as f:
            json.dump(data, f)

    def get_value(self, key):
        data = self.get_json_data()
        return data[key]

    def update_value(self, key, value):
        data = self.get_json_data()
        data[key] = value
        self.write_json_data(data)