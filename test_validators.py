from bot.validators import *

validate_symbol("BTCUSDT")
print(validate_side("buy"))
print(validate_order_type("limit"))
print(validate_quantity("0.01"))
print(validate_price("45000","LIMIT"))

print("All validators passed")