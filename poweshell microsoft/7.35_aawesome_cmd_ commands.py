# first we will see a trick to hide all our confidential photos with one cmd command .
# first we will take the photos to a zip folder then copy that 
# type in --> copy /b kitten.jpg(specifying the image )+nc_secrets.zip secret(name of your folder + name of your new secret photo )




# cipher /E
# with this command we can encrypt every file in that folder that no one can open it if they do find it .
# type --> cipher /E --> and the folder i am in  every file encrypted .so now only i can open these files and no one else can't.



# attrib+h+s+r foldername  
# this command is crazy  we can hide our folders from everyehere 
# select the folder you want to polterguist .
# type in --> attrib+h+s+r foldername  --> it's gone .
# and to bring it back --> just do the opposite --> change your + signs to minuses 
#attrib-h-s-r foldername 



# netsh wlan show profile 
# this command will show you every wifi network you have ever connected to 
# but what even crazier  thaat you can even see the wifi password for every network .
# command is --> netsh wlan show profile 
#netsh wlan show profile "wifinetwork name" key = clear | findstr "key Content "
# also we can specify profile like -->  netsh wlan show profile "SeaButterfly" key=clear --> to see the wifi passwordin clear text 
# C:\Users\rekha>netsh wlan show profile

            # Profiles on interface Wi-Fi:

            # Group policy profiles (read only)
            # ---------------------------------
            #     <None>

            # User profiles
            # -------------
            #     All User Profile     : mobile
            #     All User Profile     : lucky
            #     All User Profile     : TP-Link_3068
            #     All User Profile     : TP-Link_2FD6
            #     All User Profile     : OPPO F17 Pro
            #     All User Profile     : aloke


            # C:\Users\rekha>netsh wlan show profile "aloke" key=clear

            # Profile aloke on interface Wi-Fi:
            # =======================================================================

            # Applied: All User Profile

            # Profile information
            # -------------------
            #     Version                : 1
            #     Type                   : Wireless LAN
            #     Name                   : aloke
            #     Control options        :
            #         Connection mode    : Connect automatically
            #         Network broadcast  : Connect only if this network is broadcasting
            #         AutoSwitch         : Do not switch to other networks
            #         MAC Randomization  : Disabled

            # Connectivity settings
            # ---------------------
            #     Number of SSIDs        : 1
            #     SSID name              : "aloke"
            #     Network type           : Infrastructure
            #     Radio type             : [ Any Radio Type ]
            #     Vendor extension          : Not present

            # Security settings
            # -----------------
            #     Authentication         : WPA2-Personal
            #     Cipher                 : CCMP
            #     Authentication         : WPA2-Personal
            #     Cipher                 : GCMP
            #     Security key           : Present
            #     Key Content            : z/2aB@22

            # Cost settings
            # -------------
            #     Cost                   : Unrestricted
            #     Congested              : No
            #     Approaching Data Limit : No
            #     Over Data Limit        : No
            #     Roaming                : No
            #     Cost Source            : Default


            # C:\Users\rekha>

# if you wanna see all wifi password 
# this crazy command will allow you to do so 
# for /f skip"skip=9 tokens=1,2 delims=:" %i in ('netsh wlan show profile' )do @if "%j" NEQ "" (echo SSID: %j & netsh wlan show profiles %j key=clear | findstr "key content") & echo.
# we just have make some changes and we will get to see all the passwords of surrounding networks . 




# now that may too much info to paarse through command prompt what do you say we put into a file 
# lets do  that same command once more and at the very end we will do 
# for /f skip"skip=9 tokens=1,2 delims=:" %i in ('netsh wlan show profile' )do @if "%j" NEQ "" (echo SSID: %j & netsh wlan show profiles %j key=clear | findstr "key content")>>wifipasswords.txt(which is the name of our file )
# and bam all right there in a file ! 



# now the main problem with the long command s is you can not memorixe them 
# so ehata do we say we put it into a batch file . 
# open notepad  copy&paste in this command --> file --> save as --> .txt -->save type as 
# --> all files --> file name --> wifi.batch --> now we just have to type in wifi.batch in the command prompt 
# -->and ther we go . 




