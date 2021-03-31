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


class App:
    def __init__(self):
        self.local_monitoring = LocalMonitoring()
        self.cron_jobs = CronJobs()
        self.influx_db_data = None

    def start(self):
        config_data = YamlReader(CONFIG_FILE_PATH).yaml_data
        self.influx_db_data = InfluxDB(config_data["influx_db"][CONFIG_INFLUXDB_URL],
                                       config_data["influx_db"][CONFIG_INFLUXDB_TOKEN])
        self.influx_db_data.send_data(config_data["influx_db"][CONFIG_INFLUXDB_BUCKET],
                                      config_data["influx_db"][CONFIG_INFLUXDB_ORG],
                                      self.local_monitoring.fetchMonitoringData())
        if not config_data:
            self.cron_jobs.dataJob(5, self.local_monitoring.reloadData)
        else:
            self.cron_jobs.dataCronJob(
                config_data[CONFIG_TIME_EXECUTION_NAME], self.local_monitoring.reloadData)
            self.cron_jobs.dataCronJob(
                config_data[CONFIG_TIME_EXECUTION_NAME], self.local_monitoring.reloadData)
            # self.cron_jobs.sendInfluxDBDataCronJob(5, self.influx_db_data.send_data(
            #     config_data["influx_db"][CONFIG_INFLUXDB_BUCKET],
            #     config_data["influx_db"][CONFIG_INFLUXDB_ORG],
            #     self.local_monitoring.fetchMonitoringData()))
        self.cron_jobs.startJobs()
