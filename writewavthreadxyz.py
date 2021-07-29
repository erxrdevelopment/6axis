#!/usr/bin/env python3
# coding: utf-8
"""python script
"""

import serial
import time
import sys
import numpy as np
import matplotlib.pyplot as plt
import wave
import struct
import threading



def main():
    """main
    """
    comport = serial.Serial('COM3', baudrate=230400, parity=serial.PARITY_NONE,
                            bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE,rtscts=False,dsrdtr=False
)
    # timeout=None, wait forever
    # timeout=0, non-blocking
  
    # clear receive buffer
    comport.reset_input_buffer()
    # send data
    if comport.out_waiting > 0:
        comport.reset_output_buffer()
    # 送信データはbytes 型
    
    comport.write(b'020202')
    # recv data
    Fxd = [0]
    Fyd = [0]
    Fzd = [0]
    Mxd = [0]
    Myd = [0]
    Mzd = [0]
    while True:
        try:
            while comport.in_waiting<34:
                pass
            
            # 受信データはbytes 型
            recv_data = comport.read(34)
            #print(recv_data)
            Fx = int(recv_data[4:8],16)-2063
            Fy = int(recv_data[8:12],16)-2045
            Fz = int(recv_data[12:16],16)-2071
            Mx = int(recv_data[16:20],16)-2035
            My = int(recv_data[20:24],16)-2052
            Mz = int(recv_data[24:28],16)-2147
            Fxd.append(Fx)
            Fyd.append(Fy)
            Fzd.append(Fz)
            Mxd.append(Mx)
            Myd.append(My)
            Mzd.append(Mz)
            # print(Fx)
            # print(Fy)
            # print(Fz)
            # print(Mx)
            # print(My)
            # print(Mz)
            # print (recv_data[4:7])
            
        except KeyboardInterrupt:
            comport.close()
            # print(Fxd)
            # print(Fyd)
            # print(Fzd)
            # print(Mxd)
            # print(Myd)
            # print(Mzd)
            
            
            Fxds = [0]
            for s in Fxd:
                for i in range(440):
                    Fxds.append(s)
            print(len(Fxd))
            print(len(Fxds))
            Fxwave = [int(x*46.81) for x in Fxds]
            print(min(Fxwave), max(Fxwave))
            binwave = struct.pack("h" * len(Fxwave), *Fxwave)
            w=wave.Wave_write("Fx.wav")
            p=(1,2,44100, len(binwave),'NONE','not compressed')
            w.setparams(p)
            w.writeframes(binwave)
            w.close()

            # def worker():
            #     print(time.time())
            #     time.sleep(8)
                
            # def scheduler(interval, f, wait = True):
            #     base_time = time.time()
            #     next_time = 0
            #     while True:
            #         t = threading .Thread(target = f)
            #         t.start()
            #         if wait:
            #             t.join()
            #         next_time = ((base_time - time.time()) % interval) or interval
            #         print(next_time)
            #         time.sleep(next_time)
            # scheduler(1, worker, False)
                  
            Fyds = [0]
            for s in Fyd:
                for i in range(440):
                    Fyds.append(s)
            print(len(Fyd))
            print(len(Fyds))
            Fywave = [int(x*46.81) for x in Fyds]
            print(min(Fywave), max(Fywave))
            binwave = struct.pack("h" * len(Fywave), *Fywave)
            w=wave.Wave_write("Fy.wav")
            p=(1,2,44100, len(binwave),'NONE','not compressed')
            w.setparams(p)
            w.writeframes(binwave)
            w.close()

            # def worker():
            #     print(time.time())
            #     time.sleep(8)
                
            # def scheduler(interval, f, wait = True):
            #     base_time = time.time()
            #     next_time = 0
            #     while True:
            #         t = threading .Thread(target = f)
            #         t.start()
            #         if wait:
            #             t.join()
            #         next_time = ((base_time - time.time()) % interval) or interval
            #         print(next_time)
            #         time.sleep(next_time)
            # scheduler(1, worker, False)

            Fzds = [0]
            for s in Fzd:
                for i in range(440):
                    Fzds.append(s)
            print(len(Fzd))
            print(len(Fzds))
            Fzwave = [int(x*36.41)-32767+2621 for x in Fzds]
            print(min(Fzwave), max(Fzwave))
            binwave = struct.pack("h" * len(Fzwave), *Fzwave)
            w=wave.Wave_write("Fz.wav")
            p=(1,2,44100, len(binwave),'NONE','not compressed')
            w.setparams(p)
            w.writeframes(binwave)
            w.close()

            # def worker():
            #     print(time.time())
            #     time.sleep(8)
                
            # def scheduler(interval, f, wait = True):
            #     base_time = time.time()
            #     next_time = 0
            #     while True:
            #         t = threading .Thread(target = f)
            #         t.start()
            #         if wait:
            #             t.join()
            #         next_time = ((base_time - time.time()) % interval) or interval
            #         print(next_time)
            #         time.sleep(next_time)
            # scheduler(1, worker, False)
    
            sys.exit()
            
            # datalength = 100
            # frame = 50
            # sleepTime = 0.0001
            
    # for i in range(frame):
        #data = np.random.rand(datalength)
    plt.plot(Fxd)
    plt.plot(Fyd)
    plt.plot(Fzd)
    plt.draw()
    #plt.pause(sleepTime)
    #plt.cla
            
    comport.close()

if __name__ == '__main__':
    main()
    
        
        
        
    