# systeminfo
# this is the quick way to find out all the info on your system 
# it shows you your system info . 

            # C:\Users\rekha>systeminfo

            # Host Name:                 ALOKELAPTOP
            # OS Name:                   Microsoft Windows 11 Home Single Language
            # OS Version:                10.0.22623 N/A Build 22623
            # OS Manufacturer:           Microsoft Corporation
            # OS Configuration:          Standalone Workstation
            # OS Build Type:             Multiprocessor Free
            # Registered Owner:          rekhapramanik567984@gmail.com
            # Registered Organization:   N/A
            # Product ID:                00356-24535-66684-AAOEM
            # Original Install Date:     09-12-2022, 23:31:10
            # System Boot Time:          05-04-2023, 21:46:15
            # System Manufacturer:       Acer
            # System Model:              Aspire A315-23
            # System Type:               x64-based PC
            # Processor(s):              1 Processor(s) Installed.
            #                            [01]: AMD64 Family 23 Model 24 Stepping 1 AuthenticAMD ~2600 Mhz
            # BIOS Version:              Insyde Corp. V1.20, 22-12-2021
            # Windows Directory:         C:\WINDOWS
            # System Directory:          C:\WINDOWS\system32
            # Boot Device:               \Device\HarddiskVolume1
            # System Locale:             en-us;English (United States)
            # Input Locale:              00004009
            # Time Zone:                 (UTC+05:30) Chennai, Kolkata, Mumbai, New Delhi
            # Total Physical Memory:     3,521 MB
            # Available Physical Memory: 312 MB
            # Virtual Memory: Max Size:  8,897 MB
            # Virtual Memory: Available: 3,926 MB
            # Virtual Memory: In Use:    4,971 MB
            # Page File Location(s):     C:\pagefile.sys
            # Domain:                    WORKGROUP
            # Logon Server:              \\ALOKELAPTOP
            # Hotfix(s):                 6 Hotfix(s) Installed.
            #                            [01]: KB5022497
            #                            [02]: KB5012170
            #                            [03]: KB5015669
            #                            [04]: KB5018863
            #                            [05]: KB5021866
            #                            [06]: KB5020487
            # Network Card(s):           2 NIC(s) Installed.
            #                            [01]: Intel(R) Dual Band Wireless-AC 3168
            #                                  Connection Name: Wi-Fi
            #                                  DHCP Enabled:    Yes
            #                                  DHCP Server:     192.168.0.1
            #                                  IP address(es)
            #                                  [01]: 192.168.0.101
            #                                  [02]: fe80::dd91:61bf:5c5c:9872
            #                            [02]: Realtek PCIe GbE Family Controller
            #                                  Connection Name: Ethernet
            #                                  Status:          Media disconnected
            # Hyper-V Requirements:      A hypervisor has been detected. Features required for Hyper-V will not be displayed.

            # C:\Users\rekha>   


# scp     file.txt  root@serverip:~/file.txt
#      **file name**server name **
# it lets you copy a file to a remote server securely ,type in the file you want to copy and then the username and the server you want to copy to 
# authenticate with your password then bam , the file is copied .




# type in 'cmd' in explorer 
# i mean lets say you are in a location and then if you cut that location and type cmd then 
# the cmd will open up in that location . 




# you can also do the same in reverse 
# whreever you are , open the cmd type in explorer --> place . rigth after that 
# explore window will open right where you are 





# subst q:c:\filelocation 
# do you know that you can map any folder on your system as a mounted tribes ...
# 



# and to undo that command is : subst /d q:





# let's make your command promt pretty , just type in 
# color 07 {background:tex}
# color 24 (picking some random number )
# not really 2 will be the color of the background  and  4 will be the color of the text . 
            #   0 = Black       8 = Gray
            #     1 = Blue        9 = Light Blue
            #     2 = Green       A = Light Green
            #     3 = Aqua        B = Light Aqua
            #     4 = Red         C = Light Red
            #     5 = Purple      D = Light Purple
            #     6 = Yellow      E = Light Yellow
            #     7 = White       F = Bright White
# here is the color code and the rest is on you .


