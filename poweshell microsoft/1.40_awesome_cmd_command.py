# click on the start menu then  type in cmd then right click on the cmd option 
# then click on the run as a administration 
# then then uac window is gonna arrive then click yes and we are ready to go 


# what's your computer's ip address ? wanna  find out type in ?
# type in 
# ipconfig 
#Windows IP Configuration
# bam !!!all of your ip information on the 29 - 33 line . 

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
        
# but look closely not your mac address not your DNS server ? wanna find out ! THE BOYZ !
#  for that we need 
# ipconfig/all 

# C:\Users\rekha>ipconfig/all

        # Windows IP Configuration

        #    Host Name . . . . . . . . . . . . : alokelaptop
        #    Primary Dns Suffix  . . . . . . . :
        #    Node Type . . . . . . . . . . . . : Hybrid
        #    IP Routing Enabled. . . . . . . . : No
        #    WINS Proxy Enabled. . . . . . . . : No

        # Ethernet adapter Ethernet:

        #    Media State . . . . . . . . . . . : Media disconnected
        #    Connection-specific DNS Suffix  . :
        #    Description . . . . . . . . . . . : Realtek PCIe GbE Family Controller
        #    Physical Address. . . . . . . . . : C0-18-50-7D-DA-8F
        #    DHCP Enabled. . . . . . . . . . . : Yes
        #    Autoconfiguration Enabled . . . . : Yes

        # Wireless LAN adapter Local Area Connection* 1:

        #    Media State . . . . . . . . . . . : Media disconnected
        #    Connection-specific DNS Suffix  . :
        #    Description . . . . . . . . . . . : Microsoft Wi-Fi Direct Virtual Adapter
        #    Physical Address. . . . . . . . . : F6-A4-75-F4-49-76
        #    DHCP Enabled. . . . . . . . . . . : Yes
        #    Autoconfiguration Enabled . . . . : Yes

        # Wireless LAN adapter Local Area Connection* 3:

        #    Media State . . . . . . . . . . . : Media disconnected
        #    Connection-specific DNS Suffix  . :
        #    Description . . . . . . . . . . . : Microsoft Wi-Fi Direct Virtual Adapter #3
        #    Physical Address. . . . . . . . . : F4-A4-75-F4-49-77
        #    DHCP Enabled. . . . . . . . . . . : Yes
        #    Autoconfiguration Enabled . . . . : Yes

        # Wireless LAN adapter Wi-Fi:

        #    Connection-specific DNS Suffix  . :
        #    Description . . . . . . . . . . . : Intel(R) Dual Band Wireless-AC 3168
        #    Physical Address. . . . . . . . . : F4-A4-75-F4-49-76
        #    DHCP Enabled. . . . . . . . . . . : Yes
        #    Autoconfiguration Enabled . . . . : Yes
        #    Link-local IPv6 Address . . . . . : fe80::dd91:61bf:5c5c:9872%5(Preferred)
        #    IPv4 Address. . . . . . . . . . . : 192.168.0.101(Preferred)
        #    Subnet Mask . . . . . . . . . . . : 255.255.255.0
        #    Lease Obtained. . . . . . . . . . : 06 April 2023 07:07:08
        #    Lease Expires . . . . . . . . . . : 06 April 2023 09:09:22
        #    Default Gateway . . . . . . . . . : 192.168.0.1
        #    DHCP Server . . . . . . . . . . . : 192.168.0.1
        #    DHCPv6 IAID . . . . . . . . . . . : 99918965
        #    DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-29-5E-BA-07-C0-18-50-7D-DA-8F
        #    DNS Servers . . . . . . . . . . . : 192.168.0.1
        #    NetBIOS over Tcpip. . . . . . . . : Enabled
# this would give us all the goodies 

# now that is too much info we got to filter it and we can do it with this command 
# | --> this is called pipe .
# type in --> ipconfig /all|findstr DNS 
# there we go we have it __>
        # C:\Users\rekha>ipconfig /all|findstr DNS
        #    Connection-specific DNS Suffix  . :
        #    Connection-specific DNS Suffix  . :
        #    Connection-specific DNS Suffix  . :
        #    Connection-specific DNS Suffix  . :
        #    DNS Servers . . . . . . . . . . . : 192.168.0.1 
