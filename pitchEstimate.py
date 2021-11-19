# -*- coding: utf-8 -*-
"""

This main.py File is for Demonstration Purpose Only.
Here you can  Uncomment the plotting part to see Each Frame and their auto corellation 
This program will return a list of Estimated Pitch
Detect if it is Voiced Frame or Unvoiced Frame 
If Voiced Frame it will also Also Give the Note corresponding to the Pitch

return Format [Pitch  , 'Voiced or Unvoiced'  , 'Note' ]

Note : 0 is returned for Unvoiced Frame
"""
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from math import log2, pow



from resources import *

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
      if np.abs(np.sum(frame * frame)) >= median_energy:
        rmax , fo , peak = frequency_detect(frame, samplerate)
        csv_out.append([round(fo,3) , 'Voiced Frame',pitch(fo)])
      else:
          csv_out.append([0 , 'Unvoiced Frame'])
    return csv_out