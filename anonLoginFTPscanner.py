import ftplib
def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('ustbsmartcar')
        print '\n[*] '+ str(hostname) + ' FTP Anonymous Login Succeeded.'
        ftp.quit()
        return True
    except Exception, e:
        print '\n[-] '+ str(hostname) + ' FTP Anonymous Login Failed.'
        return False


def returnDefault(ftp):
    try:
        dirList = ftp.nlst()
        print dirList
    except:
        dirList = []
        print '[-] Could not list directory contents.'
        print '[-] Skipping To Next Target.'
        return
    retList = []
    for fileName in dirList:
        fn = fileName.lower()
        if '.php' in fn or '.htm' in fn or '.asp' in fn:
            print '[+] Found default page: '+ fileName
            retList.append(fileName)
    return retList

host = '202.204.62.43'
userName = 'ustbsmartcar'
ftp = ftplib.FTP(host)
ftp.login(userName)
returnDefault(ftp)