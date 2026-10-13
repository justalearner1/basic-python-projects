# This is the pay-up app

# "terminal.integrated.defaultProfile.windows": "Git Bash",

event = str(input("what was the event? "))
cost = float(input("How much did it cost? "))
service_charge = float(input("Enter the exact tip amount or service charge amount ")) * 10%
group_size = float(input("How many people were there? "))
grand_total = cost + service_charge
total_per_person = grand_total/group_size

print("Welcome to PayUp!")
print()
print(f"Here's the breakdown for {event}:")
print()
print(f"Cost : ${cost}")
print(f"Service charges : ${service_charge}")
print(f"Group size: ${group_size}")
print(f"Grand total : ${grand_total}")
print(f"Each person must pay up ${total_per_person}")

