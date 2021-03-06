#!/usr/bin/env python3
# Download contracts
# TODO: Make this about re-downloading contracts, as already getting
# in download-conids
# run time: 3m47s

# Local
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../'))
from lib.company import Company
from lib.filters import get_contracts_cheaper_than
from lib.util import get_symbols

# Main
try:
  print('Get symbols')
  symbols = get_symbols()
except Exception as e:
  print('ERROR: Could not get symbols:', e)
  exit(1)

try:
  print('Get contracts')
  for symbol in symbols:
    c = Company(symbol)
except Exception as e:
  print('ERROR: Could not get contracts:', e)
  exit(1)
