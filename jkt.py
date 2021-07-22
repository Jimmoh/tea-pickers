def main():
    print("Enter Tea-Pickers name")
    name = input()
    print("Enter Tea-Picker type (new or old)")
    p_type = input()
    print("number of kilos!")
    kilos = float(input())
    wage = kilos * 7
    bonus = (kilos-9)*4 if kilos > 9 else 0
    allowance_p = 110 if p_type == "old" else 75 if p_type == "new" else 0
    total = wage + allowance_p + bonus
    print(f"The total kilos for {name} are: {kilos}, and the total pay is {total}")


if __name__ == "__main__":
    main()

