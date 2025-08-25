lebanese_food = [
  "Kibbeh",
  "Tabbouleh",
  "Hummus",
  "Pita"
]

def find_meal(name, menu):
  return name if name in menu else None

def select_meal(name):
  return find_meal(name, lebanese_food)

def display_available_meals():
  print("Available Lebanese Meals:")
  for meal in lebanese_food:
    print(meal)

def create_summary(name, amount):
  order = select_meal(name)
  if order:
    return f"You ordered {amount} {name}"
  else:
    return "Meal not found"

print("Welcome to the Dash Food Order System!")
print(" ")
display_available_meals()

print("")
name_input = input("Enter your meal choice: ")
amount_input = input("How many meals would you like: ")
 
result = create_summary(name_input,amount_input)
print(result)
