from datetime import datetime
import os
from apscheduler.schedulers.background import BackgroundScheduler


class CronJobs:

    def __init__(self):
        self.scheduler = BackgroundScheduler()

    def addJobs(self, time_in_seconds, job_to_execut):
        self.scheduler.add_job(job_to_execut,
                               'interval', seconds=time_in_seconds)

    def addJobsWithArgs(self, time_in_seconds, job_to_execut, job_args, executor_name):

        self.scheduler.add_job(job_to_execut,
                               'interval', seconds=time_in_seconds, args=job_args)

    def startJobs(self):
        try:
            self.scheduler.start()
        except (KeyboardInterrupt, SystemExit):
            pass
