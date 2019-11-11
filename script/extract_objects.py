import json
from urlparse import urlparse
from socket import gethostbyname

def ip_resource_extract(json_path):
    f = open(json_path).read()
    data = json.loads(f)
    url_list = []
    for i in data:
        url_list.append(data[i]['requests'][0]['request']['url'])
    domain_list = []
    ip_list = []
    for url in url_list:
        domain_list.append(urlparse(url).hostname)
    for domain in domain_list:
        try:
            ip_list.append(gethostbyname(domain))
        except:
            pass
    return list(set(ip_list))
###########################################
def ip_js_extract(json_path):
    f = open(json_path).read()
    data = json.loads(f)
    url_list = []
    for i in data:
        url_list.append(data[i]['url'])
    domain_list = []
    ip_list = []
    for url in url_list:
        domain_list.append(urlparse(url).hostname)
    for domain in domain_list:
        try:
            ip_list.append(gethostbyname(domain))
        except:
            pass
    return list(set(ip_list))
#url_list = url_extract(path)
#ip_list = list(set(ip_addr_extract(url_list)))

