import time
import pandas as pd
import pulp as pl

if __name__ == "__main__":
  data = pd.read_csv("data.csv")
  data["profit"] = data["space"] * data["bid"]

  names = data["name"].tolist()
  space = data["space"].tolist()
  profit = data["profit"].tolist()

  n = len(names)

  # Binary decision variables: x_i = 1 if bidder i is selected, else 0
  x = [pl.LpVariable(f"x_{i}", lowBound=0, upBound=1, cat=pl.LpBinary) for i in range(n)]

  # MILP model: maximize total profit subject to capacity
  model = pl.LpProblem("Rental", pl.LpMaximize)
  # Objective: sum(profit_i * x_i)
  model += pl.lpSum(profit[i] * x[i] for i in range(n))
  # Capacity constraint: sum(space_i * x_i) <= 6000
  model += pl.lpSum(space[i] * x[i] for i in range(n)) <= 6000

  # Solve with CBC via PuLP
  start_time = time.process_time()
  model.solve(pl.PULP_CBC_CMD(msg=False))
  end_time = time.process_time()

  # Extract chosen bidders from solution values
  idx = [i for i in range(n) if x[i].value() is not None and x[i].value() > 0.5]

  print(f"Max Profit:       ${float(sum(profit[i] for i in idx)):,.2f}")
  print(f"Total Space Used: {int(sum(space[i] for i in idx))} ft3")
  print(f"Bidders Selected: {[names[i] for i in idx]}")
  print(f"Execution Time:   {end_time - start_time}")
