![alt text](https://github.com/arthur-bryan/web-opi/blob/master/static/images/facebook_cover_photo_2.png?raw=true)
[![Open Source](https://img.shields.io/badge/-Open%20Source-3066be?logo=Github&logoColor=white&link=https://github.com/arthur-bryan/pisco)](https://github.com/arthur-bryan/pisco)
[![Status Badge](	https://img.shields.io/badge/status-development-3066be)](https://github.com/arthur-bryan/web-opi)
![GitHub](https://img.shields.io/github/license/arthur-bryan/web-opi?color=blue)
[![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/arthur-bryan/web-opi)](https://github.com/arthur-bryan/web-opi/tags)
[![Python Badge](https://img.shields.io/badge/-Python-3066be?logo=Python&logoColor=white&link=https://www.python.org/)](https://www.python.org/)
![GitHub repo size](https://img.shields.io/github/repo-size/arthur-bryan/web-opi)

# :octocat: WEB-OPI
Web-OPI is a mini webserver to control your Orange PI GPIOs from wherever you are.

-   :heavy_check_mark: Control lamps, fans, relays for automation, and more 
-   :heavy_check_mark: See the current Orange PI temperature 
-   :heavy_check_mark: Access from your phone or computer

## :hammer_and_wrench: Installation
Install the dependencies and start the server on your Orange PI.

```sh
$ git clone https://github.com/arthur-bryan/web-opi
$ cd web-opi
$ chmod +x setup.sh
$ sudo ./setup.sh
$ sudo python3 start_web_opi.py
```
PS: By default, the server will start listenning on 0.0.0.0 at port 8080, change it on start_web_opi.py
Delete the files in audio_files and create new ones as you need.
There is a script that converts strings to mp3 files (see create_audio.py)

## :page_facing_up: Requirements
-   Orange Pi PC (not tested with another versions).
-   Something connected to GPIOs to be controlled.
-   Python version >= 3.6

## :movie_camera: Demonstration
-  YouTube: https://www.youtube.com/watch?v=T7odtEwHvsE
-  My site: https://arthur-bryan.github.io/website/templates/web-opi

![Screen Capture_select-area_20210223080858](https://user-images.githubusercontent.com/34891953/108835746-ab156f00-75ae-11eb-81b5-1a21d196d0c8.png)

## :copyright: License
[MIT License](https://github.com/arthur-bryan/web-opi/blob/master/LICENSE.md)
