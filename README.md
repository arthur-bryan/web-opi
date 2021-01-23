![alt text](https://github.com/arthur-bryan/web-opi/blob/master/static/images/facebook_cover_photo_2.png?raw=true)

# WEB-OPI

Web-OPI is mini webserver to control your Orange PI GPIOs from wherever you are.

  - Control lamps, fans, relays for automation, and more.
  - See the current Orange PI temperature.
  - Access by your phone or computer.

### Installation

Install the dependencies and start the server on your Orange PI.

```sh
$ git clone https://github.com/arthur-bryan/web-opi
$ cd web-opi
$ chmod +x setup.sh
$ sudo ./setup.sh
$ sudo python3 start_web_opi.py
```

PS: Delete the files in audio_files and create new ones as you need.
There is a script that converts strings to mp3 files (see /audio_files/create_audio.py)

### Requirements

  - Orange Pi PC (not tested with another versions).
  - Something connected to GPIOs to be controlled.
  - Python verion >= 3.6


### Demonstration

  - YouTube: https://www.youtube.com/watch?v=T7odtEwHvsE
  - My site: https://arthur-bryan.github.io/website/templates/web-opi
