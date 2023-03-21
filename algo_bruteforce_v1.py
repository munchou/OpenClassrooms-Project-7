import csv
from itertools import combinations


BUDGET = 500

with open("shares01.csv") as csvfile:
    shares_file = csv.reader(csvfile, delimiter=",")

    shares_data = []
    for row in shares_file:
        shares_data.append((row[0], float(row[1]), float(row[2])))

print(f"DATA : {shares_data}")


final_list = []

print(len(shares_data))

for elements in range(len(shares_data)):
    all_combinations = combinations(shares_data, elements)
    # print(range(elements))

    for combination in all_combinations:
        # print(f"Combo : {combination}")

        cost = []
        for element in combination:
            cost.append(element[1])
            # print(f"COST : {cost}")

        total_cost = sum(cost)
        # print(f"Total COST : {total_cost}")

        if total_cost <= BUDGET:
            final_list.append(combination)
            # print(f"FINAL LIST : {final_list}")

final_profits = 0


for item in final_list:
    combination_profits = []
    for i in item:
        profits = i[1] * i[2] / 100
        combination_profits.append(profits)
        item_profits = sum(combination_profits)
        # print(f"ITEM PROFITS : {item_profits}")
        if final_profits < item_profits:
            final_profits = item_profits
            final_combination = item


print(f"FINAL PROFITS : {final_profits}")

for item in final_combination:
    print(f"Stock : {item[0]}, Price {item[1]}€, Profits over 2 years : {item[2]}%")
