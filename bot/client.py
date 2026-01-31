import uuid
from datetime import datetime

from bot.logging_config import setup_logger

logger=setup_logger()

class MockBinanceClient:
    """
    Mock client simulating Binance Futures Testnet behavior.
    """

    def place_order(
            self,
            symbol:str,
            side:str,
            order_type:str,
            quantity:float,
            price:float=None,
    ):
        logger.info(
            f"Order request | symbol={symbol},side={side},"
            f"type={order_type},quantity={quantity},price={price}"
            
        )

        order_id=str(uuid.uuid4())[:10]

        if order_type=="MARKET":
            status="FILLED"
            executed_qty=quantity
            avg_price="MARKET_PRICE"
        else:
            status="NEW"
            executed_qty=0
            avg_price=price

        response={
            "orderId":order_id,
            "symbol":symbol,
            "side":side,
            "type":order_type,
            "status":status,
            "executedQty":executed_qty,
            "avgPrice":avg_price,
            "timestamp":datetime.utcnow().isoformat(),
        }

        logger.info(f"Order response | {response}")

        return response