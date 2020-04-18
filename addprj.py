import sys
import os
import pexpect
import subprocess
import argparse

SHARE_PATH="/mnt/d/Share/"
def AddGroup(ProjectName):
    subprocess.call(["/usr/sbin/groupadd",ProjectName])
    try:
        os.mkdir(SHARE_PATH+ProjectName)
        os.chgrp(SHARE_PATH+ProjectName,ProjectName)
    except:
        None


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

def a(ProjectName):
    AddGroup(ProjectName)
    if(ProjectName in GetSMBConfigs().keys()):
        return
    AddSMBConfig(ProjectName)
    with open(ProjectName+".users","r") as f:
        for user in f.read().splitlines():
            AddUser(ProjectName,user)

def d(ProjectName):
    Confs=GetSMBConfigs()
    try:
        del Confs[ProjectName]
        with open("/etc/samba/smb.conf","w") as f:
            for k,v in Confs.items():
                f.write(v)
    except:
        print("Can't find ProjectNsmr")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a',  action='store', help="add Project")
    parser.add_argument('-d',  action='store', help="delete Project")
    args = parser.parse_args()
    for k,v in vars(args).items():
        if v!=None:
            eval(k)(v)