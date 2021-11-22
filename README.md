# Pitch Estimation
This project will help user to estimate the pitch of a give sound file(.wav) . 
  <br />To use this Follow the Instructions:
  <br />Clone this repository
  <br />Open Spyder IDE
  <br />Import the resources.py and pitchEstime.py file into working enviourment 
Run the following command
- python resources.py
- python pitchEstimate.py

### To Estimate Pitch 
use:
```` 
$ git clone https://github.com/libgit2/libgit2
from resources import *
pitchEstimate(r"Your .wav File addresss Here " , winSize = 30 , hopLEN = 15 ,winType = 'rect')

````
  
<br />By Default it will take window size as 30ms  , Hoplength as 15ms  and windowtype as Hamming 


### Return Type 
pitchEstimate will return nested list as :

<br />[Estimated pitch, 'Voiced frame or not','Note ']


