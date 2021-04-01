"""Module name

Copyright (c) 2021 Hugo Monnerie
All Rights Reserved.
Released under the MIT license

"""
import psutil


class LocalMonitoring:
    """
        class local monitoring
    """

    def __init__(self):
        self.monitoring_data = {'CPU': self.cpuInfo(
        ), 'RAM': self.ramInfo(), 'SpaceDisk': self.spaceDiskInfo()}

    def cpuInfo(self):
        """

        :return: CPU info
        """
        return {'user_mode': psutil.cpu_times().user,
                'kernel_mode': psutil.cpu_times().system,
                'nothing_mode': psutil.cpu_times().idle}

    def ramInfo(self):
        """

        :return: RAM info
        """
        return {'total': psutil.virtual_memory().total,
                'available': psutil.virtual_memory().available}

    def spaceDiskInfo(self):
        """

        :return: Space Disk info
        """
        return [{'device': i.device, 'mountpoint': i.mountpoint} for i in psutil.disk_partitions()]

    def printData(self):
        print(self.monitoring_data)

    def reloadData(self):
        """
        reload data
        """
        self.monitoring_data = self.fetchMonitoringData()
        return self.monitoring_data

    def fetchMonitoringData(self):
        """
        reload data
        """
        return {'CPU': self.cpuInfo(
        ), 'RAM': self.ramInfo(), 'SpaceDisk': self.spaceDiskInfo()}
