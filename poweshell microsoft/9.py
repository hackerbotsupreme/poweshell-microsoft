
# get-alias 
# get-alias| findstr /s  pwd.
# pwd / get-location
# # get-alias| findstr /s  gps .
# gps
# get-alias |findstr /s ps
# get-alias |findstr /s cwd
# set-alias cwd get-location
# cwd
# pwd
# get-alias | findstr /s cwd
# Get-Locaation 
#cd c:\temp
# push.d
# cd c:
# cd ..
# popd 
# type --> pushd c:\windows\system32
# then type--> pushd c:
# cd..
# popd . 






# in previous video we have seen that to get the alias we have this command called --> get-alias 
# which list out all the alias commands on our screen .
# let's filter out the common ones we use .
# so let's look at the some other alias we used ,
# so, get-alias then  i can do find str which means find a string with aspect to pwd . so it tells me present working dorectorry .
# # get-alias| findstr /s  pwd.
# so you  might have notices that we have used that pwd command .
# or we can use get-location command in alter to pwd which also gives us the same return .
# get-location(verb/noun )
# so gps is the alias  of get-process or gps . ps it shortend version of process .
# and is you only type the gps it will list out all the processes in the system . #
# there's another alias for gps is get-process , you cacn check that out by 
# typing --> get-alias | findstr /s ps 
# also you will see,
# ps is also pointing to get-process 
# and gps is also pointing to the get-process .
# that is also an alias .
# now , let suppose i want to create a new alias .
# so how do we go about that ?
# get-alias will give us the alias so let''s try to chevk id there is something called cwd .
# there's no alias called cwd so let suppose we have a hypothetical alias called current  working directory 
#  and in current working directory i will create a directory simiar to present working directory .
# so i will , saay set-alias cwd get-location(whatever eqivalent command you want to type ) 
# and now i can say cwd 
# it will give mw the current working directory .
# and which is simiar to pwd .
# and if i try to look at this alias thing now --> get-alias | findstr /s cwd
# nnow if i exit the powershell and come back again this alias would be lost .
# so if i wantt to permanenetly store it we will look into another video .
# now focus on the directory we are on . 
# suppose we want to go to some another location .
# type --> cd c:\temp
# so now  the directory is changed .
# now if we want to go back to the previous oone .
#  pushd -- > so what it does is basically whatever content you give it eill push it 
# onto a stack .
# type --> pushd .--> whaat it means is whatever my current directory's there , push that on to a stack .
# let's just move to some another folder .
# # cd c:
# cd ..
# now insteadd of typing something previous long named directory 
# now if i say popd 
# now popd will take me take me to a directory where i did a pushd .
# now i can do pushd  for multiple folders also.
# type --> pushd c:\windows\system32
# then type--> pushd c:
# cd..
# popd . 
# once i do the popd i will go to system32 again .
 