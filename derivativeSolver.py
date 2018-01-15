#!/usr/bin/env python3
#
# derivativeSolver will find the derivative of f(x) for some value x
#
# the solution here was to bound the value of h to minimize the loss
# of significant digits.  the derivative formula cannot be modified
# to remove the subtraction, so the issue has to be mitigated by bounding 
# h to 0.0000001
#
# Author: Timothy Baker
# Date  : September 2017
# Class : CS 517
# Assg  : Machine Assignment 1, Problem 3

import sys
import re
from math import *

# tells the user about some of the program functionality
def helpMenu(help) :
    if help == "help" :
        print("usage: derivativeSolver [OPTION]... F(X) X-VALUE [H-VALUE]")
        print("\n         derivativeSolver will accept a function, f(x),")
        print("         from the command line as the first argument and")
        print("         the value of the x variable as the second argument")
        print("")
        print("         The program will also run with no arguments,")
        print("         allowing the user to input f(x) and x")
        print("         while the program is running.")
        print("")
        print("         Available [OPTIONS]:")
        print("            -s    only output the derivative result")
        print("")
        print("         Optional third argument specifies the h Value.")
        print("         The program will default to using the smallest")
        print("         possible value for h.")
        print("")
        print("         You must use 'x' as the independent variable. Any")
        print("         other characters will not be accepted.")
        print("")
        print("         Python math functions need to be surrounded by \" \".")
        print("         These include: sin, cos, tan, asin, acos, atan, pow,")
        print("         sqrt, and any other acceptable functions.")
        print("")
        print("         For exampe, sin(x) will NOT compute, but \"sin(x)\" will.")
        print("")
        print("         IMPORTANT: All operators should be EXPLICITLY stated.")
        print("")
        print("         For example, 2x will NOT compute, but 2*x will.")
        print("")
        print("         All Python3 compatible numerical operators will work, and")
        print("         any built in function from the math library should also work.")
    elif help == "input error" :
        print("error: Invalid Input. Try -h for help")
    elif help =="usage" :
        print("usage: derivativeSolver [OPTION]... F(X) XVALUE")
    elif help =="proc error" :
        print("error: Processing Error")
    else :
        print("error: undefined error")

# takes the function given by the user and replaces the x variable with a
# floating point value for x, then evaluates the function
def solveFunction(function, xValue) :
    function = re.sub(r"\s", "", function)
    functionWithXValues = ""
    for char in function :
        if char == 'x' :
            addOn = "("+str(float(xValue))+")"
            functionWithXValues = functionWithXValues + addOn
        else :
            functionWithXValues = functionWithXValues + str(char)
    return float(eval(functionWithXValues))

# uses the fundamental theorem of calculus
#
#    f'(x) = limit h -> 0 [f(x+h)-f(x)/h]
#
# to solve for the derivative of f(x). Given the numerical values
# of f(x), f(x+h) and h, the function will return the value of f'(x)
def findDerivative(solution, plusH, hValue) :
    derivative = (plusH-solution)/hValue
    return float(derivative)


# this function handles the user interface and user interaction
def intro() :
    function = False
    xValue = False
    hValue = False
    outputOnly = False
    cosToo = False
    args = len(sys.argv)
    if args == 2 :
        if sys.argv[1] == "-h" or sys.argv[1] == "--help" :
            return False, True, False, False, False
        else :
            return False, True, True, False, False
    else :
        if args > 3:
            if sys.argv[1][0] == "-" and sys.argv[1][1] == "s" :
                outputOnly = True
            if sys.argv[1][0] == "-" and sys.argv[1][1] == "h" :
                return False, True, False, False, False
            if args > 4 :
                hValue = float(sys.argv[4])
                xValue = sys.argv[3]
                function = sys.argv[2]
            else :
                if outputOnly == True :
                    hValue = float(0.0000001)
                    function = sys.argv[2]
                    xValue = sys.argv[3]
                else :
                    function = sys.argv[1]
                    xValue = sys.argv[2]
                    hValue = float(sys.argv[3])
                
        elif  args == 3 :
            if sys.argv[1] == "-e" :
                function = "sin(x)"
                xValue = 1
                hValue = float(sys.argv[2])
                outputOnly = True
                return function, xValue, hValue, outputOnly, cosToo
            print("\n")
            function = sys.argv[1]
            xValue = sys.argv[2]
            hValue = float(0.0000001)
        else :
            print("\n Welcome to the Derivative Solver\n")
            hValue = float(0.0000001)
            if args > 2 :
                function = sys.argv[1]
                xValue = sys.argv[2]
            else:
                function = input(" Enter f(x) : ")
                xValue =   input(" x value ?  : ")
    if function.isspace() == True or function == "\t" or function == "\n" or function =="" :
        return False, False, False, False, False
    if xValue.isspace() == True or xValue == "\t" or xValue == "\n" or xValue == "" :
        return False, False, False, False, False
    if function == "sin(x)" :
        cosToo = True
    xValue = float(xValue)
    return function, xValue, hValue, outputOnly, cosToo

def main() :
    function, xValue, hValue, outputOnly, cosToo = intro()
    if type(function) == bool :
        if (function, xValue, hValue) == (False, True, False) :
            helpMenu("help")
        elif (function, xValue, hValue) == (False, False, False) :
            helpMenu("input error")
        elif (function, xValue, hValue) == (False, True, True) :
            helpMenu("usage")
    else :
        solution = solveFunction(function, xValue)
        if type(solution) == bool :
            helpMenu("proc error")
        else :
            xPlusH = xValue + hValue
            plusH = solveFunction(function, xPlusH)
            derivative = findDerivative(solution, plusH, hValue)
            if outputOnly == False :
                print("   f(x) =", function, "\n")
                print("   f (",xValue,")  =", solution)
                print("   f'(",xValue,")  =", derivative)
                if cosToo == True :
                    print("   cos(",xValue,") =", float(cos(xValue)))
                    print("\n")
                    print("   error =", float(cos(xValue)) - derivative)
                print("\n")
            else :
                if cosToo == True :
                    print(derivative,"    ", float(cos(xValue)),"    ", float(cos(xValue)) - derivative)
                else :
                    if function == "sin(x)" :
                        print(float(cos(xValue)) - derivative)
                    else :
                        print(derivative)       
 
if __name__ == "__main__":
    main()

#end of file 
