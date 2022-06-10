import logging

from connectors.binance import BinanceClient
from connectors.bitmex import BitmexClient

from interface.root_component import Root


# Create and configure the logger object

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)  # Overall minimum logging level

stream_handler = logging.StreamHandler()  # Configure the logging messages displayed in the Terminal
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)  # Minimum logging level for the StreamHandler

file_handler = logging.FileHandler('info.log')  # Configure the logging messages written to a file
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)  # Minimum logging level for the FileHandler

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':  # Execute the following code only when executing main.py (not when importing it)

    binance = BinanceClient("42750d44a14aa3ac5b7950abceabc4c34e3f0c1caa76da551b0eb2f741dd0e76",
                            "478f69d71cfd60d46885a20ff31dec15682bf59ad7e9d0233961fe8c4fd3968f",
                            testnet=True, futures=True)
    bitmex = BitmexClient("zCd3W3emFRvitPnY7v2FUrox", "gSBtEAaCaeweJ7DD_X7_0xdgxA4yDss0RD5Z5Odr1k3tFnKh", testnet=True)

    root = Root(binance, bitmex)
    root.mainloop()
