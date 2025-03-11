import random

def flip_coin():
    return random.choice(["Heads", "Tails"])

def multiple_tosses(num_flips):
    results = {"Heads": 0, "Tails": 0}
    
    for _ in range(num_flips):
        result = flip_coin()
        results[result] += 1
        print(result)  # Display each flip result
    
    return results

def display_results(results, num_flips):
    print("\nFinal Results:")
    for outcome, count in results.items():
        percentage = (count / num_flips) * 100
        print(f"{outcome}: {count} times ({percentage:.2f}%)")

def main():
    while True:
        try:
            num_flips = int(input("Enter the number of times to flip the coin: "))
            if num_flips <= 0:
                print("Please enter a positive integer.")
                continue

            results = multiple_tosses(num_flips)
            display_results(results, num_flips)

            # Ask user if they want to play again
            choice = input("\nDo you want to flip again? (yes/no): ").strip().lower()
            if choice != "yes":
                print("Thank you for using the Virtual Coin Toss Simulator!")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
