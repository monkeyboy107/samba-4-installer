#!/usr/bin/python
import platform
os = 'unknown'
platform = platform.platform()
os = platform.split("-")
for i in range(len(os)):
    if os[i] == 'CentOS':
        os = 'CentOS'
        break
    if os[i] == 'fedora':
        os = 'fedora'
        break
    if os[i] == 'ubuntu':
        os = 'ubuntu'
        break
if os != 'unknown':
    #file = open('distro', 'wr')
    #file.write(os)
    print os
