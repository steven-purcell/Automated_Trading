import alpaca_trade_api as tradeapi

## https://github.com/alpacahq/alpaca-trade-api-python/

URL = "https://paper-api.alpaca.markets/"
symbol = ""
result = ""

# Import API keys from secure file
def get_api_keys():
    
    #TODO: Get keys from secure location here
    ##
    ###
    ####
    #####
    return(None)

# GET asset information
def get_asset_information(symbol):

    result = tradeapi.get_asset(symbol)

    return(result)

# POST buy order
def buy_signal(symbol, qty):

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
                            notional = None
                        )

    return(result)

# DELETE
def sell_signal(order_id):
    result = tradeapi.cancel_order(order_id = order_id)

    return(result)

def close_all_positions():

    result = tradeapi.cancel_all_orders()

    return(result)

# Portfolio Information
def list_positions():

    result = tradeapi.list_positions()

    return(result)

def get_portfolio_history(date_start, date_end, period, timeframe, extended_hours):

    result = tradeapi.get_portfolio_history(date_start=None, date_end=None, period=None, timeframe=None, extended_hours=None)

    return(result)