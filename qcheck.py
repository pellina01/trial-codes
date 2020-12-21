import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='18.207.159.28'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)


depth = channel.queue_declare('task_queue', passive=True)

print(depth.method.message_count)
