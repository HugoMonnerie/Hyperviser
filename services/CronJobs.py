from datetime import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler


class CronJobs:

    def __init__(self):
        self.scheduler = BlockingScheduler()
        self.scheduler.add_executor('processpool')

    def dataCronJob(self, time_in_seconds, job_to_execut):
        self.scheduler.add_job(job_to_execut,
                               'interval', seconds=time_in_seconds)

    def sendInfluxDBDataCronJob(self, time_in_seconds, job_to_execut):
        self.scheduler.add_job(job_to_execut,
                               'interval', seconds=time_in_seconds)

    def startJobs(self):
        try:
            self.scheduler.start()
        except (KeyboardInterrupt, SystemExit):
            pass
