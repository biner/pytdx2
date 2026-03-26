import zlib
from datetime import date

import pandas as pd
from client.quotationClient import QuotationClient
from const import (
    MARKET,
    PERIOD,
    ADJUST,
)
from parser.ex_quotation import file, goods
from parser.quotation import server, stock
from utils.log import log

if __name__ == "__main__":
    client = QuotationClient()
    if client.connect().login():
        print("无复权")
        print(pd.DataFrame(client.get_kline(MARKET.SZ, "000100", PERIOD.DAILY, count=3)))
        print("无复权")
        print(pd.DataFrame(client.get_kline(MARKET.SZ, "000100", PERIOD.DAILY, count=3, fq=ADJUST.QFQ)))
        print("后复权")
        print(pd.DataFrame(client.get_kline(MARKET.SZ, "000100", PERIOD.DAILY, count=3, fq=ADJUST.HFQ)))
        # part = client.call(stock.K_Line(MARKET.SZ, "000001", PERIOD.DAILY))
