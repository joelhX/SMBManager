def AddGroup(ProjectName):
    subprocess.call(["/usr/sbin/groupadd",ProjectName])
    try:
        os.mkdir(SHARE_PATH+ProjectName)
        os.chgrp(SHARE_PATH+ProjectName,ProjectName)
    except:
        None



def AddUser(ProjectName,user):
    subprocess.call(["/usr/sbin/adduser","-M","-N",user])
    subprocess.call(["/usr/sbin/usermod","-a", "-G",ProjectName,user])
    password=user
    child = pexpect.spawn("/usr/bin/smbpasswd -a "+user)
    child.expect("New SMB password:")
    child.sendline (password)
    child.expect ("Retype new SMB password:")
    child.sendline (password)
    