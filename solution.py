print("Car Service")

services = ["Wash", "Repair", "Paint"]
price = [500, 2000, 3000]

service = input("Enter service: ")
qty = int(input("Enter quantity: "))

index = services.index(service)
total = price[index] * qty

if total > 3000:
    discount = total * 0.1
else:
    discount = 0

final_amount = total - discount

print("Service:", service)
print("Total:", total)
print("Discount:", discount)
print("Final Amount:", final_amount)

for i in range(3):
    print("Booked")

print("End")