#  by the way you can apply findstr on any commands 



# lets say your computer needs a new ip address we can do that with ip config and we will 
# first do release to let it go 
# type in --> ipconfig/realse 

            # C:\Users\rekha>ipconfig /realse

            # Error: unrecognized or incomplete command line.

            # USAGE:
            #     ipconfig [/allcompartments] [/? | /all |
            #                                  /renew [adapter] | /release [adapter] |
            #                                  /renew6 [adapter] | /release6 [adapter] |
            #                                  /flushdns | /displaydns | /registerdns |
            #                                  /showclassid adapter |
            #                                  /setclassid adapter [classid] |
            #                                  /showclassid6 adapter |
            #                                  /setclassid6 adapter [classid] ]

            # where
            #     adapter             Connection name
            #                        (wildcard characters * and ? allowed, see examples)

            #     Options:
            #        /?               Display this help message
            #        /all             Display full configuration information.
            #        /release         Release the IPv4 address for the specified adapter.
            #        /release6        Release the IPv6 address for the specified adapter.
            #        /renew           Renew the IPv4 address for the specified adapter.
            #        /renew6          Renew the IPv6 address for the specified adapter.
            #        /flushdns        Purges the DNS Resolver cache.
            #        /registerdns     Refreshes all DHCP leases and re-registers DNS names
            #        /displaydns      Display the contents of the DNS Resolver Cache.
            #        /showclassid     Displays all the dhcp class IDs allowed for adapter.
            #        /setclassid      Modifies the dhcp class id.
            #        /showclassid6    Displays all the IPv6 DHCP class IDs allowed for adapter.
            #        /setclassid6     Modifies the IPv6 DHCP class id.


            # The default is to display only the IP address, subnet mask and
            # default gateway for each adapter bound to TCP/IP.

            # For Release and Renew, if no adapter name is specified, then the IP address
            # leases for all adapters bound to TCP/IP will be released or renewed.

            # For Setclassid and Setclassid6, if no ClassId is specified, then the ClassId is removed.

            # Examples:
            #     > ipconfig                       ... Show information
            #     > ipconfig /all                  ... Show detailed information
            #     > ipconfig /renew                ... renew all adapters
            #     > ipconfig /renew EL*            ... renew any connection that has its
            #                                          name starting with EL
            #     > ipconfig /release *Con*        ... release all matching connections,
            #                                          eg. "Wired Ethernet Connection 1" or
            #                                              "Wired Ethernet Connection 2"
            #     > ipconfig /allcompartments      ... Show information about all
            #                                          compartments
            #     > ipconfig /allcompartments /all ... Show detailed information about all
            #                                          compartments

            # C:\Users\rekha>
            
# then we will type in  renew reaching out to our DHCP server and getting it fresh 
# ipconfig /renew
            # C:\Users\rekha>ipconfig /renew

            # Windows IP Configuration

            # No operation can be performed on Ethernet while it has its media disconnected.
            # No operation can be performed on Local Area Connection* 1 while it has its media disconnected.
            # No operation can be performed on Local Area Connection* 3 while it has its media disconnected.

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

            # C:\Users\rekha>
# and then we will reach out to our DHcp server and get our fresh new ip address . 


