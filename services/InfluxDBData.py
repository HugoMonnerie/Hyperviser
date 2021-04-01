"""Module name

Copyright (c) 2021 Marion Meurant
All Rights Reserved.
Released under the MIT license

"""
from random import random

from services.LocalMonitoring import LocalMonitoring

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS


class InfluxDB:
    def __init__(self, url, token):
        self.client = InfluxDBClient(url=url, token=token)

    def sendData(self, bucket, org, local_monitoring_obj):
        write_api = self.client.write_api(write_options=SYNCHRONOUS)

        dataa = "mem,host=host1 used_percent=60"
        data = self.formatDataCpu(local_monitoring_obj.reloadData())
        print(local_monitoring_obj.reloadData()[
              "CPU"], "iciiiiiiiiiiiiiiiiiiiiii \n")
        write_api.write(
            bucket, org, [{"fields": data["CPU"]}])

    def formatDataCpu(self, data):
        data_formatted = "mem,host=host1"
        for elem in data["CPU"]:
            data_formatted = data_formatted + elem + \
                ": " + str(data["CPU"][elem])+", "
        print(data_formatted)
        return data["CPU"]