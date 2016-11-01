#! /usr/bin/dev python

import optparse
from threading import *
from socket import *

screenLock = Semaphore(value=1)

def connScan(tgtHost, tgtPort):
    '''Use IP address to get Hostname or use Hostname to get IP address.'''
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))

        #Send massage
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(100)
        screenLock.acquire()
        print ' [+] %d/tcp open' % tgtPort
        print ' [+] ' + str(results)
        connSkt.close()

    except:
        screenLock.acquire()
        print ' [-] %d/tcp closed' % tgtPort

    finally:
        screenLock.release()
        connSkt.close()

def portScan(tgtHost, tgtPorts):
    '''Scan port.'''
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print " [-] Cannot resolve '%s': Unknown host" % tgtHost
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print '\n [+] Scan Results for: ' + tgtName[0]
    except:
        print '\n [+] Scan Results for: ' + tgtIP
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()
        print 'Scanning port ' + tgtPort
        connScan(tgtHost, int(tgtPort))

def main():
    parser = optparse.OptionParser('use %prog -H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost',type='string',help='specify target host')
    parser.add_option('-p',dest='tgtPort',type='string',help='specify target port')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost == None ) | (tgtPorts == None):
        print parser.usage
        exit(0)
    portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()