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
        self.org = InfluxDBClient(org=org)
        self.bucket = InfluxDBClient(bucket=bucket)
        self.data = InfluxDBClient(data=data)


    def send_data(self, bucket, org, data):
        write_api = self.client.write_api(write_options=SYNCHRONOUS)
        data = "mem,host=host1 used_percent=23.43234543"
        print("juyhtg")
        write_api.write(bucket, org, data)
