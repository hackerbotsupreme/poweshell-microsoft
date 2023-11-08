# note all that we are runnig in normal cmd 


# but honestly i prefer to  use assoc . so with one command 
#  with that  same command you can specify the file type and have that equal the program we want to use .
#assoc.mp4
            # # C:\Users\rekha>assoc.mp4
            # .mp4=WMP11.AssocFile.MP4

            # C:\Users\rekha>
# see something like this . -->assoc.mp4=VLC.vlc

            # Access is denied.
            # Error occurred while processing: .mp4.

            # C:\Users\rekha>



# hey, is your computer haunted is it goingkind of slow ? does it suck?
# dont throw it away yet .. calm down buddy.
# lets check a few things .
# let's make sure it's okay  with the  command 15 -- chkdsk
            # C:\Users\rekha>chkdsk
            # Access Denied as you do not have sufficient privileges or
            # the disk may be locked by another process.
            # You have to invoke this utility running in elevated mode
            # and make sure the disk is unlocked.

            # C:\Users\rekha>
# it can check on a few things lets see if you need a repair with a for slash.
# command __> chkdsk /f
            # C:\Users\rekha>chkdsk /f
            # Access Denied as you do not have sufficient privileges or
            # the disk may be locked by another process.
            # You have to invoke this utility running in elevated mode
            # and make sure the disk is unlocked.

            # C:\Users\rekha>
# it will actually go through your disk and see if there's any errors and fix them .


# you may wanna try a command 16 -->chkdsk/r --> iit will actually check for physical  sector issues and fix'em . 
            # #  C:\Users\rekha>chkdsk/r
            # Access Denied as you do not have sufficient privileges or
            # the disk may be locked by another process.
            # You have to invoke this utility running in elevated mode
            # and make sure the disk is unlocked.

            # C:\Users\rekha>




# now if that doesnot work and your computer is still scaring the crap outof you 
# then try command 17 --> sfc /scannow 
# sfc stands for system file checker .
# it will check your system files including things like windows DLL files and replace them and fix them if they are bad . 
            # # C:\Users\rekha>sfc /scannow

            # You must be an administrator running a console session in order to
            # use the sfc utility.

            # C:\Users\rekha>
            
# now your computer is really really haunted and still having issues . then,
# now you will need --> DISM /Online /Cleanup /CheckHealth 
# it will check the health
# DISM -->deployment image servicing and management .
# it's a command line tool that actually fix your system image. 
# DISM /Online /Cleanup-Image /CheckHealth 
#C:\Users\rekha>DISM /Online /Cleanup-Image /CheckHealth

            # Error: 740

            # Elevated permissions are required to run DISM.
            # Use an elevated command prompt to complete these tasks.

            # C:\Users\rekha>
# if it's comeup with some scary issues  let's go and restore your health 
# command 20 ---> DISM /Online /Cleanup-Image /RestoreHealth

            # Error: 740

            # Elevated permissions are required to run DISM.
            # Use an elevated command prompt to complete these tasks.

            # C:\Users\rekha>
            
# after we ran the DISM  command lets fo and run the sfc command once more .
# sfc /scanow 
            # C:\Users\rekha>sfc /scanow

            # You must be an administrator running a console session in order to
            # use the sfc utility.

            # C:\Users\rekha>


# dont you hate it when someone takes a bad usb and plugs it into your computer 
# to stop this we need to do two things .first task list .we gotta find the task on our system , the process that's donig something 
# command 21 --> tasklist | findstr script 
# task list will list all of our tasks and using the fine string thing we learned 
#earlier ,  we will find what we are looking for . 
# search for script there it is -->
# tasklist | findstr script 



# and now taking that process id, i can then use task kill to kill that task . 
# command 22--> taskkill /f
# taskkill /f /pid 2018
            # C:\Windows\System32>taskkill /f /pid 2018
            # ERROR: The process "2018" not found.
# here we will specify the pid -->pid 2018<-- and its terminated . 


# now if you thought ip config was cool meet its older brother 
# NETSH
#command--> 23  netsh 
# if you type in --> netsh wlan show wlanreport 
# this will give you a superfancy wireless report of about your wireless .
# by coping that file and paasting that 
# C:\ProgramData\Microsoft\Windows\WlanReport\wlan-report-latest.html
# in the search bar of our browser --> we will get a gorgeous report 




