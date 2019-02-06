#!/usr/bin/env bash

cat ../data/venues.txt |
  sed 1d | sed -e 's/\s*|/|/g' | sed -e 's/|\s*/|/g' | # Remove whitespace and header
    awk -F '|' '{printf "%s\n", $2}' |
      uniq | python coordinates.py
