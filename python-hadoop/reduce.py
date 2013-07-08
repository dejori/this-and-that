#!/usr/bin/env python
import sys
counts={}
for lineIn in sys.stdin:
       if not lineIn.strip(): continue
       key, line = lineIn.rsplit('\t',1)
       aLine = line.split(',')
       counts[key] = counts.get(key,0) + int(aLine[3])
for k , v in counts.items():
      print k + ',' +str(v)