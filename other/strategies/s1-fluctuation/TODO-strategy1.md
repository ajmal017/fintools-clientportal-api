new plan:
- use python


Exercises:
1 / get last 1 day data for ticker
2 / specify ticker, find conid
3 / save as json to file
4 / get last 1 day data for list of tickers
5 / get last 1 day data for list of tickers, save as json in dir, separate files
6 / get last 2 day data for given tickers, split them into 2 days, save as JSON to dirs
7 x function: given average, work out +/- %, for 1,2,3,4,5%
------
Two scripts:
- / download.py: download data (adapt from ex.6):
  - / get current date, create dir, put data there, into data dirs
- x analyse.py: analyse data

analyse.py:
- / input:
  - / data dir
  - / perc1 (for day 1)
  - / perc2 (for day 2)
- output:
  - / symbols count
  - / print input (percentages)
  - for first date:
    - / rework ohlc to averages (points): Take only H and L, get median, get average over each point
    - / F1: function: (average, perc1) -> +/- % values
    - / F2: function: data (ohlc), +/- % values -> count of fluctuation (use L/H values)
  - for second date:
    - F1: +/- % values with perc2
    - F2 count
  - split table into three tables:
    - match: day 1 match, day 2 match
    - fail: day 1 match, day 2 fail
    - other: day 1 fail, day 2 fail
  - table cols:
    - symbol
    - day 1 fluct count
    - day 2 fluct count
    - day 1 low fluct price
    - day 1 hi fluct price
    - day 2 low fluct price
    - day 2 hi fluct price
