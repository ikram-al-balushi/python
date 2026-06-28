# Prices
bun_price = 150
fries_price = 120
chai_price = 50

# Quantities (numbers likhein)
bun = int(input("BunKabab qty: "))
fries = int(input("Fries qty: "))
chai = int(input("Chai qty: "))

# Basic check: negative qty mana
if bun < 0 or fries < 0 or chai < 0:
    print("Error: Quantity negative nahi ho sakti.")
else:
    # Hisaab
    subtotal = bun*bun_price + fries*fries_price + chai*chai_price

    # Discount (10% jab subtotal 500 ya zyada ho)
    if subtotal >= 500:
        discount = subtotal * 0.10
    else:
        discount = 0

    grand_total = subtotal - discount

    # Output
    print("Subtotal:", subtotal)
    print("Discount:", round(discount, 2))
    print("Grand Total:", round(grand_total, 2))









# Inputs
total = int(input("Total classes: "))
attended = int(input("Attended classes: "))

# Basic checks
if total <= 0:
    print("Error: Total classes 0 se bari honi chahiye.")
elif attended < 0 or attended > total:
    print("Error: Attended classes 0 se chhoti ya total se zyada nahi ho sakti.")
else:
    # Percentage
    percent = (attended / total) * 100

    # Message
    if percent >= 90:
        status = "Excellent"
    elif percent >= 75:
        status = "Allowed in exam"
    else:
        status = "Short attendance"

    # Output
    print("Attendance %:", round(percent, 1))
    print("Status:", status)