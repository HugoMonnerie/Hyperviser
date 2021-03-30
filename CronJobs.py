from datetime import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler


class CronJobs:

    def __init__(self, time_in_seconds, local_monitoring):
        self.scheduler = BlockingScheduler()
        self.local_monitoring = local_monitoring
        self.time_in_seconds = time_in_seconds

    def dataJob(self):
        self.scheduler.add_executor('processpool')
        self.scheduler.add_job(self.local_monitoring.reloadData,
                               'interval', seconds=self.time_in_seconds)
        try:
            self.scheduler.start()
        except (KeyboardInterrupt, SystemExit):
            pass
