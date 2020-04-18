import sys
import os
import pexpect
import subprocess

SHARE_PATH="/mnt/d/Share/"
def AddGroup(ProjectName):
    subprocess.call(["/usr/sbin/groupadd",ProjectName])
    try:
        os.mkdir(SHARE_PATH+ProjectName)
        os.chgrp(SHARE_PATH+ProjectName,ProjectName)
    except:
        None

def AddUser(user):
    subprocess.call(["/usr/sbin/adduser","-M","-N",user])
    subprocess.call(["/usr/sbin/usermod","-a", "-G",ProjectName,user])
 
    password=user
    child = pexpect.spawn("/usr/bin/smbpasswd -a "+user)
    child.expect("New SMB password:")
    child.sendline (password)
    child.expect ("Retype new SMB password:")
    child.sendline (password)

def AddSMBConfig(ProjectName):
    ConfigItem="""##############################################################
["""+ProjectName+"""]
    comment = """+ProjectName+"""
    path = """+SHARE_PATH+ProjectName+"""
    valid users = @"""+ProjectName+"""
    browseable = Yes
    read only = No
    writable = yes

"""

    with open("/etc/samba/smb.conf","r") as f:
        buffer=f.read()
    
    with open("/etc/samba/smb.conf","w") as f:
        f.write(buffer+ConfigItem)



def GetSMBConfigs(): 
    Conf=dict()
    with open("/etc/samba/smb.conf","r") as f:
        buffer=f.read()
        configs=buffer.split("##############################################################")
    for config in configs:
        PrjName=config.split("]")[0].split("[")[1]
        Conf[PrjName]=config
    return Conf
    
if __name__ == "__main__":
    option=sys.argv[1]
    ProjectName = sys.argv[2]

    if(option=="-a"):
        AddGroup(ProjectName)
        AddSMBConfig(ProjectName)
        with open(ProjectName+".users","r") as f:
            for user in f.read().splitlines():
                AddUser(user)
    
    elif(option=="-d"):
        Confs=GetSMBConfigs()
        try:
            del Confs[ProjectName]
            with open("/etc/samba/smb.conf","w") as f:
                for k,v in Confs.items():
                    f.write(v)
        
        except:
            print("Can't find ProjectNsmr")