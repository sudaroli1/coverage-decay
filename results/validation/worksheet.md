# Validation worksheet

Label each item **S** (a suppression: the exclusion set genuinely widened and coverage did not), **N** (not a suppression), or **U** (unclear).

Commit messages are withheld so the corroboration measure stays independent.


---

## V001

```
EXCLUSION  - P:CommandLine|EQ|('S', '*\Google\Drive\googledrivesync.exe\..\*')|CTX:NEG
```


---

## V002

```
EXCLUSION  + P:CommandLine|EQ|('S', '*echo /etc/post-install/*.post*')|CTX:NEG
```


---

## V003

```
EXCLUSION  + P:Image|IN|('L', (('S', 'C:\Program Files (x86)\*'), ('S', 'C:\Program Files\*'), ('S', 'C:\Windows\SysWOW64\*'), ('S', 'C:\Windows\System32\*')))|CTX:NEG
EXCLUSION  - P:Image|IN|('L', (('S', '*:\Program Files (x86)\*'), ('S', '*:\Program Files\*'), ('S', '*:\Windows\SysWOW64\*'), ('S', '*:\Windows\System32\*')))|CTX:NEG
```


---

## V004

```
EXCLUSION  + P:Image|EQ|('S', '*\OfficeClickToRun.exe')|CTX:NEG
EXCLUSION  + P:Image|IN|('L', (('S', 'C:\Program Files\Common Files\Microsoft Shared\ClickToRun\*'), ('S', 'C:\Program Files\Common Files\Microsoft Shared\ClickToRun\Updates\*')))|CTX:NEG
```


---

## V005

```
EXCLUSION  + P:ModifyingApplication|EQ|('S', '*\MsMpEng.exe')|CTX:NEG
EXCLUSION  + P:ModifyingApplication|EQ|('S', 'C:\ProgramData\Microsoft\Windows Defender\Platform\*')|CTX:NEG
EXCLUSION  + P:ModifyingApplication|EQ|('S', 'C:\Windows\System32\svchost.exe')|CTX:NEG
EXCLUSION  + P:ModifyingApplication|IN|('L', (('S', 'C:\Program Files (x86)\*'), ('S', 'C:\Program Files\*')))|CTX:NEG
```


---

## V006

```
EXCLUSION  + P:SourceImage|EQ|('S', 'C:\Program Files\internet explorer\iexplore.exe')|CTX:NEG
EXCLUSION  + P:SourceImage|EQ|('S', 'C:\Windows\System32\winlogon.exe')|CTX:NEG
EXCLUSION  + P:SourceImage|EQ|('S', 'C:\Windows\explorer.exe')|CTX:NEG
EXCLUSION  + P:SourceImage|IN|('L', (('S', 'C:\Windows\SysWOW64\schtasks.exe'), ('S', 'C:\Windows\System32\schtasks.exe')))|CTX:NEG
EXCLUSION  + P:SourceParentImage|IN|('L', (('S', 'C:\Program Files (x86)\*'), ('S', 'C:\Program Files\*')))|CTX:NEG
EXCLUSION  + P:TargetImage|EQ|('S', '')|CTX:NEG
EXCLUSION  + P:TargetImage|EQ|('S', 'C:\Windows\System32\conhost.exe')|CTX:NEG
EXCLUSION  + P:TargetImage|EQ|('S', 'C:\Windows\System32\csrss.exe')|CTX:NEG
EXCLUSION  - P:SourceImage|EQ|('S', '*:\Program Files\internet explorer\iexplore.exe*')|CTX:NEG
EXCLUSION  - P:SourceImage|EQ|('S', '*:\Windows\System32\winlogon.exe')|CTX:NEG
EXCLUSION  - P:SourceImage|EQ|('S', '*:\Windows\System32\winlogon.exe*')|CTX:NEG
EXCLUSION  - P:SourceImage|EQ|('S', '*:\Windows\explorer.exe')|CTX:NEG
EXCLUSION  - P:SourceImage|IN|('L', (('S', '*:\Windows\SysWOW64\schtasks.exe'), ('S', '*:\Windows\System32\schtasks.exe')))|CTX:NEG
EXCLUSION  - P:SourceParentImage|EQ|('S', '*:\Program Files*')|CTX:NEG
EXCLUSION  - P:TargetImage|EQ|('S', '*:\Windows\System32\conhost.exe')|CTX:NEG
EXCLUSION  - P:TargetImage|EQ|('S', '*:\Windows\System32\csrss.exe')|CTX:NEG
SELECTION  + P:TargetImage|EQ|('S', '*')|CTX:POS
```


---

## V007

```
EXCLUSION  + P:Image|EQ|('S', 'C:\WINDOWS\system32\SecurityHealthService.exe')|CTX:NEG
EXCLUSION  - P:Details|EQ|('S', '*C:\Windows\System32\SecurityHealth*')|CTX:NEG
EXCLUSION  - P:Image|EQ|('S', 'C:\Windows\system32\SecurityHealthService.exe')|CTX:NEG
```


---

## V008

```
SELECTION  + P:_raw|CONTAINS|('S', '\perfc.dat')|CTX:POS
SELECTION  - P:_raw|CONTAINS|('S', '*\perfc.dat*')|CTX:POS
```


---

## V009

```
EXCLUSION  + P:_raw|CONTAINS|('S', 'Crack')|CTX:NEG
EXCLUSION  + P:_raw|CONTAINS|('S', 'Keygen')|CTX:NEG
EXCLUSION  - P:Message|IN|('L', (('S', '*Crack*'), ('S', '*Keygen*')))|CTX:NEG
SELECTION  + P:_raw|CONTAINS|('S', 'ASP/Backdoor')|CTX:POS
SELECTION  + P:_raw|CONTAINS|('S', 'ASPXSpy')|CTX:POS
SELECTION  + P:_raw|CONTAINS|('S', 'Backdoor.ASP')|CTX:POS
SELECTION  + P:_raw|CONTAINS|('S', 'Backdoor.JSP')|CTX:POS
SELECTION  + P:_raw|CONTAINS|('S', 'Backdoor.PHP')|CTX:POS
SELECTION  + P:_raw|CONTAINS|('S', 'Chopper')|CTX:POS
SELECTION  + P:_raw|CONTAINS|('S', 'Clearlog')|CTX:POS
SELECTION  + P:_raw|CONTAINS|('S', 'HTool-')|CTX:POS
SELECTION  - P:Message|IN|('L', (('S', '*ASP/Backdoor*'), ('S', '*ASPXSpy*'), ('S', '*Backdoor.ASP*'), ('S', '*Backdoor.JSP*'), ('S', '*Backdoor.PHP*'), ('S', '*Chopper*'), ('S', '*Clearlog*'), ('S', '*HTool-*'), ('S', '*Hacktool*'),
```


---

## V010

```
(no predicate-level change)
```


---

## V011

```
EXCLUSION  + P:TargetFilename|EQ|('S', 'C:\Windows\explorer.exe')|CTX:NEG
SELECTION  + P:TargetFilename|IN|('L', (('S', '*\AtBroker.exe'), ('S', '*\LogonUI.exe'), ('S', '*\LsaIso.exe'), ('S', '*\RuntimeBroker.exe'), ('S', '*\SearchFilterHost.exe'), ('S', '*\SearchIndexer.exe'), ('S', '*\SearchProtocolHost.
SELECTION  - P:TargetFilename|IN|('L', (('S', '*\RuntimeBroker.exe'), ('S', '*\Taskmgr.exe'), ('S', '*\audiodg.exe'), ('S', '*\conhost.exe'), ('S', '*\csrss.exe'), ('S', '*\dllhost.exe'), ('S', '*\explorer.exe'), ('S', '*\lsass.exe')
```


---

## V012

```
EXCLUSION  + P:Image|EQ|('S', 'C:\ProgramData\Microsoft\Windows Defender\*')|CTX:NEG
EXCLUSION  + P:Image|IN|('L', (('S', 'C:\Program Files (x86)\*'), ('S', 'C:\Program Files\*')))|CTX:NEG
```


---

## V013

```
EXCLUSION  + P:IpAddress|EQ|('S', '169.254.0.0/16')|CTX:NEG
EXCLUSION  + P:IpAddress|EQ|('S', '::1/128')|CTX:NEG
EXCLUSION  + P:IpAddress|EQ|('S', 'fc00::/7')|CTX:NEG
EXCLUSION  + P:IpAddress|EQ|('S', 'fe80::/10')|CTX:NEG
EXCLUSION  - P:IpAddress|EQ|('S', '::1')|CTX:NEG
EXCLUSION  - P:IpAddress|IN|('L', (('S', 'fc*'), ('S', 'fd*'), ('S', 'fe80:*')))|CTX:NEG
```


---

## V014

