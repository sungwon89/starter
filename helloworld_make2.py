import csv
import platform
import json

FILENAME_FILESYSTEM="/home/user/collect_test_filesystem.csv"
FILENAME_SYSLOG="/home/user/collect_test_syslog.csv"
CLIENT_SYSLOG_FILE_LIST=['/home/user/ubuntu1_test_syslog.csv', '/home/user/ubuntu2_test_syslog.csv']
CLIENT_USED_FILE_LIST=['/home/user/ubuntu1_test_filesystem.csv', '/home/user/ubuntu2_test_filesystem.csv']


def SyslogCollector():
    SyslogOutput = open(FILENAME_SYSLOG, 'w')
    fieldnames = ['Hostname', 'Event']
    SyslogWriter = csv.DictWriter(SyslogOutput, fieldnames=fieldnames)
    SyslogWriter.writerow(dict(zip(fieldnames, fieldnames)))
    for list in CLIENT_SYSLOG_FILE_LIST:
        file = open(list,'r')
        reader = csv.DictReader(file)
        syslog_list = []
        for row in reader:
            syslog_list.append(row)
        file.close()
        SyslogWriter.writerows(syslog_list)
    SyslogOutput.close()

def FilesystemUsedCollector():
    UsedOutput = open(FILENAME_FILESYSTEM, 'w')
    fieldnames = ['Hostname','Filesystem','Used%']
    UsedWriter = csv.DictWriter(UsedOutput, fieldnames=fieldnames)
    UsedWriter.writerow(dict(zip(fieldnames, fieldnames)))
    for list in CLIENT_USED_FILE_LIST:
        file = open(list,'r')
        reader = csv.DictReader(file)
        used_list = []
        for row in reader:
            used_list.append(row)
        file.close()
        #print used_list
        UsedWriter.writerows(used_list)
    UsedOutput.close()

SyslogCollector()
FilesystemUsedCollector()