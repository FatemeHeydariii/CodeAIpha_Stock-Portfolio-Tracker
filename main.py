# Stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOG": 170,
    "AMZN": 190
}

total_investment = 0

print("=== Stock Portfolio Tracker ===")

while True:

    stock_name = input("Enter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not found!")
        continue

    quantity = int(input("Enter quantity: "))

    price = stock_prices[stock_name]
    investment = price * quantity

    total_investment += investment

    print(f"{stock_name}: {quantity} shares × ${price} = ${investment}")
    print()


print("----------------------------")
print(f"Total Investment: ${total_investment}")
print("----------------------------")


# Save result to a text file
save_result = input("Do you want to save the result? (yes/no): ").lower()

if save_result == "yes":

    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Report\n")
        file.write("----------------------\n")
        file.write(f"Total Investment: ${total_investment}\n")

    print("Result saved to portfolio.txt")