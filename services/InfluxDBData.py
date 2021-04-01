"""Module name

Copyright (c) 2021 Marion Meurant
All Rights Reserved.
Released under the MIT license

"""
from random import random

import json

from services.LocalMonitoring import LocalMonitoring

from influxdb_client import InfluxDBClient, Point, WritePrecision, client
from influxdb_client.client.write_api import SYNCHRONOUS


class InfluxDB:
    def __init__(self, url, token):
        self.client = InfluxDBClient(url=url, token=token)

    def sendData(self, bucket, org, local_monitoring_obj):
        write_api = self.client.write_api(write_options=SYNCHRONOUS)

        dataa = "mem,host=host1 used_percent=60"
        data = local_monitoring_obj.reloadData()
        dataaa = json.dumps(data)
        print(dataaa, "iciiiiiiiiiiiiiiiiiiiiii \n")
        # write_api.write(bucket, org, dataaa['CPU'])
        write_api.write(bucket, org,
                        Point("CPU").field("CPU", dataaa))
        write_api.write(bucket, org,
                        Point("RAM").field("RAM", dataaa))
        write_api.write(bucket, org,
                        Point("Partition_disk").field("Partition_disk", dataaa))
        write_api.write(bucket, org,
                        Point("Other_disk_info").field("Other_disk_info", dataaa))
        write_api.write(bucket, org,
                        Point("Network").field("Network", dataaa))
        write_api.write(bucket, org,
                        Point("Sensors").field("Sensors", dataaa))


    # def formatDataCpu(self, data):
    #     data_formatted = "mem,host=host1"
    #     for elem in data["CPU"]:
    #         data_formatted = data_formatted + elem + \
    #             ": " + str(data["CPU"][elem])+", "
    #     print(data_formatted)
    #     return data["CPU"]
