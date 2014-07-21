from time import sleep
from sensor_AK8963 import*


while 1 :
  
  #Start AK8963
  AK8963_start()

  #Read sensor value
  sampleBuffer = AK8963_read()
  
  #Print data
  print "magX =",sampleBuffer[0] * 255 + sampleBuffer[1]
  print "magY =",sampleBuffer[2] * 255 + sampleBuffer[3]
  print "magZ =",sampleBuffer[4] * 255 + sampleBuffer[4]
  print " "
  
  #Delay
  time.sleep(1)
  


  

