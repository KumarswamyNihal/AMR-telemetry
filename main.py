import time, board, busio
import adafruit_adxl34x
import ITG_3200
import Adafruit_BMP.BMP085 as BMP085

#create i2c object
i2c = busio.I2C(board.SCL, board.SDA)

#initialize accelerometer ADXL345
accelerometer = adafruit_adxl34x.ADXL345(i2c)
gyroscope = ITG_3200.ITG_3200()
press = BMP085.BMP085()

#set range of accelerometer to 16g
accelerometer.range = adafruit_adxl34x.Range.RANGE_16_G

#Open files for writing
acc_data = open('/home/pi/AMR-telemetry/'+str(time.time())+' acc', 'w+')
gyro_data = open('/home/pi/AMR-telemetry/'+str(time.time())+' gyro', 'w+')
press_data = open('/home/pi/AMR-telemetry/'+str(time.time())+' press', 'w+')

#infinite loop to keep reading sensors and write to file
while True:

    acceleration = accelerometer.acceleration
    acc_data.write(str(time.time())+', ')
    acc_data.write("%.5f, %.5f, %.5f" %(acceleration[0], acceleration[1], acceleration[2]))
    acc_data.write('\n')

    #Read gyroscope data and write to file
    gyro = gyroscope.read()
    gyro_data.write(str(time.time())+', ')
    gyro_data.write("%.5f, %.5f, %.5f" %(gyro[0], gyro[1], gyro[2]))
    gyro_data.write('\n')

    #TODO: Read pressure sensor data and write to file
    pressure = [0.0, 0.0, 0.0, 0.0]
    pressure[0] = press.read_read_temperature()
    pressure[1] = press.read_pressure()
    pressure[2] = press.read_altitude()
    pressure[3] = press.read_sealevel_pressure()

    press_data.write(str(time.time())+', ')
    press_data.write("%.2f, %.5f, %.5f %.5f" %(pressure[0], pressure[1], pressure[2], pressure[3]))
    press_data.write('\n')
    
    time.sleep(0.05)
