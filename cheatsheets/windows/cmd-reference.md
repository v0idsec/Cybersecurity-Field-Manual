# Windows Command Prompt Reference

## Navigation

```cmd
:: Current directory
cd

:: Change directory
cd C:\Windows

:: Move up one directory
cd ..

:: Change drive
D:

:: List files
dir

:: Include hidden and system files
dir /a

:: Recursive listing
dir /s

:: Create directory
mkdir C:\Temp

:: Remove directory
rmdir C:\Temp

:: Remove directory and contents
rmdir /s C:\Temp

:: Copy file
copy source.txt destination.txt

:: Move file
move source.txt destination.txt

:: Rename file
ren old.txt new.txt

:: Delete file
del file.txt
```

## System information

```cmd
:: System information
systeminfo

:: Hostname
hostname

:: Current user
whoami

:: User identity and groups
whoami /all

:: Current date and time
date /t
time /t

:: Environment variables
set

:: Display a variable
echo %USERNAME%

:: Windows version
ver
```

## User and group information

```cmd
:: Current user
whoami

:: Current user's groups
whoami /groups

:: Current user's privileges
whoami /priv

:: Local users
net user

:: Detailed user information
net user username

:: Local groups
net localgroup

:: Group membership
net localgroup Administrators
```

## Process management

```cmd
:: List processes
tasklist

:: Detailed process listing
tasklist /v

:: Find process by name
tasklist /fi "imagename eq notepad.exe"

:: Terminate process by PID
taskkill /PID 1234

:: Force termination
taskkill /PID 1234 /F

:: Terminate by image name
taskkill /IM notepad.exe /F
```

## Services

```cmd
:: List services
sc query

:: Query specific service
sc query Spooler

:: Service configuration
sc qc Spooler

:: Start service
sc start Spooler

:: Stop service
sc stop Spooler

:: List running services
net start
```

## Networking

```cmd
:: IP configuration
ipconfig

:: Full IP configuration
ipconfig /all

:: DNS cache
ipconfig /displaydns

:: Flush DNS cache
ipconfig /flushdns

:: Renew DHCP lease
ipconfig /renew

:: Ping host
ping example.com

:: Trace route
tracert example.com

:: DNS lookup
nslookup example.com

:: Network connections
netstat -ano

:: Routing table
route print

:: ARP cache
arp -a
```

## File search

```cmd
:: Search for a file
where notepad.exe

:: Search directory tree
dir C:\*.log /s

:: Search text in files
findstr "error" *.log

:: Case-insensitive search
findstr /i "failed" *.log

:: Recursive search
findstr /s /i "password" C:\Temp\*.txt
```

## Scheduled tasks

```cmd
:: List scheduled tasks
schtasks /query

:: Detailed task listing
schtasks /query /fo LIST /v

:: Query specific task
schtasks /query /tn "\TaskName"

:: Run task
schtasks /run /tn "\TaskName"

:: View task details
schtasks /query /tn "\TaskName" /xml
```

## Event logs

```cmd
:: List event logs
wevtutil el

:: Display recent System events
wevtutil qe System /c:20 /rd:true /f:text

:: Display recent Security events
wevtutil qe Security /c:20 /rd:true /f:text

:: Export event log
wevtutil epl System C:\Temp\System.evtx
```

Access to Security logs may require elevated privileges.

## Useful references

- [Windows Commands](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands)
- [Command Prompt Documentation](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/)

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
