# Binance Futures Trading Bot 

This is a Python-based CLI tool developed for the Anything.ai internship task. It allows users to execute trades on the Binance Futures Testnet with automated logging and input validation.

## Features
- **Core:** Market and Limit Orders.
- **Bonus:** Stop-Limit Order support implemented.
- **Validation:** Robust checks for quantity, price, and order types.
- **Logging:** All requests and responses are saved to `trading_bot.log`.
- **Architecture:** Modular package structure using a `bot/` sub-package.

## Project Structure
```text
Trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   └── validators.py
├── CLI_Entry_points.py
├── Set_up_logging.py
└── README.md
