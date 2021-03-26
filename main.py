import time, board, busio
import adafruit_adxl34x
import ITG_3200

#create i2c object
i2c = busio.I2C(board.SCL, board.SDA)

#initialize accelerometer ADXL345
accelerometer = adafruit_adxl34x.ADXL345(i2c)
gyroscope = ITG_3200.ITG_3200()

#TODO: set range of accelerometer to 16g
accelerometer.range = adafruit_adxl34x.Range.RANGE_16_G
#Open files for writing
acc_data = open('/home/pi/AMR-telemetry/'+str(time.time())+' acc', 'w+')
gyro_data = open('/home/pi/AMR-telemetry/'+str(time.time())+' gyro', 'w+')
comp_data = open('/home/pi/AMR-telemetry/'+str(time.time())+' comp', 'w+')
press_data = open('/home/pi/AMR-telemetry/'+str(time.time())+' press', 'w+')

#TODO: infinite loop to keep reading sensors and write to file
while True:

    acceleration = accelerometer.acceleration
    acc_data.write(str(time.time())+', ')
    acc_data.write("%.5f, %.5f, %.5f" %(str(acceleration[0]), str(acceleration[1]), str(acceleration[2])))
    acc_data.write('\n')

    #TODO: Read gyroscope data and write to file
    print(gyroscope.read())

    time.sleep(0.05)
