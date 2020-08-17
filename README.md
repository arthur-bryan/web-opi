# WEB-OPI

Web-OPI is mini webserver to control your Orange PI GPIOs from wherever you are.

  - Control lamps, fans, relays for automation and mode.
  - See the current Orange PI temperature.
  - Access by your phone or computer.

### Installation

Install the dependencies and start the server on your Orange PI.

```sh
$ git clone https://github.com/arthur-bryan/web-opi
$ cd web-opi
$ chmod +x setup.sh
$ sudo ./setup.sh
```


### Requirements

  - Orange Pi PC (not tested with another versions).
  - Something connected to GPIOs to be controlled.
  - Python verion >= 3.6


### Demonstration

  - YouTube: https://www.youtube.com
  - My site: https://arthur-bryan.github.io/website/index.html
  
  
### Tip

  - You can use tools like ngrok no expose your server to the internet 
    and access it through a subdomain whitout the need of a public IP on the local machine.
