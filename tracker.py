import sys
import os
import socket
sys.path.append("script/")
from extract_objects import *
from cert import *
from http_request import *

def get_related_ip(ip):
    command = 'mida go '+'--all-resources --all-scripts '+ip
    try:
        os.system(command)
    except:
        printinfo('error','[!]error in running mida')
    try:
        path_ip = os.getcwd() + '/results/' + ip
        path_res_json = path_ip + '/' +os.listdir(path_ip)[-1]+'/resource_metadata.json'
        path_js_json =  path_ip + '/' +os.listdir(path_ip)[-1]+'/script_metadata.json'
        printinfo('info','###ready to go###')
        print '[+]Target  ' + socket.gethostbyname(ip)
        printinfo('success','[+]resource')
        print ip_resource_extract(path_res_json)
        printinfo('success','[+]javascript')
        print ip_js_extract(path_js_json)
    except:
        printinfo('error','[!]error in pharsing json data')
    try:
        cert,result = parser(ip, port=443)
        printinfo('success','[+]certificate')
        pprint(result)
    except:
        printinfo('error','[!]error in getting or pharsing certificate')
    try:
        printinfo('success','[+]http request figerprinting')
        printinfo('info','HEAD / HEAD/1.1')
        http_request('HEAD',ip)
        printinfo('info','DELETE / HTTP/1.1')
        http_request('DELETE',ip)
        printinfo('info','GET / HTTP/1.1')
        http_request('GET',ip)
        printinfo('info','GET / HTTP/3.0')
        http_request('GET3',ip)
        printinfo('info','GET / JUNK/1.1')
        http_request('JUNK',ip)
    except:
        printinfo('error','[!]error in getting http figerprinting')


def printinfo(type, info):
    if type == 'info':
        print '\033[1;32m {0}\033[0m'.format(info).encode('utf8')
    elif type == 'error':
        print '\033[1;31m {0} \033[0m'.format(info).encode('utf8')
    elif type == 'warning':
        print '\033[1;33m {0}\033[0m'.format(info).encode('utf8')
    elif type == 'success':
        print '\033[1;36m {0}\033[0m'.format(info).encode('utf8')
try:
    get_related_ip(str(sys.argv[1]))
except:
    printinfo('error','error,')
