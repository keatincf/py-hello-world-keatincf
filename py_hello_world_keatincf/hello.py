from py_hello_world_keatincf.operations import sum


def main():
    """
    Main functionality for Hello World.  Calculates some sums and prints out the results along with a Hello World message
    """
    print(f"Hello World!\n{sum.sum()}")
    print(f"Hello World!\n{sum.squared_sum()}")


if __name__ == "__main__":
    main()
