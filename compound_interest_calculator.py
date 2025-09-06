principle = 0
rate = 0
time = 0
compound = 0

while principle <= 0:
    principle = float(input("DEPOSIT SOME MONEY(AMOUNT): "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero")

while rate <= 0:
    rate = float(input("ENTER INTEREST RATE(in decimal, e.g., 10% → 0.10): "))
    if rate <= 0:
        print("Rate can't be less than or equal to zero")

while time <= 0:
    time = int(input("ENTER TIME IN YEARS: "))
    if time <= 0:
        print("Time can't be less than or equal to zero")

while compound <= 0:
    compound = int(input("ENTER NUMBER OF TIMES INTEREST IS COMPOUNDED PER YEAR: "))
    if time <= 0:
        print("Compound can't be less than or equal to zero")


final_amount = principle * pow((1+(rate/compound)),(compound*time))
compound_interest = final_amount - principle
print(f"Your Compound Interest will be: {round(compound_interest,2)}")
print(f"Your Final Amount will be: {round(final_amount,2)}")

