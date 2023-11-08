# directory direirectory means location and that refers to folder  . 
# we can make folders on a  location /folder /diretory using mkdir command . 
# like ==   mkdir then name of the folder we want to create . mkdir aloke .
# and then we want to rename the folder then what we need to do  is to type in - 
# ren_space_aloke(name of the folder )_space_samar(new name)
# and then we want to hop inside our new folder so we will type-->
# cd_space_samar.--> and now we want to make a ppt file inside of it -->type the following -->
# (name of the file)fort.pptx --> enter --> and to perform the rename again -->
# ren_space_aloke(name of the file )_space_samar(new file)  --->
# ren_space_fort.ppt.x_space_india.pptx ---> one thing to note here is --->after .something 
# implies the type of the file and that's why there is india then .pptx is there as .ppt is 
# file type of india file. and now if we want to copy the file to the another directory 
# or location ---> command is --->copy_space_india.pptx_space_hip  ---> 
# to take a step back command is ---> cd..(take a step back )
# now we want to delete the file ---> in order to delete the file ---> first we have to move 
# to the location/directory / folder we want to delete --->cd_space_hip--->
# del_space_india.pptx --->enter ---> then the file will be deleted . 
# untill now we learened to change the location and bout folder such as  have made , copied and deleted the file if we want to move the file then--->
# move_space_india.pptx_space_hip(folder name)
# and to delete a folder --> rmdir_space_hip -->enter -->
# the  folder will be deleted . 





# cmd command course to start and stop tasks and processes 

# before that we need to understand what bootup is ? 
# whenever we turn on our computer , it loads up some files which mostly are os files 
# and the process is named booting / bootup .
# and during booting/bootup compter runs/processes some tasks by default ex- themes , audio 
# and in this session we will learn how to start and stop some of the processes/tasks . 
# ok , so what are tasks -- > when we right click on the windows toolbar and go to task manager 
# we will see a few a things here. 
# if there is no task or 0 tasks(running processes like software or a program) is running on the system 
# 
# and what is firewall ? firewall is a type of service which prvides via our os in order to protect our os from malwares and attacks .
# and the craziest thing is that  we  can turn it off or on using cmd . so learning cmd is very imp. 
# what are srevices ? the os related  processes which runs automatically is called services .    


# now its time for the commands 
# task list 
# when we type tasklist , it we will get to see the tasks which are currently running on our system .
# C:\Users\rekha>tasklist

            # Image Name                     PID Session Name        Session#    Mem Usage
            # ========================= ======== ================ =========== ============
            # System Idle Process              0 Services                   0          8 K
            # System                           4 Services                   0      2,952 K
            # Secure System                   76 Services                   0     21,792 K
            # Registry                       112 Services                   0     23,276 K
            # smss.exe                       524 Services                   0      1,012 K
            # csrss.exe                      844 Services                   0      4,596 K
            # wininit.exe                    964 Services                   0      5,824 K
            # services.exe                   612 Services                   0      8,260 K
            # LsaIso.exe                     608 Services                   0      3,420 K
            # lsass.exe                      956 Services                   0     19,876 K
            # .....................................................etc etc 
            
# to realize the signifance of current step .
# open the notepad first then type in tasklist in the cmd .

            # msedgewebview2.exe           12216 Console                    3      3,444 K
            # dllhost.exe                   7032 Console                    3      9,068 K
            # LockApp.exe                   8072 Console                    3     43,292 K
            # RuntimeBroker.exe             5264 Console                    3     35,596 K
            # svchost.exe                  12168 Console                    3     11,320 K
            # AppMonitorPlugIn.exe          6576 Console                    3     25,488 K
            # cmd.exe                      10716 Console                    3      4,964 K
            # conhost.exe                   2880 Console                    3      8,620 K
            # OpenConsole.exe               5852 Console                    3     17,448 K
            # WindowsTerminal.exe           1364 Console                    3     75,688 K
            # RuntimeBroker.exe             8440 Console                    3     10,648 K
            # Notepad.exe                   4784 Console                    3     65,244 K
            # SearchProtocolHost.exe       12404 Services                   0     14,752 K
            # tasklist.exe                 10784 Console                    3     10,360 K

            # C:\Users\rekha>
# at the line 76 we can notice -->Notepad.exe <-- which is telling  that the notepad.exe is currentlly running on the console 
# on rank 4784(PID rank/process id rank ).
# so in this way we can see what tasks/processes/programs are runnig on our console/system. 
# not only that whatever we write on the prompt thst will be opened . you can tryit by opening normal cmd and typing the name of the program with enter .like -->calculator ,  mspaint , notepad (system programs/softwares)
# so we can open by-dafault(system) softwares by only typing their names . 
# but in order to open the third party file/program we have add .exe at the very end of file name also hit enter .
# or in case of third party file we can also copy & paste their locations to open it .  


# but what could we do in order to kill the task . 
# for that we have -->taskkill<-- command 
# so to close  the notepad or to kill the notepad we will type -->taskkill_space_/pid 4784
# and hit Enter . 



        # # the next command is -->net start --> this is used to start all the services on your system   
        # #   Web Threat Defense User Service_197fdb2
        #    Windows Audio
        #    Windows Audio Endpoint Builder
        #    Windows Connection Manager
        #    Windows Defender Firewall
        #    Windows Event Log
        #    Windows Font Cache Service
        #    Windows Image Acquisition (WIA)
        #    Windows License Manager Service
        #    Windows Management Instrumentation
        #    Windows Push Notifications System Service
        #    Windows Push Notifications User Service_197fdb2
        #    Windows Search
        #    Windows Security Service
        #    WinHTTP Web Proxy Auto-Discovery Service
        #    WLAN AutoConfig
        #    WMI Performance Adapter
        #    Workstation

        # The command completed successfully.


        # C:\Users\rekha>
# from the above list --> let's choose the 'Windows Defender Firewall' .
# let's open firewall and see that if Windows Defender Firewall is running as the above says that it started/initiated  the  firewall.
# and as we know that for os default program we only have to type in their name in start bar . 
# so we also go to the start bar and type Windows Defender Firewall and press open . 
# ohh, yes it's currently running . 

# and to stop that we will type in -->net stop "Windows Defender Firewall"
            # C:\Users\rekha>net stop "Windows Defender Firewall"
            # System error 5 has occurred.

            # Access is denied.


            # C:\Users\rekha>
# it says access denieed that means if we have ran our prompt as administrator then we would have been sucessful.
# and besides we dont want to accidently left  our  firewall off . 
# so to start it again we will type in command--> net start "Windows Defender Firewall"
# it will get turned on again . 



# there is one command we use to find out about our drivers --> like what drivers are 
# currently installed and what we need to install . 
# command for it is --> driverquery  --> this will provide a breef description of all the windows drivers on our computer .


# so untill now we have learned the commands to start ,stop programs/tasks/processes and to see the griver information . 
   