# This is the pay-up app

# "terminal.integrated.defaultProfile.windows": "Git Bash",
print("Welcome to PayUp!")

event = str(input("what was the event? "))
cost = float(input("How much did it cost? "))
service_charge = int(input("Enter the exact tip amount or service charge amount in whole numbers (e.g 20 for 20%) ").strip("%")) 
service_charge_total = (service_charge /100) * cost
group_size = int(input("How many people were there? "))
grand_total = cost + service_charge_total
total_per_person = grand_total/group_size


print()
print(f"Here's the breakdown for {event}:")
print()
print(f"Cost : ${cost}")
print(f"Service charges : ${service_charge}")
print(f"Group size: ${group_size}")
print(f"Grand total : ${grand_total}")
print(f"Each person must pay up ${total_per_person:.2f}")

