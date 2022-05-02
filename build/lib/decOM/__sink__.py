#!/usr/bin/env python3
import subprocess
import os.path
from .__utils__ import *
from os import path

def create_vector(path_to_sources, key, accession, t):
    output=accession+"_vector/"
    if path.exists(output):
        subprocess.call(["rm","-rf",output])
    subprocess.call(["kmtricks","filter","--in-matrix",path_to_sources,"--key",key,"--output",output, "--out-types", "k,v"])
    subprocess.call(["kmtricks", "aggregate", "-t", str(t), "--run-dir", output, "--count" ,accession+":kmer", "--output", output+"counts/partition_100/"+accession+"_missing.txt"])
    print_status("Sink vector was created")
    return
