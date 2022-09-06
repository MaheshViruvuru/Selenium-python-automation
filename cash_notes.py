from math import floor

cash_amount = int(input("Enter amount: "))

notes = [1000, 500, 100, 50, 20, 5, 1]
for i in notes:
    no_of_notes = floor(cash_amount/i)
    print(f"Number of {i} notes is :{no_of_notes}")
    cash_amount = cash_amount - no_of_notes * i
