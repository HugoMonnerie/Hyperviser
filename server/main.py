"""Main script server

Copyright (c) 2021 Marion Meurant, Francesco Hart, Hugo Monnerie
All Rights Reserved.
Released under the MIT license

"""

from flask import Flask
import psutil
from flask import jsonify

app = Flask(__name__)


@app.route('/sensors')
def fetchSensors():
    """
    fetch sensors
    :return: json
    """
    return jsonify({
        'sensors_temperatures': psutil.sensors_temperatures(),
        'sensors_fans': psutil.sensors_fans(),
        'sensors_battery_percent': psutil.sensors_battery().percent,
        'sensors_battery_secsleft': psutil.sensors_battery().secsleft,
        'sensors_battery_power_plugged': psutil.sensors_battery().power_plugged
    })


@app.route('/network')
def fetchNetwork():
    """
    fetch network
    :return: type json
    """
    return {'net_io_counters_bytes_sent': psutil.net_io_counters().bytes_sent,
            'net_io_counters_bytes_recv': psutil.net_io_counters().bytes_recv,
            'net_io_counters_packets_sent': psutil.net_io_counters().packets_sent,
            'net_io_counters_packets_recv': psutil.net_io_counters().packets_recv,
            'net_io_counters_errin': psutil.net_io_counters().errin,
            'net_io_counters_errout': psutil.net_io_counters().errout,
            'net_io_counters_dropin': psutil.net_io_counters().dropin,
            'net_io_counters_dropout': psutil.net_io_counters().dropout
            }


@app.route('/other_disk_info')
def fetchOtherDiskInfo():
    """
    fetch other disk info
    :return: type json
    """
    return {'disk_usage_total': psutil.disk_usage('/').total,
            'disk_usage_used': psutil.disk_usage('/').used,
            'disk_usage_free': psutil.disk_usage('/').free,
            'disk_usage_percent': psutil.disk_usage('/').percent,
            'disk_io_counters_read_count': psutil.disk_io_counters().read_count,
            'disk_io_counters_write_count': psutil.disk_io_counters().write_count,
            'disk_io_counters_read_bytes': psutil.disk_io_counters().read_bytes,
            'disk_io_counters_write_bytes': psutil.disk_io_counters().write_bytes
            }


@app.route('/partition_disk')
def fetchPartitionDisk():
    """
    fetch partition disk
    :return: type json
    """
    return jsonify([{'disk_partitions_device': i.device,
                   'disk_partitions_mountpoint': i.mountpoint,
                     'disk_partitions_fstype': i.fstype,
                     'disk_partitions_opts': i.opts,
                     'disk_partitions_maxfile': i.maxfile,
                     'disk_partitions_maxpath': i.maxpath}
                    for i in psutil.disk_partitions()])


@app.route('/cpu')
def fetchCpu():
    """
    fetch CPU info
    :return: type json
    """
    return {'cpu_times_user': psutil.cpu_times().user,
            'cpu_times_system': psutil.cpu_times().system,
            'cpu_times_idle': psutil.cpu_times().idle,
            'cpu_percent': psutil.cpu_percent(),
            'cpu_times_percent': psutil.cpu_times_percent(),
            'cpu_stats_ctx_switches': psutil.cpu_stats().ctx_switches,
            'cpu_stats_interrupts': psutil.cpu_stats().interrupts,
            'cpu_stats_soft_interrupts': psutil.cpu_stats().soft_interrupts,
            'cpu_stats_syscalls': psutil.cpu_stats().syscalls,
            'getloadavg': psutil.getloadavg()
            }


@app.route('/ram')
def fetchRam():
    """
    fetch ram info
    :return: type json
    """
    return {'virtual_memory_total': psutil.virtual_memory().total,
            'virtual_memory_available': psutil.virtual_memory().available,
            'swap_memory_total': psutil.swap_memory().total,
            'swap_memory_used': psutil.swap_memory().used,
            'swap_memory_free': psutil.swap_memory().free,
            'swap_memory_percent': psutil.swap_memory().percent,
            'swap_memory_sin': psutil.swap_memory().sin,
            'swap_memory_sout': psutil.swap_memory().sout,
            }


@app.route('/')
def fetchAllData():
    """
    fetch all data
    :return: type json
    """
    return jsonify({'CPU': {'cpu_times_user': psutil.cpu_times().user,
                            'cpu_times_system': psutil.cpu_times().system,
                            'cpu_times_idle': psutil.cpu_times().idle,
                            'cpu_percent': psutil.cpu_percent(),
                            'cpu_times_percent': psutil.cpu_times_percent(),
                            'cpu_stats_ctx_switches': psutil.cpu_stats().ctx_switches,
                            'cpu_stats_interrupts': psutil.cpu_stats().interrupts,
                            'cpu_stats_soft_interrupts': psutil.cpu_stats().soft_interrupts,
                            'cpu_stats_syscalls': psutil.cpu_stats().syscalls,
                            'getloadavg': psutil.getloadavg()
                            },
                    'RAM': {'virtual_memory_total': psutil.virtual_memory().total,
                            'virtual_memory_available': psutil.virtual_memory().available,
                            'swap_memory_total': psutil.swap_memory().total,
                            'swap_memory_used': psutil.swap_memory().used,
                            'swap_memory_free': psutil.swap_memory().free,
                            'swap_memory_percent': psutil.swap_memory().percent,
                            'swap_memory_sin': psutil.swap_memory().sin,
                            'swap_memory_sout': psutil.swap_memory().sout,
                            },
                    'Partition_disk': [{'disk_partitions_device': i.device,
                                        'disk_partitions_mountpoint': i.mountpoint,
                                        'disk_partitions_fstype': i.fstype,
                                        'disk_partitions_opts': i.opts,
                                        'disk_partitions_maxfile': i.maxfile,
                                        'disk_partitions_maxpath': i.maxpath}
                                       for i in psutil.disk_partitions()],
                    'Other_disk_info': {'disk_usage_total': psutil.disk_usage('/').total,
                                        'disk_usage_used': psutil.disk_usage('/').used,
                                        'disk_usage_free': psutil.disk_usage('/').free,
                                        'disk_usage_percent': psutil.disk_usage('/').percent,
                                        'disk_io_counters_read_count': psutil.disk_io_counters().read_count,
                                        'disk_io_counters_write_count': psutil.disk_io_counters().write_count,
                                        'disk_io_counters_read_bytes': psutil.disk_io_counters().read_bytes,
                                        'disk_io_counters_write_bytes': psutil.disk_io_counters().write_bytes
                                        },
                    'Network': {'net_io_counters_bytes_sent': psutil.net_io_counters().bytes_sent,
                                'net_io_counters_bytes_recv': psutil.net_io_counters().bytes_recv,
                                'net_io_counters_packets_sent': psutil.net_io_counters().packets_sent,
                                'net_io_counters_packets_recv': psutil.net_io_counters().packets_recv,
                                'net_io_counters_errin': psutil.net_io_counters().errin,
                                'net_io_counters_errout': psutil.net_io_counters().errout,
                                'net_io_counters_dropin': psutil.net_io_counters().dropin,
                                'net_io_counters_dropout': psutil.net_io_counters().dropout
                                },
                    'Sensors': {
        'sensors_temperatures': psutil.sensors_temperatures(),
        'sensors_fans': psutil.sensors_fans(),
        'sensors_battery_percent': psutil.sensors_battery().percent,
        'sensors_battery_secsleft': psutil.sensors_battery().secsleft,
        'sensors_battery_power_plugged': psutil.sensors_battery().power_plugged
    }})
