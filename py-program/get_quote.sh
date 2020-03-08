#!/bin/bash
# $1: CONID
# AAPL: 209011562
# ./get_quote 209011562

[[ -z $1 ]] && echo No conid && exit 1
CONID=$1

URL="https://localhost:5000\
/v1/portal/iserver/marketdata/history\
?conid=$CONID\
&period=3d&bar=1d"
DATA=$(curl -sk -X GET $URL \
  -H 'Content-Type: application/x-www-form-urlencoded')
POINTS=$(jq '.' <<< $DATA)
echo $POINTS
