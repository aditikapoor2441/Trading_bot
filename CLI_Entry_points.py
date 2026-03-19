import argparse
from bot.client import BinanceFuturesClient
from bot.orders import place_order

API_KEY = "your_api_key_here"
API_SECRET = "your_secret_key_here"

client = BinanceFuturesClient(API_KEY, API_SECRET)

parser = argparse.ArgumentParser()
parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float, required=False)

args = parser.parse_args()

place_order(
    client,
    symbol=args.symbol,
    side=args.side,
    order_type=args.type,
    quantity=args.quantity,
    price=args.price
)

# This part actually runs the logic using the inputs you typed in the terminal
if __name__ == "__main__":
    print(f"--- Attempting {args.side} {args.type} for {args.symbol} ---")
    
    # This calls the function from your Order_Logic file
    response = place_order(
        client=client, 
        symbol=args.symbol, 
        side=args.side, 
        order_type=args.type, 
        quantity=args.quantity, 
        price=args.price
    )
    
    print("Binance Response:", response)