# command 24-- netsh interface show interface 
#netsh interface show interface

        # Admin State    State          Type             Interface Name
        # -------------------------------------------------------------------------
        # Enabled        Connected      Dedicated        Wi-Fi
        # Enabled        Disconnected   Dedicated        Ethernet


        # C:\Windows\System32>
# honestly this function is so so cool we can all day with it . 



# we can do one quick liner to fins the ip address 
# command 25--> netsh interface ip show address |findstr "IP Address"
#C:\Windows\System32>netsh interface ip show address |findstr "IP Address"
            #     IP Address:                           192.168.0.101
            #     IP Address:                           127.0.0.1

            # C:\Windows\System32>
# umm cool dns servers 
# command 26-->netsh interface ip show dnsservers
            # C:\Windows\System32>netsh interface ip show dnsservers

            # Configuration for interface "Ethernet"
            #     DNS servers configured through DHCP:  40.33.1.66
            #     Register with which suffix:           Primary only

            # Configuration for interface "Local Area Connection* 1"
            #     DNS servers configured through DHCP:  None
            #     Register with which suffix:           Primary only

            # Configuration for interface "Local Area Connection* 3"
            #     DNS servers configured through DHCP:  None
            #     Register with which suffix:           Primary only

            # Configuration for interface "Wi-Fi"
            #     DNS servers configured through DHCP:  192.168.0.1
            #     Register with which suffix:           Primary only

            # Configuration for interface "Loopback Pseudo-Interface 1"
            #     Statically Configured DNS Servers:    None
            #     Register with which suffix:           Primary only


            # C:\Windows\System32>
# cool!!!!!!!!!!!!!!
# and even cooler and crazier like you can turn off windows defender firewall itself 
# how crazy is that just type in .
# command 27-- > netsh advfirewall set allprofiles state off 
            # C:\Users\rekha>netsh advfirewall set allprofiles state off
            # The requested operation requires elevation (Run as administrator).


            # C:\Users\rekha>
# notice : do not run it on the administrator command prompt as it will turn off your windows security .






# lets ping network .
# command 28--> ping 
# type in -->ping networkchuck.coffee
            # C:\Windows\System32>ping networkchuck.coffee

            # Pinging networkchuck.coffee [23.227.38.65] with 32 bytes of data:
            # Reply from 23.227.38.65: bytes=32 time=37ms TTL=57
            # Reply from 23.227.38.65: bytes=32 time=38ms TTL=57
            # Reply from 23.227.38.65: bytes=32 time=37ms TTL=57
            # Reply from 23.227.38.65: bytes=32 time=37ms TTL=57

            # Ping statistics for 23.227.38.65:
            #     Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
            # Approximate round trip times in milli-seconds:
            #     Minimum = 37ms, Maximum = 38ms, Average = 37ms

            # C:\Windows\System32>
# cool we are getting response and ping is what you can use to make sure servers and websites are up .
# but it only tell us for four times .
# but what  wanna sit here and watch it  ping it over and over . 
# type in command-30: ping-t then website name or sever's ip address 
# ping -t networkchuck.coffee
# and it will never stop which is super helpful for troubleshooting .
# and it kind of looks like this -->
# Reply from 23.227.38.65: bytes=32 time=37ms TTL=57
            # Reply from 23.227.38.65: bytes=32 time=39ms TTL=57
            # Reply from 23.227.38.65: bytes=32 time=38ms TTL=57
            # Reply from 23.227.38.65: bytes=32 time=40ms TTL=57
            # Reply from 23.227.38.65: bytes=32 time=39ms TTL=57
            # Reply from 23.227.38.65: bytes=32 time=38ms TTL=57
            # Reply from 23.227.38.65: bytes=32 time=37ms TTL=57
            # Reply from 23.227.38.65: bytes=32 time=40ms TTL=57



