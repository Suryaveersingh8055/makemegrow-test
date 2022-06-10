import logging

from connectors.binance_futures import BinanceFuturesClient
from connectors.bitmex import BitmexClient

from interface.root_component import Root


logger = logging.getLogger()

logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':

    binance = BinanceFuturesClient("06bc84781f229f536a94bbd8a03ca3eb58fda0d5c1a235e4a89f89eec8a06480", "44e3c89c026dfb6dcc5168d51cb2c7b27824a64e1ad1a0c73a1185ecd12c26bf", True)
    bitmex = BitmexClient("R4SV7ZCl1BJsa3IDgYFs6hU6", "ZP_tCR3rOGXW4fwY7wZQSzUPqic5lwcAP19sJ_einqVM4erU", True)

    root = Root(binance, bitmex)
    root.mainloop()
