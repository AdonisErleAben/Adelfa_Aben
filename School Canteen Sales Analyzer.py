def get_total_sales(num_items):
    total_sales = 0.0
    meeting_target = 0
    below_target = 0

    for i in range(1, num_items + 1):
        sales = float(input(f"Enter sales for item {i}: "))
        total_sales += sales

        if sales >= 500.00:
            meeting_target += 1
        else:
            below_target += 1

    return total_sales, meeting_target, below_target


def calculate_average(total_sales, number_of_items):


    if number_of_items == 0:
        return 0.0
    return total_sales / number_of_items


def main():

    num_items = int(input("Enter number of food items: "))


    total, meeting, below = get_total_sales(num_items)


    avg_sales = calculate_average(total, num_items)


    print("\nCANTEEN SALES REPORT")
    print(f"Average Sales: PHP {avg_sales:.2f} | Meeting Target: {meeting} | Below Target: {below}")

main()
