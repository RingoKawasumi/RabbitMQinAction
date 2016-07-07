import pika

credentials = pika.PlainCredentials("guest", "guest")
conn_params = pika.ConnectionParameters("localhost", credentials=credentials)
conn_broker = pika.BlockingConnection(conn_params)

channel = conn_broker.channel()

exchange = "amq.rabbitmq.log"

errors_queue = channel.queue_declare(exclusive=True,
                                     auto_delete=True).method.queue
warnings_queue = channel.queue_declare(exclusive=True,
                                       auto_delete=True).method.queue
info_queue = channel.queue_declare(exclusive=True,
                                   auto_delete=True).method.queue

channel.queue_bind(queue=errors_queue,
                   exchange=exchange,
                   routing_key="error")

channel.queue_bind(queue=warnings_queue,
                   exchange=exchange,
                   routing_key="warning")

channel.queue_bind(queue=info_queue,
                   exchange=exchange,
                   routing_key="info")


def error_callback(channel, method, header, body):
    channel.basic_ack(delivery_tag=method.delivery_tag)
    print "error: " + body
    return


def warning_callback(channel, method, header, body):
    channel.basic_ack(delivery_tag=method.delivery_tag)
    print "waring: " + body
    return


def info_callback(channel, method, header, body):
    channel.basic_ack(delivery_tag=method.delivery_tag)
    print "info: " + body
    return

channel.basic_consume(error_callback,
                      queue=errors_queue)

channel.basic_consume(warning_callback,
                      queue=warnings_queue)

channel.basic_consume(info_callback,
                      queue=info_queue)

channel.start_consuming()
