"""
Signal filter related script for EGG competition on Kaggle.

Be put in the directory which contains the train and test dataset 
subdirectory.
"""

import numpy as np
import mne as m
import csv
import pandas as pd
from os import listdir
from scipy.signal import butter, lfilter
import sys

Fs = 500.0          # sampling frequency of the signal


SIGNAL_FIELDS = [
    "Fp1","Fp2","F7","F3","Fz","F4","F8","FC5","FC1","FC2","FC6",
    "T7","C3","Cz","C4","T8","TP9","CP5","CP1","CP2","CP6","TP10",
    "P7","P3","Pz","P4","P8","PO9","O1","Oz","O2","PO10"
]

def low_pass_filter(data, cutoff, frequency = Fs):
    data = np.array(map(float, data))
    return m.filter.low_pass_filter(data, frequency, cutoff)


def filter_one_file(fname, cutoff, frequency = Fs):
    df = pd.read_csv(fname)
    for field in SIGNAL_FIELDS:
        data = df[field]
        df[field] = low_pass_filter(data, cutoff, frequency)

    df.to_csv(fname + name_suffix)

def filter_files(cutoff, frequency = Fs):
    for fname in listdir("./train"):
        if fname.endswith("data.csv"):
            filter_one_file("./train/" + fname, cutoff)
            print("process filtering train %s file finish" % fname)

    for fname in listdir("./test"):
        if fname.endswith("data.csv"):
            filter_one_file("./test/" + fname, cutoff)
            print("process filtering test %s file finish" % fname)


if __name__ == '__main__':
    if len(sys.argv) is not 2:
        print('run comamnd')
        print('python frequency_filter.py cutoff(0.0 - 1.0)')
    else:
        cutoff = float(sys.argv[1])
        filter_files(cutoff, Fs)
