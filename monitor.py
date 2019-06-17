import os
import time
import threading
import socket
import led

global radarstate
radarstate = 0
global networkstate
networkstate = 0
global wsstate
wsstate = 0

    
class RadarCheck(object):
    def __init__():
        self.version='ibrv001'
        self.radarstatus = 0
        self.runsecs = 0
        os.system('rm /tmp/radarstate_*')

    def checkstatus(self):
        global radarstate
        self.radarstatus = radarstate;
        self.runsecs = 1
        
    def server():
        while True:
            s = socket.socket()
            s.bind(("",20000))
            s.listen(1)
            conn,address = s.accept()
            print('Connected successful...' )
            time.sleep(1000)

def checkws():
    global wsstate
    if os.path.exists('/tmp/wsstate_1'):
        wsstate = 1
    else:
        wsstate = 0
    
            
def checkradar():
    global radarstate
    if os.path.exists('/tmp/radarstate_1'):
        radarstate = 1
    else:
        radarstate = 0

def checknetwork():
    global networkstate
    if(wsstate==1):
        networkstate = 1
    else:
        ecode = os.system('ping www.baidu.com -c 1')
        if ecode==0:
            networkstate = 1
        else:
            networkstate = 0
    

def ledcontrol():
    global radarstate
    led.gpio_init()
    islight = 0
    tick = 1
    while True:
        fastshine = 0
        tick = tick+1
        if tick>=10:
            checknetwork()
            tick = 1
        checkradar()
        
        if radarstate==0:
            led.close_all_led()
        else:
            checkws()
            if(wsstate==1):
                fastshine = 1

            if networkstate==1 and wsstate==0:
                if islight==0:
                    led.light_green()
                    islight=1
            else:
                if islight==0:
                    led.light_green()
                    islight=1
                else:
                    led.close_all_led()
                    islight=0
        if(fastshine==1):
            time.sleep(0.05)
        else:
            time.sleep(0.5)
        
def main():
    collect = threading.Thread(target=ledcontrol)
    collect.setDaemon(True)
    collect.start()
    while True:
        time.sleep(1)
    #rc = RadarCheck();
    #rc.server();


if __name__ == "__main__":
    main()

