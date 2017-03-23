import csv

HOMEDIR="/home/user/"
FILENAME_FILESYSTEM="test_filesystem.csv"
FILENAME_SYSLOG="test_syslog.csv"

def SyslogChecker():
    try:
        csv_file = open(FILENAME_SYSLOG, 'rb')
    except IOError:
        print "File is not exist."
    else:
        # Make csv file
        fieldname_syslog = ['Hostname','Event']
        reader = csv.DictReader(csv_file,delimiter=',')
        for row in reader:
            print row

    finally:
        if csv_file:
            csv_file.close()

SyslogChecker()