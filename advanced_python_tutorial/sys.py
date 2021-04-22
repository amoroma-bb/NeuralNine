import sys
import getopt
filename = sys.argv[1]
message = sys.argv[2]

with open(filename,'w+') as f:
    f.write(message) 