# lets say if you waanna see road to your favourite website is a bit bumpy .
# command 31--> tracert --> which is windows dumb version of saying Trace route . 
# this will actually trace the path to your favourite website along each router  it takes to get there and tell you if 
# that suckers up or how long it's taking to go -->
# tracert networkchuck.com
# 
            # Tracing route to networkchuck.com [104.26.11.185]
            # over a maximum of 30 hops:

            #   1     1 ms     1 ms     1 ms  192.168.0.1
            #   2     2 ms     2 ms     *     10.9.42.1
            #   3     *        *        *     Request timed out.
            #   4     3 ms     2 ms     3 ms  10.240.246.1
            #   5    39 ms    40 ms    38 ms
            
# and may be that guy is slow so to speed it up we will do -->
# tracert -d
            # C:\Users\rekha>tracert -d
            # A target name or address must be specified.

            # Usage: tracert [-d] [-h maximum_hops] [-j host-list] [-w timeout]
            #                [-R] [-S srcaddr] [-4] [-6] target_name

            # Options:
            #     -d                 Do not resolve addresses to hostnames.
            #     -h maximum_hops    Maximum number of hops to search for target.
            #     -j host-list       Loose source route along host-list (IPv4-only).
            #     -w timeout         Wait timeout milliseconds for each reply.
            #     -R                 Trace round-trip path (IPv6-only).
            #     -S srcaddr         Source address to use (IPv6-only).
            #     -4                 Force using IPv4.
            #     -6                 Force using IPv6.
            
# command netstat is also a cool command for windows . 
# it tells you what connected to you and what you're connecting to . 
# also tells you what ports you have open . 
#netstat
            # #C:\Users\rekha>netstat

            # Active Connections

            #   Proto  Local Address          Foreign Address        State
            #   TCP    127.0.0.1:50269        alokelaptop:50270      ESTABLISHED
            #   TCP    127.0.0.1:50270        alokelaptop:50269      ESTABLISHED
            #   TCP    127.0.0.1:50271        alokelaptop:50272      ESTABLISHED
            #   TCP    127.0.0.1:50272        alokelaptop:50271      ESTABLISHED
            #   TCP    192.168.0.101:51224    20.198.119.84:https    ESTABLISHED
            #   TCP    192.168.0.101:51796    del11s20-in-f10:https  ESTABLISHED
            #   TCP    192.168.0.101:51801    20.198.119.143:https   ESTABLISHED
            #   TCP    192.168.0.101:52507    13.68.168.63:https     ESTABLISHED


# command 34 --> netstat -af 
# it's also gonna show you which ports are open/open ports  .
            # # C:\Users\rekha>netstat -af

            # Active Connections

            #   Proto  Local Address          Foreign Address        State
            #   TCP    0.0.0.0:135            alokelaptop:0          LISTENING
            #   TCP    0.0.0.0:445            alokelaptop:0          LISTENING
            #   TCP    0.0.0.0:5040           alokelaptop:0          LISTENING
            #   TCP    0.0.0.0:49664          alokelaptop:0          LISTENING
            #   TCP    0.0.0.0:49665          alokelaptop:0          LISTENING
            #   TCP    0.0.0.0:49666          alokelaptop:0          LISTENING
            #   TCP    0.0.0.0:49667          alokelaptop:0          LISTENING
            #   TCP    0.0.0.0:49668          alokelaptop:0          LISTENING
            #   TCP    0.0.0.0:49669          alokelaptop:0          LISTENING
            #   TCP    127.0.0.1:24642        alokelaptop:0          LISTENING
            #   TCP    127.0.0.1:50259        alokelaptop:0          LISTENING
            #   TCP    127.0.0.1:50269        alokelaptop:50270      ESTABLISHED
            #   TCP    127.0.0.1:50270        alokelaptop:50269      ESTABLISHED
            #   TCP    127.0.0.1:50271        alokelaptop:50272      ESTABLISHED
            #   TCP    127.0.0.1:50272        alokelaptop:50271      ESTABLISHED
            #   TCP    127.0.0.1:50274        alokelaptop:0          LISTENING
            #   TCP    192.168.0.101:139      alokelaptop:0          LISTENING
            #   TCP    192.168.0.101:51224    20.198.119.84:https    ESTABLISHED
            #   TCP    192.168.0.101:51796    del11s20-in-f10.1e100.net:https  ESTABLISHED
            #   TCP    192.168.0.101:51801    20.198.119.143:https   ESTABLISHED
