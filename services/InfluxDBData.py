"""Module name

Copyright (c) 2021 Marion Meurant
All Rights Reserved.
Released under the MIT license

"""
import itertools
from datetime import datetime
from random import random

import json

from services.LocalMonitoring import LocalMonitoring

from influxdb_client import InfluxDBClient, Point, WritePrecision, client
from influxdb_client.client.write_api import SYNCHRONOUS


class InfluxDB:
    """
    class InfluxDB
    """
    def __init__(self, url, token):
        self.client = InfluxDBClient(url=url, token=token)

    def sendData(self, bucket, org, local_monitoring_obj):
        """

        :param bucket:
        :param org:
        :param local_monitoring_obj:
        """
        data = local_monitoring_obj.reloadData()
        for name_hardware in data:
            print("////////////////" + name_hardware + "//////////////////")
            if name_hardware == "Partition_disk":
                for i in data[name_hardware]:
                    self.formatData(bucket, org, name_hardware, i)
            else:
                hardware_dict = data[name_hardware]
                self.formatData(bucket, org, name_hardware, hardware_dict)

    def formatData(self, bucket, org, name_hardware, data):
        """

        :param bucket:
        :param org:
        :param name_hardware:
        :param data:
        """
        try:
            for field, value in data.items():
                print(field)
                print(value)
                write_api = self.client.write_api(write_options=SYNCHRONOUS)
                point = Point("data") \
                    .tag("hardware", name_hardware) \
                    .field(field, value) \
                    .time(datetime.utcnow(), WritePrecision.NS)
                write_api.write(bucket, org, point)
        except ImportError:
            print(ImportError)
