import backtrader
import datetime
from strategies import TestStrategy
import math

def percentage(part, whole):
    return 100 * float(part)/float(whole)

cerebro = backtrader.Cerebro()
cerebro.broker.set_cash(1000)

init_portfolio = cerebro.broker.get_value()
print('Starting portfolio value: %0.2f' % init_portfolio)

data = backtrader.feeds.YahooFinanceCSVData(
    dataname='data/TSLA.csv',
    fromdate=datetime.datetime(2019,1,1),
    todate=datetime.datetime(2019,12,31),
)

cerebro.adddata(data)
cerebro.addstrategy(TestStrategy)

cerebro.run()

final_portfolio = cerebro.broker.get_value()

print('Final portfolio value: %0.2f' % final_portfolio)

rest = final_portfolio - init_portfolio
print('%0.2f percent a year' % percentage(rest, init_portfolio))
