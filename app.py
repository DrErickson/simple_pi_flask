from flask import Flask, render_template
import RPi.GPIO as GPIO
import board
import adafruit_bme680

i2c = board.I2C()

bme = adafruit_bme680.Adafruit_BME680_I2C(i2c)

# refer to the gpio rather than the board pin
GPIO.setmode(GPIO.BCM)

# Use pin 21
pirpin = 21
GPIO.setup(pirpin, GPIO.IN)

# Start Webserver
app = Flask(__name__)

# Main webpage
@app.route('/')
def index():
    return render_template('index.html', first='First', last='Last')

# sensor webpage
@app.route('/sensor')
def sensor():
    return render_template('sensor.html', temperature=bme.temperature)

# pir webpage
@app.route('/pir')
def pir():
    curr_state = GPIO.input(pirpin)
    if curr_state == 1:
        value = 'On'
    else:
        value = 'Off'
    
    return render_template('pir.html', sensor=value)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8080)
