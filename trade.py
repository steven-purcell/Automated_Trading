import alpaca_trade_api as tradeapi

from variables import APCA_API_KEY_ID, APCA_API_SECRET_KEY, APCA_API_BASE_URL

URL = APCA_API_BASE_URL 
APCA_API_KEY_ID = APCA_API_KEY_ID
APCA_API_SECRET_KEY = APCA_API_SECRET_KEY

## https://github.com/alpacahq/alpaca-trade-api-python/

symbol = ""
result = ""

api = tradeapi.REST(
                    key_id = APCA_API_KEY_ID,
                    secret_key = APCA_API_SECRET_KEY,
                    base_url = URL,
                    api_version = 'v2'
                    )

account = api.get_account()

# Import API keys from secure file


# GET asset information
def get_asset_information(symbol):

    result = api.get_asset(symbol)

    return(result)

def get_asset(symbol):
    
    result = api.)

# POST buy order
def buy_signal(symbol, qty): # Other params can be added to more granularly control the trade.

    result = tradeapi.submit_order(symbol = symbol,
                            qty = qty,       # Determine qty
                            side = "buy",
                            type = "market",
                            time_in_force = "day",
                            limit_price = None,
                            stop_price = None,
                            client_order_id = None,
                            order_class = None,
                            take_profit = None,
                            stop_loss = None,
                            trail_price = None,
                            trail_percent = None,
                            notional = None     # By fractional shares by dollar amount
                        )

    return(result)

# POST sell order
def sell_signal(symbol, qty): # Other params can be added to more granularly control the trade.

    result = tradeapi.submit_order(symbol = symbol,
                            qty = qty,       # Determine qty
                            side = "sel",
                            type = "market",
                            time_in_force = "day",
                            limit_price = None,
                            stop_price = None,
                            client_order_id = None,
                            order_class = None,
                            take_profit = None,
                            stop_loss = None,
                            trail_price = None,
                            trail_percent = None,
                            notional = None     # By fractional shares by dollar amount
                        )

    return(result)

# # DELETE
# def sell_signal(order_id):
#     result = tradeapi.cancel_order(order_id = order_id)

#     return(result)

# def close_all_positions(): # Sell and close all orders.

#     result = tradeapi.cancel_all_orders()

#     return(result)

# Portfolio Information
def list_positions():

    result = tradeapi.list_positions()

    return(result)

def get_portfolio_history(date_start, date_end, period, timeframe, extended_hours):

    result = tradeapi.get_portfolio_history(date_start=None, date_end=None, period=None, timeframe=None, extended_hours=None)

    return(result)

######## Testing

print(account.status)

x = get_asset_information("TSLA")
print(x)
