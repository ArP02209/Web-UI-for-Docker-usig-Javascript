#!/usr/bin/python3

import cgi
import subprocess
import time


print("content-type:  text/html")
print()

#time.sleep(10)
f=cgi.FieldStorage()
cmd=f.getvalue("x")
cname=f.getvalue("y")
imgname=f.getvalue("z")
cmdname=f.getvalue("c")
cmd=cmd.split()
#print(cmdname)
#Launch/Run Docker containers
if ((("launch") or ("run")) in cmd) == True:	
    print(subprocess.getoutput("sudo docker run -dit --name {} {}".format(cname,imgname)))

#List currently running containers
elif ((("list") or ("show")) and ("containers") and ("current")) in cmd:
    print(subprocess.getoutput("sudo docker ps"))
    
#List all containers
elif ((("show")or ("list")) and (("all") and ("containers"))) in cmd:
    print(subprocess.getoutput("sudo docker ps -a"))

#List all docker images
elif ((("show") or ("list") or ("display")) and ("images")) in cmd:
    print(subprocess.getoutput("sudo docker images"))

#Remove running container
elif ((("remove")or("delete")or("terminate")) and ("container")) in cmd:
    print(subprocess.getoutput("sudo docker rm -f {}".format(cname)))

#Execute shell command on docker container while launching
elif ((("execute") or ("run")) and ("command")) in cmd:
    print(subprocess.getoutput("sudo docker exec {} {}".format(cname,cmdname)))

else:
    print("Plz enter your command again")	
