import time
import csv
import os
import psutil
from tqdm import tqdm

BUDGET = 500


def main():
    """Main function launched at the start of the program."""
    file = pick_a_file()
    global DIVIDER
    if "shares01" in str(file):
        DIVIDER = 1
    else:
        DIVIDER = 100
    start_time, shares_data = load_data(file)

    selected_combinations = knapsack(BUDGET * DIVIDER, shares_data)

    final_result(start_time, selected_combinations)


def pick_a_file():
    """Menu to choose the file the user wants to load."""
    while True:
        print("Choose which file you would like to use:")
        print("1. 20 shares")
        print("2. 1000 shares - File 1")
        print("3. 1000 shares - File 2")
        print("4. Extra file - File 1 and 2 merged together: 2000 shares")
        print("\n0. Exit the program")
        chosen_file = input("\nYour choice (1, 2, 3, 4, or 0): ")

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
    """Retrieves and loads the data from the CSV file."""
    start_time = time.time()
    print("* " * 25)
    print(f"LOADED FILE: {file[11:]}")

    shares_data = []
    numofshares = 0

    with open(file) as csvfile:
        shares_file = csv.reader(csvfile)

        for row in shares_file:
            numofshares += 1
            try:
                if float(row[1]) > 0.1 and float(row[2]) > 0.1:
                    shares_data.append(
                        (
                            row[0],
                            int(float(row[1]) * DIVIDER),
                            (float(row[1]) * float(row[2]) / 100),
                        )
                    )
                    # print(shares_data)
            except ValueError:
                pass

    print(f"Number of shares: {numofshares}")
    return start_time, shares_data


def knapsack(budget, shares):
    """knapsack alogorithm"""
    # The share's cost (share_cost) CANNOT be a float as it is used
    # as an index for the table (or else "TypeError").

    print(f"* * * BUDGET: {budget}")

    share_cost = []
    share_profits = []

    for share in shares:
        share_cost.append(share[1])
        share_profits.append(share[2])

    num_of_shares = len(shares)
    print(f"* * * Number of USABLE shares: {num_of_shares}")

    table = [[0 for x in range(budget + 1)] for x in range(num_of_shares + 1)]

    for i in tqdm(range(1, num_of_shares + 1)):
        for j in range(1, budget + 1):
            if share_cost[i - 1] <= j:
                table[i][j] = max(
                    share_profits[i - 1] + table[i - 1][j - share_cost[i - 1]],
                    table[i - 1][j],
                )

            else:
                table[i][j] = table[i - 1][j]

    selected_shares = []

    while budget >= 0 and num_of_shares >= 0:
        share = shares[num_of_shares - 1]
        if (
            table[num_of_shares][budget]
            == table[num_of_shares - 1][budget - share[1]] + share[2]
        ):
            selected_shares.append(share)
            budget -= share[1]
        num_of_shares -= 1

    return selected_shares


def final_result(start_time, selected_shares):
    """Displays the final results: shares with their respective info,
    total cost, profits made, time that the program took to run."""
    total_cost = round(sum([share[1] for share in selected_shares]) / DIVIDER, 2)
    final_profits = round((sum(share[2] for share in selected_shares)), 2)

    print(f"The best investment involves these {len(selected_shares)} shares:")

    sharenumber = 1

    for share in selected_shares:
        print(
            f"\t Share {sharenumber}: {share[0]} | Price: {share[1] / DIVIDER}€ | Profits over 2 years : {round(share[2], 3)}€ ({round(((share[2]*100 * DIVIDER) / share[1]), 2)}%)"
        )
        sharenumber += 1

    print(
        f"\nIt would cost you {round(total_cost, 2)}€ and return you {round(final_profits, 2)}€."
    )
    print(
        f"Final profits: {round(((final_profits*100)/total_cost), 2)}% of your original investment."
    )
    print(f"\nTime elapsed : {round((time.time() - start_time), 6)} seconds.")

    print(
        f"\nRAM used by the program: {round((psutil.Process(os.getpid()).memory_info().rss / (1024 ** 2)), 3)} MB"
    )


if __name__ == "__main__":
    main()
