#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import argparse
import json

import optimiz as optimiz

parser = argparse.ArgumentParser()
parser.add_argument('--debug', default=False)
parser.add_argument('--stocks', nargs='+')

args = vars(parser.parse_args())

debug = args['debug']

if args['stocks'] is not None:
  print(json.dumps(optimiz.optimiz(args['stocks'], debug), indent=2))
