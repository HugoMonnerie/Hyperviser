"""App script

Copyright (c) 2021 Marion Meurant, Francesco Hart, Hugo Monnerie
All Rights Reserved.
Released under the MIT license

"""

from services.LocalMonitoring import LocalMonitoring

from services.CronJobs import CronJobs
from services.YamlReader import YamlReader
from services.InfluxDBData import InfluxDB

CONFIG_FILE_PATH = "configuration/conf.yaml"
CONFIG_TIME_EXECUTION_NAME = "time_execution_reload_data"
CONFIG_INFLUXDB_TOKEN = "token"
CONFIG_INFLUXDB_ORG = "org"
CONFIG_INFLUXDB_BUCKET = "bucket"
CONFIG_INFLUXDB_URL = "url"
CONFIG_INFLUXDB = "influx_db"


class App:
    """
    class App
    """
    def __init__(self):
        self.local_monitoring = LocalMonitoring()
        self.cron_jobs = CronJobs()
        self.influx_db_data = None

    def start(self):
        """
        start App
        """
        config_data = YamlReader(CONFIG_FILE_PATH).yaml_data

        if not config_data:
            self.cron_jobs.addJobs(5, self.local_monitoring.reloadData)
        else:
            self.influx_db_data = InfluxDB(
                config_data[CONFIG_INFLUXDB][CONFIG_INFLUXDB_URL], config_data[CONFIG_INFLUXDB][CONFIG_INFLUXDB_TOKEN])

            self.cron_jobs.addJobsWithArgs(
                config_data[CONFIG_TIME_EXECUTION_NAME], self.influx_db_data.sendData, [config_data[CONFIG_INFLUXDB][CONFIG_INFLUXDB_BUCKET], config_data[CONFIG_INFLUXDB][CONFIG_INFLUXDB_ORG], self.local_monitoring])

        self.cron_jobs.startJobs()
