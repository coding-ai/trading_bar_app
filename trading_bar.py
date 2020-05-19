import rumps
from alpha_vantage.timeseries import TimeSeries
import pandas as pd
ts = TimeSeries(key='YOUR_API_KEY')

class TradingInsights(rumps.App):

    @rumps.clicked("BA")
    def trad_ba(self, _):
        data, meta_data = ts.get_intraday('BA')
        data_df = pd.DataFrame(data).iloc[:,0]
        rumps.alert(title='BA latest stock insights',message="Open: " + data_df['1. open'] + "$" + "\nHigh: " + data_df['2. high'] + "$" + "\nLow: "
         + data_df['3. low'] + "$" + "\nClose: " + data_df['4. close'] + "$" + "\nVolume: " + data_df['5. volume'])

    @rumps.clicked("TSLA")
    def trad_tsla(self, _):
        data, meta_data = ts.get_intraday('TSLA')
        data_df = pd.DataFrame(data).iloc[:,0]
        rumps.alert(title='TSLA latest stock insights',message="Open: " + data_df['1. open'] + "$" + "\nHigh: " + data_df['2. high'] + "$" + "\nLow: "
         + data_df['3. low'] + "$" + "\nClose: " + data_df['4. close'] + "$" + "\nVolume: " + data_df['5. volume'])

    @rumps.clicked("UBER")
    def trad_uber(self, _):
        data, meta_data = ts.get_intraday('UBER')
        data_df = pd.DataFrame(data).iloc[:,0]
        rumps.alert(title='UBER latest stock insights',message="Open: " + data_df['1. open'] + "$" + "\nHigh: " + data_df['2. high'] + "$" + "\nLow: "
         + data_df['3. low'] + "$" + "\nClose: " + data_df['4. close'] + "$" + "\nVolume: " + data_df['5. volume'])
        
    @rumps.clicked("WMT")
    def trad_wmt(self, _):
        data, meta_data = ts.get_intraday('WMT')
        data_df = pd.DataFrame(data).iloc[:,0]
        rumps.alert(title='WMT latest stock insights',message="Open: " + data_df['1. open'] + "$" + "\nHigh: " + data_df['2. high'] + "$" + "\nLow: "
         + data_df['3. low'] + "$" + "\nClose: " + data_df['4. close'] + "$" + "\nVolume: " + data_df['5. volume'])

if __name__ == "__main__":
    app = TradingInsights("Stock Insights",icon="logos/stocks.png")
    app.menu = [rumps.MenuItem("BA",callback=app.trad_ba,icon="logos/boeing.png",dimensions=(18,18)),
                rumps.MenuItem("TSLA",callback=app.trad_tsla,icon="logos/tesla.jpg",dimensions=(18,18)),
                rumps.MenuItem("UBER",callback=app.trad_uber,icon="logos/uber.png",dimensions=(18,18)),
                rumps.MenuItem("WMT",callback=app.trad_wmt,icon="logos/walmart.jpg",dimensions=(18,18)),None]
    app.run()