```
EXCLUSION  + P:SourceImage|EQ|('S', '*C:\Users\*')|CTX:NEG
EXCLUSION  + P:SourceImage|EQ|('S', '*\AppData\Local\*')|CTX:NEG
EXCLUSION  + P:SourceImage|IN|('L', (('S', '*\Microsoft VS Code\Code.exe'), ('S', '*\software_reporter_tool.exe')))|CTX:NEG
EXCLUSION  - P:SourceImage|EQ|('S', 'C:\Users\*\AppData\Local\Programs\Microsoft VS Code\Code.exe')|CTX:NEG
```


---

## V015

```
EXCLUSION  + P:CommandLine|EQ|('S', '*AppData\Local\Microsoft\TeamsMeetingAddin\*')|CTX:NEG
EXCLUSION  + P:CommandLine|IN|(\'L\', ((\'S\', \'*\x64\Microsoft.Teams.AddinLoader.dll\'), (\'S\', \'*\x64\Microsoft.Teams.AddinLoader.dll\"\'), (\'S\', \'*\x86\Microsoft.Teams.AddinLoader.dll\'), (\'S\', \'*\x86\Microsoft.Teams.Addi
EXCLUSION  - P:CommandLine|IN|('L', (('S', '*AppData\Local\Microsoft\TeamsMeetingAddin\*'), ('S', '*\x86\Microsoft.Teams.AddinLoader.dll')))|CTX:NEG
```


---

## V016

```
SELECTION  + P:CommandLine|IN|('L', (('S', '* /impersonateuser:*'), ('S', '* asktgt /user:*'), ('S', '* asreproast *'), ('S', '* createnetonly /program:*'), ('S', '* dump /luid:0x*'), ('S', '* dump /service:krbtgt *'), ('S', '* golde
SELECTION  - P:CommandLine|IN|('L', (('S', '* /impersonateuser:*'), ('S', '* asktgt /user:*'), ('S', '* asreproast *'), ('S', '* createnetonly /program:*'), ('S', '* dump /luid:0x*'), ('S', '* dump /service:krbtgt *'), ('S', '* golde
```


---

## V017

```
(no predicate-level change)
```


---

## V018

```
EXCLUSION  + P:Image|EQ|('S', '*\LZMA_EXE')|CTX:NEG
```


---

## V019

```
EXCLUSION  + P:Image|EQ|('S', '*:\windows\system32\svchost.exe')|CTX:NEG
EXCLUSION  - P:Image|EQ|('S', 'C:\windows\system32\svchost.exe')|CTX:NEG
SELECTION  + P:TargetFilename|EQ|('S', '*:\Windows\Prefetch\*')|CTX:POS
SELECTION  - P:TargetFilename|EQ|('S', 'C:\Windows\Prefetch\*')|CTX:POS
```


---

## V020

```
EXCLUSION  + P:CommandLine|IN|('L', (('S', '* -c*'), ('S', '* -h*'), ('S', '* -z*'), ('S', '* /**')))|CTX:NEG
EXCLUSION  - P:CommandLine|IN|('L', (('S', '*-c*'), ('S', '*-h*'), ('S', '*-z*')))|CTX:NEG
```


---

## V021

```
SELECTION  + P:Image|EQ|('S', '*\AnyDesk.exe')|CTX:POS
```


---

## V022

```
EXCLUSION  + P:Details|EQ|('S', '*\AppData\Local\Microsoft\OneDrive\*')|CTX:NEG
EXCLUSION  - P:Details|EQ|('S', '*\AppData\Local\Microsoft\OneDrive\Update\OneDriveSetup.exe*')|CTX:NEG
```


---

## V023

```
EXCLUSION  + P:CommandLine|EQ|('S', 'PowerShell.exe')|CTX:NEG
```


---

## V024

```
EXCLUSION  + P:userIdentity.arn|EQ|('S', '*requestParameters.userName*')|CTX:NEG
EXCLUSION  - P:userIdentity.arn|EQ|('S', '*responseElements.accessKey.userName*')|CTX:NEG
```


---

## V025

```
EXCLUSION  + P:Details|EQ|('S', 'C:\Windows\System32\STAgent.dll')|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', '*\regsvr32.exe')|CTX:NEG
EXCLUSION  + P:TargetObject|EQ|('S', '*\Services\NTDS\Parameters\ServiceDll')|CTX:NEG
EXCLUSION  - P:TargetObject|EQ|('S', '*\CurrentControlSet\Services\NTDS\Parameters\ServiceDll')|CTX:NEG
SELECTION  + P:TargetObject|EQ|('S', '*ControlSet*')|CTX:POS
SELECTION  + P:TargetObject|EQ|('S', '*\Services\*')|CTX:POS
SELECTION  + P:TargetObject|EQ|('S', '*\System\*')|CTX:POS
SELECTION  - P:TargetObject|EQ|('S', 'HKLM\System\CurrentControlSet\Services\*')|CTX:POS
```


---

## V026

```
EXCLUSION  + P:ParentImage|EQ|('S', '*\Notepad++\updater\*')|CTX:NEG
SELECTION  + P:CommandLine|EQ|('S', '*')|CTX:POS
```


---

## V027

```
EXCLUSION  + P:Image|EQ|('S', '*C:\Program Files (x86)\Microsoft\EdgeUpdate\Install\{*')|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', '*\setup.exe*')|CTX:NEG
```


---

## V028

```
EXCLUSION  + P:CommandLine|EQ|('S', '* -localserver ')|CTX:NEG
EXCLUSION  - P:CommandLine|EQ|('S', '* -localserver 22d8c27b-47a1-48d1-ad08-7da7abd79617')|CTX:NEG
```


---

## V029

```
EXCLUSION  + P:ScriptBlockText|EQ|(\'S\', "*Alias(\'htdefac\')*")|CTX:NEG
EXCLUSION  + P:ScriptBlockText|EQ|(\'S\', "*Alias(\'ltdefac\')*")|CTX:NEG
EXCLUSION  + P:ScriptBlockText|EQ|(\'S\', "*Alias(\'mtdefac\')*")|CTX:NEG
EXCLUSION  + P:ScriptBlockText|EQ|(\'S\', "*Alias(\'stdefac\')*")|CTX:NEG
SELECTION  + P:ScriptBlockText|IN|('L', (('S', '*htdefac*'), ('S', '*ltdefac*'), ('S', '*mtdefac*'), ('S', '*stdefac*')))|CTX:POS
```


---

## V030

```
EXCLUSION  + P:Image|EQ|('S', '*C:\ProgramData\Microsoft\Windows Defender\Platform\*')|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', '*\MsMpEng.exe*')|CTX:NEG
```


---

## V031

```
EXCLUSION  + P:CommandLine|EQ|(\'S\', \'*\AppData\Local\Microsoft\Teams\Update.exe\" --processStart \"Teams.exe\"*\')|CTX:NEG
```


---

## V032

```
SELECTION  + P:eventName|EQ|('S', 'AssumeRole')|CTX:POS
SELECTION  + P:userIdentity.sessionContext.sessionIssuer.type|EQ|('S', 'Role')|CTX:POS
SELECTION  - P:eventName|EQ|('S', 'AssumedRole')|CTX:POS
SELECTION  - P:userIdentity.sessionContext|EQ|('S', 'Role')|CTX:POS
```


---

## V033

```
EXCLUSION  + P:Image|EQ|('S', '*\MsMpEng.exe')|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', 'C:\ProgramData\Microsoft\Windows Defender\Platform\*')|CTX:NEG
EXCLUSION  + P:Image|IN|('L', (('S', '*\MsMpEng.exe'), ('S', '*\SearchApp.exe'), ('S', '*\autochk.exe'), ('S', '*\compattelrunner.exe'), ('S', '*\csrss.exe'), ('S', '*\defrag.exe'), ('S', '*\dfsrs.exe'), ('S', '*\lsass.exe'), ('S', '
EXCLUSION  + P:Image|IN|('L', (('S', 'C:\Program Files\Bitdefender Antivirus Free\downloader.exe'), ('S', 'C:\Program Files\Bitdefender Antivirus Free\updatesrv.exe'), ('S', 'C:\Program Files\Bitdefender Antivirus Free\vsserv.exe'), 
EXCLUSION  - P:Image|IN|('L', (('S', '*C:\Windows\System32\DeviceCensus.exe'), ('S', '*C:\Windows\System32\SrTasks.exe'), ('S', '*C:\Windows\System32\dllhost.exe'), ('S', '*C:\Windows\System32\taskhostw.exe'), ('S', '*\MsMpEng.exe'),
EXCLUSION  - P:Image|IN|('L', (('S', 'C:\Program Files\Bitdefender Antivirus Free\downloader.exe'), ('S', 'C:\Program Files\Bitdefender Antivirus Free\updatesrv.exe'), ('S', 'C:\Program Files\Bitdefender Antivirus Free\vsserv.exe'), 
```


---

## V034

