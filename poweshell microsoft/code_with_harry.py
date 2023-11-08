# changing the color of text in command prompt 
# changing the prompt i.e. name of the directory which shows up on everytime we click enter on the prompt i,e..
# C:\Users\rekha><-- this --> C:\Users\rekha>
            # when we write -->help prompt 
            # the following showa up i dont know the usage of it yet but i  surely will . 
            # help prompt
            # Changes the cmd.exe command prompt.

            # PROMPT [text]

            #   text    Specifies a new command prompt.

            # Prompt can be made up of normal characters and the following special codes:

            #   $A   & (Ampersand)
            #   $B   | (pipe)
            #   $C   ( (Left parenthesis)
            #   $D   Current date
            #   $E   Escape code (ASCII code 27)
            #   $F   ) (Right parenthesis)
            #   $G   > (greater-than sign)
            #   $H   Backspace (erases previous character)
            #   $L   < (less-than sign)
            #   $N   Current drive
            #   $P   Current drive and path
            #   $Q   = (equal sign)
            #   $S     (space)
            #   $T   Current time
            #   $V   Windows version number
            #   $_   Carriage return and linefeed
            #   $$   $ (dollar sign)

            # If Command Extensions are enabled the PROMPT command supports
            # the following additional formatting characters:

            #   $+   zero or more plus sign (+) characters depending upon the
            #        depth of the PUSHD directory stack, one character for each
            #        level pushed.

            #   $M   Displays the remote name associated with the current drive
            #        letter or the empty string if current drive is not a network
            #        drive.

            # C:\Users\rekha>$A
            # '$A' is not recognized as an internal or external command,
            # operable program or batch file.

            # C:\Users\rekha>
# provides this weird thing 




# to change the prompt (C:\Users\rekha>) we will write -->  prompt   aloke@hacker$G
# output 
            # C:\Users\rekha>prompt   aloke@hacker$G

            # aloke@hacker>
            # aloke@hacker>
            # aloke@hacker>
            # aloke@hacker>
            # aloke@hacker>
            # aloke@hacker>
            # aloke@hacker>




# next is changing the title 
# the command prompt on abovve itself 
# title  No_system_is_safe


# we can watch starwars movie in cmd --> we need to write 
# Telnet towel.blinkenlights.nl






# hide your personal stuff 
# we will write -->attrib  +h +s +r harry 
# the -->harry folder is gone <-- but if we want to see that again then 
# we will write -->attrib  -h -s -r harry



# if we run the --> dir <-- command 
            #  Volume in drive C is Acer
            #  Volume Serial Number is 88B9-35D9

            #  Directory of C:\Users\rekha

            # 07-04-2023  19:43    <DIR>          .
            # 04-01-2023  07:20    <DIR>          ..
            # 21-03-2023  18:31    <DIR>          .VirtualBox
            # 10-12-2022  01:44    <DIR>          .vscode
            # 06-04-2023  07:14    <DIR>          aloke
            # 06-04-2023  11:46            73,916 battery-report.html
            # 10-12-2022  01:22    <DIR>          Contacts
            # 22-02-2023  21:39                14 demo1.m
            # 11-12-2022  12:01    <DIR>          Documents
            # 06-04-2023  20:01    <DIR>          Downloads
            # 10-12-2022  01:22    <DIR>          Favorites
            # 10-12-2022  01:22    <DIR>          Links
            # 10-12-2022  01:22    <DIR>          Music
            # 08-04-2023  08:20    <DIR>          OneDrive
            # 10-12-2022  01:22    <DIR>          Saved Games
            # 05-01-2023  10:15    <DIR>          Searches
            # 06-01-2023  18:03    <DIR>          Videos
            # 21-03-2023  18:30    <DIR>          VirtualBox VMs
            # 05-04-2023  11:26               865 Wi-Fi-aloke.xml
            # 05-04-2023  11:26               869 Wi-Fi-lucky.xml
            # 05-04-2023  11:26               714 Wi-Fi-mobile.xml
            # 05-04-2023  11:26               908 Wi-Fi-OPPO F17 Pro.xml
            # 05-04-2023  11:26               893 Wi-Fi-TP-Link_2FD6.xml
            # 05-04-2023  11:26               892 Wi-Fi-TP-Link_3068.xml
            #                8 File(s)         79,071 bytes
            #               16 Dir(s)  163,515,658,240 bytes free

            # aloke@hacker>



# when you write --> ipconfig 
# aloke@hacker>ipconfig

            # Windows IP Configuration


            # Ethernet adapter Ethernet:

            #    Media State . . . . . . . . . . . : Media disconnected
            #    Connection-specific DNS Suffix  . :

            # Wireless LAN adapter Local Area Connection* 1:

            #    Media State . . . . . . . . . . . : Media disconnected
            #    Connection-specific DNS Suffix  . :

            # Wireless LAN adapter Local Area Connection* 3:

            #    Media State . . . . . . . . . . . : Media disconnected
            #    Connection-specific DNS Suffix  . :

            # Wireless LAN adapter Wi-Fi:

            #    Connection-specific DNS Suffix  . :
            #    Link-local IPv6 Address . . . . . : fe80::dd91:61bf:5c5c:9872%5
            #    IPv4 Address. . . . . . . . . . . : 192.168.0.101
            #    Subnet Mask . . . . . . . . . . . : 255.255.255.0
            #    Default Gateway . . . . . . . . . : 192.168.0.1

            # aloke@hacker>
# this shows this 




# when we want to  copy the output 
#  we will write 
# ipconfig |clip 
# similarly for dir 
# dir |clip




# if we want to see command history then we will type 
# f7 key
#  you  will see all the commands you have ran since after opening cmd / means of that session  
# or we can also use up/ down/ right  arrow keys to see that.




# if we want to view all the installed programs 
# we will write 
# wmic product get name 
# aloke@hacker>wmic product get name
            # Name
            # Office 16 Click-to-Run Extensibility Component
            # Office 16 Click-to-Run Licensing Component
            # ExpressVPN
            # Microsoft Visual C++ 2019 X86 Additional Runtime - 14.25.28508
            # Microsoft Visual C++ 2019 X64 Additional Runtime - 14.28.29325
            # Microsoft Visual C++ 2019 X64 Minimum Runtime - 14.28.29325
            # Care Center Service

            # Google Update Helper
            # DriverSetupUtility
            # Acer Jumpstart
            # Quick Access Service
            # Acer Configuration Manager
            # Microsoft Visual C++ 2019 X86 Minimum Runtime - 14.25.28508
            # User Experience Improvement Program Service
            # PowerShell 7-preview-x64
            # PowerShell 7-x64


            # aloke@hacker>
# it will list all the programs that are installed in your program and show it to you .
#  



