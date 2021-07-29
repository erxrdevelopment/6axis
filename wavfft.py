# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 17:36:33 2021

@author: eRXRd
"""
def fft():
    

    import numpy as np
    import wave
    import matplotlib.pyplot as plt
    
    filename = r"C:\Users\eRXRd\.spyder-py3\Fx.wav"
    
    w = wave.open(filename, 'rb')
    data = w.readframes(w.getnframes())
    w.close()
    
    fs = w.getframerate()
    s = (np.frombuffer(data, dtype="int16") / 32767.0)[0:fs]
    
    F = np.fft.fft(s)
    F_abs = np.abs(F)
    F_a = F_abs / fs * 2
    F_a[0] = F_abs[0] / fs
    
    plt.plot(F_a[:int(fs/2)+1])
    plt.show()

