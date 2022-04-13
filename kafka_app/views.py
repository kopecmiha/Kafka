from django.http import HttpResponse
from kafka import KafkaProducer
from kafka import KafkaConsumer
import pickle


def kfk(request):
    producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')
    v = {
        'msg': {
            'hello': 'world4656',
        },
    }
    serialized_data = pickle.dumps(v, pickle.HIGHEST_PROTOCOL)
    producer.send('Ptopic', serialized_data)
    return HttpResponse(200)


def cons(request):
    consumer = KafkaConsumer('Ptopic',
                             bootstrap_servers='127.0.0.1:9092',
                             )

    for message in consumer:
        deserialized_data = pickle.loads(message.value)
        print(deserialized_data)
    return HttpResponse(300)