```
SELECTION  + P:dst_port|IN|('L', (('X', 11211), ('X', 1433), ('X', 1521), ('X', 15672), ('X', 21), ('X', 23), ('X', 27017), ('X', 3306), ('X', 50000), ('X', 5900), ('X', 5901), ('X', 5902), ('X', 5903), ('X', 5904), ('X', 80), ('X', 
SELECTION  - P:destination.port|IN|('L', (('X', 11211), ('X', 1433), ('X', 1521), ('X', 15672), ('X', 21), ('X', 23), ('X', 27017), ('X', 3306), ('X', 50000), ('X', 5900), ('X', 5901), ('X', 5902), ('X', 5903), ('X', 5904), ('X', 80)
```


---

## V035

```
EXCLUSION  + P:CommandLine|IN|('L', (('S', '* >*'), ('S', '*-WindowStyle hidden -Verb runAs*'), ('S', '*ConvertTo-Json*'), ('S', '*Out-File*')))|CTX:NEG
EXCLUSION  - P:CommandLine|IN|('L', (('S', '* >*'), ('S', '*ConvertTo-Json*'), ('S', '*Out-File*')))|CTX:NEG
```


---

## V036

```
EXCLUSION  + P:User|IN|('L', (('S', '*AUTHORI*'), ('S', '*AUTORI*')))|CTX:NEG
EXCLUSION  - P:User|IN|('L', (('S', 'AUTORITE NT\Sys*'), ('S', 'NT AUTHORITY\SYSTEM*')))|CTX:NEG
```


---

## V037

```
EXCLUSION  + P:CommandLine|EQ|('S', 'C:\Windows\syswow64\MsiExec.exe -Embedding*')|CTX:NEG
EXCLUSION  + P:ParentImage|EQ|('S', '*:\Windows\SysWOW64\msiexec.exe')|CTX:NEG
```


---

## V038

```
EXCLUSION  + P:Image|EQ|(\'S\', "-\'*\adexplorer.exe\' -\'*\procdump.exe\' -\'*\msbuild.exe\' -\'*\dotnet.exe\' -\'*\cmd.exe\' -\'*\powershell.exe\' -\'*\psexec.exe\' -\'*\installutil.exe\' -\'*\cscript.exe\' -\'*\wscript.exe\' -\'*\
EXCLUSION  - P:Image|IN|('L', (('S', '*\7z.exe'), ('S', '*\adexplorer.exe'), ('S', '*\certutil.exe'), ('S', '*\cmd.exe'), ('S', '*\cmstp.exe'), ('S', '*\cscript.exe'), ('S', '*\dotnet.exe'), ('S', '*\installutil.exe'), ('S', '*\msbui
```


---

## V039

```
EXCLUSION  + P:Image|IN|('L', (('S', '*\vcredist_x64.exe'), ('S', '*\vcredist_x86.exe')))|CTX:NEG
EXCLUSION  + P:Image|IN|('L', (('S', 'C:\Program Files (x86)\Microsoft Visual Studio\*'), ('S', 'C:\Program Files\Microsoft Visual Studio\*')))|CTX:NEG
EXCLUSION  + P:ParentImage|EQ|('S', '*\WebEx\WebexHost.exe')|CTX:NEG
EXCLUSION  + P:ParentImage|EQ|('S', '*\thor\thor64.exe')|CTX:NEG
EXCLUSION  - P:Image|EQ|('S', '*\vcredi*')|CTX:NEG
EXCLUSION  - P:ParentImage|IN|('L', (('S', '*-installer.exe'), ('S', '*\WebEx\WebexHost.exe'), ('S', '*\thor\thor64.exe')))|CTX:NEG
SELECTION  + P:Image|IN|('L', (('S', '*~1.bat*'), ('S', '*~1.dll*'), ('S', '*~1.exe*'), ('S', '*~1.hta*'), ('S', '*~1.js*'), ('S', '*~1.msi*'), ('S', '*~1.ps1*'), ('S', '*~1.tmp*'), ('S', '*~1.vbe*'), ('S', '*~1.vbs*'), ('S', '*~2.ba
SELECTION  - P:Image|IN|('L', (('S', '*~1.bat*'), ('S', '*~1.dll*'), ('S', '*~1.exe*'), ('S', '*~1.hta*'), ('S', '*~1.js*'), ('S', '*~1.msi*'), ('S', '*~1.ps1*'), ('S', '*~1.vbe*'), ('S', '*~1.vbs*'), ('S', '*~2.bat*'), ('S', '*~2.dl
```


---

## V040

```
EXCLUSION  + P:r-dns|IN|('L', (('S', '*.au'), ('S', '*.ca'), ('S', '*.ch'), ('S', '*.com'), ('S', '*.de'), ('S', '*.edu'), ('S', '*.es'), ('S', '*.fr'), ('S', '*.gov'), ('S', '*.it'), ('S', '*.jp'), ('S', '*.net'), ('S', '*.nl'), ('S
SELECTION  + P:c-uri-extension|IN|('L', (('S', 'bat'), ('S', 'docx'), ('S', 'exe'), ('S', 'ps1'), ('S', 'rar'), ('S', 'vbs')))|CTX:POS
SELECTION  - P:c-uri-extension|EQ|('S', 'exe')|CTX:POS
```


---

## V041

```
SELECTION  + P:EventType|EQ|('S', 'SetValue')|CTX:POS
```


---

## V042

```
EXCLUSION  + P:FileNameBuffer|EQ|('S', '*\Program Files\ESET\ESET Security\eamsi.dll')|CTX:NEG
EXCLUSION  + P:FileNameBuffer|EQ|('S', '*\Program Files\National Instruments\Shared\mDNS Responder\nimdnsNSP.dll ')|CTX:NEG
EXCLUSION  + P:FileNameBuffer|IN|('L', (('S', '*\Program Files\McAfee\Endpoint Security\Threat Prevention\MfeAmsiProvider.dll'), ('S', '*\Program Files\McAfee\MfeAV\AMSIExt.dll')))|CTX:NEG
EXCLUSION  - P:ValidatedPolicy|EQ|('X', 1)|CTX:NEG
EXCLUSION  - P:ValidatedPolicy|IN|('L', (('X', 1), ('X', 2)))|CTX:NEG
```


---

## V043

```
SELECTION  + P:Hash|IN|('L', (('S', '*IMPHASH=021BCCA20BA3381B11BDDE26B4E62F20*'), ('S', '*IMPHASH=03866661686829d806989e2fc5a72606*'), ('S', '*IMPHASH=0588081AB0E63BA785938467E1B10CCA*'), ('S', '*IMPHASH=07A2D4DCBD6CB2C6A45E6B101F0B
SELECTION  + P:Imphash|IN|('L', (('S', '021bcca20ba3381b11bdde26b4e62f20'), ('S', '03866661686829d806989e2fc5a72606'), ('S', '0588081ab0e63ba785938467e1b10cca'), ('S', '07a2d4dcbd6cb2c6a45e6b101f0b6d51'), ('S', '09D278F9DE118EF09163C
SELECTION  - P:Hash|IN|('L', (('S', '*IMPHASH=03866661686829d806989e2fc5a72606*'), ('S', '*IMPHASH=0588081AB0E63BA785938467E1B10CCA*'), ('S', '*IMPHASH=07A2D4DCBD6CB2C6A45E6B101F0B6D51*'), ('S', '*IMPHASH=09D278F9DE118EF09163C6140255
SELECTION  - P:Imphash|IN|('L', (('S', '03866661686829d806989e2fc5a72606'), ('S', '0588081ab0e63ba785938467e1b10cca'), ('S', '07a2d4dcbd6cb2c6a45e6b101f0b6d51'), ('S', '09D278F9DE118EF09163C6140255C690'), ('S', '0c106686a31bfe2ba931a
```


---

## V044

```
SELECTION  + P:CommandLine|IN|('L', (('S', '*%COMSPEC%*'), ('S', '*cmd*')))|CTX:POS
SELECTION  - P:CommandLine|EQ|('S', '*%COMSPEC%*')|CTX:POS
SELECTION  - P:CommandLine|EQ|('S', '*cmd.exe*')|CTX:POS
```


---

## V045

```
EXCLUSION  + P:Image|IN|('L', (('S', 'C:\WINDOWS\system32\wevtutil.exe'), ('S', 'C:\Windows\Sysmon.exe'), ('S', 'C:\Windows\Sysmon64.exe'), ('S', 'C:\Windows\System32\conhost.exe'), ('S', 'wevtutil.exe')))|CTX:NEG
EXCLUSION  - P:Image|IN|('L', (('S', 'C:\WINDOWS\system32\wevtutil.exe'), ('S', 'C:\Windows\Sysmon64.exe'), ('S', 'C:\Windows\System32\WerFault.exe'), ('S', 'C:\Windows\System32\conhost.exe'), ('S', 'wevtutil.exe')))|CTX:NEG
```


---

## V046

