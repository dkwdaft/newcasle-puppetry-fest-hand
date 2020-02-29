# Add your Python code here. E.g.
from microbit import *
import speech
speech.say("ready")
display.scroll("ready)
while True:

    #Checks how much current tra vels from pin1 to ground
    #If nobody is holding on to pin1 and ground this number will be
    #lower. When somebody is holding this pin (and is conducting the
    #current) then this value will be higher)
    threshold = pin1.read_analog()
    #If the value of threshold is over 300
    if threshold < 100:
        #Say hello
        speech.say("welcome to the gateshead rasberry jam in the maker place")
