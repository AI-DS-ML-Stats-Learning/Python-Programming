import sys

from Fundamentals.udf_package import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])