import time
import numpy as np
import pandas as pd

from pymoo.core.problem import Problem
from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.optimize import minimize
from pymoo.termination.ftol import SingleObjectiveSpaceTermination
from pymoo.termination.robust import RobustTermination
from pymoo.operators.sampling.rnd import BinaryRandomSampling
from pymoo.operators.crossover.hux import HUX
from pymoo.operators.mutation.bitflip import BitflipMutation


class Rental(Problem):
  def __init__(self, space: np.ndarray, profit: np.ndarray):
    # Vectorized single-objective, single-constraint binary problem
    super().__init__(n_var=space.shape[0], n_obj=1, n_constr=1, xl=0, xu=1)
    self.space = space
    self.profit = profit

  def _evaluate(self, x, out, *args, **kwargs):
    # x is a population matrix (n_pop x n_items)
    # Objective: maximize total profit (negated to minimize)
    out["F"] = (~x @ self.profit).reshape(-1, 1)
    # Constraint: total space must not exceed capacity (<= 0 means feasible)
    out["G"] = (x @ self.space - 6000).reshape(-1, 1)


if __name__ == "__main__":
  data = pd.read_csv("data.csv")
  data["profit"] = data["space"] * data["bid"]

  problem = Rental(
    space=data["space"].to_numpy(dtype=float),
    profit=data["profit"].to_numpy(dtype=float),
  )

  algorithm = GA(
    pop_size=100,
    sampling=BinaryRandomSampling(),
    crossover=HUX(prob=0.9),
    mutation=BitflipMutation(prob=0.02),
    eliminate_duplicates=True,
  )

  # Stop when improvement slows in objective space
  termination = SingleObjectiveSpaceTermination(tol=250, n_skip=1)

  # Solve the problem with genetic algorithm
  start_time = time.process_time()
  res = minimize(
    problem,
    algorithm,
    termination,
    save_history=False,
    verbose=False,
  )
  end_time = time.process_time()

  # Extract chosen items from the best solution, ensure 1D vector
  idx = np.where(np.atleast_2d(res.X).astype(int)[0] == 1)[0].tolist()

  print(f"Max Profit:       ${float(data['profit'].to_numpy(dtype=float)[idx].sum()):,.2f}")
  print(f"Total Space Used: {int(data['space'].to_numpy(dtype=float)[idx].sum())} ft3")
  print(f"Bidders Selected: {[str(data['name'].to_numpy()[i]) for i in idx]}")
  print(f"Execution Time:   {end_time - start_time}")
