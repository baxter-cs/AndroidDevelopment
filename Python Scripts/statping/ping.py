#!python2
# This script will ping google every 5 minutes and record it to a log file 'logping.txt'
# Problems: the script may overwrite the entire log file on restart
'''
import platform,subprocess,re
def Ping(hostname,timeout):
    if platform.system() == "Windows":
        command="ping "+hostname+" -n 1 -w "+str(timeout*1000)
    else:
        command="ping -i "+str(timeout)+" -c 1 " + hostname
    proccess = subprocess.Popen(command, stdout=subprocess.PIPE)
    matches=re.match('.*time=([0-9]+)ms.*', proccess.stdout.read(),re.DOTALL)
    if matches:
        return matches.group(1)
    else: 
        return False
'''
import platform, subprocess, re, datetime, time
log = open('logping.txt', 'a')


def Ping(hostname,timeout):
    if platform.system() == "Windows":
        command="ping "+hostname+" -n 1 -w "+str(timeout*1000)
    else:
        command="ping -i "+str(timeout)+" -c 1 " + hostname
    proccess = subprocess.Popen(command, stdout=subprocess.PIPE)
    matches=re.match('.*time=([0-9]+)ms.*', proccess.stdout.read(),re.DOTALL)
    if matches:
        return matches.group(1)
    else: 
        return False

while True:
    fetch = Ping("google.com", 5) + "," + str(datetime.datetime.now())
    print fetch
    log.write(fetch)
    log.write('\n')
    time.sleep(300)