# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 18:05:16 2021

@author: eRXRd
"""

import sys
import wave
import numpy as np
import matplotlib.pyplot as plt

def main():
        
    filename = r"C:\Users\eRXRd\.spyder-py3\Fx.wav"
    
    w = wave.open(filename, 'r')
    p = w.getparams()
    tdata = w.readframes(p.nframes)
    data = np.frombuffer(tdata, dtype = "int16")
    
    plt.specgram(data, Fs=p.framerate)
    
    plt.xlabel('time [sec]')
    plt.ylabel('frequency [Hz]')
    plt.show
    
    w.close()
    
if __name__ == '__main__':
    main()
    