#if you want some help with ? then you can type in 
# color /?
# this will show you all things you need . 
# color 70 is cool 




# we can also make it more pretty 
# prompt {text}$G
# to reset it type : prompt
# prompt 








# you can change the title of the window as well .
# title{stuff}
# like --> title {THE BOYZ}
# look at that . 




# how much can you curl. 
# curl wttr.in/location --> this command is crazy  .
# curl wttr.in/kolkata
# ahh! whether it literally showing us the whether .




# this is also pretty cool
# you can actually unshorten shorten links .
# type--> curl --head --location "the shorten url "
# and then because we only care about the location of it , where it's going .
# we'll do a bracket . we'll type -->
# curl --head --location "the shorten url "|findstr location 





# you can also see the status of a website if it's up .
# type in --> curl -Is the website 
# curl -Is  https :// networkchuck .com

            # C:\Users\rekha>curl -Is  https://networkchuck.com
            # HTTP/1.1 200 OK
            # Date: Fri, 07 Apr 2023 06:06:06 GMT
            # Content-Type: text/html; charset=UTF-8
            # Connection: keep-alive
            # CF-Ray: 7b401524fe09f377-BOM
            # Link: <https://networkchuck.com/>; rel=shortlink
            # CF-Cache-Status: DYNAMIC
            # cf-apo-via: origin,host
            # Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=BTXSi%2BcUEIikvJfla2ZjkUPsBL5l2rz1UHg1lc4xDEOs%2BYIUaKUKZRYJ%2FvpAz4PyX3u0sBGJnHn3f9mF7bFMHdy1gbSRcvbdXn%2FsIwL1a679LKL%2BcmFpgU7kSovCjbnzhQ4%3D"}],"group":"cf-nel","max_age":604800}
            # NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
            # Server: cloudflare


            # C:\Users\rekha>



# curl continues . what's your public IP address .
# curl checkip.amazonaws.com
            # # C:\Users\rekha>curl checkip.amazonaws.com
            # 103.193.91.153

            # C:\Users\rekha>

# this is also crazy , you can use curl from your command prompt to create a QR code 
# curl qrenco.de//https://networkchuck.coffee
# curl qrenco.de//https://google.com
# C:\Users\rekha>curl qrenco.de//https://google.com
            # █████████████████████████████████
            # █████████████████████████████████
            # ████ ▄▄▄▄▄ ██▀▀▄▄█ █▀█ ▄▄▄▄▄ ████
            # ████ █   █ █▀███ █ ▀ █ █   █ ████
            # ████ █▄▄▄█ █▄▄█▀▀ ██ █ █▄▄▄█ ████
            # ████▄▄▄▄▄▄▄█▄█ ▀▄█▄▀▄█▄▄▄▄▄▄▄████
            # ████  █▀▀ ▄ █ █▄▀▀▀ ███▀  ▀▀█████
            # █████▄█▀██▄ ▄▀▄█▀ ▄ ▀ █ ▄ █▄ ████
            # ████  ██ █▄█  █▄▄▄█▀▄█▄ ███▀▄████
            # ████ █▀█  ▄▀▀▀█ ▄██▄▄ █ ▄ ▀▄ ████
            # ████▄████▄▄█ ▀▀▄▀▀▀▄ ▄▄▄ █▄██████
            # ████ ▄▄▄▄▄ █ █ ▄▀▀█▀ █▄█ ██▀▄████
            # ████ █   █ ██▀▄█▄█ ▄   ▄▄█▄▀ ████
            # ████ █▄▄▄█ █▀▄█ ▄█▀█ ▀▀▀▀▄▄█ ████
            # ████▄▄▄▄▄▄▄█▄▄███▄▄█▄████▄██▄████
            # █████████████████████████████████
            # █████████████████████████████████

            # C:\Users\rekha>



# you dont have to rely on youtube to knnow when i upload a video .
# you can use the command prompt .
# curl -s https://decapi.me/youtube/latest_video?user=networkchuck
            # #C:\Users\rekha> curl -s https://decapi.me/youtube/latest_video?user=networkchuck
            # Kids vs. MALWARE!! - https://youtu.be/bZ7PAzrWyvc
            # C:\Users\rekha>
            
