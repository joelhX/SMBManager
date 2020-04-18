


def GetSMBConfigs(): 
    with open("/etc/samba/smb.conf","r") as f:
        buffer=f.read()
        configs=buffer.split("##############################################################")
    print(configs)

def DelSMBConfig(ProjectName): 
    GetSMBConfigs[]

def AddSMBConfig(ProjectName):
    ConfigItem="["+ProjectName+"]"+"""
    comment = """+ProjectName+"""
    path = /mnt/d/share/"""+ProjectName+"""
    valid users = @"""+ProjectName+"""
    browseable = Yes
    read only = No
    writable = yes
    ##############################################################
"""