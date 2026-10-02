budget = 300.0

name = input("What's your name?: ")
# print(f"\n ****** (name) - value: {name}, type: {type(name)}\n")

service_name = input("What's your streaming service?: ")
# print(f"\n ****** (service_name) - value: {service_name}, type: {type(service_name)}\n")

service_price = float(input("What's your streaming service price?: "))
# print(f"\n ****** (service_price) - value: {service_price}, type: {type(service_price)}\n")

months = int(input("How many months?: "))
# print(f"\n ****** (service_price) - value: {service_price}, type: {type(service_price)}\n")

total = service_price * months

# print(f"\n ****** (total) - value: {total}, type: {type(total)}\n")

is_over_budget = total > budget
# print(f"\n ****** (is_over_budget) - value: {is_over_budget}, type: {type(is_over_budget)}\n")

print()
print("===========\t=======")
print(f"{name}'s Report")
print("╚══════════════════════════════╝")
print(f"Service Name:{service_name}: ${service_price}/mo")
print("\t=================")
print(f"Total over {months}: ${total:.5f}")
print(f"Over {budget}?: {is_over_budget}")
print("==================")
