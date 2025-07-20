import random

class VirtualStockMarket:
    def __init__(self):
        self.balance = 10000
        self.stocks = {"AAPL": 150, "GOOG": 2800, "TSLA": 750}
        self.portfolio = {}

    def update_prices(self):
        for stock in self.stocks:
            self.stocks[stock] *= round(random.uniform(0.95, 1.05), 2)

    def buy(self, stock, qty):
        price = self.stocks.get(stock)
        if price:
            total = price * qty
            if self.balance >= total:
                self.balance -= total
                self.portfolio[stock] = self.portfolio.get(stock, 0) + qty
                print(f"Bought {qty} of {stock}")
            else:
                print("Insufficient funds!")
        else:
            print("Stock not found!")

    def sell(self, stock, qty):
        if self.portfolio.get(stock, 0) >= qty:
            self.balance += self.stocks[stock] * qty
            self.portfolio[stock] -= qty
            print(f"Sold {qty} of {stock}")
        else:
            print("Not enough shares!")

    def show(self):
        print("\n--- Portfolio ---")
        print("Balance:", round(self.balance, 2))
        print("Stocks:", self.portfolio)
        print("Prices:", self.stocks)

# Example run
sim = VirtualStockMarket()
sim.show()
sim.buy("AAPL", 5)
sim.update_prices()
sim.sell("AAPL", 2)
sim.show()
