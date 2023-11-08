# $PSVersionTable 
# $PSVersionTable.PSVersion
#start-transcript  -path c:\temp\file1.txt
#Get-Command 
# stop-Transcript 













# we will start with the versioin we will try to look which version of the powershell you are using .
# the reason might be sometime you are targeting a script for different version of powershell .
# or it might be slightly incompetable or some of the command might be in a higher or lower version of a powershell.
# so the command to look at the version is -->$PSVersionTable ( then tap tab and it will complete automatically ) 
            # PS C:\Users\rekha> $PSVersionTable

            # Name                           Value
            # ----                           -----
            # PSVersion                      7.3.3
            # PSEdition                      Core
            # GitCommitId                    7.3.3
            # OS                             Microsoft Windows 10.0.22623
            # Platform                       Win32NT
            # PSCompatibleVersions           {1.0, 2.0, 3.0, 4.0…}
            # PSRemotingProtocolVersion      2.3
            # SerializationVersion           1.1.0.1
            # WSManStackVersion              3.0

            # PS C:\Users\rekha>
# and if you see here , iget the partial version or psversion 
# then we can also get that out of it like :
# $PSVersionTable.PSVersion--> as psversion is a property .

# in the powershell sometimes you might forget what commands you have typed 
# but sometimes somecommands may be working now they was not working in th epast .
# so there is a command called --> start-transcript 
# what this command will do it start recording everyything you have typed in so if you 
# ever forget any command also  with that you have to give it a path  any folder and a file name  where you wanna keep it . 
#start-transcript  -path c:\temp\file1.txt
# and if you dont give a path it will take the default path .
# let's write , Get-Command 
# Get-command -- it is the command which will list out all the commands, cmdlets, functions  which are present in the system 
# transcript file is recording everything now if i want to stop the transcript file.
# type--> stop-Transcript  
# now let's go and see how transcript file looks like .
# open run , type directory location --> c:
# open temp folder --> file1.txt --> open with notepad . 
