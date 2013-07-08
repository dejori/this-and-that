#! /usr/bin/env python
#!/usr/bin/env python
import sys
for lineIn in sys.stdin:
       zip = lineIn[0:5]
       if "zip" in zip: continue;
#       Note: Key is defined here
       print zip + '\t' + lineIn