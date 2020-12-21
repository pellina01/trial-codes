import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='18.207.159.28'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)


def send_msg(msg):
    message = msg
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        ))
    print(" [x] Sent %r" % message)


while True:
    msg = input('say something: ')
    send_msg(msg)

# connection.close()
