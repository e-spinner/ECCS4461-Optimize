# Setup

install uv via:
```zsh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

setup environment with:
```zsh
uv sync
```

# Report

## Data

```txt
❭ uv run brute.py
Max Profit:       $35,580.00
Total Space Used: 6000 ft3
Bidders Selected: ['Byte Repair', 'EcoHome Goods', 'VR Arena']
Execution Time:   0.03264065599999988
```

```txt
❭ uv run genetic.py
Max Profit:       $33,600.00
Total Space Used: 6000 ft3
Bidders Selected: ['Polar Brew Coffee', 'Tech Haven', 'Byte Repair', "Clyde's Photo, Ada"]
Execution Time:   0.23351022499999985
```

```txt
❭ uv run mixed.py
Max Profit:       $35,580.00
Total Space Used: 6000 ft3
Bidders Selected: ['Byte Repair', 'EcoHome Goods', 'VR Arena']
Execution Time:   0.0004531260000000259
```

## Anylysis

Brute Force and Mixed-Integer Programming both reach the global optimum: Max Profit = $35,580.00 at 6000 ft3 with bidders ['Byte Repair', 'EcoHome Goods', 'VR Arena']. The Genetic Algorithm returns a feasible but slightly worse solution: Max Profit = $33,600.00 at 6000 ft3 with bidders ['Polar Brew Coffee', 'Tech Haven', 'Byte Repair', "Clyde's Photo, Ada"]. This is typical without heavier tuning or longer runs.

Mixed-Integer Programming took the least time at ~0.00045 s, while Brute Force took quite a but longer at ~0.0326 s. Finally Genetic Algorithm too the longest at ~0.2335 s, likely slower here due to population-based search and the overhead required to do genetic optimization.

# Overview

For this assignment, you're going to solve a problem with three different methods:

* **Brute Force**
* **Mixed-integer programming**
* **Genetic algorithm**

---

## Problem

**Ohio Northern University (ONU)** has planned to subdivide the former RiteAid into several individual businesses and has opened an auction for proposed businesses to bid on renting the space. There is **6,000 $ft^3$** available.

### Bidders for Rental at Former RiteAid Location

| Business Name | Space requested ($ft^3$) | Bid ($/ft^3$) | Category |
| :--- | :--- | :--- | :--- |
| Polar Brew Coffee | 1,200 | 4.5 | Food & Beverage |
| Tech Haven | 2,500 | 6.2 | Electronics |
| Green Leaf Market | 1,800 | 5.1 | Grocery |
| Campus Books & Co. | 2,200 | 4.8 | Retail |
| FitZone Gym | 3,500 | 3.9 | Fitness |
| Byte Repair | 900 | 6.8 | Electronics |
| Urban Threads | 1,600 | 5.5 | Clothing |
| Clyde's Photo, Ada | 1,400 | 4.7 | Arts |
| GameSphere | 2,000 | 5.9 | Entertainment |
| Serenity Spa | 2,800 | 4.2 | Wellness |
| QuickPrint Center | 1,100 | 5 | Services |
| EcoHome Goods | 1,900 | 5.4 | Retail |
| Smoothie Spot | 1,000 | 4.6 | Food & Beverage |
| VR Arena | 3,200 | 6 | Entertainment |
| Study Lounge Café | 2,100 | 4.9 | Food & Beverage |

**Your Goal:** Find the combination of bidders that would maximize the university's profits.

---

## Deliverables

Please submit the following in one **zip file**:

1.  **Three source files:** One for each of the optimization techniques. Use **Python** or **MATLAB**.
2.  **A brief report:** Detail the outcomes of each optimization technique. Include analyses on:
    * **Performance:** How optimal the solutions are.
    * **Speed:** How many CPU cycles (or execution time) it took to execute.

---

## AI Usage

> **AI Usage: Yellow Light**
> You may use any AI coding tools; however, you should avoid using them blindly. The concepts for this assignment will be on the final exam. If you have an LLM do the entire project for you, you will not learn the concepts sufficiently to succeed on the exam.