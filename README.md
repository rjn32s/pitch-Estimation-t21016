# Pitch Estimation
The fundamental frequency of a spoken signal is called pitch.More suitable definition of pitch is "Pitch is a perceptual property of sounds that allows their ordering on a frequency-related scale, or more commonly, pitch is the quality that makes it possible to judge sounds as {higher} and {lower} in the sense associated with musical melodies Pitch is a major auditory attribute of musical tones, along with duration, loudness, and timbre." .
The goal of this project is to use the auto-correlation function to identify the pitch of spoken discrete speech. An discrete wave is divided into several overlapping frames by the method, which then performs auto-correlation on each frame. The pitch estimation is derived from them. We first divide the audio signal into voiced and unvoiced samples based on its energy content, and then apply our algorithm to it.

### To Estimate Pitch 
use:
```` 
! git clone https://github.com/rjn32s/pitch-Estimation-t21016.git
from resources import *
pitchEstimate(r"Your .wav File addresss Here " , winSize = 30 , hopLEN = 15 ,winType = 'rect')

````
  



### Return Type 
pitchEstimate will return nested list as :

<br />[Estimated pitch, 1 or 0,'Note']
<br /> Voiced Frame => 1
<br /> Unvoiced Frame =>0



