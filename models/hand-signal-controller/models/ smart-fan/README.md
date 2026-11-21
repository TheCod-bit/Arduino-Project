Architecture: The DH11 sensor in my Arduino measures temperatures and humidity. The AI Model will then take these two numbers and output one decision: fan off or on . A normal rule 
will set such as " on above 80 degrees Fahrenheit ".The model can learn the users preferences depending on where the userr lives . For the demo , the output could be just lighting up 
and LED. 

DataSet: I will collect readings in different room conditions and label each one myself with what if felt . Around 30 to 40 readings per label, at different times of day and after things
 that change the room, like a hot shower for humidity. 


 Learning Method: I will record my readings over to my laptop over serial , label them , train a small decision tree in Python , convert it to C, and then upload it to the Arduino.
