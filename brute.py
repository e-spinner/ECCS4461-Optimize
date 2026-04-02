from itertools import combinations
import pandas as pd
import time

if __name__ == "__main__":
  data = pd.read_csv("data.csv")
  # Profit for each bidder = requested space * bid per ft^3
  data["profit"] = data["space"] * data["bid"]

  best_profit = 0
  best_combo = None

  start_time = time.process_time()

  # Enumerate all subsets (c) by length (r) by number of businesses
  for r in range(1, len(data["name"].tolist()) + 1):
    for c in combinations(data.to_dict(orient="records"), r):
      # Aggregate totals for this candidate subset
      total_space = sum(item["space"] for item in c)
      total_profit = sum(item["profit"] for item in c)

      # Update best profit if feasible and better than current best
      if total_space <= 6000:
        if total_profit > best_profit:
          best_profit = total_profit
          best_combo = c

  end_time = time.process_time()

  print(f"Max Profit:       ${best_profit:,.2f}")
  print(f"Total Space Used: {sum(i['space'] for i in best_combo)} ft3")
  print(f"Bidders Selected: {[i['name'] for i in best_combo]}")
  print(f"Execution Time:   {end_time - start_time}")
