#! /usr/bin/env python

from __future__ import print_function

import os
import ConfigParser

DEFAULT_CONFIG_FILE = os.path.expanduser("~/.btsmarc")


class BTSMAInverter(object):
    def __init__(self, name, bdaddr):
        self.name = name
        self.bdaddr = bdaddr


def read_config(configfile=DEFAULT_CONFIG_FILE):
    config = ConfigParser.SafeConfigParser()
    config.read(configfile)

    invs = []

    for s in config.sections():
        addr = config.get(s, 'bluetooth')
        inv = BTSMAInverter(s, addr)
        invs.append(inv)

    return invs

if __name__ == '__main__':
    invs = read_config()
    for inv in invs:
        print("%s:" % inv.name)
        print("\tBluetooth address: %s" % inv.bdaddr)
