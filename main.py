import time
import sensor_AK8963


while 1 :
  
  #Start AK8963
  sensor_AK8963.AK8963_start()

  #Read sensor value
  sampleBuffer = sensor_AK8963.AK8963_read()
  
  #Print data
  print "magX =",sampleBuffer[0] * 255 + sampleBuffer[1]
  print "magY =",sampleBuffer[2] * 255 + sampleBuffer[3]
  print "magZ =",sampleBuffer[4] * 255 + sampleBuffer[4]
  print " "
  
  #Delay
  time.sleep(1)
  


  

