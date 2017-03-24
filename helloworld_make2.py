import csv
import json

FILENAME_FILESYSTEM="/home/user/collect_test_filesystem.csv"
FILENAME_SYSLOG="/home/user/collect_test_syslog.csv"
CLIENT_SYSLOG_FILE_LIST=['/home/user/ubuntu1_test_syslog.csv', '/home/user/ubuntu2_test_syslog.csv']
CLIENT_USED_FILE_LIST=['/home/user/ubuntu1_test_filesystem.csv', '/home/user/ubuntu2_test_filesystem.csv','/home/user/ubuntu3_test_filesystem.csv']


def SyslogCollector():
    SyslogOutput = open(FILENAME_SYSLOG, 'w')
    Fieldname = ['Hostname', 'Event']
    SyslogWriter = csv.DictWriter(SyslogOutput, fieldnames=Fieldname)
    SyslogWriter.writerow(dict(zip(Fieldname, Fieldname)))
    for list in CLIENT_SYSLOG_FILE_LIST:
        try:
            file = open(list,'r')
        except IOError:
            print "No Syslog Check FILE!!"
        else:
            reader = csv.DictReader(file)
            syslog_list = []
            for row in reader:
                syslog_list.append(row)
        finally:
            if file:
                file.close()
        SyslogWriter.writerows(syslog_list)
    SyslogOutput.close()

def FilesystemUsedCollector():
    UsedOutput = open(FILENAME_FILESYSTEM, 'w')
    Fieldname = ['Hostname','Filesystem','Used%']
    UsedWriter = csv.DictWriter(UsedOutput, fieldnames=Fieldname)
    UsedWriter.writerow(dict(zip(Fieldname, Fieldname)))
    for list in CLIENT_USED_FILE_LIST:
        try:
            file = open(list,'r')
        except IOError:
            print "NO Filesystem Used Check File!!"
        else:
            reader = csv.DictReader(file)
            used_list = []
            for row in reader:
                used_list.append(row)
        finally:
            if file:
                file.close()
        UsedWriter.writerows(used_list)
    UsedOutput.close()

SyslogCollector()
FilesystemUsedCollector()