# you can also do it for other platforms 
#  curl -s https://decapi.me/twitter/latest?name=networkchuck
                # #C:\Users\rekha>curl -s https://decapi.me/twitter/latest?name=networkchuck
                # Have you seen our new merch? 👀   ——-> https://t.co/xjAlm7qG7P https://t.co/9vRm2lGFGC
                # C:\Users\rekha>



# why i feel like i never ever have to leave the command prompt . yeah! point of this video.


# curl dict.org/d:website 
# "d" for dictionary and then the word . 
# you can define a word right in command .
# and it will show you what you are searching for  .
# C:\Users\rekha>curl dict.org/d:website
            # 220 dict.dict.org dictd 1.12.1/rf on Linux 4.19.0-10-amd64 <auth.mime> <180835293.3561.1680850236@dict.dict.org>
            # 250 ok
            # 150 1 definitions retrieved
            # 151 "website" wn "WordNet (r) 3.0 (2006)"
            # website
            #     n 1: a computer connected to the internet that maintains a
            #          series of web pages on the World Wide Web; "the Israeli web
            #          site was damaged by hostile hackers" [syn: {web site},
            #          {website}, {internet site}, {site}]
            # .
            # 250 ok [d/m/c = 1/0/28; 0.000r 0.000u 0.000s]
            # 221 bye [d/m/c = 0/0/0; 0.000r 0.000u 0.000s]

            # C:\Users\rekha>
# and there we go the meaning of the "wbsite " is rigt here .





# did you know you can use chatgpt from the command line 
# we are gonna type in --> 
# curl https://api.openai.com/v1/chat/completions -H "Authorization: _____________________________________________" -H  "Content-Type: application/json"  -d "{\"model\":\"gpt-3.5-turbo\,\"messages\":[{\"role\":}\"user\",\"content\":\"question?\"}]}"
# find out what gonna be on the fill in the blanks then you are ready to go 




# you can open a website right from your  terminal with these two commands 
#  start website name 
# start www.google.com
            # C:\Users\rekha>start www.google.com

            # C:\Users\rekha>
# and there we go its crazy its literally awesome ! 



# with these two commands below we can delete all temporary files to save some space if you are running out of space  
# del/q /f /s %temp%\*
# del /s /q C:\Windows\temp\*


# type in telnet to see if youu have it or not . 
# then hit windowskey + s . search for features and click on that first option . we are going to enable telnet . 
# telnet telehack.com
# its a protocol , find telnet , click on it enable it . 
# tupe in telnet in the command prompt 
# exit 
# exit()
# leave 
# it gonna be like this , how do i get out of it ? see by youurself ..
            # Welcome to Microsoft Telnet Client                                                                                                                                                                                                                                                                                      Escape Character is 'CTRL+]'                                                                                                                                                                                                                                                                                            Microsoft Telnet> exit                                                                                                                                      Invalid Command. type ?/help for help                                                                                                                       Microsoft Telnet> exit(                                                                                                                                     Invalid Command. type ?/help for help                                                                                                                       Microsoft Telnet> exit()                                                                                                                                    Invalid Command. type ?/help for help                                                                                                                       Microsoft Telnet> /                                                                                                                                         Invalid Command. type ?/help for help                                                                                                                       Microsoft Telnet> ?                                                                                                                                                                                                                                                                                                     Commands may be abbreviated. Supported commands are:                                                                                                                                                                                                                                                                    c    - close                    close current connection                                                                                                    d    - display                  display operating parameters                                                                                                o    - open hostname [port]     connect to hostname (default port 23).                                                                                      q    - quit                     exit telnet                                                                                                                 set  - set                      set options (type 'set ?' for a list)                                                                                       sen  - send                     send strings to server                                                                                                      st   - status                   print status information                                                                                                    u    - unset                    unset options (type 'unset ?' for a list)                                                                                   ?/h  - help                     print help information                                                                                                      Microsoft Telnet> q                                                                                                                                         
            #c    - close                    close current connection                    
            # d    - display                  display operating parameters      
            # o    - open hostname [port]     connect to hostname (default port 23). 
            # q    - quit                     exit telnet                             
            # set  - set                      set options (type 'set ?' for a list)   
            # sen  - send                     send strings to server                  
            # st   - status                   print status information                
            # u    - unset                    unset options (type 'unset ?' for a list) 
            # ?/h  - help                     print help information  
