import pika

credentials = pika.PlainCredentials("guest", "guest")
conn_params = pika.ConnectionParameters("localhost", credentials=credentials)
conn_broker = pika.BlockingConnection(conn_params)

channel = conn_broker.channel()

channel.exchange_declare(exchange="logs-exchange",
                         type="topic",
                         passive=False,
                         durable=True,
                         auto_delete=False)

channel.queue_declare(queue="msg-inbox-errors",
                      passive=False,
                      durable=True,
                      exclusive=False,
                      auto_delete=False)

channel.queue_declare(queue="msg-inbox-logs",
                      passive=False,
                      durable=True,
                      exclusive=False,
                      auto_delete=False)

channel.queue_declare(queue="all-logs",
                      passive=False,
                      durable=True,
                      exclusive=False,
                      auto_delete=False)

channel.queue_bind(queue="msg-inbox-errors",
                   exchange="logs-exchange",
                   routing_key="error.msg-inbox")

channel.queue_bind(queue="msg-inbox-logs",
                   exchange="logs-exchange",
                   routing_key="*.msg-inbox")


