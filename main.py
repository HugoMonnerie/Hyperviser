"""Main script

Copyright (c) 2021 Hugo Monnerie
All Rights Reserved.
Released under the MIT license

"""

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from services.App import App
import sys
import os
from services.RabbitMq import RabbitMq


def main():
    rabbit_mq = RabbitMq()
    App().start()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
