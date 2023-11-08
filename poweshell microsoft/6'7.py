# powershell : zero to hero 
# 1.46.11


# get-service_tab_|convertTo-html -property   name , status 
# get-service_tab_|convertTo-html -property   name , status  | out-file c:\ test.html
# c:\test.html
# get-service | stop-service -whatif 


# get help *out* 
# beides seding syff out there's also creative ways to do stuff 
# we also have -->convert-to <-- command 
# get-service_tab_|convertTo-html -property   name , status 
# tab autocompletes and formats the  command 
# notice that we have given two parameters/attribute to property to do the convert to we have noticed that via syntax in the help file .
# help is your friend dont forget to discuss with him before you do something especially in the powersshell.
# now it will show me the html version of det-service on my screen .

# but now i want it to show me this on a  file .
# for that we will pipe it out .
# get-service_tab_|convertTo-html -property   name , status  | out-file c:\ test.html
# c:\test.html



# cmdlets that kills 
# stop-process/kill
# stop-service 
# $ConfirmPreference 
# $Whatifpreference 
# -confirm
# -whatif 


# when you ever do something wrong ?
# in powershell if you ever have something that you are uncertain of you can always typw in 
# -whatif 
# and you would get --> and it eill tell you what you will do but it does not actually do it .
# after you type this 
## get-service | stop-service -whatif 
# and when you look at the output 
# it will say i would have stop these services .
# we also have -confirm 
# and -confirm with do you actually want to do actually want to do this ? 
# no .
#  open the video and watch closely .1.47--1.55





# the concept of the pipeline is 
# you got a cmdlet , you are gonna pipe the results of that commandlet to the next one 
# so its like do this then do this then this till your needs are done ,
# and what you are gonna notice is as we go through this 
# and you get  more and more cmdlets you are see that the way you are thinnking about this 
# solving the problem the way you are actually be building the commands in the pipeline .
# and you cannot do everything as a one-liner 
# but we are also gonna do scripting ehere .