# and they are open on every single ip address on my system and they are all listening and waiting for connnections .





# netstat can show you the process id (PID) for all your connections .
# command 35--> netstat -o
            # C:\Users\rekha>netstat -o

            # Active Connections

            #   Proto  Local Address          Foreign Address        State           PID
            #   TCP    127.0.0.1:50269        alokelaptop:50270      ESTABLISHED     13236
            #   TCP    127.0.0.1:50270        alokelaptop:50269      ESTABLISHED     13236
            #   TCP    127.0.0.1:50271        alokelaptop:50272      ESTABLISHED     13236
            #   TCP    127.0.0.1:50272        alokelaptop:50271      ESTABLISHED     13236
            #   TCP    192.168.0.101:51224    20.198.119.84:https    ESTABLISHED     3416
            #   TCP    192.168.0.101:51796    del11s20-in-f10:https  ESTABLISHED     9688
# so if there's any dangerous connections,you can drop that pid and delete tthis with task hill.







#and you can get more sweet sweet netstats with -->
# netstat -e -t 5 --> giving you some sent receive statistics every five seconds 
#C:\Users\rekha>netstat -e -t 5
            # Interface Statistics

            #                            Received            Sent

            # Bytes                    1774347996       265623222
            # Unicast packets              670392          572028
            # Non-unicast packets           40266            9690
            # Discards                          0               0
            # Errors                            0               0
            # Unknown protocols                 0
            # Interface Statistics

            #                            Received            Sent

            # Bytes                    1774347996       265623222
            # Unicast packets              670392          572028
            # Non-unicast packets           40266            9690
            # Discards                          0               0
            # Errors                            0               0
            # Unknown protocols                 0
            # Interface Statistics

            #                            Received            Sent

            # Bytes                    1774350870       265624632
            # Unicast packets              670392          572052
            # Non-unicast packets           40290            9690
            # Discards                          0               0
            # Errors                            0               0
            # Unknown protocols                 0





# this one is for the network geeks 
# coomand 37-- > route point 
# this will show you the routes your computer will take to get to certain networks gateways you usse .
            # C:\Users\rekha>route print
            # ===========================================================================
            # Interface List
            #  10...c0 18 50 7d da 8f ......Realtek PCIe GbE Family Controller
            #   8...f6 a4 75 f4 49 76 ......Microsoft Wi-Fi Direct Virtual Adapter
            #   3...f4 a4 75 f4 49 77 ......Microsoft Wi-Fi Direct Virtual Adapter #3
            #   5...f4 a4 75 f4 49 76 ......Intel(R) Dual Band Wireless-AC 3168
            #   1...........................Software Loopback Interface 1
            # ===========================================================================

            # IPv4 Route Table
            # ===========================================================================
            # Active Routes:
            # Network Destination        Netmask          Gateway       Interface  Metric
            #         127.0.0.0        255.0.0.0         On-link         127.0.0.1    331
            #         127.0.0.1  255.255.255.255         On-link         127.0.0.1    331
            #   127.255.255.255  255.255.255.255         On-link         127.0.0.1    331
            #         224.0.0.0        240.0.0.0         On-link         127.0.0.1    331
            #   255.255.255.255  255.255.255.255         On-link         127.0.0.1    331
            # ===========================================================================
            # Persistent Routes:
            #   None

            # IPv6 Route Table
            # ===========================================================================
            # Active Routes:
            #  If Metric Network Destination      Gateway
            #   1    331 ::1/128                  On-link
            #   1    331 ff00::/8                 On-link
            # ===========================================================================
            # Persistent Routes:
            #   None

            # C:\Users\rekha>

# and with the same command we can also add rotes to our computer . 
# allowing us to customize where a computer reaches certain networks .
# route add 192.168.40.0 mask 255.255.255.0 10.7.1.44
# then if you print the route again 
# there it is .
# and with --> route delete  192.168.40.0
# it goes away . 
# it's super handy when you are playing with docker containers on a local vn and you wanna route to ccertain networks .




# and finally the shutdown command .
# shutdown ---> it will shutdown our computer .
# and to restart it to our syatem BIOS   our computer the command will be -->
# shutdown  /r /fw /f /t 0 
# without touching a damn thing .



