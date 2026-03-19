# bot/orders.py
from bot.client import BinanceFuturesClient
from bot.validators import validate_order
import logging

def place_order(client, symbol, side, order_type, quantity, price=None, stop_price=None):
    """
    Place an order on Binance Futures Testnet
    Supports: MARKET, LIMIT, STOP_LIMIT
    """
    try:
        validate_order(symbol, side, order_type, quantity, price, stop_price)

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        elif order_type == "STOP_LIMIT":
            if price is None or stop_price is None:
                raise ValueError("STOP_LIMIT requires both price and stop_price")
            params["price"] = price          # limit price to execute
            params["stopPrice"] = stop_price # trigger price
            params["timeInForce"] = "GTC"

        logging.info(f"Placing order: {params}")
        order = client.client.futures_create_order(**params)
        logging.info(f"Order response: {order}")

        print(" Order placed successfully!")
        print(order)
        return order

    except Exception as e:
        logging.error(f"Error placing order: {e}")
        print(" Error placing order:", e)