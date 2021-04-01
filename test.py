import pika
import json


"""Main script

Copyright (c) 2021 Hugo Monnerie
All Rights Reserved.
Released under the MIT license

"""

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from services.YamlReader import YamlReader
import sys
import os
from services.InfluxDBData import InfluxDB

CONFIG_FILE_PATH = "configuration/conf.yaml"
CONFIG_TIME_EXECUTION_NAME = "time_execution_reload_data"
CONFIG_INFLUXDB_TOKEN = "token"
CONFIG_INFLUXDB_ORG = "org"
CONFIG_INFLUXDB_BUCKET = "bucket"
CONFIG_INFLUXDB_URL = "url"
CONFIG_INFLUXDB = "influx_db"


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    config_data = YamlReader(CONFIG_FILE_PATH).yaml_data
    influx_db_data = InfluxDB(
        config_data[CONFIG_INFLUXDB][CONFIG_INFLUXDB_URL], config_data[CONFIG_INFLUXDB][CONFIG_INFLUXDB_TOKEN], config_data[CONFIG_INFLUXDB][CONFIG_INFLUXDB_BUCKET], config_data[CONFIG_INFLUXDB][CONFIG_INFLUXDB_ORG],)

    influx_db_data.fetchData(channel)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
