import network

class Wifi:
    def __init__(self, ssid = None, key = None, state = True):
        self.ssid = ssid
        self.key = key
        self.state = state      
    
    def wlan(self):
        if self.state == True:
            self.nic = network.WLAN(network.STA_IF)
            self.nic.active(True)
            self.nic.connect(self.ssid, self.key)
        else:
            self.nic = network.WLAN(network.AP_IF)
            self.nic.active(True)
            self.nic.config(essid ='microcontroller_wifi',password = 'Micropython')
        
    def wlan_scan(self):
        if self.state == True:
            scan = self.nic.scan()
        return scan
        
    def disconnect(self):
        if self.nic.isconnected() == True:
            self.nic.disconnect()

    def check_ip(self):
        try:
            ip = self.nic.ifconfig()
            print(f'ip rpi pico ip: {ip[0]}')
            print(f'ip modem: {ip[2]}')
        except:
            pass
        return ip

connection = Wifi('put here your ssid', 'put here your password')
#connection = Wifi(ssid="Syntra_WiFi_Studenten")
connection.wlan()
#print(connection.wlan_scan())
connection.check_ip()
