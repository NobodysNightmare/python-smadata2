#! /usr/bin/env python

import argparse

from nose.tools import *

import smadata2.sma2mon


def test_argparser():
    "Test that the function to generate the argparser doesn't crash"
    ap = smadata2.sma2mon.argparser()
    assert isinstance(ap, argparse.ArgumentParser)
