from time import sleep
from sensor_AK8963 import*
from csv import*

outputFile = open('./MAG_log.csv', 'wb')
writer = writer(outputFile,  delimiter='\t', quotechar='"')

while 1 :
  
  #Start AK8963
  AK8963_start()

  #Read sensor value
  sampleBuffer = AK8963_read()
  
  #Concatenate data
  magX = sampleBuffer[0] * 255 + sampleBuffer[1]
  magY = sampleBuffer[2] * 255 + sampleBuffer[3]
  magZ = sampleBuffer[4] * 255 + sampleBuffer[5]
  
  #Print data onto the CSV file
  #TODO
  
  #Print data
  print "magX =",magX
  print "magY =",magY
  print "magZ =",magZ
  
  #Delay
  time.sleep(1)
  


  

