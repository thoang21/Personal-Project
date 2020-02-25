# Continuous Servo Test Program for CircuitPython
import time
import board
import pulseio
import adafruit_bno055
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pulseio.PWMOut(board.D3, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.ContinuousServo(pwm)

# Create a orientation obect
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055(i2c)

# Variable
setpoint = 0
tolerance = 10

while True:
    if sensor.euler[2] > setpoint + tolerance:
        print("forward")
        my_servo.throttle = 1.0
    elif sensor.euler[2] < setpoint - tolerance:
        print("reverse")
        my_servo.throttle = -1.0
    else:
        print("stop")
        my_servo.throttle = 0.0
