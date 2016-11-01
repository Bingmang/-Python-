#! /usr/bin/dev python

import nmap
import optparse
from threading import *
def nmapScan(tgtHost,tgtPort):
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost,tgtPort)
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print " [*] "+tgtHost+" tcp/"+tgtPort+" "+state

def main():
    parser=optparse.OptionParser('use %prog -H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target port')
    (options, args)=parser.parse_args()
    print options
    print args
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')

    if (tgtHost == None) | (tgtPorts == None):
        print parser.usage
        exit(0)

    for tgtPort in tgtPorts:
        t = Thread(target=nmapScan,args=(tgtHost,tgtPort))
        t.start()
        # nmapScan(tgtHost,tgtPort)

if __name__ == '__main__':
    main()