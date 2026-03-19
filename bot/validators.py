def validate_order(symbol, side, order_type, quantity, price=None, stop_price=None):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")
    
    if order_type not in ["MARKET", "LIMIT", "STOP_LIMIT"]:
        raise ValueError("Order type must be MARKET, LIMIT, or STOP_LIMIT")
    
    if quantity <= 0:
        raise ValueError("Quantity must be > 0")
    
    if order_type == "LIMIT" and (price is None or price <= 0):
        raise ValueError("LIMIT orders require a price")

    if order_type == "STOP_LIMIT":
        if price is None or price <= 0:
            raise ValueError("STOP_LIMIT requires a Limit Price")
        if stop_price is None or stop_price <= 0:
            raise ValueError("STOP_LIMIT requires a Stop Price")
