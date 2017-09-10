
from flask import Flask, render_template, request, redirect
import quandl
import datetime as dt
import pandas as pd
from math import pi

from bokeh.plotting import *
from bokeh.models import DatetimeTickFormatter
from bokeh.embed import components

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')


@app.route('/stock', methods =['POST'])#output
def stock():
    quandl.ApiConfig.api_key = "u7fbraLt9bcvgxYqzXag"
    tick_input = str(request.form['ticker'])
    stock = "WIKI/" + tick_input
    today = str(dt.date.today())
    month_ago = str(dt.date.today() - dt.timedelta(days=30))

    df1 = mydata = quandl.get(stock, start_date=month_ago, end_date=today)
    p = figure(plot_width=400, plot_height=400, title = "Change of "+ tick_input + " in the last month", x_axis_label='Dates', y_axis_label='Stock Price ($)')
    p.line(df1.index.values, df1["Close"], line_width=2)
    p.xaxis.formatter=DatetimeTickFormatter(
            hours=["%d %B %Y"],
            days=["%d %B %Y"],
            months=["%d %B %Y"],
            years=["%d %B %Y"],
        )
    p.xaxis.major_label_orientation = pi/4

    script, div = components(p)

    return render_template ('stock.html', script = script, div = div)

if __name__ == '__main__':
  app.run(port=33507)
