from bot.client import MockBinanceClient
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)
from bot.logging_config import setup_logger

logger=setup_logger()

def place_order(
        symbol:str,
        side:str,
        order_type:str,
        quantity:float,
        price:float =None,
):
    validate_symbol(symbol)
    side=validate_side(side)
    order_type=validate_order_type(order_type)
    quantity=validate_quantity(quantity)
    price=validate_price(price,order_type)

    logger.info("All inputs validated successfully.")

    client=MockBinanceClient()

    try:
        order_response=client.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
        )
        return order_response
    except Exception as e:
        logger.error(f"Order placement failed:{e}")
        raise