#!/usr/bin/env python

from lxml import etree
import sys

if __name__ == '__main__':
  (_, f, fout) = sys.argv
  p = etree.XMLParser(attribute_defaults=True, load_dtd=True)
  t = etree.parse(open(f), p)
  r = t.getroot()
  counts = {} # (author -> [years])
  for pub in r.getchildren():
    bt = pub.find('booktitle')
    if bt is None:
      continue
    yr = pub.find('year')
    if yr is None:
      continue
    if bt.text.find('SIGMOD') == -1:
      continue
    yr = int(yr.text.strip())
    authors = pub.findall('author')
    for a in authors:
      a = a.text.strip()
      if a in counts:
        counts[a].append(yr)
      else:
        counts[a] = [yr]
  with open(fout, 'w') as fp:
    print >>fp, 'RESULTS=', repr(counts)

