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
import sys
import os
import pika
import json
import time


class InfluxDB:
    """
    class InfluxDB
    """

    def __init__(self, url, token, bucket, org):
        self.client = InfluxDBClient(url=url, token=token)
        self.org = org
        self.bucket = bucket
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()

    def sendData(self,  fetchData):
        print("laaaaaaaaaaaa")
        """

        :param bucket:
        :param org:
        :param local_monitoring_obj:
        """
        try:
            time.sleep(2)
            self.channel.queue_declare(queue='hardware')
            data_to_send = json.dumps(fetchData)
            self.channel.basic_publish(exchange='',
                                       routing_key="hardware",
                                       body=data_to_send)
        except ImportError:
            pass

    def formatAndWriteData(self, name_hardware, data):
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
                write_api.write(self.bucket, self.org, point)
        except ImportError:
            print(ImportError)

    def callback(self, ch, method, properties, body):

        for name_hardware in body:
            print("////////////////" + name_hardware + "//////////////////")
            if name_hardware == "Partition_disk":
                for i in body[name_hardware]:
                    self.formatAndWriteData(
                        name_hardware, i)
            else:
                hardware_dict = body[name_hardware]
                self.formatAndWriteData(
                    name_hardware, hardware_dict)
        print(" [x] Received %r" % body)

    def fetchData(self, channel):
        channel.queue_declare(queue='hardware')

        try:
            channel.basic_consume(queue='hardware',
                                  auto_ack=True,
                                  on_message_callback=self.callback)
            print("I heard you")

            channel.start_consuming()
        except:
            pass
