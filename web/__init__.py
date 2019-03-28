import responder
from time import sleep
from worker.redis_queue import pull
import json


api = responder.API(static_dir='web/static/', templates_dir='web/template')

@api.route("/predict/{stock}")
async def greet_world(req, resp, *, stock):
    stock_values = pull(stock)
    stock_values = json.loads(stock_values)['values'] or False
    print(stock_values)
    if stock_values:
        resp.html = api.template('df.html', stock_name=stock, stock_values=stock_values)
    else:
        resp.html = f'Pending for {stock}'