# now thats sweet











# one more cool thing is , type in -->
# telnet telehack.com
# ready ? 
# go?
                # Escape Character is 'CTRL+]'                                                                                                                                                                                                                                                                                            Microsoft Telnet> exit                                                                                                                                      Invalid Command. type ?/help for help                                                                                                                       
                # Connected to TELEHACK port 75

                # It is 12:37 am on Friday, April 7, 2023 in Mountain View, California, USA.
                # There are 119 local users. There are 26647 hosts on the network.

                #   Type HELP for a detailed command list.
                #   Type NEWUSER to create an account.

                # May the command line live forever.

                # Command, one of the following:
                #   2048         a2           ac           advent       aquarium     basic
                #   bf           c8           cal          calc         callsign     cat
                #   ching        clear        clock        cowsay       date         ddate
                #   delta        diff         dir          exit         file         finger
                #   fnord        help         ipaddr       liff         login        mac
                #   md5          minesweeper  netstat      newuser      octopus      phoon
                #   pong         privacy      rain         rfc          roll         rot13
                #   run          salvo        sleep        starwars     sudoku       tail
                #   traceroute   typespeed    units        uptime       users        uumap
                #   uupath       uuplot       weather      when         zc           zork

                # Press control-C to interrupt any command.
                # More commands become available after login.
                # .
# now pick your poison , like maybe you wanna watch starwars (in line 450)
# in terminal ? why not suuuuuuuuuuuuuuuuuuuuuu.............................
# type in starwars 
# magic
# press ctrl+c to stop it .
# type in in the terminal -->aquarium(line 443).  
# awesome !


# now its time for the f's.
# f1 to f9 



# type in f1 
# how we can press f1-f9 we gotta find out .






# if you want to see the history of commands you have used in cmd 
# doskey /history 
# and you will find out everything you ever did  in since opening cmd 







# try to use the terminal/powershell . the new bad boy . 
#unfortunately cmd is now old. and why becaause cmd is default to it so that means we can open and use it whenever we needs it in just ine click .  
# and because we are in terminal it opens up some new features .
# for example drag and drop files .
# maybe you are like secure copy to copy feature but you are like man? what's that file name .
# scp location 
# explore find it .. and drag it to the powershelland it copies it .
# literally besiides can you imagine typing this out .







