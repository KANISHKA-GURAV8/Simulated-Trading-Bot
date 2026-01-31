import argparse
import sys

from bot.orders import place_order
from bot.logging_config import setup_logger

logger = setup_logger()


def main():
    parser = argparse.ArgumentParser(
        description="Simplified Trading Bot (Binance Futures Testnet - Mock)"
    )

    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g. BTCUSDT)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")

    args = parser.parse_args()

    print("\n📌 Order Request Summary")
    print("-----------------------")
    print(f"Symbol     : {args.symbol}")
    print(f"Side       : {args.side}")
    print(f"Type       : {args.type}")
    print(f"Quantity   : {args.quantity}")
    if args.type == "LIMIT":
        print(f"Price      : {args.price}")

    try:
        order = place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price,
        )

        print("\n✅ Order Placed Successfully")
        print("----------------------------")
        print(f"Order ID      : {order['orderId']}")
        print(f"Status        : {order['status']}")
        print(f"Executed Qty  : {order['executedQty']}")
        print(f"Avg Price     : {order['avgPrice']}")

    except Exception as e:
        logger.error(str(e))
        print("\n❌ Order Failed")
        print("Reason:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
