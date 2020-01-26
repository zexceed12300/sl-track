# sl-track - GeoPosition Tracking
Author : xzen@zexceed12300

Version : 1.2 (stable)

Facebook : https://www.facebook.com/profile.php?id=100011531026694

Github : https://github.com/zexceed12300

-- Jika ada saran / issue / bug / dll PM saya di Facebook

-- If there are suggestions / issues / bugs / etc. PM I am on Facebook

# HowTo Install / Cara install
## 1. Update or install package and library
### -- Linux
```
apt-get update && apt-get upgrade
apt-get install python3
apt-get install php
```
### -- Termux
```
apt-get update && apt-get upgrade
pkg install git
pkg install python
pkg install php
```
   
## 2. Download Repository wl-phisher
```
git clone https://github.com/zexceed12300/sl-track
cd sl-track
python3 sl-track.py
```   
# HowTo Using sl-track
You should use port forwarding like ngrok,portmap,etc for forward your localhost webserver

```
usage: sl-track.py [-h] [-r [URL]] [-T [enable/disable]] [-H [enable/disable]]

optional arguments:
  -h, --help            show this help message and exit
  -r [URL], --redirect [URL]
                        after click the continue button and waiting for 10
                        second in phising page, victim redirect to ?? (ex:
                        https://google.com)
  -T [enable/disable], --tracking [enable/disable]
                        enable/disable geolocation tracking. (default:
                        disable)
  -H [enable/disable], --harvester [enable/disable]
                        enable/disable device information harvester. (default:
                        enable)
```                      
### Enjoy!..
