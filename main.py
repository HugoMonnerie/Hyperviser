"""Main script

Copyright (c) 2021 Hugo Monnerie
All Rights Reserved.
Released under the MIT license

"""

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from localMonitoring import LocalMonitoring

def main():
    LocalMonitoring().printData()
    LocalMonitoring().reloadData()

if __name__ == '__main__':
    main()
