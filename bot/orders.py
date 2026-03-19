import logging

def place_order(client, symbol, side, order_type, quantity, price=None, stop_price=None):
    try:
        # Validate all inputs including the new stop_price
        from bot.validators import validate_order
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
            params["price"] = price
            params["stopPrice"] = stop_price
            params["timeInForce"] = "GTC"
            # In Binance Futures, STOP_LIMIT often uses the 'STOP' or 'STOP_MARKET' type string
            # but 'STOP' with a price parameter acts as a Stop-Limit.
            params["type"] = "STOP" 

        logging.info(f"Sending Request: {params}")
        
        # Accessing the underlying python-binance client
        order = client.client.futures_create_order(**params)
        
        logging.info(f"Binance Response: {order}")
        return order

    except Exception as e:
        logging.error(f"Order Failed: {e}")
        return {"error": str(e)}
