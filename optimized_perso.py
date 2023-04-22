import time
import csv
from itertools import combinations
import os
import psutil


BUDGET = 500


def main():
    """Main function launched at the start of the program."""
    file = pick_a_file()
    start_time, shares_data = load_data(file)

    good_shares = removebadshares(shares_data)

    final_list, total_cost, total_profits, profits_ratio = getbestshares(good_shares)

    final_result(start_time, final_list, total_cost, total_profits, profits_ratio)


def pick_a_file():
    while True:
        print("Choose which file you would like to use:")
        print("1. 20 shares")
        print("2. 1000 shares - File 1")
        print("3. 1000 shares - File 2")
        print("4. Extra file - File 1 and 2 merged together: 2000 shares")
        print("\n0. Exit the program")
        chosen_file = input("\nYour choice (1, 2, 3, 4 or 0): ")

        if chosen_file == "1":
            return "data_files/shares01.csv"

        if chosen_file == "2":
            return "data_files/dataset1_Python+P7.csv"

        if chosen_file == "3":
            return "data_files/dataset2_Python+P7.csv"

        if chosen_file == "4":
            return "data_files/dataset3_Python+P7.csv"

        if chosen_file == "0":
            exit()


def load_data(file):
    """Retrieves and load the data from the CSV file."""
    start_time = time.time()
    print("* " * 25)
    print(f"LOADED FILE: {file[11:]}")

    shares_data = []

    # with open("dataset1_Python+P7.csv") as csvfile:
    with open(file) as csvfile:
        shares_file = csv.reader(csvfile)

        for row in shares_file:
            try:
                shares_data.append((row[0], float(row[1]), float(row[2])))
            except ValueError:
                pass

    return start_time, shares_data


def removebadshares(shares):
    shares_to_keep = []
    for share in shares:
        if share[1] > 0 and share[2] > 0:
            shares_to_keep.append(share)

    return shares_to_keep


def getbestshares(shares):
    """Get the best shares in two different lists:
    Those with the best base profits (column 2)
    Those with the best final profits (math)"""
    budget_base = BUDGET
    budget_profits = BUDGET + BUDGET / 10

    best_base_profits = []

    shares.sort(key=lambda x: x[2], reverse=True)
    for share in shares:
        if 3 <= share[1] <= budget_base:
            best_base_profits.append(share)
            budget_base -= share[1]

    shares.sort(key=lambda x: x[1] * x[2] / 100, reverse=True)
    for share in shares:
        if 3 <= share[1] <= budget_profits and share not in best_base_profits:
            best_base_profits.append(share)
            budget_profits -= share[1]

    best_base_profits.sort(key=lambda x: x[2], reverse=True)
    total_cost = 0
    total_profits = 0
    final_list = []

    for share in best_base_profits:
        if total_cost <= BUDGET and share[1] + total_cost <= BUDGET:
            final_list.append(share)
            total_cost += share[1]
            total_profits += share[1] * share[2] / 100

    profits_ratio = total_profits * 100 / total_cost

    return final_list, total_cost, total_profits, profits_ratio


def final_result(start_time, final_list, total_cost, total_profits, profits_ratio):
    """Displays the final results: shares with their respective info,
    total cost, profits made, time that the program took to run."""

    print("* " * 25)
    print(f"The best investment involves these {len(final_list)} shares:")

    for share in final_list:
        print(
            f"\tStock : {share[0]}, Price {share[1]}€, Profits over 2 years : {share[1] * share[2] / 100}€ ({share[2]}%)"
        )

    print(
        f"\nIt would cost you {round(total_cost, 2)}€ and return you {round(total_profits, 2)}€."
    )
    print(f"Final profits: {round(profits_ratio, 2)}% of your original investment.")
    print(f"\nTime elapsed : {round((time.time() - start_time), 6)} seconds.")

    print(
        f"\nRAM used by the program: {round((psutil.Process(os.getpid()).memory_info().rss / (1024 ** 2)), 3)} MB"
    )


if __name__ == "__main__":
    main()
