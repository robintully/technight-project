from redis import Redis
from huey import RedisHuey
from .stocks import make_prediction
from time import sleep
import json

r = Redis()#host='redis')
r.flushdb()
huey = RedisHuey()#host='redis')

@huey.task()
def train_model(stock):  
    result = make_prediction(stock)
    r.set(stock, str(result))

def pull(stock):
    result = r.get(stock)
    if not result:
        r.set(stock,json.dumps({'values': False}))
        train_model(stock)
    return result
