#!/usr/bin/env python3
#
#
# script to autogenerate a txt file in a format that is readable by
# the gnuplot program.  this is a companion  script for the derivativeSolver
# program, which has an option -e to generate the error between cos(1) generated
# by the machine, and sin'(1) generated with the fundamental theorem of calculus

import subprocess
import sys

def main() :
    gnuDataFile = open("gnuplotData.txt","w", encoding="utf-8")
    gnuDataFile.seek(0)
    gnuDataFile.truncate()
    for i in range (-10, 100) :
        h = 1/pow(2, i)
        command = "./derivativeSolver.py " + " -e " + str(h)
        result = subprocess.check_output(command, shell=True)
        result = result.decode(sys.stdout.encoding).strip()
        print(h, " ",result,file=gnuDataFile)
    gnuDataFile.close();

if __name__ == "__main__":
    main()

