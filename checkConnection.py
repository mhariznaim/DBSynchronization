import socket
import os
import fcntl
import struct


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,
        struct.pack('256s', ifname[:15])
        )[20:24])
ipslave1 = '192.168.135.121'
ipmaster1 = '10.73.32.201' 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(0.5)
ip = get_ip_address('wlan0')

try:
    #os.system('sudo dhclient -r wlan0')
    os.system('sudo dhclient')
    s.connect(('10.73.33.201', 3306))
    print 'Connected'
    
    #if ip != ipslave1:
        #print 'change b'
        #os.system('sudo ifconfig wlan0 down')
        #os.system('sudo ifconfig wlan0 '+ipslave1)
        #os.system('sudo ifconfig wlan0 up')
except Exception, e:
        print 'Not connected'
        os.system('sudo ifconfig wlan0 down')
        os.system('sudo ifconfig wlan0 '+ipmaster1)
        os.system('sudo ifconfig wlan0 up')

s.close()
