import os
import argparse
import subprocess
from src import benchmark
  
def getArg():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d',"--data", help = "path of data")
    parser.add_argument('-m',"--model", help = "path of model")
    parser.add_argument('-q',"--quantization", help = "quantization true or not")
    args = parser.parse_args()
    return args

def args_to_param(args):
    param = dict()
    param["data"] = args.data
    param["model"] = args.model
    param["quantization"] = False
    if args.quantization:
        if args.quantization == "True":
            param["quantization"] = True
    return param
    
if __name__ == "__main__":
    args = getArg()
    param = args_to_param(args)
    benchmark.benchmark(**param)
    