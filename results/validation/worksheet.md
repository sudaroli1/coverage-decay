# Validation worksheet

Label each item **S** (a suppression: the exclusion set genuinely widened and coverage did not), **N** (not a suppression), or **U** (unclear).

Commit messages are withheld so the corroboration measure stays independent.


---

## V001

```
EXCLUSION  + P:Details|EQ|(\'S\', \'\"C:\ProgramData\Package Cache\{d21a4f20-968a-4b0c-bf04-a38da5f06e41}\windowsdesktop-runtime-*\')|CTX:NEG
```


---

## V002

```
EXCLUSION  + P:ParentImage|EQ|('S', 'C:\Windows\System32\Dism.exe')|CTX:NEG
EXCLUSION  + P:ParentImage|IN|('L', (('S', '*\Ninite.exe'), ('S', '*\target.bat'), ('S', '*\target.exe')))|CTX:NEG
SELECTION  + P:CommandLine|IN|('L', (('S', '*~1.*'), ('S', '*~1\*'), ('S', '*~2.*'), ('S', '*~2\*')))|CTX:POS
SELECTION  + P:Image|IN|('L', (('S', '*~1.*'), ('S', '*~1\*'), ('S', '*~2.*'), ('S', '*~2\*')))|CTX:POS
SELECTION  - P:CommandLine|IN|('L', (('S', '*~1.*'), ('S', '*~2.*')))|CTX:POS
```


---

## V003

```
EXCLUSION  + P:SourceImage|IN|('L', (('S', 'C:\WINDOWS\system32\wbem\wmiprvse.exe'), ('S', 'C:\Windows\System32\msiexec.exe'), ('S', 'C:\Windows\syswow64\MsiExec.exe')))|CTX:NEG
EXCLUSION  - P:SourceImage|EQ|('S', '*\Installer\setup.exe')|CTX:NEG
EXCLUSION  - P:SourceImage|EQ|('S', 'C:\Program Files (x86)\Microsoft\Edge\Application\*')|CTX:NEG
EXCLUSION  - P:SourceImage|EQ|('S', 'C:\WINDOWS\system32\wbem\wmiprvse.exe')|CTX:NEG
```


---

## V004

```
EXCLUSION  + P:CommandLine|IN|('L', (('S', '*https://10.*'), ('S', '*https://127.*'), ('S', '*https://169.254.*'), ('S', '*https://172.16.*'), ('S', '*https://172.17.*'), ('S', '*https://172.18.*'), ('S', '*https://172.19.*'), ('S', 
```


---

## V005

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

## V006

```
SELECTION  + P:TargetFilename|IN|('L', (('S', '*\SAM-2021-*'), ('S', '*\SAM-2022-*'), ('S', '*\SAM-haxx*'), ('S', '*\Sam.save*'), ('S', '*\hive_sam_*')))|CTX:POS
SELECTION  - P:TargetFilename|IN|('L', (('S', '*\SAM-2021-*'), ('S', '*\SAM-2022-*'), ('S', '*\Sam.save*'), ('S', '*\hive_sam_*')))|CTX:POS
```


---

## V007

```
EXCLUSION  + P:Image|IN|('L', (('S', '*\MsMpEng.exe'), ('S', '*\SearchApp.exe'), ('S', '*\autochk.exe'), ('S', '*\compattelrunner.exe'), ('S', '*\csrss.exe'), ('S', '*\defrag.exe'), ('S', '*\dfsrs.exe'), ('S', '*\lsass.exe'), ('S', '
EXCLUSION  + P:Image|IN|('L', (('S', 'C:\Program Files\Bitdefender Antivirus Free\downloader.exe'), ('S', 'C:\Program Files\Bitdefender Antivirus Free\updatesrv.exe'), ('S', 'C:\Program Files\Bitdefender Antivirus Free\vsserv.exe'), 
EXCLUSION  - P:Image|IN|('L', (('S', '*\MsMpEng.exe'), ('S', '*\SearchApp.exe'), ('S', '*\autochk.exe'), ('S', '*\compattelrunner.exe'), ('S', '*\csrss.exe'), ('S', '*\defrag.exe'), ('S', '*\dfsrs.exe'), ('S', '*\lsass.exe'), ('S', '
EXCLUSION  - P:Image|IN|('L', (('S', 'C:\Program Files\Bitdefender Antivirus Free\downloader.exe'), ('S', 'C:\Program Files\Bitdefender Antivirus Free\updatesrv.exe'), ('S', 'C:\Program Files\Bitdefender Antivirus Free\vsserv.exe'), 
```


---

## V008

```
EXCLUSION  + P:Image|IN|('L', (('S', 'C:\Program Files\Windows Defender\*'), ('S', 'C:\ProgramData\Microsoft\Windows Defender\Platform\*')))|CTX:NEG
EXCLUSION  - P:Image|IN|('L', (('S', '*C:\Program Files\Windows Defender\*'), ('S', '*C:\ProgramData\Microsoft\Windows Defender\Platform\*')))|CTX:NEG
```


---

## V009

```
EXCLUSION  + P:userIdentity.arn|EQ|('S', '*requestParameters.userName*')|CTX:NEG
EXCLUSION  - P:userIdentity.arn|EQ|('S', '*responseElements.accessKey.userName*')|CTX:NEG
```


---

## V010

```
EXCLUSION  + P:Details|EQ|('S', '*C:\Windows\System32\Autopilot.dll*')|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', 'C:\Windows\System32\poqexec.exe')|CTX:NEG
```


---

## V011

```
EXCLUSION  + P:Image|EQ|('S', '*\Common Files\Microsoft Shared\*')|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', '*\Google\Chrome\application\*')|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', '*\HTML Help Workshop\*')|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', '*\Lenovo\Communication Utility\*')|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', '*\Microsoft Device Emulator\*')|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', '*\Microsoft Security Center\*')|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', '*\Windows Media Player\*')|CTX:NEG
EXCLUSION  + P:Image|IN|('L', (('S', '*\AntiMalware\*'), ('S', '*\Microsoft Security Client\*'), ('S', '*\Windows Defender\*')))|CTX:NEG
EXCLUSION  - P:Image|EQ|('S', '*\Common Files\Microsoft Shared\*')|CTX:NEG
EXCLUSION  - P:Image|EQ|('S', '*\Google\Chrome\application\*')|CTX:NEG
EXCLUSION  - P:Image|EQ|('S', '*\HTML Help Workshop\*')|CTX:NEG
EXCLUSION  - P:Image|EQ|('S', '*\Lenovo\Communication Utility\*')|CTX:NEG
EXCLUSION  - P:Image|EQ|('S', '*\Microsoft Device Emulator\*')|CTX:NEG
EXCLUSION  - P:Image|EQ|('S', '*\Microsoft Security Center\*')|CTX:NEG
EXCLUSION  - P:Image|EQ|('S', '*\Windows Media Player\*')|CTX:NEG
EXCLUSION  - P:Image|IN|('L', (('S', '*\AntiMalware\*'), ('S', '*\Microsoft Security Client\*'), ('S', '*\Windows Defender\*')))|CTX:NEG
```


---

## V012

```
EXCLUSION  + P:UserAgent|EQ|('S', 'Mozilla/3.0 * Acrobat *')|CTX:NEG
```


---

## V013

```
EXCLUSION  + P:Image|IN|('L', (('S', 'C:\Windows\SysWOW64\*'), ('S', 'C:\Windows\SysWow64\*'), ('S', 'C:\Windows\System32\*'), ('S', 'C:\Windows\WinSxS\*'), ('S', 'C:\Windows\explorer.exe'), ('S', 'C:\Windows\winsxs\*')))|CTX:NEG
EXCLUSION  - P:Image|IN|('L', (('S', 'C:\Windows\SysWow64\*'), ('S', 'C:\Windows\System32\*'), ('S', 'C:\Windows\explorer.exe'), ('S', 'C:\Windows\winsxs\*'), ('S', '\SystemRoot\System32\*')))|CTX:NEG
```


---

