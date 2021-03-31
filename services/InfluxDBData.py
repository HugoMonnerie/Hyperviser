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
        dataa = "mem,host=host1 used_percent=23.43234543"
        print(local_monitoring_obj.reloadData(), "iciiiiiiiiiiiiiiiiiiiiii \n")
        write_api.write(bucket, org, dataa)

    def formatData(self, bucket, org, local_monitoring_obj):
        write_api = self.client.write_api(write_options=SYNCHRONOUS)
        dataa = "mem,host=host1 used_percent=23.43234543"
        print(local_monitoring_obj.reloadData(), "iciiiiiiiiiiiiiiiiiiiiii \n")
        write_api.write(bucket, org, dataa)