# keeping in mind that we will refresh every singlr interface on your computer .
# if you dont wanna do that then specify the interface just after your command .
# now DNS can be a problem infact its always dns , its never the network , remember that .
# so lets jump into DNS  and see what's my computer knows . 
# command 6 -- ipconfig/displaydns
# basically it will show all the websites it knows about and their ip ddresses . 
        # Windows IP Configuration

        #     femetrics.grammarly.io
        #     ----------------------------------------
        #     Record Name . . . . . : femetrics.grammarly.io
        #     Record Type . . . . . : 1
        #     Time To Live  . . . . : 3
        #     Data Length . . . . . : 4
        #     Section . . . . . . . : Answer
        #     A (Host) Record . . . : 52.21.217.21


        #     Record Name . . . . . : femetrics.grammarly.io
        #     Record Type . . . . . : 1
        #     Time To Live  . . . . : 3
        #     Data Length . . . . . : 4
        #     Section . . . . . . . : Answer
        #     A (Host) Record . . . : 34.202.47.182


        #     Record Name . . . . . : femetrics.grammarly.io
        #     Record Type . . . . . : 1
        #     Time To Live  . . . . : 3
        #     Data Length . . . . . : 4
        #     Section . . . . . . . : Answer
        #     A (Host) Record . . . : 3.226.103.1


        #     Record Name . . . . . : femetrics.grammarly.io
        #     Record Type . . . . . : 1
        #     Time To Live  . . . . : 3
        #     Data Length . . . . . : 4
        #     Section . . . . . . . : Answer
        #     A (Host) Record . . . : 3.234.130.57


        #     Record Name . . . . . : femetrics.grammarly.io
        #     Record Type . . . . . : 1
        #     Time To Live  . . . . : 3
        #     Data Length . . . . . : 4
        #     Section . . . . . . . : Answer
        #     A (Host) Record . . . : 52.73.66.226


        #     Record Name . . . . . : femetrics.grammarly.io
        #     Record Type . . . . . : 1
        #     Time To Live  . . . . : 3
        #     Data Length . . . . . : 4
        #     Section . . . . . . . : Answer
        #     A (Host) Record . . . : 52.86.225.179


        #     Record Name . . . . . : femetrics.grammarly.io
        #     Record Type . . . . . : 1
        #     Time To Live  . . . . : 3
        #     Data Length . . . . . : 4
        #     Section . . . . . . . : Answer
        #     A (Host) Record . . . : 52.54.112.3


        #     Record Name . . . . . : femetrics.grammarly.io
        #     Record Type . . . . . : 1
        #     Time To Live  . . . . : 3
        #     Data Length . . . . . : 4
        #     Section . . . . . . . : Answer
        #     A (Host) Record . . . : 34.204.132.242


        #     api.appexnw.com
        #     ----------------------------------------
        #     Record Name . . . . . : api.appexnw.com
        #     Record Type . . . . . : 1
        #     Time To Live  . . . . : 82
        #     Data Length . . . . . : 4
        #     Section . . . . . . . : Answer
        #     A (Host) Record . . . : 104.16.236.42


        #     Record Name . . . . . : api.appexnw.com
        #     Record Type . . . . . : 1
        #     Time To Live  . . . . : 82
        #     Data Length . . . . . : 4
        #     Section . . . . . . . : Answer
        #     A (Host) Record . . . : 104.16.235.42


        #     az764295.vo.msecnd.net
        #     ----------------------------------------
        #     Record Name . . . . . : az764295.vo.msecnd.net
        #     Record Type . . . . . : 5
        #     Time To Live  . . . . : 211
        #     Data Length . . . . . : 8
        #     Section . . . . . . . : Answer
        #     CNAME Record  . . . . : cs22.wpc.v0cdn.net


        #     Record Name . . . . . : cs22.wpc.v0cdn.net
        #     Record Type . . . . . : 1
        #     Time To Live  . . . . : 211
        #     Data Length . . . . . : 4
        #     Section . . . . . . . : Answer
        #     A (Host) Record . . . : 117.18.232.200



        # C:\Users\rekha>
# but when you aae trouble shooting dns this is kind of hard to read and it will be great to just copy that 
# to our clipboard to look it at somewhere else with this command .this command is awesome by the way .
# command 7-- ipconfig /displaydns| clip ---> this command will copy the output of above command to my clipboard .
# and then open up your favouurite notepad  and paste it . 



# also sometimes you might wanna flush your DNS and for that the command is 
# command 8 ---> ipconfig /flushdns 
# C:\Users\rekha>ipconfig /flushdns

        # Windows IP Configuration

        # Successfully flushed the DNS Resolver Cache.

        # C:\Users\rekha>
# removing any old , stale DNS entries 


# now the trouvle shooting DNS even further you may want to use --
# command 9 --> nslookup
# type in --> nslookup networkchuck.com
            # C:\Users\rekha>nslookup networkchuck.com
            # Server:  UnKnown
            # Address:  192.168.0.1 # DNS SERVER  YOU ARE USING 

            # Non-authoritative answer:
            # Name:    networkchuck.com
            # Addresses:  2606:4700:20::681a:ab9
            #           2606:4700:20::ac43:4aeb
            #           2606:4700:20::681a:bb9
            #           104.26.10.185
            #           172.67.74.235# WHAT ANSWER IT GAVE YOU 
            #           104.26.11.185


            # C:\Users\rekha>
