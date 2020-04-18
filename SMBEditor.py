import sys
import os
import pexpect
import subprocess
import argparse

SHARE_PATH="/mnt/d/Share/"
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
   if(ProjectName in GetSMBConfigs().keys()):
        return
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
    
    with open("/etc/samba/smb.conf","w") as
     f:
        f.write(buffer+ConfigItem)

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