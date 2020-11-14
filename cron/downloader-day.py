#!/usr/bin/env python3
# Download today's data for tickers under $1/share
# Optionally, supply list of tickers, e.g.
# ./$0 AAPL AMZN
# 6min25s with 100 workers, price 3
# 7min7s with 400 wokers, price 3
# Could not get symbol BURG only
import argparse
import concurrent.futures
import config
import glob
import ib_web_api
import json
import os
import pprint
import urllib3
import urllib.request
from lib.company import Company
from lib.icompany import ICompany
from ib_web_api import MarketDataApi

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
debug = False
count_total = 0
count_progress = 0
count_perc = 0

def get_quote(symbol):
  global count_total
  global count_progress
  global count_perc
  conid = Company(symbol).get_conid()
  company = ICompany(conid)
  try:
    quote = ICompany(conid).get_quote('1d', '1min')
    # Log progress
    count_progress += 1
    if (count_progress/count_total)*10 >= count_perc:
      print(str(count_perc*10) + '%')
      count_perc = count_perc + 1
  except Exception as e:
    raise Exception('Could not get symbol %s' % symbol)
  return { symbol: quote }

# Main
# Parse args
parser = argparse.ArgumentParser(description='Download today\'s data')
parser.add_argument('symbols',
  metavar='S',
  type=str,
  nargs='*',
  help='List of symbols, e.g. AAPL AMZN'
)
args = parser.parse_args()

# Get cheap symbols
with urllib.request.urlopen(config.url_cheap_symbols) as response:
  symbols = json.loads(response.read().decode('utf-8'))
  day_quotes = {}
  if debug is True:
    symbols = { key: symbols[key] for key in list(symbols)[0:5] }
  if args.symbols:
    symbols = args.symbols
  count_total = len(symbols)
  with concurrent.futures.ThreadPoolExecutor(max_workers=400) as executor:
    future_to_data = {
      executor.submit(get_quote, symbol): symbol
      for symbol in symbols
    }
    for future in concurrent.futures.as_completed(future_to_data):
      try:
        day_quotes.update(future.result())
      except Exception as e:
        # Failed to get conid, skip
        print('EXC: %s' % e)
        pass
  # Save to day dir
  print('Got %i quotes' % len(day_quotes))
  for f in glob.glob(config.dir_day + '/*.json'):
    os.remove(f)
  for symbol in day_quotes:
    f_path = config.dir_day + '/' + symbol + '.json'
    with open(f_path, 'w') as f:
      if day_quotes[symbol] is not None:
        f.write(json.dumps(day_quotes[symbol]))
      else:
        print(f'No data for {symbol}')
        os.remove(f_path)
