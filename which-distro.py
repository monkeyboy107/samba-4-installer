#!/usr/bin/python
######################################
#Programmer: Isaac Kerley
#Updated date: 10/6/17
##############Imports#################
import platform                      
#############Varibles#################
distro = 'unknown'                   #Defines the distro var for distro 
platform = platform.platform()       #Gets what the platform is from platform library
distro = platform.split("-")         #Splits for getting what distro it is
######################################
for i in range(len(distro)):         #Iterates through the distro var to see what distro it is
    if distro[i] == 'centos':        #Detects for CentOS
        distro = 'centos'            #Defines disro as centos
        break                        #Leaves the loop
    elif distro[i] == 'fedora':      #Iterates through the distro var to see what distro it is
        distro = 'fedora'            #Detects for Fedora
        break                        #Leaves the loop
    elif distro[i] == 'Ubuntu':      #Detects for Ubuntu
        distro = 'ubuntu'            #Defines disro as ubuntu
        break                        #Leaves the loop
    elif distro[i] == 'debian':      #Detects for Debian
        distro = 'debian'            #Defines disro as debian
        break                        #Leaves the loop
    else:                            #If there aren't any of the supported distros it will say unknown distro
        distro = unknown             #Defines distro as distro unknown
        break                        #Leaves the loop
######################################
if distro != 'unknown':              
    file = open('distro.txt', 'wr')  
    file.write(distro)               
    print distro                     
######################################
