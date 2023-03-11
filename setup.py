#!/usr/bin/env python3

import json
import sys
import collections
from pathlib import Path

# CONFIG STRUCTURE
config = collections.OrderedDict([
    ('log', collections.OrderedDict()),
    ('outbounds', [collections.OrderedDict()]),
    ('inbounds', []),
])

# CONFIG DEFAULTS
config['log']['loglevel'] = 'warning'
config['log']['access'] = '/var/log/v2ray/access.log'
config['log']['error'] = '/var/log/v2ray/error.log'
config['outbounds'][0]['protocol'] = 'freedom'
config['outbounds'][0]['tag'] = 'freedom'

# INPUT: NUMBER OF UPSTREAM SERVERS
count = int(input("Enter number of upstream servers: "))
if count == 0:
    sys.exit("You must have at least one server.")

for i in range(count):
    IP = input(f"Enter server #{i + 1} IP address: ")
    Port = int(input(f"Enter server #{i + 1} port number: "))
    if Port < 1 or Port > 65535:
        sys.exit("Port number must be between 1 and 65535.")
    config['inbounds'].append(collections.OrderedDict([
        ('listen', '0.0.0.0'),
        ('protocol', 'dokodemo-door'),
        ('port', Port),
        ('settings', collections.OrderedDict([
            ('address', IP),
            ('port', Port),
            ('network', 'tcp,udp'),
        ])),
    ]))

# SAVE CONFIG FILE
basePath = Path(__file__).parent
configPath = str(basePath.joinpath('config/config.json'))
configContent = json.dumps(config, indent=2)
open(configPath, 'w', encoding='utf-8').write(configContent)

# PRINT OUT RESULT

print(f"Done! Saved in {configPath}.\n")
