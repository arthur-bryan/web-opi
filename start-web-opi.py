from flask import Flask, render_template, redirect, url_for
import OPi.GPIO as GPIO
import os
import threading
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

DEFAULT_LISTEN_ADDR = '0.0.0.0'
DEFAULT_LISTEN_PORT = 8080

# SETUP THE Orange PI PC GPIO's, SEE: https://opi-gpio.readthedocs.io/en/latest/
GPIO.setboard(GPIO.PC2)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIOs = {
    7: {'nome': 'GPIO 7', 'status': GPIO.LOW},
    11: {'nome': 'GPIO 11', 'status': GPIO.LOW},
    13: {'nome': 'GPIO 13', 'status': GPIO.LOW},
    15: {'nome': 'GPIO 15', 'status': GPIO.LOW},
    22: {'nome': 'GPIO 22', 'status': GPIO.LOW}
}

temp = float(open('/sys/class/thermal/thermal_zone0/temp').read())
temp = "{0:0.1f} °C".format(temp / 1000)

for pin in GPIOs:
    GPIO.setup(pin, GPIO.OUT)  # set the pins to output mode.


@app.route("/")
def control_panel():
    """Route that render the main template with current GPIOs status"""
    for GPIO_number in GPIOs:
        GPIOs[GPIO_number]['status'] = GPIO.input(GPIO_number)
    data_for_template = {
        'pins': GPIOs,
        'temp': temp
    }
    return render_template('panel.html', **data_for_template)


def change_gpio(gpio_num, value):
    """Changes the current value of the GPIO

        Args:
            gpio_num (int): the GPIO number to be controlled
            value (str):    'on' to power on the pin, 'off' to power off
    """
    if gpio_num in list(GPIOs.keys()):
        status = {'on': True, 'off': False}.get(value)
        GPIO.output(gpio_num, status)


def speak(pin_number, status):
    """Uses the mpg123 program to play an audio based on the taken action"""
    os.system("mpg123 " + os.path.abspath("static/audio/{}-{}.mp3".format(pin_number, status)))


@app.route("/<pin_number>/<status>")
def send_action(pin_number, status):
    """Route that render the updated GPIO's status after an taken action
        On button press, two threads starts: one for speaking the action, other
        for changing the GPIO status.
    """
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
    return render_template('panel.html', **data_for_template)


if __name__ == "__main__":
    app.run(host=DEFAULT_LISTEN_ADDR, port=DEFAULT_LISTEN_PORT)
