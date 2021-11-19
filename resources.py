# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 12:22:42 2021

@author: Rajan
"""

import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from math import log2, pow

#%%
# Enframe Function
def enframe(data , winsize , hoplen ,fs, wintype):
  final_outcome = []
  filenames = []
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

  frame_len = int(len(frame))
  rxx= np.correlate(frame , frame , 'full')
  corr = rxx[len(rxx) // 2 :]
  dcorr = np.diff(corr)
  # Find the First minimum
  rmin= np.where(dcorr > 0)[0]
  if len(rmin) > 0:
    rmin1 = rmin[0]
  peak = np.argmax(corr[rmin1:]) + rmin1
  rmax = corr[peak] / corr[0]
  fo = fs / peak
  return rmax , fo , peak




    
def pitch(freq):
    A4 = 440
    C0 = A4*pow(2, -4.75)
    name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    h = round(12*log2(freq/C0))
    octave = h // 12
    n = h % 12
    return name[n] + str(octave)

