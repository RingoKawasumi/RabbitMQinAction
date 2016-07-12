import sys, pika

EXIT_OK = 0
EXIT_WARNING = 1
EXIT_CRITICAL = 2
EXIT_UNKNOW = 3

server, port = sys.argv[1].split(":")
vhost = sys.argv[2]
username = sys.argv[3]
password = sys.argv[4]

creds_broker = pika.PlainCredentials(username, password)
conn_params = pika.ConnectionParameters(server,
                                        virtual_host=vhost,
                                        credentials=creds_broker)

try:
    conn_broker = pika.BlockingConnection(conn_params)
    channel = conn_broker.channel()
except Exception:
    print "CRITICAL: Could not connect to %s:%s!" % (server, port)
    exit(EXIT_CRITICAL)

print "OK: Connect to %s:%s successful." % (server, port)
exit(EXIT_OK)