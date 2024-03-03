
import random

MAX_INCREASE = 0.1
MAX_DECREASE = 0.05
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0
OUTPUT_FILE = "file.txt"

out_file = open(OUTPUT_FILE, 'w')
price = INITIAL_PRICE
print(f"Starting price: ${price:,.2f}")

total = 0
while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    total = total + 1

    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print(f"On day {total} price is: ${price:,.2f}", file=out_file)
out_file.close()