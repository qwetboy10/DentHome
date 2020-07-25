#!/usr/bin/env python
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
import os

env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html', 'xml'])
)
template = env.get_template('index.html')
uptime = os.popen('uptime').read()
ip = os.popen('dig @resolver1.opendns.com ANY myip.opendns.com +short').read()
s = ["NetworkManager"]
services = []
for a in s:
    services.append(os.popen('systemctl status ' + a + ' | grep Active').read())
print("Content-type: text/html\n\n")
print(template.render(uptime=uptime, ip=ip, services=services))
