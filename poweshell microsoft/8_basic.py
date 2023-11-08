# open powershell in administttrator mode 
# get-executionpolicy 






# execution policy 
#  microsoft has this scripting by default in an effort to preveant  malicious code from running using powershell environment .
# does that means we will not able to execte any code any powershell code ?  
# no  
# if you make any scrips for powershell / or to use in powershell you have to give it extensioin of ps1.
# so suppose we have written some script to do some task . how do we execcute ? 
# so we open a normal command prompt . then say --> powershell c:\where is your script  \PSscripts \measure.ps1
# powershell c:\temp  \PSscripts \measure.ps1
# it will show error that the running scripts are disabled .
# so how can we enable script running .
# open the windows powershell in administrator miode .
# go in administrator mode, bcz if you run in non-admin mode you will not be able to set/enable  the exeecution policy.
# now lets try to see what is my execution  policy .
# type in    get-executionpolicy hit enter it will say resticted.
# which means it is the default execution policy for powershell which also means you can only run digitally and remote signed scripts .
# remote signed that means you can run any script locally so if remotely someone is trying to execute something in your environment they will  fail .
# so thus you should be knowing ehat you are doing .
# type in --> set-executionpoict remotesigned 
# it means for local script it will work fine but for remote script it has to be digitally signed .
# now  if you go back to the smd and try to run the same previous command then then this time it will give no errors .
# 
# 