```
EXCLUSION  + P:IpAddress|EQ|('S', '169.254.0.0/16')|CTX:NEG
EXCLUSION  + P:IpAddress|EQ|('S', '::1/128')|CTX:NEG
EXCLUSION  + P:IpAddress|EQ|('S', 'fc00::/7')|CTX:NEG
EXCLUSION  + P:IpAddress|EQ|('S', 'fe80::/10')|CTX:NEG
EXCLUSION  - P:IpAddress|EQ|('S', '::1')|CTX:NEG
EXCLUSION  - P:IpAddress|IN|('L', (('S', 'fc*'), ('S', 'fd*'), ('S', 'fe80:*')))|CTX:NEG
```


---

## V047

```
EXCLUSION  + P:ImageLoaded|IN|('L', (('S', 'C:\Program Files (x86)\*'), ('S', 'C:\Program Files\*')))|CTX:NEG
EXCLUSION  - P:ImageLoaded|IN|('L', (('S', 'C:\Program Files (x86)\Pidgin\*'), ('S', 'C:\Program Files (x86)\ossec-agent\*'), ('S', 'C:\Program Files\Inkscape\bin\*')))|CTX:NEG
```


---

## V048

```
EXCLUSION  + P:DestinationIp|EQ|('S', '::1')|CTX:NEG
EXCLUSION  + P:SourceIp|EQ|('S', '::1')|CTX:NEG
```


---

## V049

```
EXCLUSION  + P:Provider_Name|EQ|('S', 'Microsoft-Windows-Kernel-Process')|CTX:NEG
SELECTION  + P:Image|EQ|('S', '*')|CTX:POS
```


---

## V050

```
SELECTION  + P:ImageLoaded|IN|('L', (('S', '*\VBE7.DLL*'), ('S', '*\VBE7INTL.DLL*'), ('S', '*\VBEUI.DLL*')))|CTX:POS
SELECTION  + P:Image|IN|('L', (('S', '*\excel.exe*'), ('S', '*\outlook.exe*'), ('S', '*\powerpnt.exe*'), ('S', '*\winword.exe*')))|CTX:POS
SELECTION  - P:ImageLoaded|IN|('L', (('S', '*\VBE7.DLL'), ('S', '*\VBE7INTL.DLL'), ('S', '*\VBEUI.DLL')))|CTX:POS
SELECTION  - P:Image|IN|('L', (('S', '*\excel.exe'), ('S', '*\outlook.exe'), ('S', '*\powerpnt.exe'), ('S', '*\winword.exe')))|CTX:POS
```


---

## V051

```
SELECTION  + P:EventID|EQ|('X', 4697)|CTX:POS
SELECTION  + P:ServiceFileName|EQ|('S', '*%COMSPEC%*')|CTX:POS
SELECTION  + P:ServiceFileName|EQ|('S', '*.dll,a*')|CTX:POS
SELECTION  + P:ServiceFileName|EQ|('S', '*/c*')|CTX:POS
SELECTION  + P:ServiceFileName|EQ|('S', '*/p:*')|CTX:POS
SELECTION  + P:ServiceFileName|EQ|('S', '*\pipe\*')|CTX:POS
SELECTION  + P:ServiceFileName|EQ|('S', '*cmd*')|CTX:POS
SELECTION  + P:ServiceFileName|EQ|('S', '*echo*')|CTX:POS
SELECTION  - P:EventID|IN|('L', (('X', 4697), ('X', 7045)))|CTX:POS
SELECTION  - P:ServiceFileName|IN|('L', (('S', '%COMSPEC% /c echo * > \.\pipe\*'), ('S', '*cmd* /c echo * > \.\pipe\*'), ('S', '*rundll32*.dll,a /p:*')))|CTX:POS
```


---

## V052

```
EXCLUSION  + P:SubjectUserName|EQ|('S', '*$')|CTX:NEG
```


---

## V053

```
EXCLUSION  + P:GrantedAccess|EQ|('S', '0x1010')|CTX:NEG
EXCLUSION  + P:SourceImage|EQ|('S', 'C:\Windows\sysWOW64\wbem\wmiprvse.exe')|CTX:NEG
```


---

## V054

```
EXCLUSION  + P:Image|EQ|('S', '*\MicrosoftEdgeUpdate.exe')|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', 'C:\Windows\System32\RuntimeBroker.exe')|CTX:NEG
```


---

## V055

```
(no predicate-level change)
```


---

## V056

```
EXCLUSION  + P:Image|EQ|('S', 'C:\Program Files\Mozilla Firefox\firefox.exe')|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', 'C:\Program Files\SplunkUniversalForwarder\bin\*')|CTX:NEG
EXCLUSION  - P:Image|IN|('L', (('S', 'C:\Program Files\Mozilla Firefox\firefox.exe*'), ('S', 'C:\Program Files\SplunkUniversalForwarder\bin\*')))|CTX:NEG
```


---

## V057

```
EXCLUSION  - P:TargetObject|EQ|('S', '*\NgcFirst\ConsecutiveSwitchCount')|CTX:NEG
```


---

## V058

```
EXCLUSION  + P:Image|IN|('L', (('S', 'C:\Program Files (x86)\*'), ('S', 'C:\Program Files\*'), ('S', 'C:\Windows\System32\*')))|CTX:NEG
EXCLUSION  + P:TargetObject|IN|('L', (('S', '*\CLSID\{098f2470-bae0-11cd-b579-08002b30bfeb}\*'), ('S', '*\CLSID\{1AA9BF05-9A97-48c1-BA28-D9DCE795E93C}\*'), ('S', '*\CLSID\{2e2294a9-50d7-4fe7-a09f-e6492e185884}\*'), ('S', '*\CLSID\{34
```


---

## V059

```
EXCLUSION  + P:CommandLine|EQ|('S', '*\UpdateDeploy.dll /ClassId *')|CTX:NEG
EXCLUSION  + P:DestinationIp|IN|('L', (('S', '20.184.*'), ('S', '20.185.*'), ('S', '20.186.*'), ('S', '20.187.*'), ('S', '20.188.*'), ('S', '20.189.*'), ('S', '20.190.*'), ('S', '20.191.*'), ('S', '23.79.*'), ('S', '51.10.*'), ('S', 
EXCLUSION  - P:CommandLine|EQ|('S', '')|CTX:NEG
EXCLUSION  - P:CommandLine|IN|('L', (('S', '*:\Windows\UUS\Packages\Preview\amd64\updatedeploy.dll /ClassId*'), ('S', '*:\Windows\UUS\amd64\UpdateDeploy.dll /ClassId*')))|CTX:NEG
EXCLUSION  - P:CommandLine|IN|('L', (('S', '*:\Windows\WinSxS\*'), ('S', '*\UpdateDeploy.dll /ClassId *')))|CTX:NEG
EXCLUSION  - P:DestinationIp|IN|('L', (('S', '0:0:0:0:0:0:0:1*'), ('S', '::1*'), ('S', 'fc*'), ('S', 'fd*'), ('S', 'fe80:*')))|CTX:NEG
EXCLUSION  - P:DestinationIp|IN|('L', (('S', '10.*'), ('S', '127.*'), ('S', '169.254.*'), ('S', '172.16*'), ('S', '172.17*'), ('S', '172.18*'), ('S', '172.19*'), ('S', '172.20*'), ('S', '172.21*'), ('S', '172.22*'), ('S', '172.23*'),
EXCLUSION  - P:DestinationIp|IN|('L', (('S', '20.184.*'), ('S', '20.185.*'), ('S', '20.186.*'), ('S', '20.187.*'), ('S', '20.188.*'), ('S', '20.189.*'), ('S', '20.190.*'), ('S', '20.191.*'), ('S', '20.220.*'), ('S', '20.221.*'), ('S'
SELECTION  - P:CommandLine|EQ|('S', '* /RunHandlerComServer*')|CTX:POS
SELECTION  - P:CommandLine|EQ|('S', '*')|CTX:POS
```


---

## V060

```
SELECTION  + P:CommandLine|IN|('L', (('S', '*10.*'), ('S', '*127.*'), ('S', '*169.254.*'), ('S', '*172.16.*'), ('S', '*172.17.*'), ('S', '*172.18.*'), ('S', '*172.19.*'), ('S', '*172.20.*'), ('S', '*172.21.*'), ('S', '*172.22.*'), ('
```


---

## V061

```
EXCLUSION  + P:Details|IN|('L', (('S', '%SystemRoot%\System32\vmictimeprovider.dll'), ('S', '%systemroot%\system32\w32time.dll'), ('S', 'C:\Windows\SYSTEM32\w32time.DLL')))|CTX:NEG
EXCLUSION  - P:Details|EQ|('S', 'C:\Windows\SYSTEM32\w32time.DLL')|CTX:NEG
SELECTION  + P:TargetObject|EQ|('S', '*\DllName')|CTX:POS
SELECTION  + P:TargetObject|EQ|('S', '*\Services\W32Time\TimeProviders*')|CTX:POS
SELECTION  - P:TargetObject|EQ|('S', '*DllName')|CTX:POS
SELECTION  - P:TargetObject|EQ|('S', 'HKLM\System\CurrentControlSet\Services\W32Time\TimeProviders*')|CTX:POS
```


---

## V062

