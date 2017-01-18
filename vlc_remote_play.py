"""" VLC Remote Play/Pause Request by saarkia 
 This code will use the requests library to pull a play/pause request to VLC
 Make sure that VLC is set up for HTTP interface first
 For more information visit https://wiki.videolan.org/documentation:modules/http_intf/

 Make sure to edit the password in line 13, and IP address in line 15 """



import requests
def getInfo():
    s = requests.Session()
    s.auth = ('', '1234')
    # Auth is username then password - username is blank, set password to match VLC
    r = s.get('http://192.168.1.17:8080/requests/status.xml?command=pl_pause', verify=False)
    # Edit the IP address (xxx.xxx.x.xx) in the line above to match the target computer
    print "Command Executed"

getInfo()