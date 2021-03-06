# OS
import json

# Local
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../'))
from lib.config import Config
from lib.company import Company


def get_symbols_cheaper_than(price):
  res = {}
  try:
    cfg = Config()
    dir_quote = cfg['paths']['quotes']
    symbols = os.listdir(dir_quote)
  except Exception as e:
    raise Exception('Could not read dir:', dir_quote)

  for s_file in os.listdir(dir_quote):
    # For each quote, find cheap ones
    try:
      symbol = s_file.split('.')[0]
      fname = dir_quote + '/' + s_file
      if os.stat(fname).st_size > 1:
        with open(fname) as f:
          price_found = json.load(f)['c']
          if float(price_found) <= float(price):
            res[symbol] = price_found
    except Exception as e:
      print('Unable to read %s' % s_file)
    for k, v in sorted(res.items()):
      # Sort by symbol
      res[k] = v
  return res

def get_contracts_cheaper_than(price, redownload=False):
  try:
    # Get cheap symbols
    # returns:
    # - price
    # - category
    # - industry
    symbols = get_symbols_cheaper_than(price)
  except Exception as e:
    raise Exception('Could not get cheap symbols:', e)

  res = {}
  for symbol, price in symbols.items():
    # Get contracts
    try:
      company = Company(symbol)
      contract = company.get_contract(redownload=redownload)
      res[symbol] = {
        'price': price,
        'category': contract['category'],
        'industry': contract['industry'],
      }
    except Exception as e:
      print('Could not get contract', symbol, ':', e)
  return res

def get_winners_lt_perc(price, perc_increase):
  # Winners price less than PRICE, increase higher than PERC
  # TODO: Finish this
  # Return: { symbol: { price, perc }, ... }
  out = {}
  try:
    # Get cheap symbols
    symbols = get_symbols_cheaper_than(price)
  except Exception as e:
    print('Could not get winners', price, ',', perc_increase, ':', e)
  # TODO: Get here the difference, perc, hi/lo
  # Wrong. Need to use the day data
  for symbol in symbols:
    company = Company(symbol)
    quote = company.get_quote_single()
    print('l', quote['l'])
    print('h', quote['h'])
    pass
  return symbols
