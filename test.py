import sys
import os
import argparse
import re
from time import time
import boto
from boto import ec2
from boto import rds
from boto import elasticache
from boto import route53
import six

from six.moves import configparser
from collections import defaultdict

ec2_default_ini_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'ec2.ini')

print ec2_default_ini_path
ec2_ini_path = os.path.expanduser(os.path.expandvars(os.environ.get('EC2_INI_PATH', ec2_default_ini_path)))
print ec2_ini_path
if six.PY3:
  config = configparser.ConfigParser()
  print 'Regular config'
else:
  config = configparser.SafeConfigParser()
  print 'Safe Config'

config.read(ec2_ini_path)
print   config.has_option('ec2', 'eucalyptus')

