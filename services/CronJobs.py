"""Cron jobs script

Copyright (c) 2021 Marion Meurant, Francesco Hart, Hugo Monnerie
All Rights Reserved.
Released under the MIT license

"""

from apscheduler.schedulers.blocking import BlockingScheduler


class CronJobs:
    """
    class Cron Jobs
    """
    def __init__(self):
        self.scheduler = BlockingScheduler()
        self.scheduler.add_executor('processpool')

    def addJobs(self, time_in_seconds, job_to_execut):
        """
        add jobs
        :param time_in_seconds: time interval
        :param job_to_execut: execute the job
        """
        self.scheduler.add_job(job_to_execut,
                               'interval', seconds=time_in_seconds)

    def addJobsWithArgs(self, time_in_seconds, job_to_execut, job_args=None):
        """
        add jobs with arguments
        :param time_in_seconds: time interval
        :param job_to_execut: execute the job
        :param job_args: argument's job
        """
        self.scheduler.add_job(job_to_execut,
                               'interval', seconds=time_in_seconds, args=job_args)

    def startJobs(self):
        """
        start jobs
        """
        try:
            self.scheduler.start()
        except (KeyboardInterrupt, SystemExit):
            pass
