#!/usr/bin/python
#####################################
#    Name : Daily Check
#    Language : Python
#    Create date : 2017.03.23
#    Version : 0.1
######################################

import csv
import platform
import commands

######################################
# Variables
# 0. System_ENV
# 1. SyslogChecker
# 2. FilesystemUsedChecker
######################################
FILENAME_FILESYSTEM="/home/user/test_filesystem.csv"
FILENAME_SYSLOG="/home/user/test_syslog.csv"
#CHECK_ERROR_LIST=['FAIL','ERROR','Fail','Error','fail','error']
#CHECK_NO_LIST=['WARNING','Warning','warning']
Hostname=platform.uname()[1]
USAGE = 4
MOUNT_POINT = 5
HEADER = 1


def SyslogChecker():
    try:
        syslog_file = open('/var/log/syslog', 'r')
    except IOError:
        print "File is not exist."
    else:
        # Make csv file
        csv_file = open(FILENAME_SYSLOG, 'w')
        fieldname_syslog = ['Hostname','Event']
        writer = csv.DictWriter(csv_file, fieldnames=fieldname_syslog)
        writer.writeheader()

        # print syslog
        while True:
            syslog_line = syslog_file.readline()
            if len(syslog_line) == 0:
                break
            if isError(syslog_line):
                writer.writerow({'Hostname':Hostname, 'Event': syslog_line})
    finally:
        if syslog_file:
            syslog_file.close()
        csv_file.close()


def isError(syslog_line):
    return ("FAIL" in syslog_line.upper() or "ERROR" in syslog_line.upper()) and "WARNING" not in syslog_line.upper()


# FileSystem used%
class FilesystemException(Exception):
    def __init__(self,erroutput):
        Exception.__init__(self)

def FilesystemUsedChecker():
    status,cmdResult = commands.getstatusoutput('df -h')
    df_result = extractResult(HEADER, cmdResult)        # remove header

    try:
        if status != 0:
            raise FilesystemException
    except FilesystemException:
        print 'Error : Filesystem used%'
    else:
        # Make csv file
        csv_file = open(FILENAME_FILESYSTEM, 'w')
        fieldname_filesystem = ['Hostname','Filesystem','Used%']
        writer = csv.DictWriter(csv_file, fieldnames=fieldname_filesystem)
        writer.writeheader()

        for dfline in df_result:
            dfline = dfline.split()
            # 80% -> 80
            if long(dfline[USAGE][:-1]) >= 80:
                writer.writerow({'Hostname': Hostname, 'Filesystem': dfline[MOUNT_POINT], 'Used%': dfline[USAGE]})
        csv_file.close()

def extractResult(RESULT, cmdResult):
    return cmdResult.split('\n')[RESULT:]


def main():
    FilesystemUsedChecker()
    SyslogChecker()

if __name__ == "__main__":
    main()

