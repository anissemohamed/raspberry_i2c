from time import sleep
from sensor_AK8963 import*
from csv import*

#Open CSV file
outputFile = open('./MAG_log.csv', 'wb')
writer = writer(outputFile,  delimiter=';', quotechar='"')

#Init nbLine
lineNb = 1

#Start sensor
AK8963_start()

while 1 :

  #Read sensor value
  sampleBuffer = AK8963_read()
  
  #Concatenate data
  magX = sampleBuffer[0] * 255 + sampleBuffer[1]
  magY = sampleBuffer[2] * 255 + sampleBuffer[3]
  magZ = sampleBuffer[4] * 255 + sampleBuffer[5]
  
  #Print data onto the CSV file
  outputFile.seek(0, 2)
  writer.writerow([magX, magY, magZ])
  
  #Print data
  print "magX =",magX
  print "magY =",magY
  print "magZ =",magZ
  
  #Delay
  sleep(1)
  


  

