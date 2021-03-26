import time, board, busio
import adafruit_adxl34x

#create i2c object
i2c = busio.I2C(board.SCL, board.SDA)

#initialize accelerometer ADXL345
accelerometer = adafruit_adxl34x.ADXL345(i2c)

#TODO: set range of accelerometer to 16g

#Open files for writing
acc_data = open('home/pi/AMR-telemetry'+str(time.time())+' acc', 'w+')
gyro_data = open('home/pi/AMR-telemetry'+str(time.time())+' gyro', 'w+')
comp_data = open('/home/pi/AMR-telemetry'+str(time.time())+' comp', 'w+')
press_data = open('/home/pi/AMR-telemetry'+str(time.time())+' press', 'w+')

#TODO: infinite loop to keep reading sensors and write to file
while True:
    acceleration = accelerometer.acceleration
    acc_data.write(str(time.time())+', ')
    acc_data.write(str(acceleration[0])+', '+str(acceleration[1])+', '+str(acceleration[2]))
    acc_data.write('\n')
    time.sleep(0.05)
