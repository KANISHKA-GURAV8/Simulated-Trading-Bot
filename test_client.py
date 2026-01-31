from bot.client import MockBinanceClient

client=MockBinanceClient()

market_order=client.place_order(
    symbol="BICUSDT",
    side="BUY",
    order_type="MARKET",
    quantity=0.01
)

limit_order=client.place_order(
    symbol="BICUSDT",
    side="SELL",
    order_type="LIMIT",
    quantity=0.01,
    price=45000
)

print("Market Order:",market_order)
print("Limit Order:",limit_order)