# another cool thing no matter where you are in explorer  you can shift+right click a folder and say open in terminal and bam there you are .
# if you need help just type in help  in the powershell/terminal .
# it will show you all the commands you need  proceed forward 
# in cmd . 
#C:\Users\rekha>help
            # For more information on a specific command, type HELP command-name
            # ASSOC          Displays or modifies file extension associations.
            # ATTRIB         Displays or changes file attributes.
            # BREAK          Sets or clears extended CTRL+C checking.
            # BCDEDIT        Sets properties in boot database to control boot loading.
            # CACLS          Displays or modifies access control lists (ACLs) of files.
            # CALL           Calls one batch program from another.
            # CD             Displays the name of or changes the current directory.
            # CHCP           Displays or sets the active code page number.
            # CHDIR          Displays the name of or changes the current directory.
            # CHKDSK         Checks a disk and displays a status report.
            # CHKNTFS        Displays or modifies the checking of disk at boot time.
            # CLS            Clears the screen.
            # CMD            Starts a new instance of the Windows command interpreter.
            # COLOR          Sets the default console foreground and background colors.
            # COMP           Compares the contents of two files or sets of files.
            # COMPACT        Displays or alters the compression of files on NTFS partitions.
            # CONVERT        Converts FAT volumes to NTFS.  You cannot convert the
            #                current drive.
            # COPY           Copies one or more files to another location.
            # DATE           Displays or sets the date.
            # DEL            Deletes one or more files.
            # DIR            Displays a list of files and subdirectories in a directory.
            # DISKPART       Displays or configures Disk Partition properties.
            # DOSKEY         Edits command lines, recalls Windows commands, and
            #                creates macros.
            # DRIVERQUERY    Displays current device driver status and properties.
            # ECHO           Displays messages, or turns command echoing on or off.
            # ENDLOCAL       Ends localization of environment changes in a batch file.
            # ERASE          Deletes one or more files.
            # EXIT           Quits the CMD.EXE program (command interpreter).
            # FC             Compares two files or sets of files, and displays the
            #                differences between them.
            # FIND           Searches for a text string in a file or files.
            # FINDSTR        Searches for strings in files.
            # FOR            Runs a specified command for each file in a set of files.
            # FORMAT         Formats a disk for use with Windows.
            # FSUTIL         Displays or configures the file system properties.
            # FTYPE          Displays or modifies file types used in file extension
            #                associations.
            # GOTO           Directs the Windows command interpreter to a labeled line in
            #                a batch program.
            # GPRESULT       Displays Group Policy information for machine or user.
            # GRAFTABL       Enables Windows to display an extended character set in
            #                graphics mode.
            # HELP           Provides Help information for Windows commands.
            # ICACLS         Display, modify, backup, or restore ACLs for files and
            #                directories.
            # IF             Performs conditional processing in batch programs.
            # LABEL          Creates, changes, or deletes the volume label of a disk.
            # MD             Creates a directory.
            # MKDIR          Creates a directory.
            # MKLINK         Creates Symbolic Links and Hard Links
            # MODE           Configures a system device.
            # MORE           Displays output one screen at a time.
            # MOVE           Moves one or more files from one directory to another
            #                directory.
            # OPENFILES      Displays files opened by remote users for a file share.
            # PATH           Displays or sets a search path for executable files.
            # PAUSE          Suspends processing of a batch file and displays a message.
            # POPD           Restores the previous value of the current directory saved by
            #                PUSHD.
            # PRINT          Prints a text file.
            # PROMPT         Changes the Windows command prompt.
            # PUSHD          Saves the current directory then changes it.
            # RD             Removes a directory.
            # RECOVER        Recovers readable information from a bad or defective disk.
            # REM            Records comments (remarks) in batch files or CONFIG.SYS.
            # REN            Renames a file or files.
            # RENAME         Renames a file or files.
            # REPLACE        Replaces files.
            # RMDIR          Removes a directory.
            # ROBOCOPY       Advanced utility to copy files and directory trees
            # SET            Displays, sets, or removes Windows environment variables.
            # SETLOCAL       Begins localization of environment changes in a batch file.
            # SC             Displays or configures services (background processes).
            # SCHTASKS       Schedules commands and programs to run on a computer.
            # SHIFT          Shifts the position of replaceable parameters in batch files.
            # SHUTDOWN       Allows proper local or remote shutdown of machine.
            # SORT           Sorts input.
            # START          Starts a separate window to run a specified program or command.
            # SUBST          Associates a path with a drive letter.
            # SYSTEMINFO     Displays machine specific properties and configuration.
            # TASKLIST       Displays all currently running tasks including services.
            # TASKKILL       Kill or stop a running process or application.
            # TIME           Displays or sets the system time.
            # TITLE          Sets the window title for a CMD.EXE session.
            # TREE           Graphically displays the directory structure of a drive or
            #                path.
            # TYPE           Displays the contents of a text file.
            # VER            Displays the Windows version.
            # VERIFY         Tells Windows whether to verify that your files are written
            #                correctly to a disk.
            # VOL            Displays a disk volume label and serial number.
            # XCOPY          Copies files and directory trees.
            # WMIC           Displays WMI information inside interactive command shell.

            # For more information on tools see the command-line reference in the online help.

            # C:\Users\rekha>













