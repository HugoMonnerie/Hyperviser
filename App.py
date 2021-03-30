
from LocalMonitoring import LocalMonitoring
from CronJobs import CronJobs


class App:
    def __init__(self):
        self.local_monitoring = LocalMonitoring()
        self.cron_jobs = CronJobs(5, self.local_monitoring)

    def start(self):
        self.cron_jobs.dataJob()
