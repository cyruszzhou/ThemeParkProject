import math
import random
import os
import glob
from os import listdir
from os.path import isfile, join

import signal

def signal_handler(signum, frame):
    raise Exception("Timed out! Try dp")
"""
def solve(N,Attraction):

    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(60)   # 60 seconds
    try:
        return btsolve()
    except Exception, msg:
        print "Timed out!"
    return dpsolve(N,Attraction)
"""
# dynamic progamming solver
def solve(N,Attraction):
    attWithSource = [[200,200,0,1440,0,0]]+Attraction
    UtilMatrix, PrevMatrix = dynamicProgram(N,Attraction)
    Sequence = PrevMatrix[1440][0]
    if Sequence != []:
        Sequence.pop(0)
        Sequence.pop()
    return len(Sequence),Sequence

def dynamicProgram(N,Attraction):
    #Initialization:
    UtilLine = [-math.inf for i in range(1441)]
    UtilMatrix = [UtilLine for i in range(N+1)]

    return UtilMatrix,PrevMatrix





def read_input(input_text):
    input_split = input_text.split("\n")
    N = int(input_split[0])
    latter_split = input_split[1:]
    attraction = []

    for i in range(N):
        this_attraction = latter_split[i]
        attraction.append([int(val) for val in this_attraction.split()])

    return N, attraction


def main():

    output_dir = "all_outputs/"
    output_suffix = '.out'

    for filename in glob.glob('all_inputs/*.in'):
        input_name = (filename.split("/"))[1]
        team_name = (input_name.split("."))[0]
        output_name = output_dir + team_name + output_suffix
        print("Now working on" + filename)
        
        with open(os.path.join(os.getcwd(), filename), 'r') as input:
            input_text = input.read()
            N, attraction = read_input(input_text)
            a, l = solve(N, attraction)

            with open(os.path.join(os.getcwd(),output_name),'w') as output:
                print(a,file=output)
                separator = " "
                print(separator.join(map(str,l)),file=output)

        input.close()
        output.close()

    #print(a)
    #separator = " "
    #print(separator.join(map(str,l)))
    
if __name__ == '__main__':
    main()