# in terminal / powershell 
            # Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

            # PS C:\Users\rekha> help

            # TOPIC
            #     Windows PowerShell Help System

            # SHORT DESCRIPTION
            #     Displays help about Windows PowerShell cmdlets and concepts.

            # LONG DESCRIPTION
            #     Windows PowerShell Help describes Windows PowerShell cmdlets,
            #     functions, scripts, and modules, and explains concepts, including
            #     the elements of the Windows PowerShell language.

            #     Windows PowerShell does not include help files, but you can read the
            #     help topics online, or use the Update-Help cmdlet to download help files
            #     to your computer and then use the Get-Help cmdlet to display the help
            #     topics at the command line.

            #     You can also use the Update-Help cmdlet to download updated help files
            #     as they are released so that your local help content is never obsolete.

            #     Without help files, Get-Help displays auto-generated help for cmdlets,
            #     functions, and scripts.


            #   ONLINE HELP
            #     You can find help for Windows PowerShell online in the TechNet Library
            #     beginning at http://go.microsoft.com/fwlink/?LinkID=108518.

            #     To open online help for any cmdlet or function, type:
            # -- More  --





 
# 
                # what is url

                # A URL (Uniform Resource Locator) is a specific type of URI (Uniform Resource Identifier) that is used to identify the location of a resource on the internet.

                # A URL typically consists of several parts, including the protocol (such as HTTP or HTTPS), the domain name (such as www.example.com), and the path to the specific resource or page (such as /about-us). For example, the URL for the Google homepage is https://www.google.com/.

                # URLs are used to locate web pages, images, videos, and other types of resources on the internet, and they can be typed directly into a web browser's address bar or included in hyperlinks on web pages or in emails.




                # aloke.geek@gmail.com
                # what is link
                # In the context of the internet and web browsing, a link is a clickable element or object on a web page that takes you to another location or resource on the internet when you click on it. Links are often highlighted in a different color or underlined to make them stand out from the surrounding text or images.

                # Links can be used to navigate between different web pages, access downloadable files, view images or videos, or even initiate actions such as submitting a form or sending an email. Links can also be used to reference content on the same web page or within the same document, allowing users to quickly jump to a specific section of the page or document.

                # Links can be created using HTML code, which specifies the destination URL and the text or image that should be displayed as the link. Links can also be created in other formats such as PDFs, emails, and social media posts.




                # aloke.geek@gmail.com
                # what is the difference between link and url 
                # A link and a URL (Uniform Resource Locator) are related concepts, but they refer to slightly different things.

                # A URL is a specific type of URI (Uniform Resource Identifier) that is used to identify the location of a resource on the internet. It typically consists of the protocol (such as HTTP or HTTPS), the domain name (such as www.example.com), and the path to the specific resource or page (such as /about-us).

                # On the other hand, a link is a clickable element or object on a web page that takes you to another location or resource on the internet when you click on it. A link can be created using a URL as its destination, but it can also be used to reference content on the same web page or within the same document.

                # In other words, a URL is a specific identifier that points to a resource on the internet, while a link is a clickable element that can use a URL as its destination or point to content within the same document.


        # PS C:\WINDOWS\system32> winget
        # Windows Package Manager v1.4.10173
        # Copyright (c) Microsoft Corporation. All rights reserved.

        # The winget command line utility enables installing applications and other packages from the command line.

        # usage: winget  [<command>] [<options>]

        # The following commands are available:
        #   install    Installs the given package
        #   show       Shows information about a package
        #   source     Manage sources of packages
        #   search     Find and show basic info of packages
        #   list       Display installed packages
        #   upgrade    Shows and performs available upgrades
        #   uninstall  Uninstalls the given package
        #   hash       Helper to hash installer files
        #   validate   Validates a manifest file
        #   settings   Open settings or set administrator settings
        #   features   Shows the status of experimental features
        #   export     Exports a list of the installed packages
        #   import     Installs all the packages in a file

        # For more details on a specific command, pass it the help argument. [-?]

        # The following options are available:
        #   -v,--version              Display the version of the tool
        #   --info                    Display general info of the tool
        #   -?,--help                 Shows help about the selected command
        #   --wait                    Prompts the user to press any key before exiting
        #   --verbose,--verbose-logs  Enables verbose logging for WinGet
        #   --disable-interactivity   Disable interactive prompts

        # More help can be found at: https://aka.ms/winget-command-help
        # PS C:\WINDOWS\system32>









