import os,platform
os.system('git pull')
 
jkw=platform.architecture()[0]
if jkw=="32bit":
    print('Sorry 32 Bit Not Supported...')
elif jkw=="64bit":
     __import__("data")
 
