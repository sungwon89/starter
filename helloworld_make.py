import csv
import platform

HOMEDIR="/home/user/"
FILENAME_FILESYSTEM="collect_test_filesystem.csv"
FILENAME_SYSLOG="collect_test_syslog.csv"
HOSTNAME=platform.uname()[1]
CLIENT_SYSLOG_FILE_LIST=['/home/user/ubuntu1_test_syslog.csv','/home/user/ubuntu2_test_syslog.csv']
CLIENT_USED_FILE_LIST=['/home/user/ubuntu1_test_filesystem.csv','/home/user/ubuntu2_test_filesystem.csv']


def SyslogCollector():
    try:
        syslog_collecter = open(HOMEDIR+FILENAME_SYSLOG,'w')
    except IOError:
        print "File is not exist."
    else:
        fieldname_syslog = ['Hostname', 'Event']
        writer = csv.DictWriter(syslog_collecter, fieldnames=fieldname_syslog)
        writer.writeheader()

        for client_file in CLIENT_SYSLOG_FILE_LIST:
            #print client_file
            syslog_file = open(client_file, 'r')
            reader = csv.DictReader(syslog_file)
            for row in reader:
                print row[0]
                if len(row[0]) == 0:
                    break
                writer.writerow({'Hostname':row[0], 'Event':row[1]})
            if syslog_file:
                syslog_file.close()
            #print 222

    finally:
        syslog_collecter.close()


def FilesystemUsedCollector():
    try:
        used_collecter = open(HOMEDIR+FILENAME_FILESYSTEM,'w')

    except IOError:
        print "File is not exist."
    else:
        fieldname_filesystem = ['Hostname','Filesystem','Used%']
        writer = csv.DictWriter(used_collecter, fieldnames=fieldname_filesystem)
        writer.writeheader()

        for client_file in CLIENT_USED_FILE_LIST:
            csv_file = open(client_file, 'r')
            reader = csv.DictReader(csv_file)
            for Mountpoint, Used, Host in reader:
                if len(Host) == 0:
                    break
                writer.writerow({'Hostname':Host, 'Filesystem':Mountpoint, 'Used%':Used})
                    #print Mountpoint, Used, Host
            if csv_file:
                    csv_file.close()

    finally:
        used_collecter.close()


SyslogCollector()
FilesystemUsedCollector()