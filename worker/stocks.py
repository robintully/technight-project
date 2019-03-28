import pandas_datareader.data as web
from datetime import datetime
from fbprophet import Prophet
import pandas as pd
import json

start = datetime(2018, 1, 1)
end = datetime(2019, 3, 22)


def make_prediction(stock):
    f = web.DataReader(stock, 'iex', start, end)
    df = f['open']
    prophet_df = pd.DataFrame(df).reset_index()
    prophet_df.columns = ['ds','y']
    m = Prophet()
    m.fit(prophet_df)
    future = m.make_future_dataframe(periods=20)
    forecast = m.predict(future)
    forecast_df =  forecast[['ds','yhat']][-30:]
    formatted = [(str(a[1]).split(' ')[0],a[2]) for a in forecast_df.itertuples()] 
    return json.dumps({'values': formatted})