# with ns lookup where is networkchuck.com ?what is the ip address? 
# and it will tell you  DNS server  you are using and what answer it gave you . 



# WE CAN ALSO TRY ANOTHER DNS SERVER REAL QUICK 
# TYPE IN-- > NSLOOKUP NETWORKCHUCK.COFFEE 8.8.8.8(RIGHT AFTER SPECIFY ITHER DNS SERVER )
            # C:\Users\rekha>nslookup networkchuck.coffee 8.8.8.8
            # Server:  dns.google
            # Address:  8.8.8.8

            # Non-authoritative answer:
            # Name:    networkchuck.coffee
            # Address:  23.227.38.65


            # C:\Users\rekha>
# right after we have specifies the other dns server  which is google . 

# you can alos check for other types of dns records from mx to txt pointer . trust me , you gonna need those commands because it's always dns .always . 
# command--> nslookup -type=mx networkchuck.com 

            # C:\Users\rekha>nslookup -type=mx networkchuck.com
            # Server:  UnKnown
            # Address:  192.168.0.1

            # Non-authoritative answer:
            # networkchuck.com        MX preference = 1, mail exchanger = aspmx.l.google.com
            # networkchuck.com        MX preference = 10, mail exchanger = aspmx2.googlemail.com
            # networkchuck.com        MX preference = 10, mail exchanger = aspmx3.googlemail.com
            # networkchuck.com        MX preference = 5, mail exchanger = alt1.aspmx.l.google.com
            # networkchuck.com        MX preference = 5, mail exchanger = alt2.aspmx.l.google.com

            # C:\Users\rekha>
# another command is -->nslookup -type=ptr networkchuck.com  
            # C:\Users\rekha>nslookup -type=ptr networkchuck.com
            # Server:  UnKnown
            # Address:  192.168.0.1

            # networkchuck.com
            #         primary name server = jade.ns.cloudflare.com
            #         responsible mail addr = dns.cloudflare.com
            #         serial  = 2300075626
            #         refresh = 10000 (2 hours 46 mins 40 secs)
            #         retry   = 2400 (40 mins)
            #         expire  = 604800 (7 days)
            #         default TTL = 3600 (1 hour)

            # C:\Users\rekha>
# and the ptr stands for pointers . 




# now look at the screen its messy and we can clean it up with one command 
# command 10 --> cls
# cls stands for clean the screen . 

# what's your mac address ? 
# HAHAHAHA...
# JUSt typr in -->
# command 11 --> getmac /v
            # # C:\Users\rekha>getmac /v

            # Connection Name Network Adapter Physical Address    Transport Name

            # =============== =============== =================== ==========================================================
            # Wi-Fi           Intel(R) Dual B F4-A4-75-F4-49-76   \Device\Tcpip_{34683B29-6AEE-454C-BD70-15300DFC2E7A}
            # Ethernet        Realtek PCIe Gb C0-18-50-7D-DA-8F   Media disconnected


            # C:\Users\rekha>
# / --> this is called forward slash  .


# the command of you have any energy or power issues .
# command 12-->powercfg /energy 
            # C:\Users\rekha>powercfg /energy
            # This command requires administrator privileges and must be executed from an elevated command prompt.

            # C:\Users\rekha>
# give it some time and it give give you some awesome stuffs 
# like energy issues and a great report on how you're energy doing also how'is your battery?
# command 13 is --> powercfg /batteryreport              
            # C:\Users\rekha>powercfg /batteryreport
            # Battery life report saved to file path C:\Users\rekha\battery-report.html.

            # C:\Users\rekha>
# just copy that file location --> C:\Users\rekha\battery-report.html<-- this one 
# and paste it to your command prompt .BAM!!. there is your battery report . 




