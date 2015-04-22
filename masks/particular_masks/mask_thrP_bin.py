#!/bin/python
import os
from optparse import OptionParser

### Parse parameters, store into variables: ###
optparser = OptionParser()
(options, args) = optparser.parse_args()

fn_list=args

com = 'fslmaths ' + fn_list[0] + ' -thrP 50 -bin ' + fn_list[1] + '_50_bin'
print(com)
res = os.system(com)
