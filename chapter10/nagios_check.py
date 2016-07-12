import sys, json, httplib, base64

status = sys.argv[1]

if status.lower() == "warning":
    print "Status is WARN"
    exit(1)
elif status.lower() == "critical":
    print "Status is CRITICAL"
    exit(2)
elif status.lower() == "unknow":
    print "Status is UNKNOW"
    exit(3)
else:
    print "Status is OK"
    exit(0)