# this one is super handy , 
# command 14 --> assoc 
# and its donna shoe you whitch file types are associated with which program .
# assoc
            # .386=vxdfile
            # .3g2=WMP11.AssocFile.3G2
            # .3gp=WMP11.AssocFile.3GP
            # .3gp2=WMP11.AssocFile.3G2
            # .3gpp=WMP11.AssocFile.3GP
            # .aac=WMP11.AssocFile.ADTS
            # .accda=Access.ACCDAExtension.16
            # .accdb=Access.Application.16
            # .accdc=Access.ACCDCFile.16
            # .accde=Access.ACCDEFile.16
            # .accdr=Access.ACCDRFile.16
            # .accdt=Access.ACCDTFile.16
            # .accdu=Access.WizardUserDataFile.16
            # .accdw=Access.WebApplicationReference.16
            # .accft=Access.ACCFTFile.16
            # .accountpicture-ms=accountpicturefile
            # .acl=ACLFile
            # .ade=Access.ADEFile.16
            # .adn=Access.BlankProjectTemplate.16
            # .adp=Access.Project.16
            # .adt=WMP11.AssocFile.ADTS
            # .adts=WMP11.AssocFile.ADTS
            # .aif=WMP11.AssocFile.AIFF
            # .aifc=WMP11.AssocFile.AIFF
            # .aiff=WMP11.AssocFile.AIFF
            # .ani=anifile
            # .appcontent-ms=ApplicationContent
            # .application=Application.Manifest
            # .appref-ms=Application.Reference
            # .asa=aspfile
            # .asd=Word.AutoRecovery.8
            # .asf=WMP11.AssocFile.ASF
            # .asp=aspfile
            # .asx=WMP11.AssocFile.ASX
            # .au=WMP11.AssocFile.AU
            # .avi=WMP11.AssocFile.AVI
            # .aw=AWFile
            # .bat=batfile
            # .blg=Diagnostic.Perfmon.Document
            # .bmp=Paint.Picture
            # .cab=CABFolder
            # .camp=campfile
            # .cat=CATFile
            # .cda=WMP11.AssocFile.CDA
            # .cdmp=cdmpfile
            # .cdx=aspfile
            # .cdxml=Microsoft.PowerShellCmdletDefinitionXML.1
            # .cer=CERFile
            # .chk=chkfile
            # .chm=chm.file
            # .cmd=cmdfile
            # .com=comfile
            # .compositefont=Windows.CompositeFont
            # .cpl=cplfile
            # .crl=CRLFile
            # .crt=CERFile
            # .crtx=CRTXFile
            # .css=CSSfile
            # .csv=Excel.CSV
            # .cur=curfile
            # .db=dbfile
            # .dctx=IMEDictionaryCompiler
            # .dctxc=IMEDictionaryCompiler
            # .dds=ddsfile
            # .der=CERFile
            # .desklink=CLSID\{9E56BE61-C50F-11CF-9A2C-00A0C90A90CE}
            # .deskthemepack=desktopthemepackfile
            # .det=Outlook.File.det.15
            # .diagcab=Diagnostic.Cabinet
            # .diagcfg=Diagnostic.Config
            # .diagpkg=Diagnostic.Document
            # .dic=txtfile
            # .dll=dllfile
            # .doc=Word.Document.8
            # .dochtml=wordhtmlfile
            # .docm=Word.DocumentMacroEnabled.12
            # .docmhtml=wordmhtmlfile
            # .docx=Word.Document.12
            # .docxml=wordxmlfile
            # .dot=Word.Template.8
            # .dothtml=wordhtmltemplate
            # .dotm=Word.TemplateMacroEnabled.12
            # .dotx=Word.Template.12
            # .dqy=dqyfile
            # .drv=drvfile
            # .dsn=MSDASQL
            # .elm=ELMFile
            # .eml=Outlook.File.eml.15
            # .evt=evtfile
            # .evtx=evtxfile
            # .exc=txtfile
            # .exe=exefile
            # .fdm=Outlook.File.fdm.15
            # .flac=WMP11.AssocFile.FLAC
            # .fon=fonfile
            # .gcsx=GCSXFile
            # .gif=giffile
            # .gitattributes=txtfile
            # .gitignore=txtfile
            # .gitmodules=txtfile
            # .glox=GLOXFile
            # .gmmp=gmmpfile
            # .gqsx=GQSXFile
            # .gra=MSGraph.Chart.8
            # .grp=MSProgramGroup
            # .hlp=hlpfile
            # .hol=Outlook.File.hol.15
            # .hta=htafile
            # .htm=htmlfile
            # .html=htmlfile
            # .hxa=MSHelp.hxa.2.5
            # .hxc=MSHelp.hxc.2.5
            # .hxd=MSHelp.hxd.2.5
            # .hxe=MSHelp.hxe.2.5
            # .hxf=MSHelp.hxf.2.5
            # .hxh=MSHelp.hxh.2.5
            # .hxi=MSHelp.hxi.2.5
            # .hxk=MSHelp.hxk.2.5
            # .hxq=MSHelp.hxq.2.5
            # .hxr=MSHelp.hxr.2.5
            # .hxs=MSHelp.hxs.2.5
            # .hxt=MSHelp.hxt.2.5
            # .hxv=MSHelp.hxv.2.5
            # .hxw=MSHelp.hxa.2.5
            # .icc=icmfile
            # .icl=IconLibraryFile
            # .icm=icmfile
            # .ico=icofile
            # .ics=Outlook.File.ics.15
            # .imesx=imesxfile
            # .img=Windows.IsoFile
            # .iqy=iqyfile
            # .iso=Windows.IsoFile
            # .jfif=pjpegfile
            # .Job=JobObject
            # .jod=Microsoft.Jet.OLEDB.4.0
            # .jpe=jpegfile
            # .jpeg=jpegfile
            # .jpg=jpegfile
            # .js=JSFile
            # .JSE=JSEFile
            # .jxr=wdpfile
            # .label=Label
            # .laccdb=Access.LockFile.16
            # .ldb=Access.LockFile.16
            # .lex=LEXFile
            # .library-ms=LibraryFolder
            # .lnk=lnkfile
            # .m=Octave.Document.7.3.0
            # .m1v=WMP11.AssocFile.MPEG
            # .m2t=WMP11.AssocFile.M2TS
            # .m2ts=WMP11.AssocFile.M2TS
            # .m2v=WMP11.AssocFile.MPEG
            # .m3u=WMP11.AssocFile.m3u
            # .m4a=WMP11.AssocFile.M4A
            # .m4v=WMP11.AssocFile.MP4
            # .mad=Access.Shortcut.Module.1
            # .maf=Access.Shortcut.Form.1
            # .mag=Access.Shortcut.Diagram.1
            # .mam=Access.Shortcut.Macro.1
            # .mapimail=CLSID\{9E56BE60-C50F-11CF-9A2C-00A0C90A90CE}
            # .maq=Access.Shortcut.Query.1
            # .mar=Access.Shortcut.Report.1
            # .mas=Access.Shortcut.StoredProcedure.1
            # .mat=Access.Shortcut.Table.1
            # .mau=Access.Shortcut.Function.1
            # .mav=Access.Shortcut.View.1
            # .maw=Access.Shortcut.DataAccessPage.1
            # .mda=Access.Extension.16
            # .mdb=Access.MDBFile
            # .mdbhtml=accesshtmlfile
            # .mde=Access.MDEFile.16
            # .mdn=Access.BlankDatabaseTemplate.16
            # .mdt=Access.WizardDataFile.16
            # .mdw=Access.Workgroup.16
            # .mht=mhtmlfile
            # .mhtml=mhtmlfile
            # .mid=WMP11.AssocFile.MIDI
            # .midi=WMP11.AssocFile.MIDI
            # .mk3d=WMP11.AssocFile.MK3D
            # .mka=WMP11.AssocFile.MKA
            # .mkv=WMP11.AssocFile.MKV
            # .mlc=LpkSetup.1
            # .mod=WMP11.AssocFile.MPEG
            # .mov=WMP11.AssocFile.MOV
            # .mp2=WMP11.AssocFile.MP3
            # .mp2v=WMP11.AssocFile.MPEG
            # .mp3=WMP11.AssocFile.MP3
            # .mp4=WMP11.AssocFile.MP4
            # .mp4v=WMP11.AssocFile.MP4
            # .mpa=WMP11.AssocFile.MPEG
            # .mpe=WMP11.AssocFile.MPEG
            # .mpeg=WMP11.AssocFile.MPEG
            # .mpg=WMP11.AssocFile.MPEG
            # .mpv2=WMP11.AssocFile.MPEG
            # .ms-windows-store-license=WindowsStore.License
            # .msc=MSCFile
            # .msg=Outlook.File.msg.15
            # .msi=Msi.Package
            # .msp=Msi.Patch
            # .msrcincident=RemoteAssistance.1
            # .msstyles=msstylesfile
            # .msu=Microsoft.System.Update.1
            # .mts=WMP11.AssocFile.M2TS
            # .mydocs=CLSID\{ECF03A32-103D-11d2-854D-006008059367}
            # .nfo=MSInfoFile
            # .nk2=Outlook.File.nk2.15
            # .nst=Outlook.File.nst.15
            # .ocx=ocxfile
            # .odc=odcfile
            # .odccubefile=odccubefile
            # .odcdatabasefile=odcdatabasefile
            # .odcnewfile=odcnewfile
            # .odctablecollectionfile=odctablecollectionfile
            # .odctablefile=odctablefile
            # .odp=PowerPoint.OpenDocumentPresentation.12
            # .ods=Excel.OpenDocumentSpreadsheet.12
            # .odt=Word.OpenDocumentText.12
            # .ofs=Outlook.File.ofs.15
            # .oft=Outlook.File.oft.15
            # .ols=OfficeListShortcut
            # .one=OneNote.Section.1
            # .onepkg=OneNote.Package
            # .onetoc=OneNote.TableOfContents
            # .onetoc2=OneNote.TableOfContents.12
            # .opc=OPCFile
            # .oqy=oqyfile
            # .osdx=opensearchdescription
            # .ost=Outlook.File.ost.15
            # .otf=otffile
            # .otm=Outlook.File.otm.15
            # .p10=P10File
            # .p12=PFXFile
            # .p7b=SPCFile
            # .p7c=certificate_wab_auto_file
            # .p7m=P7MFile
            # .p7r=P7RFile
            # .p7s=P7SFile
            # .pab=Outlook.File.pab.15
            # .partial=IE.AssocFile.PARTIAL
            # .pbk=pbkfile
            # .pcb=PCBFile
            # .perfmoncfg=Diagnostic.Perfmon.Config
            # .pfm=pfmfile
            # .pfx=PFXFile
            # .pif=piffile
            # .pko=PKOFile
            # .pnf=pnffile
            # .png=pngfile
            # .pot=PowerPoint.Template.8
            # .pothtml=powerpointhtmltemplate
            # .potm=PowerPoint.TemplateMacroEnabled.12
            # .potx=PowerPoint.Template.12
            # .ppa=PowerPoint.Addin.8
            # .ppam=PowerPoint.Addin.12
            # .ppkg=Microsoft.ProvTool.Provisioning.1
            # .pps=PowerPoint.SlideShow.8
            # .ppsm=PowerPoint.SlideShowMacroEnabled.12
            # .ppsx=PowerPoint.SlideShow.12
            # .ppt=PowerPoint.Show.8
            # .ppthtml=powerpointhtmlfile
            # .pptm=PowerPoint.ShowMacroEnabled.12
            # .pptmhtml=powerpointmhtmlfile
            # .pptx=PowerPoint.Show.12
            # .pptxml=powerpointxmlfile
            # .prf=prffile
            # .ps1xml=Microsoft.PowerShellXMLData.1
            # .psc1=Microsoft.PowerShellConsole.1
            # .pssc=Microsoft.PowerShellSessionConfiguration.1
            # .pst=Outlook.File.pst.15
            # .pub=Publisher.Document.16
            # .pubhtml=publisherhtmlfile
            # .pubmhtml=publishermhtmlfile
            # .pwz=PowerPoint.Wizard.8
            # .qds=SavedDsQuery
            # .rat=ratfile
            # .RDP=RDP.File
            # .reg=regfile
            # .resmoncfg=Diagnostic.Resmon.Config
            # .rll=dllfile
            # .rmi=WMP11.AssocFile.MIDI
            # .rqy=rqyfile
            # .rtf=Word.RTF.8
            # .scf=SHCmdFile
            # .scr=scrfile
            # .sct=scriptletfile
            # .search-ms=SearchFolder
            # .searchConnector-ms=SearchConnectorFolder
            # .settingcontent-ms=SettingContent
            # .sfcache=RDBFileProperties.1
            # .sh=sh_auto_file
            # .shtml=shtmlfile
            # .sldm=PowerPoint.SlideMacroEnabled.12
            # .sldx=PowerPoint.Slide.12
            # .slk=Excel.SLK
            # .snd=WMP11.AssocFile.AU
            # .spc=SPCFile
            # .sst=CertificateStoreFile
            # .svg=svgfile
            # .symlink=.symlink
            # .sys=sysfile
            # .theme=themefile
            # .themepack=themepackfile
            # .thmx=OfficeTheme.12
            # .tif=TIFImage.Document
            # .tiff=TIFImage.Document
            # .ts=WMP11.AssocFile.TTS
            # .ttc=ttcfile
            # .ttf=ttffile
            # .tts=WMP11.AssocFile.TTS
            # .txt=txtfilelegacy
            # .UDL=MSDASC
            # .URL=InternetShortcut
            # .uxdc=UXDCFILE
            # .VBE=VBEFile
            # .vbs=VBSFile
            # .vcf=Outlook.File.vcf.15
            # .vcs=Outlook.File.vcs.15
            # .vdw=VisioViewer.Viewer
            # .vdx=VisioViewer.Viewer
            # .vhdpmem=Windows.VhdPmemFile
            # .vhdx=Windows.VhdFile
            # .vsd=VisioViewer.Viewer
            # .vsdm=VisioViewer.Viewer
            # .vsdx=VisioViewer.Viewer
            # .vss=VisioViewer.Viewer
            # .vssm=VisioViewer.Viewer
            # .vssx=VisioViewer.Viewer
            # .vst=VisioViewer.Viewer
            # .vstm=VisioViewer.Viewer
            # .vsto=bootstrap.vsto.1
            # .vstx=VisioViewer.Viewer
            # .vsx=VisioViewer.Viewer
            # .vtx=VisioViewer.Viewer
            # .vxd=vxdfile
            # .wab=wab_auto_file
            # .wav=WMP11.AssocFile.WAV
            # .wax=WMP11.AssocFile.WAX
            # .wbcat=wbcatfile
            # .wbk=Word.Backup.8
            # .wcx=wcxfile
            # .wdp=wdpfile
            # .webpnp=webpnpFile
            # .website=Microsoft.Website
            # .wiz=Word.Wizard.8
            # .wizhtml=accessthmltemplate
            # .wll=Word.Addin.8
            # .wm=WMP11.AssocFile.ASF
            # .wma=WMP11.AssocFile.WMA
            # .WMD=WMP11.AssocFile.WMD
            # .wmdb=WMP.WMDBFile
            # .WMS=WMP11.AssocFile.WMS
            # .wmv=WMP11.AssocFile.WMV
            # .wmx=WMP11.AssocFile.ASX
            # .wmz=WMP11.AssocFile.WMZ
            # .wpl=WMP11.AssocFile.WPL
            # .wsc=scriptletfile
            # .WSF=WSFFile
            # .WSH=WSHFile
            # .wvx=WMP11.AssocFile.WVX
            # .xaml=Windows.XamlDocument
            # .xbap=Windows.Xbap
            # .xevgenxml=XEV.GenericApp
            # .xht=xhtmlfile
            # .xhtml=xhtmlfile
            # .xla=Excel.Addin
            # .xlam=Excel.AddInMacroEnabled
            # .xld=Excel.Dialog
            # .xlk=Excel.Backup
            # .xll=Excel.XLL
            # .xlm=Excel.Macrosheet
            # .xls=Excel.Sheet.8
            # .xlsb=Excel.SheetBinaryMacroEnabled.12
            # .xlshtml=Excelhtmlfile
            # .xlsm=Excel.SheetMacroEnabled.12
            # .xlsmhtml=excelmhtmlfile
            # .xlsx=Excel.Sheet.12
            # .xlt=Excel.Template.8
            # .xlthtml=Excelhtmltemplate
            # .xltm=Excel.TemplateMacroEnabled
            # .xltx=Excel.Template
            # .xlw=Excel.Workspace
            # .xlxml=Excelxmlss
            # .xrm-ms=MSSppLicenseFile
            # .xsl=xslfile
            # .zfsendtotarget=CLSID\{888DCA60-FC0A-11CF-8F0F-00C04FD7D062}
            # .zip=CompressedFolder

            # C:\Users\rekha>
# for example mp4 will open with Windows  media player and much more . 