```
EXCLUSION  + P:IntegrityLevel|IN|('L', (('S', 'S-1-16-16384'), ('S', 'System')))|CTX:NEG
EXCLUSION  - P:IntegrityLevel|EQ|('S', 'System')|CTX:NEG
```


---

## V063

```
EXCLUSION  + P:Details|EQ|('S', 'DWORD (0x00000002)')|CTX:NEG
EXCLUSION  + P:TargetObject|EQ|('S', '*\SecurityLayer')|CTX:NEG
SELECTION  + P:TargetObject|IN|('L', (('S', '*\Control\Terminal Server\InitialProgram*'), ('S', '*\Control\Terminal Server\WinStations\RDP-Tcp\InitialProgram*'), ('S', '*\Terminal Server\WinStations\RDP-Tcp\SecurityLayer*'), ('S', '*
SELECTION  - P:TargetObject|IN|('L', (('S', '*\Control\Terminal Server\InitialProgram*'), ('S', '*\Control\Terminal Server\WinStations\RDP-Tcp\InitialProgram*'), ('S', '*\Windows NT\Terminal Services\InitialProgram*'), ('S', '*\servi
```


---

## V064

```
EXCLUSION  + P:SourceImage|EQ|('S', '*C:\Program Files\Mozilla Firefox\firefox.exe')|CTX:NEG
EXCLUSION  + P:TargetImage|EQ|('S', '*C:\Program Files\Mozilla Firefox\firefox.exe')|CTX:NEG
```


---

## V065

```
EXCLUSION  + P:CommandLine|EQ|('S', '* -d *')|CTX:NEG
EXCLUSION  + P:CommandLine|EQ|('S', '* -e kill *')|CTX:NEG
EXCLUSION  + P:ParentImage|EQ|('S', '*\cmd.exe')|CTX:NEG
```


---

## V066

```
EXCLUSION  + P:DestinationIp|IN|('L', (('S', '10.*'), ('S', '127.0.0.1'), ('S', '172.*'), ('S', '192.168.*')))|CTX:NEG
EXCLUSION  + P:DestinationIsIpv6|EQ|('S', 'false')|CTX:NEG
```


---

## V067

```
EXCLUSION  + P:CallTrace|EQ|('S', '*)')|CTX:NEG
```


---

## V068

```
EXCLUSION  + P:CurrentDirectory|EQ|('S', '*\ccmcache\*')|CTX:NEG
EXCLUSION  - P:CurrentDirectory|EQ|('S', '*\ccmcache\*')|CTX:NEG
```


---

## V069

```
EXCLUSION  + P:Image|EQ|('S', '*\installer.exe')|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', '*peazip*')|CTX:NEG
EXCLUSION  + P:Image|IN|('L', (('S', 'C:\Program Files (x86)\Opera\*'), ('S', 'C:\Program Files\Opera\*')))|CTX:NEG
EXCLUSION  + P:TargetObject|EQ|('S', '\PeaZip.*')|CTX:NEG
```


---

## V070

```
SELECTION  + P:CommandLine|IN|('L', (('S', '* /ntlm:NTLMhash *'), ('S', '* ntlmrelay*'), ('S', '* smbrelay*'), ('S', '*.exe -t * -p *'), ('S', '*Invoke-PetitPotam*'), ('S', '*Invoke-Tater*'), ('S', '*cme smb *')))|CTX:POS
SELECTION  - P:CommandLine|IN|('L', (('S', '* /ntlm:NTLMhash *'), ('S', '* ntlmrelay*'), ('S', '* smbrelay*'), ('S', '*Invoke-PetitPotam*'), ('S', '*Invoke-Tater*'), ('S', '*cme smb *')))|CTX:POS
```


---

## V071

```
EXCLUSION  + P:CommandLine|IN|(\'L\', ((\'S\', \'*\control.exe input.dll\'), (\'S\', \'*\control.exe\" input.dll\')))|CTX:NEG
EXCLUSION  - P:CommandLine|EQ|('S', '*\control.exe input.dll')|CTX:NEG
```


---

## V072

```
EXCLUSION  + P:CommandLine|EQ|('S', '*powershell.exe -ExecutionPolicy Restricted -Command $Res = 0;*')|CTX:NEG
EXCLUSION  + P:CommandLine|EQ|(\'S\', "*{ $Res = 1; break; } } Write-Host \'Final result:\', $Res;")|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', '*\powershell.exe')|CTX:NEG
```


---

## V073

```
SELECTION  + P:CommandLine|EQ|('S', '*WebPages\Errors\webErrorLog.txt*')|CTX:POS
SELECTION  + P:CommandLine|EQ|('S', '*del /s /q /f*')|CTX:POS
```


---

## V074

```
SELECTION  + P:Description|EQ|('S', 'Process Hacker')|CTX:POS
SELECTION  + P:Image|EQ|('S', '*\ProcessHacker.exe')|CTX:POS
SELECTION  + P:OriginalFileName|IN|('L', (('S', 'Process Hacker'), ('S', 'ProcessHacker.exe')))|CTX:POS
SELECTION  - P:Description|IN|('L', (('S', 'Process Hacker'), ('S', 'System Informer')))|CTX:POS
SELECTION  - P:Image|IN|('L', (('S', '*\ProcessHacker.exe'), ('S', '*\SystemInformer.exe')))|CTX:POS
SELECTION  - P:OriginalFileName|IN|('L', (('S', 'Process Hacker'), ('S', 'ProcessHacker.exe'), ('S', 'SystemInformer.exe')))|CTX:POS
```


---

## V075

```
EXCLUSION  + P:_raw|CONTAINS|(\'S\', "(New-Object System.Net.WebClient).DownloadString(\'https://chocolatey.org/install.ps1\')")|CTX:NEG
```


---

## V076

```
EXCLUSION  + P:Image|EQ|('S', 'C:\Windows\System32\wuauclt.exe')|CTX:NEG
```


---

## V077

```
EXCLUSION  + P:Image|IN|('L', (('S', '*\powershell.exe'), ('S', '*\powershell_ise.exe'), ('S', '*\pwsh.exe')))|CTX:NEG
EXCLUSION  - P:Image|IN|('L', (('S', '*\powershell.exe'), ('S', '*\powershell_ise.exe')))|CTX:NEG
SELECTION  + P:Description|IN|('L', (('S', 'Windows PowerShell*'), ('S', 'pwsh*')))|CTX:POS
SELECTION  - P:Description|EQ|('S', 'Windows PowerShell')|CTX:POS
```


---

## V078

```
EXCLUSION  - P:Description|EQ|('S', 'Failed to open service configuration with error 19 - Last error: The media is write protected.')|CTX:NEG
SELECTION  + P:EventID|EQ|('X', 16)|CTX:POS
SELECTION  - P:Description|IN|('L', (('S', '*Failed to connect to the driver to update configuration*'), ('S', '*Failed to open service configuration with error*')))|CTX:POS
```


---

## V079

```
EXCLUSION  + P:Image|IN|('L', (('S', 'C:\Windows\SysWOW64\*'), ('S', 'C:\Windows\System32\*')))|CTX:NEG
EXCLUSION  - P:TargetFilename|IN|('L', (('S', 'C:\Windows\SysWOW64\*'), ('S', 'C:\Windows\System32\*')))|CTX:NEG
SELECTION  + P:CommandLine|EQ|('S', '*winrm*')|CTX:POS
SELECTION  + P:CommandLine|IN|(\'L\', ((\'S\', \'*format:\"pretty\"*\'), (\'S\', \'*format:\"text\"*\'), (\'S\', \'*format:pretty*\'), (\'S\', \'*format:text*\')))|CTX:POS
SELECTION  - P:TargetFilename|IN|('L', (('S', '*WsmPty.xsl'), ('S', '*WsmTxt.xsl')))|CTX:POS
```


---

## V080

```
EXCLUSION  + P:TargetFilename|IN|('L', (('S', '*:\$WINDOWS.~BT\NewOS\*'), ('S', '*:\$WinREAgent\*'), ('S', '*:\WUDownloadCache\*'), ('S', '*:\Windows\SoftwareDistribution\Download\*'), ('S', '*:\Windows\SysWOW64\*'), ('S', '*:\Window
EXCLUSION  - P:TargetFilename|IN|('L', (('S', '*:\$WINDOWS.~BT\NewOS\*'), ('S', '*:\$WinREAgent\*'), ('S', '*:\WUDownloadCache\*'), ('S', '*:\Windows\SysWOW64\*'), ('S', '*:\Windows\System32\*'), ('S', '*:\Windows\WinSxS\*'), ('S', '
```


---

## V081

```
EXCLUSION  + P:dst_ip|EQ|('S', '10.0.0.0/8')|CTX:NEG
EXCLUSION  + P:dst_ip|EQ|('S', '127.0.0.0/8')|CTX:NEG
EXCLUSION  + P:dst_ip|EQ|('S', '172.16.0.0/12')|CTX:NEG
EXCLUSION  + P:dst_ip|EQ|('S', '192.168.0.0/16')|CTX:NEG
EXCLUSION  - P:dst_ip|IN|('L', (('S', '10.0.0.0/8'), ('S', '127.0.0.0/8'), ('S', '172.16.0.0/12'), ('S', '192.168.0.0/16')))|CTX:NEG
```


