import smbus

#Init I2C port 1
myI2c = smbus.SMBus(1)    

#Slave address
AK8963_ADDR       = 0x0C

#Register address
AK8963_REG_WHOAMI = 0x00
AK8963_REG_INFO   = 0x01
AK8963_REG_ST1    = 0x02
AK8963_REG_HXL    = 0x03
AK8963_REG_HXH    = 0x04
AK8963_REG_HYL    = 0x05
AK8963_REG_HYH    = 0x06
AK8963_REG_HZL    = 0x07
AK8963_REG_HZH    = 0x08
AK8963_REG_ST2    = 0x09      
AK8963_REG_CTRL1  = 0x0A
AK8963_REG_CTRL2  = 0x0B

#Init AK8963
myI2c.write_byte_data(AK8963_ADDR, AK8963_REG_CTRL1, 0x16)

#Read sensor value
sampleBuffer = myI2c.read_i2c_block_data(AK8963_ADDR, AK8963_REG_HXL, 6)

#Print data
print "magX =",sampleBuffer[0] * 255 + sampleBuffer[1]
print "magY =",sampleBuffer[2] * 255 + sampleBuffer[3]
print "magZ =",sampleBuffer[4] * 255 + sampleBuffer[4]

