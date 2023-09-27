#!/usr/bin/python3
import sys

userName= 'root'

# get a user name from command arguments
if len(sys.argv) > 1 :
    userName= sys.argv[1]

# get a group name from /etc/passwd file
file= open( "/etc/passwd" )
for line in file :
    splitedLine= line.split(":")
    if splitedLine[0] == userName :
        groupName= splitedLine[4]
file.close()

# get a groups name from /etc/group file
file= open( "/etc/group" )
groupList= []
for line in file :
    splitedLine= line.split(":")
    if splitedLine[3].find(userName) != -1 :
        groupList.append(splitedLine[0])
file.close()

# retrun the result with a format-string:
print( f"{userName}:{groupName} groups: {groupList}" )
