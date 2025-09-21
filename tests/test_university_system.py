def get_second_largest():
    numbers = []
    try:
        print("Enter exactly 5 integers:")
        for i in range(5):
            try:
                num = int(input(f"Enter number {i + 1}: "))
                numbers.append(num)
            except ValueError:
                print("❌ Invalid input! Please enter an integer.")
                return
        if len(set(numbers)) < 2:
            raise IndexError("❌ Need at least 2 unique numbers to find the second largest.")

        numbers = list(set(numbers))  # remove duplicates
        numbers.sort(reverse=True)
        print("Second largest number is:", numbers[1])

    except IndexError as e:
        print(e)
    except KeyboardInterrupt:
        print("\n⚠️ Program interrupted by user. Exiting gracefully.")


if __name__ == "__main__":
    get_second_largest()
