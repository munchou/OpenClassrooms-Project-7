import time
import csv
from itertools import combinations

start_time = time.time()

BUDGET = 500


def main():
    """Main function launched at the start of the program."""
    shares_data = load_data()

    all_combinations = make_combinations(shares_data)

    selected_combinations, final_profits = shares_profits(all_combinations)
    # print(f"selected_combinations {selected_combinations}")

    final_result(selected_combinations, final_profits)


def load_data():
    """Retrieves and load the data from the CSV file."""
    shares_data = []

    with open("shares01.csv") as csvfile:
        shares_file = csv.reader(csvfile)

        for row in shares_file:
            shares_data.append((row[0], float(row[1]), float(row[2])))

    return shares_data


def shares_cost(combination):
    """Calculates the cost of every possible combination."""
    cost = []

    for share in combination:
        cost.append(share[1])

    return sum(cost)


def make_combinations(shares_data):
    """Makes all the combinations and keeps the ones
    of which their cost matches the budget."""
    final_list = []

    for elements in range(len(shares_data)):
        all_combinations = combinations(shares_data, elements)

        for combination in all_combinations:
            total_cost = shares_cost(combination)

            if total_cost <= BUDGET:
                final_list.append(combination)

    return final_list


def shares_profits(selected_list):
    """Calculates the total profits to return the final list."""
    final_profits = 0

    for share in selected_list:
        combination_profits = []
        for i in share:
            profits = i[1] * i[2] / 100
            combination_profits.append(profits)
            item_profits = sum(combination_profits)

            if final_profits < item_profits:
                final_profits = item_profits

                selected_shares = share

                # print(f"selected_share {selected_shares}")

    # print(f"Total profits: {final_profits}")
    # print(f"SHARES: {selected_shares}")

    return selected_shares, final_profits


def final_result(final_list, final_profits):
    """Displays the final results: shares with their respective info,
    total cost, profits made, time that the program took to run."""
    total_cost = 0

    # print(f"Final list: {final_list}")

    print(f"The best investment involves these {len(final_list)} shares:")

    for item in final_list:
        print(
            f"\tStock : {item[0]}, Price {item[1]}€, Profits over 2 years : {item[1] * item[2] / 100}€ ({item[2]}%)"
        )
        total_cost += item[1]

    print(f"\nIt would cost you {total_cost}€ and brings you {final_profits}€.")
    print(f"\nTime elapsed : {time.time() - start_time} seconds.")


if __name__ == "__main__":
    main()