## V014

```
EXCLUSION  + P:Image|EQ|('S', '')|CTX:NEG
SELECTION  + P:Image|EQ|('S', '*')|CTX:POS
```


---

## V015

```
EXCLUSION  + P:ServerAddress|EQ|('S', '10.0.0.0/8')|CTX:NEG
EXCLUSION  + P:ServerAddress|EQ|('S', '127.0.0.0/8')|CTX:NEG
EXCLUSION  + P:ServerAddress|EQ|('S', '169.254.0.0/16')|CTX:NEG
EXCLUSION  + P:ServerAddress|EQ|('S', '172.16.0.0/12')|CTX:NEG
EXCLUSION  + P:ServerAddress|EQ|('S', '192.168.0.0/16')|CTX:NEG
EXCLUSION  - P:ServerAddress|IN|('L', (('S', '10.*'), ('S', '127.*'), ('S', '169.254.*'), ('S', '172.16.*'), ('S', '172.17.*'), ('S', '172.18.*'), ('S', '172.19.*'), ('S', '172.20.*'), ('S', '172.21.*'), ('S', '172.22.*'), ('S', '172
```


---

## V016

```
EXCLUSION  + P:Image|IN|('L', (('S', 'C:\Program Files (x86)\*'), ('S', 'C:\Program Files\*'), ('S', 'C:\Windows\SysWOW64\*'), ('S', 'C:\Windows\system32\*')))|CTX:NEG
EXCLUSION  - P:Image|IN|('L', (('S', '*:\Program Files (x86)\*'), ('S', '*:\Program Files\*'), ('S', '*:\Windows\SysWOW64\*'), ('S', '*:\Windows\system32\*')))|CTX:NEG
```


---

## V017

```
EXCLUSION  + P:Image|IN|('L', (('S', '*\procdump.exe'), ('S', '*\procdump64.exe')))|CTX:NEG
EXCLUSION  - P:Image|IN|('L', (('S', '*\procdump64.exe'), ('S', '*\prodcump.exe')))|CTX:NEG
```


---

## V018

```
EXCLUSION  + P:CallTrace|EQ|('S', '*\System.ni.dll+*')|CTX:NEG
EXCLUSION  + P:CallTrace|EQ|('S', 'C:\Windows\SYSTEM32\ntdll.dll*')|CTX:NEG
EXCLUSION  + P:SourceImage|EQ|('S', 'C:\Windows\System32\Wbem\Wmiprvse.exe')|CTX:NEG
EXCLUSION  + P:TargetImage|EQ|('S', 'C:\Windows\system32\lsass.exe')|CTX:NEG
```


---

## V019

```
EXCLUSION  + P:Details|EQ|('S', '*\Microsoft\Teams\Update.exe --processStart *')|CTX:NEG
EXCLUSION  + P:Details|EQ|('S', 'ctfmon.exe /n')|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', '*\Microsoft\Teams\current\Teams.exe')|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', 'C:\Windows\system32\userinit.exe')|CTX:NEG
```


---

## V020

```
SELECTION  + P:SubStatus|IN|('L', (('S', '0xC000006F'), ('S', '0xC0000070'), ('S', '0xC0000072'), ('S', '0xC000015B'), ('S', '0xC000018C'), ('S', '0xC0000413')))|CTX:POS
```


---

## V021

```
EXCLUSION  + P:ModifyingApplication|EQ|('S', 'C:\Program Files\Windows Defender\MsMpEng.exe')|CTX:NEG
```


---

## V022

```
EXCLUSION  + P:CommandLine|EQ|('S', '*\netlogon.bat')|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', '*\explorer.exe')|CTX:NEG
EXCLUSION  - P:CommandLine|EQ|('S', 'netlogon.bat')|CTX:NEG
EXCLUSION  - P:Image|EQ|('S', 'explorer.exe')|CTX:NEG
SELECTION  + P:ParentImage|EQ|('S', '*\userinit.exe')|CTX:POS
SELECTION  - P:ParentImage|EQ|('S', 'userinit.exe')|CTX:POS
```


---

## V023

```
EXCLUSION  + P:ParentCommandLine|EQ|('S', '*.cpl*')|CTX:NEG
EXCLUSION  + P:ParentImage|EQ|('S', 'C:\Windows\System32\control.exe')|CTX:NEG
```


---

## V024

```
EXCLUSION  + P:CommandLine|EQ|('S', '*:\Windows\Installer\*')|CTX:NEG
EXCLUSION  + P:CommandLine|IN|('L', (('S', '*.cpl *'), ('S', '*.cpl,*'), ('S', '*.dll *'), ('S', '*.dll,*'), ('S', '*.inf *'), ('S', '*.inf,*')))|CTX:NEG
EXCLUSION  + P:CommandLine|IN|(\'L\', ((\'S\', "*.cpl\'"), (\'S\', "*.dll\'"), (\'S\', "*.inf\'"), (\'S\', \'*.cpl\'), (\'S\', \'*.cpl\"\'), (\'S\', \'*.dll\'), (\'S\', \'*.dll\"\'), (\'S\', \'*.inf\'), (\'S\', \'*.inf\"\')))|CTX:NEG
EXCLUSION  + P:ParentImage|EQ|('S', '*\msiexec.exe')|CTX:NEG
EXCLUSION  - P:CommandLine|EQ|('S', '*C:\Windows\Installer\MSI*')|CTX:NEG
EXCLUSION  - P:CommandLine|IN|('L', (('S', '*.cpl*'), ('S', '*.dll*'), ('S', '*.inf*')))|CTX:NEG
```


---

## V025

```
EXCLUSION  + P:ParentImage|EQ|('S', '*:\Program Files\Windows Defender Advanced Threat Protection\SenseIR.exe')|CTX:NEG
```


---

## V026

