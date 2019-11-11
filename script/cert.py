'''
input: IP address
output: all info from certificate
'''
import ssl
import socket
import OpenSSL
from pprint import pprint
from datetime import datetime


def parser(ip_addr, port=443):
    try:
        certificate = ssl.get_server_certificate((ip_addr, port))
        #certificate = parser(ip,443)
	x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, certificate)

	result = {
	    'subject': dict(x509.get_subject().get_components()),
	    'issuer': dict(x509.get_issuer().get_components()),
	    'serialNumber': x509.get_serial_number(),
	    'version': x509.get_version(),
	    'notBefore': datetime.strptime(x509.get_notBefore(), '%Y%m%d%H%M%SZ'),
	    'notAfter': datetime.strptime(x509.get_notAfter(), '%Y%m%d%H%M%SZ'),
	}

	extensions = (x509.get_extension(i) for i in range(x509.get_extension_count()))
	extension_data = {e.get_short_name(): str(e) for e in extensions}
	result.update(extension_data)
    except:
	print "error when getting server certificate"
    return certificate,result
#cert,result = parser('183.232.231.174', port=443)  #baidu.com
#cert,result = parser('216.58.194.164', port=443)   #google.com
#cert,result = parser('172.217.164.110', port=443)   #youtube.com
#cert,result = parser('13.32.204.24', port=443)      #amazon.com
#pprint(result)
