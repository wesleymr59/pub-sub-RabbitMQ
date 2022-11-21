import pika, json


class QueueRabbit():
    def __init__(self) -> None:
        credentials = pika.PlainCredentials(username='guest', password='guest')
        parameters = pika.ConnectionParameters(host="192.168.1.109",port=5672,virtual_host='/', credentials=credentials)
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()

        self.channel.queue_declare(queue='teste_queue')
        
    def sendMessage(self, message: str):
        self.channel.basic_publish(exchange='', routing_key='teste_queue', body=json.dumps(message))
        self.connection.close()
        print(" [x] Sent 'Hello World!'")