---

## V082

```
EXCLUSION  + P:SourceImage|EQ|('S', '*\AppData\Local\yammerdesktop\app-*')|CTX:NEG
EXCLUSION  + P:SourceImage|EQ|('S', '*\Yammer.exe')|CTX:NEG
EXCLUSION  + P:TargetImage|EQ|('S', '*\AppData\Local\yammerdesktop\app-*')|CTX:NEG
EXCLUSION  + P:TargetImage|EQ|('S', '*\Yammer.exe')|CTX:NEG
EXCLUSION  - P:SourceImage|EQ|('S', '*\AppData\Local\yammerdesktop\app-3.4.5\Yammer.exe')|CTX:NEG
EXCLUSION  - P:TargetImage|EQ|('S', '*\AppData\Local\yammerdesktop\app-3.4.5\Yammer.exe')|CTX:NEG
```


---

## V083

```
EXCLUSION  + P:Path|IN|('L', (('S', '*https://installer.teams.static.microsoft/*'), ('S', '*https://statics.teams.cdn.live.net/*'), ('S', '*https://statics.teams.cdn.office.net/*'), ('S', '*microsoft.com*')))|CTX:NEG
EXCLUSION  - P:Path|IN|('L', (('S', '*https://statics.teams.cdn.live.net/*'), ('S', '*https://statics.teams.cdn.office.net/*'), ('S', '*microsoft.com*')))|CTX:NEG
```


---

## V084

```
EXCLUSION  + P:Image|IN|('L', (('S', 'C:\Program Files\Google\Chrome\Application\chrome.exe'), ('S', 'C:\Program Files\Mozilla Firefox\firefox.exe'), ('S', 'C:\Windows\System32\lsass.exe')))|CTX:NEG
EXCLUSION  - P:Image|IN|('L', (('S', '*\chrome.exe'), ('S', '*\firefox.exe'), ('S', '*\lsass.exe'), ('S', '*\opera.exe'), ('S', '*\tomcat\bin\tomcat8.exe')))|CTX:NEG
```


---

## V085

```
EXCLUSION  + P:Image|IN|('L', (('S', 'C:\Windows\SysWOW64\*'), ('S', 'C:\Windows\System32\*'), ('S', 'C:\Windows\WinSxS\*'), ('S', 'C:\avast! sandbox*')))|CTX:NEG
EXCLUSION  - P:Image|IN|('L', (('S', 'C:\Windows\SysWOW64\*'), ('S', 'C:\Windows\SysWow64\*'), ('S', 'C:\Windows\System32\*'), ('S', 'C:\Windows\WinSxS\*'), ('S', 'C:\Windows\system32\*'), ('S', 'C:\Windows\winsxs\*'), ('S', 'C:\avas
```


---

## V086

```
EXCLUSION  + P:Hashes|EQ|('S', '*IMPHASH=00000000000000000000000000000000*')|CTX:NEG
EXCLUSION  - P:Imphash|EQ|('S', '00000000000000000000000000000000')|CTX:NEG
SELECTION  + P:Hashes|EQ|('S', '*IMPHASH=*')|CTX:POS
SELECTION  - P:Imphash|EQ|('S', '*')|CTX:POS
```


---

## V087

```
EXCLUSION  + P:Image|EQ|('S', '*\Citrix\System32\icast.exe')|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', 'C:\WINDOWS\explorer.exe')|CTX:NEG
EXCLUSION  + P:Image|IN|('L', (('S', 'C:\Windows\SysWOW64\proquota.exe'), ('S', 'C:\Windows\System32\proquota.exe')))|CTX:NEG
EXCLUSION  - P:Image|EQ|('S', '*:\WINDOWS\explorer.exe')|CTX:NEG
EXCLUSION  - P:Image|IN|('L', (('S', '*:\Program Files (x86)\Citrix\HDX\bin\cmstart.exe'), ('S', '*:\Program Files (x86)\Citrix\HDX\bin\icast.exe'), ('S', '*:\Program Files (x86)\Citrix\System32\icast.exe'), ('S', '*:\Program Files\C
EXCLUSION  - P:Image|IN|('L', (('S', '*:\Windows\SysWOW64\proquota.exe'), ('S', '*:\Windows\System32\proquota.exe')))|CTX:NEG
```


---

## V088

```
EXCLUSION  + P:FileNameBuffer|IN|('L', (('S', '*Program Files (x86)\Avast Software\Avast\aswAMSI.dll'), ('S', '*Program Files\Avast Software\Avast\aswAMSI.dll')))|CTX:NEG
EXCLUSION  + P:ProcessNameBuffer|EQ|('S', '*\AppData\Local\Keybase\Gui\Keybase.exe')|CTX:NEG
EXCLUSION  + P:ProcessNameBuffer|EQ|('S', '*\Windows\System32\SIHClient.exe')|CTX:NEG
EXCLUSION  - P:FileNameBuffer|IN|('L', (('S', '*\Mozilla Firefox\mozavcodec.dll'), ('S', '*\Mozilla Firefox\mozavutil.dll')))|CTX:NEG
EXCLUSION  - P:ProcessNameBuffer|EQ|('S', '*\AppData\Local\slack\app-*')|CTX:NEG
EXCLUSION  - P:ProcessNameBuffer|EQ|('S', '*\Mozilla Firefox\firefox.exe')|CTX:NEG
EXCLUSION  - P:ProcessNameBuffer|EQ|('S', '*\slack.exe')|CTX:NEG
EXCLUSION  - P:ProcessNameBuffer|IN|('L', (('S', '*\AppData\Local\Keybase\Gui\Keybase.exe'), ('S', '*\Microsoft\Teams\stage\Teams.exe')))|CTX:NEG
```


---

## V089

```
EXCLUSION  + P:TargetFilename|IN|('L', (('S', 'C:\Program Files (x86)\*'), ('S', 'C:\Program Files\*')))|CTX:NEG
```


---

## V090

```
EXCLUSION  + P:TargetObject|EQ|('S', '*\SOFTWARE\Microsoft\Active Setup\Installed Components\{9459C573-B17A-45AE-9F64-1857B5D58CEE}\*')|CTX:NEG
EXCLUSION  + P:TargetObject|EQ|('S', '*\Software\Microsoft\Active Setup\Installed Components\{89820200-ECBD-11cf-8B85-00AA005B4383}\*')|CTX:NEG
```


---

## V091

```
EXCLUSION  + P:CommandLine|IN|('L', (('S', '*ClearMyTracksByProcess*'), ('S', '*PrintUIEntry*'), ('S', '*UpdatePerUserSystemParameters*')))|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', '*\rundll32.exe')|CTX:NEG
SELECTION  + P:Image|EQ|('S', '*\rundll32.exe')|CTX:POS
```


---

## V092

```
EXCLUSION  + P:TargetObject|EQ|('S', '*\SOFTWARE\Microsoft\Active Setup\Installed Components\{8A69D345-D564-463c-AFF1-A69D9E530F96}*')|CTX:NEG
EXCLUSION  + P:TargetObject|EQ|('S', '*\SOFTWARE\Microsoft\Active Setup\Installed Components\{9459C573-B17A-45AE-9F64-1857B5D58CEE}*')|CTX:NEG
EXCLUSION  + P:TargetObject|EQ|('S', '*\Software\Microsoft\Active Setup\Installed Components\{89820200-ECBD-11cf-8B85-00AA005B4383}*')|CTX:NEG
EXCLUSION  - P:TargetObject|EQ|('S', '*\SOFTWARE\Microsoft\Active Setup\Installed Components\{8A69D345-D564-463c-AFF1-A69D9E530F96}\*')|CTX:NEG
EXCLUSION  - P:TargetObject|EQ|('S', '*\SOFTWARE\Microsoft\Active Setup\Installed Components\{9459C573-B17A-45AE-9F64-1857B5D58CEE}\*')|CTX:NEG
EXCLUSION  - P:TargetObject|EQ|('S', '*\Software\Microsoft\Active Setup\Installed Components\{89820200-ECBD-11cf-8B85-00AA005B4383}\*')|CTX:NEG
```


---

## V093

```
EXCLUSION  + P:CommandLine|EQ|('S', '*,#1*')|CTX:NEG
EXCLUSION  + P:CommandLine|EQ|('S', '*\FileTracker32.dll*')|CTX:NEG
```


---

## V094

