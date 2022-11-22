import pika, json, inspect, tabulate, sys


def debug(*args,exitDebug):

    # Busca o contexto de quem chamou a função debug:
    context = inspect.stack()[1][0]

    # Obtém detalhes de onde foi executado o debug:
    filename = context.f_code.co_filename
    linenumber = context.f_lineno

    # Resultados a serem exibidos:
    result = []

    # Percorre todas as variáveis a serem exibidas:
    for name in args:
        # Verifica se é uma variável local no contexto:
        if name in context.f_locals:
            result.append([name, context.f_locals[name], type(context.f_locals[name])])
        # Verifica se é uma variável global no contexto:
        elif name in context.f_globals:
            result.append([name, context.f_globals[name],type(context.f_locals[name])])
        # Variável não encontrada no contexto:
        else:
            result.append([name, "Variable Not Found"])

    # Exibe os resultados em forma de tabela:
    print(f'[DEBUG] {filename} ({linenumber})')
    print(tabulate.tabulate(result, headers=['Variável', 'Valor', 'Type' ]))
    if exitDebug:
            sys.exit("Leaving The Debugger Running")
class QueueRabbit():
    def __init__(self) -> None:
        parameters = pika.ConnectionParameters(host="192.168.1.109",port=5672,virtual_host='/', 
                                               credentials=pika.PlainCredentials(username='guest', password='guest'))
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()

        self.channel.queue_declare(queue='teste_queue')
        
    def sendMessage(self, message: str):
        self.channel.basic_publish(exchange='', routing_key='teste_queue', body=json.dumps(message))
        self.connection.close()
        print(" [x] Sent 'Hello World!'")