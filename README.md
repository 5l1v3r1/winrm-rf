```winrm-rf```
===============

A python3 based psuedo-shell for Windows Remote Management. 

### Help Page

```
usage: winrm-shell.py [-h] -u  -p  [-d]

WinRM Shell

positional arguments:
                    Host to connect to

optional arguments:
  -h, --help        show this help message and exit
  -u , --username   Username to authenticate as
  -p , --password   Password to authenticate with
  -d , --domain     The domain said creds will work on
```

### Example

```

█╗    ██╗██╗███╗   ██╗██████╗ ███╗   ███╗      ██████╗ ███████╗
█║    ██║██║████╗  ██║██╔══██╗████╗ ████║      ██╔══██╗██╔════╝
█║ █╗ ██║██║██╔██╗ ██║██████╔╝██╔████╔██║█████╗██████╔╝█████╗  
█║███╗██║██║██║╚██╗██║██╔══██╗██║╚██╔╝██║╚════╝██╔══██╗██╔══╝  
███╔███╔╝██║██║ ╚████║██║  ██║██║ ╚═╝ ██║      ██║  ██║██║     
╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝      ╚═╝  ╚═╝╚═╝     

Connecting to: 10.10.10.10
Using credentials: DOMAIN\administrator:Password1
[12:15:23] >> dir
 Volume in drive C has no label.
 Volume Serial Number is 78E3-E62D

 Directory of C:\Users\Administrator

04/22/2019  06:11 PM    <DIR>          .
04/22/2019  06:11 PM    <DIR>          ..
04/21/2019  11:08 AM    <DIR>          3D Objects
04/21/2019  11:08 AM    <DIR>          Contacts
04/22/2019  09:05 AM    <DIR>          Desktop
04/22/2019  08:13 AM    <DIR>          Documents
04/21/2019  11:08 AM    <DIR>          Downloads
04/21/2019  11:08 AM    <DIR>          Favorites
04/21/2019  11:08 AM    <DIR>          Links
04/21/2019  11:08 AM    <DIR>          Music
04/21/2019  11:08 AM    <DIR>          Pictures
04/21/2019  11:08 AM    <DIR>          Saved Games
04/21/2019  11:08 AM    <DIR>          Searches
04/21/2019  11:08 AM    <DIR>          Videos
               0 File(s)              0 bytes
              14 Dir(s)   5,151,686,656 bytes free
```