```
EXCLUSION  + P:TargetObject|IN|('L', (('S', '*\Microsoft\Windows\CurrentVersion\WINEVT\Channels\Microsoft-Windows-ASN1\*'), ('S', '*\Microsoft\Windows\CurrentVersion\WINEVT\Channels\Microsoft-Windows-FileInfoMinifilter*'), ('S', '*\M
EXCLUSION  - P:TargetObject|IN|('L', (('S', '*\Microsoft\Windows\CurrentVersion\WINEVT\Channels\Microsoft-Windows-ASN1\*'), ('S', '*\Microsoft\Windows\CurrentVersion\WINEVT\Channels\Microsoft-Windows-FileInfoMinifilter*')))|CTX:NEG
```


---

## V095

```
EXCLUSION  + P:Image|EQ|('S', '*.tmp\MicrosoftEdgeUpdate.exe')|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', 'C:\Program Files (x86)\Microsoft\Temp\*')|CTX:NEG
```


---

## V096

```
EXCLUSION  + P:Image|IN|('L', (('S', 'C:\Windows\SysWOW64\*'), ('S', 'C:\Windows\System32\*')))|CTX:NEG
EXCLUSION  - P:Image|EQ|('S', 'C:\Windows\System32\*')|CTX:NEG
SELECTION  + P:OriginalFileName|EQ|('S', 'xwizard.exe')|CTX:POS
```


---

## V097

```
EXCLUSION  + P:CommandLine|IN|('L', (('S', '*C:\Program Files*'), ('S', '*C:\ProgramData*'), ('S', '*\AppData\Roaming\Code\*')))|CTX:NEG
```


---

## V098

```
EXCLUSION  + P:ParentCommandLine|EQ|('S', '* --ms-enable-electron-run-as-node *')|CTX:NEG
EXCLUSION  + P:ParentImage|EQ|('S', '*\AppData\Local\Programs\Microsoft VS Code\Code.exe')|CTX:NEG
EXCLUSION  + P:ParentImage|EQ|('S', 'C:\Users\*')|CTX:NEG
SELECTION  + P:Image|IN|('L', (('S', '*\powershell.exe'), ('S', '*\pwsh.exe')))|CTX:POS
SELECTION  + P:OriginalFileName|IN|('L', (('S', 'PowerShell.EXE'), ('S', 'pwsh.dll')))|CTX:POS
SELECTION  - P:Image|EQ|('S', '*\powershell.exe')|CTX:POS
```


---

## V099

```
EXCLUSION  + P:CommandLine|IN|('L', (('S', '*export*'), ('S', '*save*')))|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', '*reg.exe')|CTX:NEG
SELECTION  + P:CommandLine|IN|('L', (('S', '*\Software\Aerofox\FoxmailPreview*'), ('S', '*\Software\Aerofox\Foxmail\V3.1*'), ('S', '*\Software\DownloadManager\Passwords*'), ('S', '*\Software\FTPWare\COREFTP\Sites*'), ('S', '*\Softwar
SELECTION  - P:CommandLine|IN|('L', (('S', '*\Software\Aerofox\FoxmailPreview*'), ('S', '*\Software\Aerofox\Foxmail\V3.1*'), ('S', '*\Software\DownloadManager\Passwords*'), ('S', '*\Software\FTPWare\COREFTP\Sites*'), ('S', '*\Softwar
```


---

## V100

```
EXCLUSION  + P:CommandLine|EQ|('S', '*#141*')|CTX:NEG
EXCLUSION  + P:CommandLine|EQ|('S', '*EDGEHTML.dll*')|CTX:NEG
```


---

## V101

```
EXCLUSION  - P:TargetObject|EQ|('S', '*\NgcFirst\ConsecutiveSwitchCount')|CTX:NEG
```


---

## V102

```
EXCLUSION  + P:Image|EQ|('S', '*\SecurityHealthSetup.exe')|CTX:NEG
EXCLUSION  + P:TargetFilename|EQ|('S', '*\SecurityHealthSystray.exe')|CTX:NEG
EXCLUSION  + P:TargetFilename|EQ|('S', 'C:\Windows\System32\SecurityHealth\*')|CTX:NEG
```


---

## V103

```
EXCLUSION  + P:Image|EQ|('S', '')|CTX:NEG
SELECTION  + P:Image|EQ|('S', '*')|CTX:POS
```


---

## V104

```
EXCLUSION  + P:Image|EQ|('S', 'C:\Windows\System32\poqexec.exe')|CTX:NEG
EXCLUSION  + P:Image|IN|('L', (('S', 'C:\Program Files (x86)\Microsoft Office\root\integration\integrator.exe'), ('S', 'C:\Program Files\Microsoft Office\root\integration\integrator.exe')))|CTX:NEG
EXCLUSION  - P:Image|IN|('L', (('S', 'C:\Program Files (x86)\Microsoft Office\root\integration\integrator.exe'), ('S', 'C:\Program Files\Microsoft Office\root\integration\integrator.exe'), ('S', 'C:\Windows\System32\poqexec.exe')))|C
SELECTION  + P:Details|EQ|('S', '*')|CTX:POS
```


---

## V105

```
EXCLUSION  + P:CommandLine|EQ|('S', '+R +H +S +A \*.cui')|CTX:NEG
EXCLUSION  - P:CommandLine|EQ|('S', '+R +H +S +A \*.cui')|CTX:NEG
```


---

## V106

```
EXCLUSION  + P:Image|EQ|('S', 'C:\Windows\System32\poqexec.exe')|CTX:NEG
SELECTION  + P:Details|EQ|('S', '*')|CTX:POS
```


---

## V107

```
EXCLUSION  + P:ParentImage|IN|('L', (('S', 'c:\windows\system32\*'), ('S', 'c:\windows\syswow64\*')))|CTX:NEG
SELECTION  + P:Image|IN|('L', (('S', '*\fltmc.exe'), ('S', '*\schtasks.exe'), ('S', '*\systeminfo.exe')))|CTX:POS
SELECTION  - P:Image|EQ|('S', '*\fltmc.exe')|CTX:POS
SELECTION  - P:Image|EQ|('S', '*\schtasks.exe')|CTX:POS
SELECTION  - P:Image|EQ|('S', '*\systeminfo.exe')|CTX:POS
```


---

## V108

```
EXCLUSION  + P:OldUacValue|IN|('L', (('S', '*1****'), ('S', '*3****'), ('S', '*5****'), ('S', '*7****'), ('S', '*9****'), ('S', '*B****'), ('S', '*D****'), ('S', '*F****')))|CTX:NEG
EXCLUSION  + P:OldUacValue|IN|('L', (('S', '*8**'), ('S', '*9**'), ('S', '*A**'), ('S', '*B**'), ('S', '*C**'), ('S', '*D**'), ('S', '*E**'), ('S', '*F**')))|CTX:NEG
EXCLUSION  + P:OldUacValue|IN|('L', (('S', '*8***'), ('S', '*9***'), ('S', '*A***'), ('S', '*B***'), ('S', '*C***'), ('S', '*D***'), ('S', '*E***'), ('S', '*F***')))|CTX:NEG
SELECTION  + P:NewUacValue|IN|('L', (('S', '*1****'), ('S', '*3****'), ('S', '*5****'), ('S', '*7****'), ('S', '*9****'), ('S', '*B****'), ('S', '*D****'), ('S', '*F****')))|CTX:POS
SELECTION  + P:NewUacValue|IN|('L', (('S', '*8**'), ('S', '*9**'), ('S', '*A**'), ('S', '*B**'), ('S', '*C**'), ('S', '*D**'), ('S', '*E**'), ('S', '*F**')))|CTX:POS
SELECTION  + P:NewUacValue|IN|('L', (('S', '*8***'), ('S', '*9***'), ('S', '*A***'), ('S', '*B***'), ('S', '*C***'), ('S', '*D***'), ('S', '*E***'), ('S', '*F***')))|CTX:POS
SELECTION  - P:Message|EQ|('S', '*Enabled*')|CTX:POS
SELECTION  - P:Message|IN|('L', (('S', '*DES*'), ('S', '*Encrypted*'), ('S', '*Preauth*')))|CTX:POS
```


---

## V109

```
EXCLUSION  + P:Image|EQ|('S', '*\OfficeClickToRun.exe')|CTX:NEG
EXCLUSION  + P:Image|IN|('L', (('S', 'C:\Program Files (x86)\Microsoft Office\root\integration\integrator.exe'), ('S', 'C:\Windows\System32\poqexec.exe')))|CTX:NEG
EXCLUSION  + P:Image|IN|('L', (('S', 'C:\Program Files\Common Files\Microsoft Shared\ClickToRun\*'), ('S', 'C:\Program Files\Common Files\Microsoft Shared\ClickToRun\Updates\*')))|CTX:NEG
EXCLUSION  - P:Image|IN|('L', (('S', 'C:\Program Files (x86)\Microsoft Office\root\integration\integrator.exe'), ('S', 'C:\Program Files\Common Files\Microsoft Shared\ClickToRun\OfficeClickToRun.exe'), ('S', 'C:\Windows\System32\poqe
```


---

## V110

```
EXCLUSION  + P:FileNameBuffer|EQ|('S', '*\Trend Micro\Client Server Security Agent\perficrcperfmonmgr.dll')|CTX:NEG
```


