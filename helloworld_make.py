import csv
import platform

HOMEDIR="/home/user/"
FILENAME_FILESYSTEM="test_filesystem.csv"
FILENAME_SYSLOG="test_syslog.csv"
# HOSTNAME=platform.uname()[1]

def SyslogCollector():
    try:
        csv_collecter = open(HOMEDIR+FILENAME_SYSLOG,'w')
        csv_file = open(FILENAME_SYSLOG, 'r')
    except IOError:
        print "File is not exist."
    else:
        fieldname_syslog = ['Hostname','Event']
        #reader = csv.DictReader(csv_file,delimiter=',')
        #for row in reader:
        #    print row
        writer = csv.DictWriter(csv_collecter,fieldnames=fieldname_syslog)
        writer.writeheader()

        # file read and write collect


        #while True:
        #    syslog_line = syslog_file.readline()
        #    if len(syslog_line) == 0:
        #        break
        #    if ("FAIL" in syslog_line.upper() or "ERROR" in syslog_line.upper()) \
        #            and "WARNING" not in syslog_line.upper():
        #        writer.writerow({'Hostname':platform.uname()[HOSTNAME],'Event': syslog_line})

    finally:
        if csv_file:
            csv_file.close()
        csv_collecter.close()

SyslogCollector()