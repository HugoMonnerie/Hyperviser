import pika
import json


class RabbitMq:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()

    def sendData(self, local_monitoring_obj):
        self.channel.queue_declare(queue='CPU')

        data_to_send = json.dumps(local_monitoring_obj.reloadData())
        self.channel.basic_publish(exchange='',
                                   routing_key="CPU",
                                   body=data_to_send)

    def callback(self, ch, method, properties, body):
        print(" [x] Received %r" % body)

    def fetchData(self):
        try:
            self.channel.basic_consume(queue='CPU',
                                       auto_ack=True,
                                       on_message_callback=self.callback)
            self.channel.start_consuming()
        except:
            pass
