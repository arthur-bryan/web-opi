from flask import Flask, render_template, request, redirect, url_for
import OPi.GPIO as GPIO
import os
from gtts import gTTS
import threading
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

# SETUP THE Orange PI PC GPIO's - SEE MORE: https://opi-gpio.readthedocs.io/en/latest/
# GPIO.setboard(GPIO.PC2)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIOs = {
    7: {'nome': 'GPIO 7', 'status': GPIO.LOW},
    11: {'nome': 'GPIO 11', 'status': GPIO.LOW},
    12: {'nome': 'GPIO 12', 'status': GPIO.LOW},
    13: {'nome': 'GPIO 13', 'status': GPIO.LOW},
	15: {'nome': 'GPIO 15', 'status': GPIO.LOW}
}

temp = float(open('/sys/class/thermal/thermal_zone0/temp').read())
temp = "{0:0.1f} °C".format(temp / 1000)

for pin in GPIOs:  # set all GPIOs on gpios dict to output mode
    GPIO.setup(pin, GPIO.OUT)


@app.route("/")
def default_route():
    for GPIO_number in GPIOs:
        GPIOs[GPIO_number]['status'] = GPIO.input(GPIO_number)
    data_for_template = {
        'pins': GPIOs,
        'temp': temp
    }
    return render_template('painel.html', **data_for_template)


def change_gpio(gpio_num, value):
    if gpio_num in list(GPIOs.keys()) and value == "on":
        GPIO.output(gpio_num, True)
    elif gpio_num in list(GPIOs.keys()) and value == "off":
        GPIO.output(gpio_num, False)


def speak(pin_number, status):
    if status == "on" and pin_number in list(GPIOs.keys()):
        os.system("mpg123 " + os.path.abspath("audio_files/{}-on.mp3".format(pin_number)))
    elif status == "off" and pin_number in list(GPIOs.keys()):
        os.system("mpg123 " + os.path.abspath("audio_files/{}-off.mp3".format(pin_number)))


@app.route("/<pin_number>/<status>")
def send_action(pin_number, status):
    f1 = threading.Thread(target=speak, args=[int(pin_number), status])
    f2 = threading.Thread(target=change_gpio, args=[int(pin_number), status])
    f1.start()
    f2.start()
    for GPIO_number in GPIOs:
        GPIOs[GPIO_number]['status'] = GPIO.input(GPIO_number)
    data_for_template = {
        'pins': GPIOs,
        'temp': temp
    }
    return render_template('painel.html', **data_for_template)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
