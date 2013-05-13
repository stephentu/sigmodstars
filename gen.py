#!/usr/bin/env python2
import sys
import itertools
import operator
if __name__ == '__main__':
  (_, dfile) = sys.argv
  execfile(dfile)
  assert RESULTS is not None
  # map (author => count)
  cmap = { k : len(v) for (k, v) in RESULTS.iteritems() }
  # sort by value, desc
  res = sorted(cmap.iteritems(), key=operator.itemgetter(1), reverse=True)
  # take 50
  top50 = res[:50]

  # min year
  min_year = min(itertools.chain.from_iterable(RESULTS.values()))
  # max year
  max_year = max(itertools.chain.from_iterable(RESULTS.values()))

  year_slots = max_year - min_year + 1

  # format: name | year_slots | sum
  print r'\begin{tabular}{l%s|p{1pt}}' % ('p{1pt}' * year_slots)
  print r'& %s & \\' % (' & '.join(r'\begin{sideways}%s\end{sideways}' % (str(d+min_year)[2:]) for d in range(year_slots)))
  print r'\hline'

  for a, total in top50:
    years = RESULTS[a]
    breakdown = [0 for _ in range(year_slots)]
    for y in years:
      breakdown[y - min_year] += 1
    #print breakdown
    print r'%s & %s & %d \\' % (a.encode('utf-8'), ' & '.join(map(lambda x: str(x) if x else ' ', breakdown)), total)
  print r'\end{tabular}'
