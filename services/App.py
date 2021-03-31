
from services.LocalMonitoring import LocalMonitoring

from services.CronJobs import CronJobs
from services.YamlReader import YamlReader

CONFIG_FILE_PATH = "configuration/conf.yaml"
CONFIG_TIME_EXECUTION_NAME = "time_execution_reload_data"


class App:
    def __init__(self):
        self.local_monitoring = LocalMonitoring()
        self.cron_jobs = CronJobs()

    def start(self):
        config_data = YamlReader(CONFIG_FILE_PATH).yaml_data
        if not config_data:
            self.cron_jobs.dataJob(5, LocalMonitoring().reloadData)
        else:
            self.cron_jobs.dataCronJob(
                config_data[CONFIG_TIME_EXECUTION_NAME], LocalMonitoring().reloadData)
