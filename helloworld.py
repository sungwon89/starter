#####################################
#    Name : Daily Check
#    Language : Python
#    Create date : 2017.03.23
#    Version : 0.1
######################################

import commands

# /var/log/syslog
# /var/log/test_syslog
def Errorlog():
    try:
        syslog_file = open('/var/log/syslog', 'r')
    except IOError:
        print "File is not exist."
    else:
        while True:
            syslog_line = syslog_file.readline()

            if len(syslog_line) == 0:
                break
            if ("FAIL" in syslog_line.upper() or "ERROR" in syslog_line.upper()) \
                    and "WARNING" not in syslog_line.upper():
                print syslog_line
 #   finally:
        syslog_file.close()



# FileSystem used%
class FilesystemException(Exception):
    def __init__(self,erroutput):
        Exception.__init__(self)

def Filesystem_Check():
    USAGE = 4
    MOUNT_POINT = 5
    RESULT = 1
    STATUS = 0

    df = commands.getstatusoutput('df -h')
    df_result = df[RESULT]
    df_result = df_result.split('\n')[RESULT:]
    df_status = df[STATUS]

    try:
        if df_status != 0:
            raise FilesystemException
    except FilesystemException:
        print 'Error : Filesystem used%'
    else:
        for dfline in df_result:
            dfline = dfline.split()
            if long(dfline[USAGE][:-1]) >= 20:
                print 'Used% : {} \t\t Filesystem : {}'.format(dfline[USAGE],dfline[MOUNT_POINT])

#def main():
print 'FILESYSTEM USED'
Filesystem_Check()
print '\n'
print 'ERROR LOG'
Errorlog()

#if __name__ == "__main__":
#    main()

