# Pitch Estimation
This project will help user to estimate the pitch of a give sound file(.wav) . 
  To use this Follow the Instructions:
  Clone the Repositery
  Open Spyder IDE
  Import the resources.py and pitchEstime.py file into working enviourment 
Run the following command
- python resources.py
- python pitchEstimate.py

### To Estimate Pitch 
use:
  pitchEstimate(r"Your .wav File addresss Here " , winSize = 30 , hopLEN = 15 ,winType = 'hamm')
By Default it will take window size as 30ms  , Hoplength as 15ms  and windowtype as Hamming 


### Return Type 
pitchEstimate will return nested list as :

[Estimated pitch, 'Voiced frame or not','Note ']