---

## V111

```
EXCLUSION  + P:Image|IN|('L', (('S', '*:\PerfLogs\*'), ('S', '*:\Temp\*'), ('S', '*:\Users\Public\*'), ('S', '*\AppData\Temp\*'), ('S', '*\Windows\System32\Tasks\*'), ('S', '*\Windows\Tasks\*'), ('S', '*\Windows\Temp\*')))|CTX:NEG
EXCLUSION  + P:Image|IN|('L', (('S', '*\calc.exe'), ('S', '*\cmd.exe'), ('S', '*\cscript.exe'), ('S', '*\mshta.exe'), ('S', '*\notepad.exe'), ('S', '*\powershell.exe'), ('S', '*\pwsh.exe'), ('S', '*\regsvr32.exe'), ('S', '*\rundll32.
SELECTION  + P:ParentImage|EQ|('S', '*\provlaunch.exe')|CTX:POS
SELECTION  - P:Description|EQ|('S', 'Provisioning package runtime command launching tool')|CTX:POS
SELECTION  - P:Image|EQ|('S', '*\provlaunch.exe')|CTX:POS
SELECTION  - P:OriginalFileName|EQ|('S', 'provlaunch')|CTX:POS
```


---

## V112

```
EXCLUSION  + P:IpAddress|EQ|('S', '*-*')|CTX:NEG
EXCLUSION  + P:IpAddress|EQ|('S', '::1')|CTX:NEG
EXCLUSION  + P:IpAddress|IN|('L', (('S', '10.*'), ('S', '127.*'), ('S', '169.254.*'), ('S', '172.16.*'), ('S', '172.17.*'), ('S', '172.18.*'), ('S', '172.19.*'), ('S', '172.20.*'), ('S', '172.21.*'), ('S', '172.22.*'), ('S', '172.23.
EXCLUSION  + P:IpAddress|IN|('L', (('S', 'fc00::*'), ('S', 'fe80::*')))|CTX:NEG
EXCLUSION  - P:SourceNetworkAddress|EQ|('S', '*-*')|CTX:NEG
EXCLUSION  - P:SourceNetworkAddress|EQ|('S', '::1')|CTX:NEG
EXCLUSION  - P:SourceNetworkAddress|IN|('L', (('S', '10.*'), ('S', '127.*'), ('S', '169.254.*'), ('S', '172.16.*'), ('S', '172.17.*'), ('S', '172.18.*'), ('S', '172.19.*'), ('S', '172.20.*'), ('S', '172.21.*'), ('S', '172.22.*'), ('S
EXCLUSION  - P:SourceNetworkAddress|IN|('L', (('S', 'fc00::*'), ('S', 'fe80::*')))|CTX:NEG
```


---

## V113

```
EXCLUSION  + P:SourceImage|EQ|('S', '*\Installer\setup.exe')|CTX:NEG
EXCLUSION  + P:SourceImage|EQ|('S', 'C:\Program Files (x86)\Microsoft\Edge\Application\*')|CTX:NEG
```


---

## V114

```
EXCLUSION  + P:ApplicationPath|IN|('L', (('S', '*\AppData\Local\Keybase\keybase.exe'), ('S', '*\AppData\Local\Programs\Messenger\Messenger.exe'), ('S', '*\AppData\local\microsoft\teams\current\teams.exe')))|CTX:NEG
EXCLUSION  - P:ApplicationPath|IN|('L', (('S', '*AppData\Local\Keybase\keybase.exe'), ('S', '*AppData\Local\Programs\Messenger\Messenger.exe'), ('S', '*AppData\local\microsoft\teams\current\teams.exe')))|CTX:NEG
SELECTION  + P:ApplicationPath|IN|('L', (('S', '*\AppData\*'), ('S', '*\Temp\*')))|CTX:POS
SELECTION  - P:ApplicationPath|IN|('L', (('S', '*\AppData\*'), ('S', '*\temp\*')))|CTX:POS
```


---

## V115

```
EXCLUSION  + P:ParentImage|EQ|('S', 'C:\Windows\System32\lxss\wslhost.exe')|CTX:NEG
```


---

## V116

```
EXCLUSION  + P:Image|IN|('L', (('S', '*C:\Windows\System32\SrTasks.exe'), ('S', '*C:\Windows\System32\dllhost.exe'), ('S', '*C:\Windows\System32\taskhostw.exe'), ('S', '*\autochk.exe'), ('S', '*\compattelrunner.exe'), ('S', '*\csrss.
EXCLUSION  - P:Image|IN|('L', (('S', '*C:\Windows\System32\SrTasks.exe'), ('S', '*C:\Windows\System32\taskhostw.exe'), ('S', '*\autochk.exe'), ('S', '*\compattelrunner.exe'), ('S', '*\csrss.exe'), ('S', '*\defrag.exe'), ('S', '*\dfsr
```


---

## V117

```
EXCLUSION  + P:Image|EQ|('S', '*\GitHubDesktop.exe')|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', '*\chrome.exe')|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', '*\discord.exe')|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', '*\keybase.exe')|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', '*\msedge.exe')|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', '*\msedgewebview2.exe')|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', '*\msteams.exe')|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', '*\slack.exe')|CTX:NEG
SELECTION  + P:Image|IN|('L', (('S', '*:\Temp\*'), ('S', '*\AppData\Local\Temp\*'), ('S', '*\Users\Public\*'), ('S', '*\Windows\Temp\*')))|CTX:POS
SELECTION  + P:Image|IN|('L', (('S', '*\cmd.exe'), ('S', '*\cscript.exe'), ('S', '*\mshta.exe'), ('S', '*\powershell.exe'), ('S', '*\pwsh.exe'), ('S', '*\regsvr32.exe'), ('S', '*\wscript.exe')))|CTX:POS
SELECTION  + P:ParentImage|IN|('L', (('S', '*\GitHubDesktop.exe'), ('S', '*\Teams.exe'), ('S', '*\chrome.exe'), ('S', '*\discord.exe'), ('S', '*\keybase.exe'), ('S', '*\msedge.exe'), ('S', '*\msedgewebview2.exe'), ('S', '*\msteams.ex
SELECTION  - P:Image|IN|('L', (('S', '*\cmd.exe'), ('S', '*\cscript.exe'), ('S', '*\mshta.exe'), ('S', '*\powershell.exe'), ('S', '*\pwsh.exe'), ('S', '*\wscript.exe')))|CTX:POS
SELECTION  - P:ParentImage|IN|('L', (('S', '*\Teams.exe'), ('S', '*\discord.exe'), ('S', '*\slack.exe')))|CTX:POS
```


---

## V118

```
SELECTION  + P:ScriptBlockText|IN|('L', (('S', '*Add-Exfiltration*'), ('S', '*Add-Persistence*'), ('S', '*Add-RegBackdoor*'), ('S', '*Add-RemoteRegBackdoor*'), ('S', '*Add-ScrnSaveBackdoor*'), ('S', '*Check-VM*'), ('S', '*ConvertTo-R
SELECTION  - P:ScriptBlockText|IN|('L', (('S', '*Add-Exfiltration*'), ('S', '*Add-Persistence*'), ('S', '*Add-RegBackdoor*'), ('S', '*Add-RemoteRegBackdoor*'), ('S', '*Add-ScrnSaveBackdoor*'), ('S', '*Check-VM*'), ('S', '*ConvertTo-R
```


---

## V119

```
EXCLUSION  + P:TargetFilename|IN|('L', (('S', '*C:\$WINDOWS.~BT\*'), ('S', '*C:\$WinREAgent\*'), ('S', '*C:\Windows\SoftwareDistribution\*'), ('S', '*C:\Windows\SysWOW64\*'), ('S', '*C:\Windows\System32\*'), ('S', '*C:\Windows\WinSxS
EXCLUSION  - P:TargetFilename|IN|('L', (('S', '*C:\$WINDOWS.~BT\*'), ('S', '*C:\$WinREAgent\*'), ('S', '*C:\Windows\SoftwareDistribution\*'), ('S', '*C:\Windows\SysWOW64\*'), ('S', '*C:\Windows\System32\*'), ('S', '*C:\Windows\WinSxS
```


---

## V120

```
EXCLUSION  + P:RelativeTargetName|IN|('L', (('S', 'HydraLsPipe'), ('S', 'LSM_API_service'), ('S', 'MsFteWds'), ('S', 'TermSrv_API_service'), ('S', 'atsvc'), ('S', 'browser'), ('S', 'eventlog'), ('S', 'lsarpc'), ('S', 'lsass'), ('S', 
EXCLUSION  - P:RelativeTargetName|IN|('L', (('S', 'HydraLsPipe'), ('S', 'LSM_API_service'), ('S', 'MsFteWds'), ('S', 'TermSrv_API_service'), ('S', 'atsvc'), ('S', 'browser'), ('S', 'lsarpc'), ('S', 'lsass'), ('S', 'netdfs'), ('S', 'n
```