```
EXCLUSION  + P:CommandLine|EQ|('S', '*${env:path}*')|CTX:NEG
SELECTION  + P:CommandLineMatch3|MATCHES_REGEX|('S', '(?<CommandLineMatch3>(?i)\$\{`?e`?n`?v`?:`?p`?a`?t`?h`?\})')|CTX:POS
SELECTION  - P:CommandLineMatch3|MATCHES_REGEX|('S', '(?<CommandLineMatch3>(?i)\$\{(?=.*`)+?`?e`?n`?v`?:`?p`?a`?t`?h`?\})')|CTX:POS
```


---

## V027

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

## V028

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

## V029

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

## V030

```
EXCLUSION  + P:_raw|CONTAINS|('S', '/nessus}')|CTX:NEG
EXCLUSION  + P:_raw|CONTAINS|('S', 'w.nessus.org/nessus')|CTX:NEG
SELECTION  + P:_raw|CONTAINS|('S', '$%7Bjndi:')|CTX:POS
SELECTION  + P:_raw|CONTAINS|('S', '${${::-j}${::-n}${::-d}${::-i}:')|CTX:POS
SELECTION  + P:_raw|CONTAINS|('S', '${${env:BARFOO:-j}')|CTX:POS
SELECTION  + P:_raw|CONTAINS|('S', '${${env:ENV_NAME:-j}ndi${env:ENV_NAME:-:}$')|CTX:POS
SELECTION  + P:_raw|CONTAINS|('S', '${${lower:j}ndi:')|CTX:POS
SELECTION  + P:_raw|CONTAINS|('S', '${${upper:j}ndi:')|CTX:POS
SELECTION  + P:_raw|CONTAINS|('S', '${::-j}${')|CTX:POS
SELECTION  + P:_raw|CONTAINS|('S', '${::-l}${::-d}${::-a}${::-p}')|CTX:POS
SELECTION  - P:_raw|CONTAINS|('D', (('type', ('S', 'field')), ('value', ('S', '$%7Bjndi:'))))|CTX:POS
SELECTION  - P:_raw|CONTAINS|('D', (('type', ('S', 'field')), ('value', ('S', '${${::-j}${::-n}${::-d}${::-i}:'))))|CTX:POS
SELECTION  - P:_raw|CONTAINS|('D', (('type', ('S', 'field')), ('value', ('S', '${${env:BARFOO:-j}'))))|CTX:POS
SELECTION  - P:_raw|CONTAINS|('D', (('type', ('S', 'field')), ('value', ('S', '${${env:ENV_NAME:-j}ndi${env:ENV_NAME:-:}$'))))|CTX:POS
SELECTION  - P:_raw|CONTAINS|('D', (('type', ('S', 'field')), ('value', ('S', '${${lower:j}ndi:'))))|CTX:POS
SELECTION  - P:_raw|CONTAINS|('D', (('type', ('S', 'field')), ('value', ('S', '${${upper:j}ndi:'))))|CTX:POS
SELECTION  - P:_raw|CONTAINS|('D', (('type', ('S', 'field')), ('value', ('S', '${::-j}${'))))|CTX:POS
SELECTION  - P:_raw|CONTAINS|('D', (('type', ('S', 'field')), ('value', ('S', '${::-l}${::-d}${::-a}${::-p}'))))|CTX:POS
```


---

## V031

```
EXCLUSION  + P:Image|EQ|('S', 'C:\Windows\System32\poqexec.exe')|CTX:NEG
EXCLUSION  + P:Image|IN|('L', (('S', 'C:\Program Files (x86)\Microsoft Office\root\integration\integrator.exe'), ('S', 'C:\Program Files\Microsoft Office\root\integration\integrator.exe')))|CTX:NEG
EXCLUSION  - P:Image|IN|('L', (('S', 'C:\Program Files (x86)\Microsoft Office\root\integration\integrator.exe'), ('S', 'C:\Program Files\Microsoft Office\root\integration\integrator.exe'), ('S', 'C:\Windows\System32\poqexec.exe')))|C
SELECTION  + P:Details|EQ|('S', '*')|CTX:POS
```


---

## V032

```
SELECTION  + P:Hash|IN|('L', (('S', '*IMPHASH=021BCCA20BA3381B11BDDE26B4E62F20*'), ('S', '*IMPHASH=03866661686829d806989e2fc5a72606*'), ('S', '*IMPHASH=0588081AB0E63BA785938467E1B10CCA*'), ('S', '*IMPHASH=07A2D4DCBD6CB2C6A45E6B101F0B
SELECTION  + P:Imphash|IN|('L', (('S', '021bcca20ba3381b11bdde26b4e62f20'), ('S', '03866661686829d806989e2fc5a72606'), ('S', '0588081ab0e63ba785938467e1b10cca'), ('S', '07a2d4dcbd6cb2c6a45e6b101f0b6d51'), ('S', '09D278F9DE118EF09163C
SELECTION  - P:Hash|IN|('L', (('S', '*IMPHASH=03866661686829d806989e2fc5a72606*'), ('S', '*IMPHASH=0588081AB0E63BA785938467E1B10CCA*'), ('S', '*IMPHASH=07A2D4DCBD6CB2C6A45E6B101F0B6D51*'), ('S', '*IMPHASH=09D278F9DE118EF09163C6140255
SELECTION  - P:Imphash|IN|('L', (('S', '03866661686829d806989e2fc5a72606'), ('S', '0588081ab0e63ba785938467e1b10cca'), ('S', '07a2d4dcbd6cb2c6a45e6b101f0b6d51'), ('S', '09D278F9DE118EF09163C6140255C690'), ('S', '0c106686a31bfe2ba931a
```


---

## V033

```
EXCLUSION  + P:CommandLine|EQ|('S', '*.cpl*')|CTX:NEG
EXCLUSION  + P:CommandLine|EQ|('S', '*Control_RunDLL*')|CTX:NEG
EXCLUSION  + P:CommandLine|EQ|('S', '*Shell32.dll*')|CTX:NEG
SELECTION  + P:CommandLine|EQ|('S', '*MiniDump*')|CTX:POS
SELECTION  + P:CommandLine|EQ|('S', '*comsvcs.dll*')|CTX:POS
```


---

## V034

```
EXCLUSION  + P:Image|IN|('L', (('S', '*\SMSComponent\*'), ('S', '*\Tools\*'), ('S', '*bin\*')))|CTX:NEG
EXCLUSION  - P:Image|IN|('L', (('S', '*\SMSComponent\*'), ('S', '*\Tools\*'), ('S', '*bin\*')))|CTX:NEG
SELECTION  + P:Image|IN|('L', (('S', '*\htdocs\*'), ('S', '*\wmpub\*'), ('S', '*\wwwroot\*')))|CTX:POS
SELECTION  - P:Image|IN|('L', (('S', '*\htdocs\*'), ('S', '*\wmpub\*'), ('S', '*\wwwroot\*')))|CTX:POS
```


---

## V035

```
EXCLUSION  + P:ParentCommandLine|IN|('L', (('S', '*-k LocalSystemNetworkRestricted -p -s NgcSvc*'), ('S', '*-k apphost -s AppHostSvc*'), ('S', '*-k imgsvc*'), ('S', '*-k netsvcs -p -s NetSetupSvc*'), ('S', '*-k wsappx -p -s ClipSVC*'
EXCLUSION  - P:ParentCommandLine|IN|('L', (('S', '*-k apphost -s AppHostSvc*'), ('S', '*-k imgsvc*'), ('S', '*-k netsvcs -p -s NetSetupSvc*')))|CTX:NEG
```


---

## V036

```
EXCLUSION  + P:Image|IN|('L', (('S', 'C:\Program Files (x86)\Microsoft Office\root\integration\integrator.exe'), ('S', 'C:\Program Files\Common Files\Microsoft Shared\ClickToRun\OfficeClickToRun.exe'), ('S', 'C:\Windows\System32\poqe
```


---

## V037

```
EXCLUSION  + P:Image|EQ|('S', '*\SecurityHealthSetup.exe')|CTX:NEG
EXCLUSION  + P:TargetFilename|EQ|('S', '*\SecurityHealthSystray.exe')|CTX:NEG
EXCLUSION  + P:TargetFilename|EQ|('S', 'C:\Windows\System32\SecurityHealth\*')|CTX:NEG
```


---

## V038

```
SELECTION  + P:_raw|CONTAINS|('S', '\perfc.dat')|CTX:POS
SELECTION  - P:_raw|CONTAINS|('S', '*\perfc.dat*')|CTX:POS
```


---

## V039

```
SELECTION  + P:Image|EQ|('S', '*\AnyDesk.exe')|CTX:POS
```


---

## V040

```
SELECTION  + P:EventType|EQ|('S', 'SetValue')|CTX:POS
```


---

## V041

```
EXCLUSION  + P:Details|EQ|(\'S\', \'*\Installer\chrmstp.exe\" --configure-user-settings --verbose-logging --system-level\')|CTX:NEG
EXCLUSION  + P:Details|EQ|(\'S\', \'\"C:\Program Files\Google\Chrome\Application\*\')|CTX:NEG
```


---

## V042

```
EXCLUSION  + P:qtype_name|IN|('L', (('S', 'MX'), ('S', 'MX'), ('S', 'NS'), ('S', 'ns')))|CTX:NEG
EXCLUSION  - P:qtype_name|IN|('L', (('S', 'NS'), ('S', 'ns')))|CTX:NEG
```


---

## V043

```
SELECTION  + P:CommandLine|EQ|('S', '*WebPages\Errors\webErrorLog.txt*')|CTX:POS
SELECTION  + P:CommandLine|EQ|('S', '*del /s /q /f*')|CTX:POS
```


---

## V044

```
EXCLUSION  + P:Image|IN|('L', (('S', '*Installer.x64.exe'), ('S', '*\target.exe')))|CTX:NEG
EXCLUSION  - P:Image|EQ|('S', '*\target.exe')|CTX:NEG
```


---

## V045

```
SELECTION  + P:eventName|EQ|('S', 'AssumeRole')|CTX:POS
SELECTION  + P:userIdentity.sessionContext.sessionIssuer.type|EQ|('S', 'Role')|CTX:POS
SELECTION  - P:eventName|EQ|('S', 'AssumedRole')|CTX:POS
SELECTION  - P:userIdentity.sessionContext|EQ|('S', 'Role')|CTX:POS
```


---

## V046

```
SELECTION  + P:CommandLine|EQ|('S', '*\CurrentVersion\Image File Execution Options\*')|CTX:POS
SELECTION  + P:CommandLine|IN|('L', (('S', '*atbroker.exe*'), ('S', '*displayswitch.exe*'), ('S', '*magnify.exe*'), ('S', '*narrator.exe*'), ('S', '*osk.exe*'), ('S', '*sethc.exe*'), ('S', '*utilman.exe*')))|CTX:POS
SELECTION  - P:CommandLine|IN|('L', (('S', '*\CurrentVersion\Image File Execution Options\atbroker.exe*'), ('S', '*\CurrentVersion\Image File Execution Options\displayswitch.exe*'), ('S', '*\CurrentVersion\Image File Execution Option
```


---

## V047

```
EXCLUSION  + P:IpAddress|EQ|('S', '10.0.0.0/8')|CTX:NEG
EXCLUSION  + P:IpAddress|EQ|('S', '127.0.0.0/8')|CTX:NEG
EXCLUSION  + P:IpAddress|EQ|('S', '169.254.0.0/16')|CTX:NEG
EXCLUSION  + P:IpAddress|EQ|('S', '172.16.0.0/12')|CTX:NEG
EXCLUSION  + P:IpAddress|EQ|('S', '192.168.0.0/16')|CTX:NEG
EXCLUSION  + P:IpAddress|EQ|('S', '::1/128')|CTX:NEG
EXCLUSION  + P:IpAddress|EQ|('S', 'fc00::/7')|CTX:NEG
EXCLUSION  + P:IpAddress|EQ|('S', 'fe80::/10')|CTX:NEG
EXCLUSION  - P:IpAddress|EQ|('S', '::1')|CTX:NEG
EXCLUSION  - P:IpAddress|IN|('L', (('S', '10.*'), ('S', '127.*'), ('S', '169.254.*'), ('S', '172.16.*'), ('S', '172.17.*'), ('S', '172.18.*'), ('S', '172.19.*'), ('S', '172.20.*'), ('S', '172.21.*'), ('S', '172.22.*'), ('S', '172.23.
EXCLUSION  - P:IpAddress|IN|('L', (('S', 'fc00::*'), ('S', 'fe80::*')))|CTX:NEG
```


---

## V048

```
EXCLUSION  + P:CommandLine|EQ|('S', '*} /I {*')|CTX:NEG
EXCLUSION  + P:CommandLine|EQ|(\'S\', \'*verclsid.exe\" /S /C {*\')|CTX:NEG
EXCLUSION  + P:ParentImage|EQ|('S', '*C:\Windows\System32\RuntimeBroker.exe')|CTX:NEG
```


---

## V049

```
EXCLUSION  + P:Image|IN|('L', (('S', '*\WINDOWS\System32\sdiagnhost.exe'), ('S', '*\powershell.exe'), ('S', '*\powershell_ise.exe')))|CTX:NEG
EXCLUSION  - P:Image|IN|('L', (('S', '*\powershell.exe'), ('S', '*\powershell_ise.exe')))|CTX:NEG
```


---

## V050

```
EXCLUSION  + P:TargetObject|EQ|('S', '*Print\Monitors\Appmon\Ports\Microsoft.Office.OneNote_*')|CTX:NEG
EXCLUSION  + P:User|IN|('L', (('S', '*AUTHORI*'), ('S', '*AUTORI*')))|CTX:NEG
```


---

## V051

```
EXCLUSION  + P:TargetFilename|IN|('L', (('S', '*C:\$WINDOWS.~BT\*'), ('S', '*C:\$WinREAgent\*'), ('S', '*C:\Windows\SoftwareDistribution\*'), ('S', '*C:\Windows\SysWOW64\*'), ('S', '*C:\Windows\System32\*'), ('S', '*C:\Windows\WinSxS
EXCLUSION  - P:TargetFilename|IN|('L', (('S', '*C:\$WINDOWS.~BT\*'), ('S', '*C:\$WinREAgent\*'), ('S', '*C:\Windows\SoftwareDistribution\*'), ('S', '*C:\Windows\SysWOW64\*'), ('S', '*C:\Windows\System32\*'), ('S', '*C:\Windows\WinSxS
```


---

## V052

```
EXCLUSION  + P:cs-referer|EQ|('S', '*/root/user/remote-user/saml-user/*')|CTX:NEG
SELECTION  + P:cs-referer|EQ|('S', '*')|CTX:POS
SELECTION  - P:content-disposition|EQ|('S', '*`*')|CTX:POS
SELECTION  - P:content-type|EQ|('S', 'multipart/form-data;*')|CTX:POS
```


---

## V053

```
EXCLUSION  + P:CommandLine|EQ|('S', '*02*')|CTX:NEG
EXCLUSION  + P:CommandLine|EQ|('S', '*SecurityLayer*')|CTX:NEG
SELECTION  + P:CommandLine|IN|('L', (('S', '*AllowTSConnections*'), ('S', '*IdleWinStationPoolCount*'), ('S', '*MaxInstanceCount*'), ('S', '*SecurityLayer*'), ('S', '*TSAdvertise*'), ('S', '*TSAppCompat*'), ('S', '*TSEnabled*'), ('S'
SELECTION  - P:CommandLine|IN|('L', (('S', '*AllowTSConnections*'), ('S', '*IdleWinStationPoolCount*'), ('S', '*MaxInstanceCount*'), ('S', '*TSAdvertise*'), ('S', '*TSAppCompat*'), ('S', '*TSEnabled*'), ('S', '*TSUserEnabled*'), ('S'
```


---

## V054

```
SELECTION  + P:dst_port|IN|('L', (('X', 11211), ('X', 1433), ('X', 1521), ('X', 15672), ('X', 21), ('X', 23), ('X', 27017), ('X', 3306), ('X', 50000), ('X', 5900), ('X', 5901), ('X', 5902), ('X', 5903), ('X', 5904), ('X', 80), ('X', 
SELECTION  - P:destination.port|IN|('L', (('X', 11211), ('X', 1433), ('X', 1521), ('X', 15672), ('X', 21), ('X', 23), ('X', 27017), ('X', 3306), ('X', 50000), ('X', 5900), ('X', 5901), ('X', 5902), ('X', 5903), ('X', 5904), ('X', 80)
```


---

## V055

```
EXCLUSION  + P:ParentImage|EQ|('S', '*\Microsoft.Management.Services.IntuneWindowsAgent.exe')|CTX:NEG
```


---

## V056

```
EXCLUSION  + P:ParentImage|EQ|('S', '')|CTX:NEG
EXCLUSION  + P:ParentImage|EQ|('S', 'C:\Program Files\Microsoft Monitoring Agent\Agent\MonitoringHost.exe')|CTX:NEG
EXCLUSION  - P:ParentImage|IN|('L', (('S', ''), ('S', 'C:\Program Files\Microsoft Monitoring Agent\Agent\MonitoringHost.exe')))|CTX:NEG
SELECTION  - P:CommandLine|IN|('L', (('S', '*whoami -all*'), ('S', '*whoami /all*'), ('S', '*whoami >*'), ('S', '*whoami.exe -all*'), ('S', '*whoami.exe /all*'), ('S', '*whoami.exe >*')))|CTX:POS
```


---

## V057

```
EXCLUSION  + P:ApplicationPath|IN|('L', (('S', 'C:\Program Files (x86)\*'), ('S', 'C:\Program Files\*')))|CTX:NEG
EXCLUSION  + P:ModifyingApplication|EQ|('S', 'C:\Windows\SysWOW64\msiexec.exe')|CTX:NEG
EXCLUSION  - P:ModifyingApplication|EQ|('S', 'C:\Program Files\Windows Defender\MsMpEng.exe')|CTX:NEG
```


---

## V058

```
EXCLUSION  + P:Image|IN|('L', (('S', '*:\Windows\System32\Taskmgr.exe'), ('S', '*:\Windows\System32\mmc.exe'), ('S', '*:\Windows\System32\resmon.exe')))|CTX:NEG
EXCLUSION  - P:Image|IN|('L', (('S', '*\mmc.exe'), ('S', '*\resmon.exe'), ('S', '*\taskmgr.exe')))|CTX:NEG
```


---

## V059

```
(no predicate-level change)
```


---

## V060

```
EXCLUSION  - P:CommandLine|EQ|('S', '*\Google\Drive\googledrivesync.exe\..\*')|CTX:NEG
```


---

## V061

```
EXCLUSION  + P:ApplicationPath|IN|('L', (('S', '*:\PerfLogs\*'), ('S', '*:\Temp\*'), ('S', '*:\Tmp\*'), ('S', '*:\Users\Public\*'), ('S', '*:\Windows\Tasks\*'), ('S', '*:\Windows\Temp\*'), ('S', '*\AppData\Local\Temp\*')))|CTX:NEG
EXCLUSION  - P:ApplicationPath|IN|('L', (('S', '*:\PerfLogs\*'), ('S', '*:\Temp\*'), ('S', '*:\Users\Public\*'), ('S', '*:\Windows\Tasks\*'), ('S', '*:\Windows\Temp\*'), ('S', '*\AppData\Local\Temp\*')))|CTX:NEG
SELECTION  + P:EventID|IN|('L', (('X', 2004), ('X', 2071), ('X', 2097)))|CTX:POS
SELECTION  - P:EventID|IN|('L', (('X', 2004), ('X', 2071)))|CTX:POS
```


---

## V062

```
EXCLUSION  + P:Image|IN|('L', (('S', '*\WmiAPsrv.exe'), ('S', '*\WmiPrvSE.exe'), ('S', '*\WmiPrvSe.exe'), ('S', '*\svchost.exe')))|CTX:NEG
EXCLUSION  - P:Image|IN|('L', (('S', '*\WmiAPsrv.exe'), ('S', '*\WmiPrvSe.exe'), ('S', '*\svchost.exe')))|CTX:NEG
```


---

## V063

```
EXCLUSION  + P:TargetFilename|IN|('L', (('S', '*\AppData\Local\Microsoft\SquirrelTemp\tempb\'), ('S', '*\AppData\Local\Microsoft\Teams\stage\Squirrel.exe'), ('S', '*\AppData\Local\Microsoft\Teams\stage\Teams.exe')))|CTX:NEG
EXCLUSION  - P:TargetFilename|IN|('L', (('S', '*\AppData\Local\Microsoft\Teams\stage\Squirrel.exe'), ('S', '*\AppData\Local\Microsoft\Teams\stage\Teams.exe')))|CTX:NEG
```


---

## V064

```
EXCLUSION  + P:Image|EQ|('S', '*\AppData\Local\GitHubDesktop\Update.exe')|CTX:NEG
EXCLUSION  + P:TargetFilename|EQ|('S', '*\AppData\Local\SquirrelTemp\*')|CTX:NEG
```


---

## V065

```
(no predicate-level change)
```


---

## V066

```
EXCLUSION  + P:TargetObject|IN|('L', (('S', '*Microsoft\Windows\GroupPolicy\{*}\Index*'), ('S', '*Microsoft\Windows\PushToInstall\Registration\Index*'), ('S', '*Microsoft\Windows\WindowsUpdate\Scheduled Start\Index*')))|CTX:NEG
EXCLUSION  - P:TargetObject|EQ|('S', '*Microsoft\Windows\WindowsUpdate\Scheduled Start\Index*')|CTX:NEG
```


---

## V067

```
EXCLUSION  + P:ParentImage|EQ|('S', '*\Notepad++\updater\*')|CTX:NEG
SELECTION  + P:CommandLine|EQ|('S', '*')|CTX:POS
```


---

## V068

```
EXCLUSION  + P:Image|EQ|('S', 'C:\Program Files\Windows Defender\MsMpEng.exe')|CTX:NEG
```


---

## V069

```
SELECTION  + P:CommandLine|IN|('L', (('S', '*%COMSPEC%*'), ('S', '*cmd*')))|CTX:POS
SELECTION  - P:CommandLine|EQ|('S', '*%COMSPEC%*')|CTX:POS
SELECTION  - P:CommandLine|EQ|('S', '*cmd.exe*')|CTX:POS
```


---

## V070

```
EXCLUSION  - P:CommandLine|EQ|('S', '*\PhotoViewer.dll*')|CTX:NEG
EXCLUSION  - P:CommandLine|EQ|('S', '*\SYSTEM32\SPOOL\DRIVERS\*')|CTX:NEG
EXCLUSION  - P:CommandLine|EQ|('S', '*shell32.dll,Control_RunDLL*')|CTX:NEG
EXCLUSION  - P:Image|EQ|('S', '*\rundll32.exe')|CTX:NEG
EXCLUSION  - P:ParentImage|EQ|('S', '*\OUTLOOK.EXE')|CTX:NEG
SELECTION  + P:ParentImage|IN|('L', (('S', '*\EQNEDT32.EXE'), ('S', '*\EXCEL.EXE'), ('S', '*\MSACCESS.EXE'), ('S', '*\MSPUB.exe'), ('S', '*\POWERPNT.exe'), ('S', '*\VISIO.exe'), ('S', '*\WINWORD.EXE')))|CTX:POS
SELECTION  - P:ParentImage|IN|('L', (('S', '*\EQNEDT32.EXE'), ('S', '*\EXCEL.EXE'), ('S', '*\MSACCESS.EXE'), ('S', '*\MSPUB.exe'), ('S', '*\OUTLOOK.EXE'), ('S', '*\POWERPNT.exe'), ('S', '*\VISIO.exe'), ('S', '*\WINWORD.EXE')))|CTX:PO
```


---

## V071

```
EXCLUSION  + P:EventID|EQ|('X', 4699)|CTX:NEG
EXCLUSION  + P:Task|EQ|('S', '*\Windows\Windows Defender\*')|CTX:NEG
```


---

## V072

```
SELECTION  + P:Description|EQ|('S', 'Process Hacker')|CTX:POS
SELECTION  + P:Image|EQ|('S', '*\ProcessHacker.exe')|CTX:POS
SELECTION  + P:OriginalFileName|IN|('L', (('S', 'Process Hacker'), ('S', 'ProcessHacker.exe')))|CTX:POS
SELECTION  - P:Description|IN|('L', (('S', 'Process Hacker'), ('S', 'System Informer')))|CTX:POS
SELECTION  - P:Image|IN|('L', (('S', '*\ProcessHacker.exe'), ('S', '*\SystemInformer.exe')))|CTX:POS
SELECTION  - P:OriginalFileName|IN|('L', (('S', 'Process Hacker'), ('S', 'ProcessHacker.exe'), ('S', 'SystemInformer.exe')))|CTX:POS
```


---

## V073

```
SELECTION  + P:ImageLoaded|IN|('L', (('S', '*\VBE7.DLL*'), ('S', '*\VBE7INTL.DLL*'), ('S', '*\VBEUI.DLL*')))|CTX:POS
SELECTION  + P:Image|IN|('L', (('S', '*\excel.exe*'), ('S', '*\outlook.exe*'), ('S', '*\powerpnt.exe*'), ('S', '*\winword.exe*')))|CTX:POS
SELECTION  - P:ImageLoaded|IN|('L', (('S', '*\VBE7.DLL'), ('S', '*\VBE7INTL.DLL'), ('S', '*\VBEUI.DLL')))|CTX:POS
SELECTION  - P:Image|IN|('L', (('S', '*\excel.exe'), ('S', '*\outlook.exe'), ('S', '*\powerpnt.exe'), ('S', '*\winword.exe')))|CTX:POS
```


---

## V074

```
EXCLUSION  + P:SourceImage|EQ|('S', 'C:\WINDOWS\Explorer.EXE')|CTX:NEG
EXCLUSION  + P:TargetImage|EQ|('S', 'C:\WINDOWS\system32\backgroundTaskHost.exe')|CTX:NEG
```


---

## V075

```
EXCLUSION  + P:ParentImage|EQ|('S', '*.tmp')|CTX:NEG
EXCLUSION  + P:ParentImage|IN|('L', (('S', '*:\Windows\Temp*'), ('S', '*\AppData\Local\Temp\*')))|CTX:NEG
```


---

## V076

```
EXCLUSION  + P:GrantedAccess|EQ|('S', '0x1410')|CTX:NEG
EXCLUSION  + P:SourceImage|EQ|('S', '*\AppData\Local\Temp\*')|CTX:NEG
EXCLUSION  + P:SourceImage|EQ|('S', '*\vs_bootstrapper_*')|CTX:NEG
EXCLUSION  + P:SourceImage|IN|('L', (('S', '*\DropboxUpdate.exe'), ('S', '*\MBAMInstallerService.exe'), ('S', '*\Microsoft VS Code\Code.exe'), ('S', '*\WebexMTA.exe'), ('S', '*\software_reporter_tool.exe')))|CTX:NEG
EXCLUSION  - P:SourceImage|IN|('L', (('S', '*\DropboxUpdate.exe'), ('S', '*\MBAMInstallerService.exe'), ('S', '*\Microsoft VS Code\Code.exe'), ('S', '*\WebEx\WebexHost.exe'), ('S', '*\WebexMTA.exe'), ('S', '*\software_reporter_tool.e
```


---

## V077

```
EXCLUSION  + P:Image|IN|('L', (('S', 'C:\Program Files\Google\Chrome\Application\chrome.exe'), ('S', 'C:\Program Files\Mozilla Firefox\firefox.exe'), ('S', 'C:\Windows\System32\lsass.exe')))|CTX:NEG
EXCLUSION  - P:Image|IN|('L', (('S', '*\chrome.exe'), ('S', '*\firefox.exe'), ('S', '*\lsass.exe'), ('S', '*\opera.exe'), ('S', '*\tomcat\bin\tomcat8.exe')))|CTX:NEG
```


---

## V078

```
EXCLUSION  + P:SourceImage|EQ|('S', '*\DropboxUpdate.exe')|CTX:NEG
EXCLUSION  + P:SourceImage|IN|('L', (('S', 'C:\Program Files (x86)\Dropbox\*'), ('S', 'C:\Program Files\Dropbox\*')))|CTX:NEG
```


---

## V079

```
EXCLUSION  + P:Company|EQ|('S', 'InstallShield Software Corporation')|CTX:NEG
EXCLUSION  + P:Description|EQ|('S', 'InstallShield (R) Setup Engine')|CTX:NEG
EXCLUSION  + P:Product|EQ|('S', 'InstallShield (R)')|CTX:NEG
```


---

## V080

```
EXCLUSION  + P:CommandLine|EQ|('S', '*rundll32.exe')|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', '*\rundll32.exe')|CTX:NEG
EXCLUSION  + P:ParentCommandLine|EQ|('S', '*--uninstall --channel=stable*')|CTX:NEG
EXCLUSION  + P:ParentImage|EQ|('S', '*\AppData\Local\Google\Chrome\Application\*')|CTX:NEG
EXCLUSION  + P:ParentImage|EQ|('S', '*\Installer\setup.exe')|CTX:NEG
SELECTION  - P:ParentCommandLine|EQ|('S', '*--uninstall --channel=stable*')|CTX:POS
SELECTION  - P:ParentImage|EQ|('S', '*:\Users\*')|CTX:POS
SELECTION  - P:ParentImage|EQ|('S', '*\AppData\Local\Google\Chrome\Application\*')|CTX:POS
SELECTION  - P:ParentImage|EQ|('S', '*\Installer\setup.exe')|CTX:POS
```


---

## V081

```
EXCLUSION  + P:RelativeTargetName|IN|('L', (('S', 'atsvc'), ('S', 'browser'), ('S', 'lsarpc'), ('S', 'netdfs'), ('S', 'netlogon'), ('S', 'protected_storage'), ('S', 'samr'), ('S', 'srvsvc'), ('S', 'winreg'), ('S', 'wkssvc')))|CTX:NEG
EXCLUSION  - P:RelativeTargetName|IN|('L', (('S', 'atsvc'), ('S', 'lsarpc'), ('S', 'netlogon'), ('S', 'protected_storage'), ('S', 'samr'), ('S', 'srvsvc'), ('S', 'winreg'), ('S', 'wkssvc')))|CTX:NEG
```


---

## V082

```
EXCLUSION  + P:Image|IN|('L', (('S', 'C:\Windows\SysWOW64\*'), ('S', 'C:\Windows\System32\*'), ('S', 'C:\Windows\WinSxS\*'), ('S', 'C:\avast! sandbox*')))|CTX:NEG
EXCLUSION  - P:Image|IN|('L', (('S', 'C:\Windows\SysWOW64\*'), ('S', 'C:\Windows\SysWow64\*'), ('S', 'C:\Windows\System32\*'), ('S', 'C:\Windows\WinSxS\*'), ('S', 'C:\Windows\system32\*'), ('S', 'C:\Windows\winsxs\*'), ('S', 'C:\avas
```


---

## V083

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

## V084

```
EXCLUSION  + P:FileNameBuffer|EQ|('S', '*\Program Files\ESET\ESET Security\eamsi.dll')|CTX:NEG
EXCLUSION  + P:FileNameBuffer|EQ|('S', '*\Program Files\National Instruments\Shared\mDNS Responder\nimdnsNSP.dll ')|CTX:NEG
EXCLUSION  + P:FileNameBuffer|IN|('L', (('S', '*\Program Files\McAfee\Endpoint Security\Threat Prevention\MfeAmsiProvider.dll'), ('S', '*\Program Files\McAfee\MfeAV\AMSIExt.dll')))|CTX:NEG
EXCLUSION  - P:ValidatedPolicy|EQ|('X', 1)|CTX:NEG
EXCLUSION  - P:ValidatedPolicy|IN|('L', (('X', 1), ('X', 2)))|CTX:NEG
```


---

## V085

```
EXCLUSION  + P:Details|EQ|('S', '*C:\Windows\System32\SecurityHealth*')|CTX:NEG
EXCLUSION  - P:Details|EQ|('S', '*\C:\Windows\System32\SecurityHealth*')|CTX:NEG
```


---

## V086

```
EXCLUSION  + P:Image|EQ|('S', '*\MsMpEng.exe')|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', 'C:\ProgramData\Microsoft\Windows Defender\Platform\*')|CTX:NEG
SELECTION  + P:TargetObject|EQ|('S', '*\Microsoft\Windows Defender\Features\TamperProtection*')|CTX:POS
SELECTION  - P:TargetObject|EQ|('S', '*HKLM\SOFTWARE\Microsoft\Windows Defender\Features\TamperProtection*')|CTX:POS
```


---

## V087

```
EXCLUSION  + P:Image|EQ|('S', 'C:\Program Files\Windows Defender\MsMpEng.exe')|CTX:NEG
```


---

## V088

```
EXCLUSION  + P:ParentCommandLine|EQ|('S', '* --ms-enable-electron-run-as-node *')|CTX:NEG
EXCLUSION  + P:ParentImage|EQ|('S', '*\AppData\Local\Programs\Microsoft VS Code\Code.exe')|CTX:NEG
EXCLUSION  + P:ParentImage|EQ|('S', 'C:\Users\*')|CTX:NEG
SELECTION  + P:Image|IN|('L', (('S', '*\powershell.exe'), ('S', '*\pwsh.exe')))|CTX:POS
SELECTION  + P:OriginalFileName|IN|('L', (('S', 'PowerShell.EXE'), ('S', 'pwsh.dll')))|CTX:POS
SELECTION  - P:Image|EQ|('S', '*\powershell.exe')|CTX:POS
```


---

## V089

```
EXCLUSION  + P:Details|EQ|('S', 'DWORD (0x00000002)')|CTX:NEG
EXCLUSION  + P:TargetObject|EQ|('S', '*\SecurityLayer')|CTX:NEG
SELECTION  + P:TargetObject|IN|('L', (('S', '*\Control\Terminal Server\InitialProgram*'), ('S', '*\Control\Terminal Server\WinStations\RDP-Tcp\InitialProgram*'), ('S', '*\Terminal Server\WinStations\RDP-Tcp\SecurityLayer*'), ('S', '*
SELECTION  - P:TargetObject|IN|('L', (('S', '*\Control\Terminal Server\InitialProgram*'), ('S', '*\Control\Terminal Server\WinStations\RDP-Tcp\InitialProgram*'), ('S', '*\Windows NT\Terminal Services\InitialProgram*'), ('S', '*\servi
```


---

## V090

```
EXCLUSION  + P:CommandLine|EQ|('S', '*Yammer.exe*')|CTX:NEG
EXCLUSION  + P:CommandLine|EQ|('S', '*\AppData\Local\yammerdesktop\Update.exe*')|CTX:NEG
```


---

## V091

```
EXCLUSION  + P:CommandLine|IN|('L', (('S', 'sc stop KSCWebConsoleMessageQueue'), ('S', 'sc stop LGHUBUpdaterService')))|CTX:NEG
EXCLUSION  - P:CommandLine|EQ|('S', 'sc stop KSCWebConsoleMessageQueue')|CTX:NEG
```


---

## V092

```
EXCLUSION  + P:CommandLine|EQ|('S', '*,#1*')|CTX:NEG
EXCLUSION  + P:CommandLine|EQ|('S', '*\FileTracker32.dll*')|CTX:NEG
```


---

## V093

```
EXCLUSION  + P:Image|EQ|('S', '*\Citrix\System32\icast.exe')|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', 'C:\WINDOWS\explorer.exe')|CTX:NEG
EXCLUSION  + P:Image|IN|('L', (('S', 'C:\Windows\SysWOW64\proquota.exe'), ('S', 'C:\Windows\System32\proquota.exe')))|CTX:NEG
EXCLUSION  - P:Image|EQ|('S', '*:\WINDOWS\explorer.exe')|CTX:NEG
EXCLUSION  - P:Image|IN|('L', (('S', '*:\Program Files (x86)\Citrix\HDX\bin\cmstart.exe'), ('S', '*:\Program Files (x86)\Citrix\HDX\bin\icast.exe'), ('S', '*:\Program Files (x86)\Citrix\System32\icast.exe'), ('S', '*:\Program Files\C
EXCLUSION  - P:Image|IN|('L', (('S', '*:\Windows\SysWOW64\proquota.exe'), ('S', '*:\Windows\System32\proquota.exe')))|CTX:NEG
```


---

## V094

```
EXCLUSION  + P:ParentImage|IN|('L', (('S', 'c:\windows\system32\*'), ('S', 'c:\windows\syswow64\*')))|CTX:NEG
SELECTION  + P:Image|IN|('L', (('S', '*\fltmc.exe'), ('S', '*\schtasks.exe'), ('S', '*\systeminfo.exe')))|CTX:POS
SELECTION  - P:Image|EQ|('S', '*\fltmc.exe')|CTX:POS
SELECTION  - P:Image|EQ|('S', '*\schtasks.exe')|CTX:POS
SELECTION  - P:Image|EQ|('S', '*\systeminfo.exe')|CTX:POS
```


---

## V095

```
EXCLUSION  - P:Description|EQ|('S', 'Failed to open service configuration with error 19 - Last error: The media is write protected.')|CTX:NEG
SELECTION  + P:EventID|EQ|('X', 16)|CTX:POS
SELECTION  - P:Description|IN|('L', (('S', '*Failed to connect to the driver to update configuration*'), ('S', '*Failed to open service configuration with error*')))|CTX:POS
```


---

## V096

```
EXCLUSION  + P:Image|EQ|('S', '*C:\ProgramData\Microsoft\Windows Defender\platform\*')|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', '*\MsMpEng.exe*')|CTX:NEG
```


---

## V097

```
EXCLUSION  + P:CommandLine|EQ|('S', '* shell32.dll,Control_RunDLL *')|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', '*\rundll32.exe')|CTX:NEG
```


---

## V098

```
EXCLUSION  + P:ImageLoaded|IN|('L', (('S', 'C:\Program Files (x86)\*'), ('S', 'C:\Program Files\*')))|CTX:NEG
EXCLUSION  - P:ImageLoaded|IN|('L', (('S', 'C:\Program Files (x86)\Pidgin\*'), ('S', 'C:\Program Files (x86)\ossec-agent\*'), ('S', 'C:\Program Files\Inkscape\bin\*')))|CTX:NEG
```


---

## V099

```
EXCLUSION  + P:SourceImage|EQ|('S', '*Antivirus*')|CTX:NEG
EXCLUSION  + P:SourceImage|IN|('L', (('S', 'C:\PROGRAMDATA\MALWAREBYTES\MBAMSERVICE\ctlrupdate\mbupdatr.exe'), ('S', 'C:\Program Files\Malwarebytes\Anti-Malware\MBAMService.exe'), ('S', 'C:\WINDOWS\system32\taskmgr.exe')))|CTX:NEG
EXCLUSION  + P:SourceImage|IN|('L', (('S', 'C:\Progra Files (x86)\*'), ('S', 'C:\Progra Files\*')))|CTX:NEG
EXCLUSION  - P:SourceImage|EQ|('S', 'C:\WINDOWS\system32\taskmgr.exe')|CTX:NEG
```


---

## V100

```
EXCLUSION  + P:Image|IN|('L', (('S', 'C:\Windows\SysWOW64\*'), ('S', 'C:\Windows\System32\*')))|CTX:NEG
EXCLUSION  - P:Image|EQ|('S', 'C:\Windows\System32\*')|CTX:NEG
SELECTION  + P:OriginalFileName|EQ|('S', 'xwizard.exe')|CTX:POS
```


---

## V101

```
EXCLUSION  + P:CommandLine|IN|(\'L\', ((\'S\', \'*\control.exe input.dll\'), (\'S\', \'*\control.exe\" input.dll\')))|CTX:NEG
EXCLUSION  - P:CommandLine|EQ|('S', '*\control.exe input.dll')|CTX:NEG
```


---

## V102

```
EXCLUSION  - P:CommandLine|EQ|('S', 'null')|CTX:NEG
SELECTION  + P:ParentImage|EQ|('S', '*\WmiPrvSE.exe')|CTX:POS
SELECTION  - P:CommandLine|EQ|('S', '*')|CTX:POS
SELECTION  - P:ParentImage|EQ|('S', '*\wmiprvse.exe')|CTX:POS
```


---

## V103

```
EXCLUSION  + P:ScriptBlockText|EQ|(\'S\', "*Alias(\'htdefac\')*")|CTX:NEG
EXCLUSION  + P:ScriptBlockText|EQ|(\'S\', "*Alias(\'ltdefac\')*")|CTX:NEG
EXCLUSION  + P:ScriptBlockText|EQ|(\'S\', "*Alias(\'mtdefac\')*")|CTX:NEG
EXCLUSION  + P:ScriptBlockText|EQ|(\'S\', "*Alias(\'stdefac\')*")|CTX:NEG
SELECTION  + P:ScriptBlockText|IN|('L', (('S', '*htdefac*'), ('S', '*ltdefac*'), ('S', '*mtdefac*'), ('S', '*stdefac*')))|CTX:POS
```


---

## V104

```
EXCLUSION  + P:CommandLine|EQ|('S', '* -GetLoadLibraryWAddress32*')|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', '*\MpCmdRun.exe')|CTX:NEG
```


---

## V105

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

## V106

```
EXCLUSION  + P:ModifyingApplication|IN|('L', (('S', 'C:\Windows\SysWOW64\msiexec.exe'), ('S', 'C:\Windows\System32\svchost.exe')))|CTX:NEG
EXCLUSION  - P:ModifyingApplication|EQ|('S', 'C:\Windows\SysWOW64\msiexec.exe')|CTX:NEG
```


---

## V107

```
EXCLUSION  + P:Image|EQ|('S', '<unknown process>')|CTX:NEG
```


---

## V108

```
EXCLUSION  + P:TargetFilename|EQ|('S', '*\Microsoft\WindowsApps\*')|CTX:NEG
```


---

## V109

```
EXCLUSION  + P:Image|IN|('L', (('S', '*\EXCEL.exe'), ('S', '*\MSACCESS.exe'), ('S', '*\MSPUB.EXE'), ('S', '*\ONENOTE.EXE'), ('S', '*\ONENOTEM.EXE'), ('S', '*\OUTLOOK.EXE'), ('S', '*\POWERPNT.EXE'), ('S', '*\WINWORD.exe'), ('S', '*\ex
EXCLUSION  - P:Image|IN|('L', (('S', '*\EXCEL.exe'), ('S', '*\MSACCESS.exe'), ('S', '*\ONENOTE.EXE'), ('S', '*\POWERPNT.EXE'), ('S', '*\WINWORD.exe')))|CTX:NEG
SELECTION  + P:Description|IN|('L', (('S', 'Microsoft Access'), ('S', 'Microsoft Excel'), ('S', 'Microsoft OneNote'), ('S', 'Microsoft Outlook'), ('S', 'Microsoft PowerPoint'), ('S', 'Microsoft Publisher'), ('S', 'Microsoft Word'), (
SELECTION  + P:OriginalFileName|IN|('L', (('S', 'Excel.exe'), ('S', 'MSACCESS.EXE'), ('S', 'MSPUB.EXE'), ('S', 'OUTLOOK.EXE'), ('S', 'OneNote.exe'), ('S', 'OneNoteM.exe'), ('S', 'POWERPNT.EXE'), ('S', 'WinWord.exe')))|CTX:POS
SELECTION  - P:Description|IN|('L', (('S', 'Microsoft Access'), ('S', 'Microsoft Excel'), ('S', 'Microsoft OneNote'), ('S', 'Microsoft PowerPoint'), ('S', 'Microsoft Word')))|CTX:POS
SELECTION  - P:OriginalFileName|IN|('L', (('S', 'Excel.exe'), ('S', 'MSACCESS.EXE'), ('S', 'OneNote.exe'), ('S', 'POWERPNT.EXE'), ('S', 'WinWord.exe')))|CTX:POS
```


---

## V110

```
EXCLUSION  + P:Image|IN|('L', (('S', 'C:\Program Files\Mozilla Firefox\firefox.exe*'), ('S', 'C:\Program Files\SplunkUniversalForwarder\bin\*')))|CTX:NEG
EXCLUSION  - P:Image|EQ|('S', 'C:\Program Files\SplunkUniversalForwarder\bin\*')|CTX:NEG
```


---

## V111

```
EXCLUSION  + P:StartFunction|EQ|('S', 'EtwpNotificationThread')|CTX:NEG
SELECTION  + P:TargetImage|IN|('L', (('S', '*\calc.exe'), ('S', '*\explorer.exe'), ('S', '*\mspaint.exe'), ('S', '*\notepad.exe'), ('S', '*\sethc.exe'), ('S', '*\wordpad.exe'), ('S', '*\write.exe')))|CTX:POS
SELECTION  - P:TargetImage|IN|('L', (('S', '*\calc.exe'), ('S', '*\mspaint.exe'), ('S', '*\notepad.exe'), ('S', '*\sethc.exe'), ('S', '*\wordpad.exe'), ('S', '*\write.exe')))|CTX:POS
```


---

## V112

```
EXCLUSION  + P:CommandLine|EQ|('S', '* /s *')|CTX:NEG
EXCLUSION  + P:CommandLine|EQ|('S', '*igfxCPL.cpl*')|CTX:NEG
EXCLUSION  + P:CommandLine|EQ|('S', '*regsvr32 *')|CTX:NEG
```


---

## V113

```
EXCLUSION  + P:Image|EQ|('S', '*:\WINDOWS\explorer.exe')|CTX:NEG
EXCLUSION  + P:Image|IN|('L', (('S', '*:\Program Files (x86)\Citrix\HDX\bin\cmstart.exe'), ('S', '*:\Program Files (x86)\Citrix\HDX\bin\icast.exe'), ('S', '*:\Program Files (x86)\Citrix\System32\icast.exe'), ('S', '*:\Program Files\C
EXCLUSION  + P:Image|IN|('L', (('S', '*:\Windows\SysWOW64\proquota.exe'), ('S', '*:\Windows\System32\proquota.exe')))|CTX:NEG
EXCLUSION  - P:Image|EQ|('S', '*\Citrix\System32\icast.exe')|CTX:NEG
EXCLUSION  - P:Image|EQ|('S', 'C:\WINDOWS\explorer.exe')|CTX:NEG
EXCLUSION  - P:Image|IN|('L', (('S', 'C:\Windows\SysWOW64\proquota.exe'), ('S', 'C:\Windows\System32\proquota.exe')))|CTX:NEG
```


---

## V114

```
EXCLUSION  + P:Provider_Name|EQ|('S', 'Microsoft-Windows-Kernel-Process')|CTX:NEG
SELECTION  + P:Image|EQ|('S', '*')|CTX:POS
```


---

## V115

```
SELECTION  + P:CommandLine|IN|('L', (('S', '* /impersonateuser:*'), ('S', '* asktgt /user:*'), ('S', '* asreproast *'), ('S', '* createnetonly /program:*'), ('S', '* dump /luid:0x*'), ('S', '* dump /service:krbtgt *'), ('S', '* golde
SELECTION  - P:CommandLine|IN|('L', (('S', '* /impersonateuser:*'), ('S', '* asktgt /user:*'), ('S', '* asreproast *'), ('S', '* createnetonly /program:*'), ('S', '* dump /luid:0x*'), ('S', '* dump /service:krbtgt *'), ('S', '* golde
```


---

## V116

```
EXCLUSION  + P:Image|EQ|(\'S\', "-\'*\adexplorer.exe\' -\'*\procdump.exe\' -\'*\msbuild.exe\' -\'*\dotnet.exe\' -\'*\cmd.exe\' -\'*\powershell.exe\' -\'*\psexec.exe\' -\'*\installutil.exe\' -\'*\cscript.exe\' -\'*\wscript.exe\' -\'*\
EXCLUSION  - P:Image|IN|('L', (('S', '*\7z.exe'), ('S', '*\adexplorer.exe'), ('S', '*\certutil.exe'), ('S', '*\cmd.exe'), ('S', '*\cmstp.exe'), ('S', '*\cscript.exe'), ('S', '*\dotnet.exe'), ('S', '*\installutil.exe'), ('S', '*\msbui
```


---

## V117

```
EXCLUSION  + P:Image|EQ|('S', '*\AppData\Local\JetBrains\Toolbox\bin\7z.exe')|CTX:NEG
EXCLUSION  + P:TargetFilename|EQ|('S', '*\JetBrains\apps\*')|CTX:NEG
```


---

## V118

```
EXCLUSION  - P:TargetObject|EQ|('S', '*\NgcFirst\ConsecutiveSwitchCount')|CTX:NEG
```


---

## V119

```
EXCLUSION  - P:TargetObject|EQ|('S', '*\NgcFirst\ConsecutiveSwitchCount')|CTX:NEG
```


---

## V120

```
EXCLUSION  + P:CommandLine|IN|('L', (('S', '*ClearMyTracksByProcess*'), ('S', '*PrintUIEntry*'), ('S', '*UpdatePerUserSystemParameters*')))|CTX:NEG
EXCLUSION  + P:Image|EQ|('S', '*\rundll32.exe')|CTX:NEG
SELECTION  + P:Image|EQ|('S', '*\rundll32.exe')|CTX:POS
```
