def calculate_tax(filing_status, income):
    brackets = {
        0: [  # Single
            (8350, 0.10),
            (33950, 0.15),
            (82250, 0.25),
            (171550, 0.28),
            (372950, 0.33),
            (float('inf'), 0.35)
        ],
        1: [  # Married filing jointly or widow(er)
            (16700, 0.10),
            (67900, 0.15),
            (137050, 0.25),
            (208850, 0.28),
            (372950, 0.33),
            (float('inf'), 0.35)
        ],
        2: [  # Married filing separately
            (8350, 0.10),
            (33950, 0.15),
            (68525, 0.25),
            (104425, 0.28),
            (186475, 0.33),
            (float('inf'), 0.35)
        ],
        3: [  # Head of household
            (11950, 0.10),
            (45500, 0.15),
            (117450, 0.25),
            (190200, 0.28),
            (372950, 0.33),
            (float('inf'), 0.35)
        ]
    }
    limits = {
        0: [8350, 33950, 82250, 171550, 372950],
        1: [16700, 67900, 137050, 208850, 372950],
        2: [8350, 33950, 68525, 104425, 186475],
        3: [11950, 45500, 117450, 190200, 372950]
    }

    total_tax = 0
    prev_limit = 0

    for limit, rate in zip(limits[filing_status], [brackets[filing_status][j][1] for j in range(5)]):
        if income > limit:
            taxable_chunk = limit - prev_limit
            total_tax += taxable_chunk * rate
            prev_limit = limit
        else:
            taxable_chunk = income - prev_limit
            total_tax += taxable_chunk * rate
            break
    return total_tax

def main():
    print("Choose your filing status:")
    print("0 - Single")
    print("1 - Married filing jointly or widow(er)")
    print("2 - Married filing separately")
    print("3 - Head of household")
    try:
        status_input = int(input("Enter number (0-3): "))
        if status_input not in [0, 1, 2, 3]:
            print("Oops! That's not a valid option.")
            return
        income_input = float(input("Enter your taxable income: "))
        if income_input < 0:
            print("Income can't be negative.")
            return
        tax_due = calculate_tax(status_input, income_input)
        print(f"\nBased on that, your tax is: ${tax_due:,.2f}")
    except ValueError:
        print("Hmm, please make sure to enter valid numbers.")

if __name__ == "__main__":
    main()