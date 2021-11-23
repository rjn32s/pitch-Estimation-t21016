# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 12:22:42 2021

@author: Rajan
"""

import numpy as np
import soundfile as sf
from scipy import signal
from math import log2, pow
from scipy import fftpack

#%%
# Enframe Function
def enframe(data , winsize , hoplen ,fs, wintype):
    
    final_outcome = []
    winsize = int(winsize* fs /1000)
    hoplen = int(hoplen* fs / 1000)
    for k in range(int(len(data)/hoplen)+2):
      try:
        zr = np.zeros(data.shape)
        
        if wintype =='rect':
          zr[hoplen*k:k*hoplen+winsize] = np.ones(winsize)
          result = zr * data
        if wintype == 'hamm':
          zr[hoplen*k:k*hoplen+winsize] = np.hamming(winsize)
          result = zr * data
      except:
        result = zr
      result = result[result !=0]
      final_outcome.append(result)
    return final_outcome


def frequency_detect(frame,fs):
    
    frame = frame - np.mean(frame)
    rxx= signal.correlate(frame , frame , 'full', 'auto')
    #peaks = signal.find_peaks(rxx)
    #peaks, _ = signal.find_peaks(rxx,height=0)
    #interval =np.diff(peaks)
    #half_peak = peaks[len(peaks)//2:]
    #interval =np.diff(half_peak)
    #pitch= fs / interval[0]
    
    
    corr = rxx[len(rxx) // 2 :]
    dcorr = np.diff(corr)
    
    ##########################################################################################
    # This chunk of code has been taken fron kaggel user url :https://www.kaggle.com/asparago/simple-pitch-detector
    rmin= np.where(dcorr > 0)[0]
    #print(rmin)
    if len(rmin) > 0:
        rmin1 = rmin[0]
    peak = np.argmax(corr[rmin1:]) + rmin1
    ########################################################################################
    #rmax = corr[peak] / corr[0]
    fo = fs / peak
    return fo

#    rxx= signal.correlate(frame , frame , 'full', 'auto')
#    corr = rxx[len(rxx) // 2 :]
#    dcorr = np.diff(corr)
#      # Find the First minimum
#    rmin= np.where(dcorr > 0)[0]
 #   if len(rmin) > 0:
 #       rmin1 = rmin[0]
 #   peak = np.argmax(corr[rmin1:]) + rmin1
 #  rmax = corr[peak] / corr[0]
  #  fo = fs / peak
   # return rmax , fo , peak
    
#def capestrum_detect(frame , fs):
    
 #   X = np.abs(np.log10(fftpack.fft(frame)))
        
  #  corr = X[len(X) // 2 :]
   # dcorr = np.diff(corr)
        # Find the First minimum
   # rmin= np.where(dcorr > 0)[0]
   # if len(rmin) > 0:
   #     rmin1 = rmin[0]
   # peak = np.argmax(corr[rmin1:]) + rmin1
   # rmax = corr[peak] / corr[0]
   # fo = fs / peak
    #return rmax , fo , peak



########################################################################################################################################    
# This part has been taken from stack exchanges:
# link : https://tinyurl.com/baxk4man
def pitch(freq):
    
    A4 = 440
    C0 = A4*pow(2, -4.75)
    name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    h = round(12*log2(freq/C0))
    octave = h // 12
    n = h % 12
    return name[n] + str(octave)
##############################################################################################################################################
#%%


def pitchEstimate(address = " " , winSize = 30 , hopLEN = 15 , winType = 'hamm' ):
    
    
    ########################################## Loading The .Wav File####################################
    data, samplerate = sf.read(address) 
    out = enframe(data, winsize=winSize , hoplen=hopLEN, fs = samplerate , wintype= winType) # Using Enframe from Resources
    
    
    ########################################### Calculating the Energy In Each Frame For Segmentation ################
    mask = []
    for frame in out: 
      #print('run')
      
      mask.append((np.abs(np.sum(frame * frame))))
    avg_energy = np.mean(mask)
    median_energy = np.median(mask)
    ################################################################################################
    
    
    
    csv_out = []
    for frame in out: 
      if np.abs(np.sum(frame * frame)) >=avg_energy:
          
         # if app == 'acf':
              
          peak = frequency_detect(frame, samplerate)
          csv_out.append([round(peak,3),1,pitch(peak)]) #, 'Voiced Frame',pitch(peak)])
         # if app == 'freq':
          #    rmax , fo , peak = capestrum_detect(frame, samplerate)
           #   csv_out.append([round(fo,3) , 'Voice Frame',pitch(fo)])
              
      else:
          csv_out.append([0.000,0,'NA'])
    return csv_out
