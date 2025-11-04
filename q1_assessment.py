"""
Year 1 Python — Modular Assessment (Student Template)

INSTRUCTIONS
- Work in this single file. Each exercise has its own function: ex01() … ex14().
- Read the docstring under each function for the prompt, constraints, and tasks evaluated.
- Write your code where it says TODO. Do not delete the function headers or docstrings.
- Use descriptive variable names and add brief comments where useful.
- When finished, run the file and verify each exercise works as specified.
- Commit and push to a PUBLIC GitHub repo.

NOTE
- If an exercise asks for input, make your function handle that input and print the required output.
- Keep each exercise independent; do not rely on global state from other exercises.
"""

# ---------- Exercise 1 ----------


def ex01():
    """
    Exercise 1 — Basic I/O & Variables
    Prompt: Ask the user for their first name and their age. Print: "Hello, <name>! Next year you will be <age+1>."
    Constraints:
      - Use input() and print().
      - Convert age to int before adding.
    Evaluates tasks: 3, 4
    """
    # TODO: Implement per prompt
    username = input("Please enter your first name: ")
    user_age = int(input("Please enter your age: "))
    print(f"Hello {username}! Next year you will be {user_age+1}")
    pass
# ---------- Exercise 2 ----------


def ex02():
    """
    Exercise 2 — Arithmetic, Type Conversion, Rounding
    Prompt: Ask for a price (float) and a quantity (int). Compute subtotal, 6% tax, and total. Display each on its own line, rounded to two decimals.
    Constraints:
      - Use round(value, 2) for display.
      - Use only numeric operators (+ - * /).
    Evaluates tasks: 5, 6
    """
    # TODO: Implement per prompt
    price = float(input("Please enter the price: "))
    quantity = int(input("Please enter quantity: "))
    print(f"subtotal = {(price*quantity)}")
    print(f"Total after 6% tax {((price*quantity)*0.06 + (price*quantity)):.2f}")
    pass


# ---------- Exercise 3 ----------


def ex03():
    """
    Exercise 3 — String Methods & Formatting
    Prompt: Input a full name like "  aLeX JoRdan  ". Output lines for:
      - Cleaned full name in title case (no extra spaces)
      - First and last name with no leading or trailing spaces in UPPER CASE
      - Character count (excluding spaces)
    Constraints:
      - Use .strip(), .title(), .upper(), .replace() or similar.
      - Show counts using len().
    Evaluates tasks: 7, 8, 9
    """
    # TODO: Implement per prompt
    username = input("Enter full name: ")
    username = username.strip(" ").title()
    print(username)
    print(f"Length of Name: {len(username.strip().strip(" "))}")
    pass
# ---------- Exercise 4 ----------


def ex04():
    """
    Exercise 4 — Comparisons & Conditionals
    Prompt: Ask for a test score (0–100). Print a letter grade using standard bands (A/B/C/D/F)
            Bands: A = 93–100, B = 86–93, C = 78–85, D = 70–77, F = below 70.
    Constraints:
      - Use if/elif/else.
      - Validate that input is within 0–100; if not, print "Invalid".
    Evaluates tasks: 10, 17
    """
    # TODO: Implement per prompt
    user_test_score = int(input("Please enter your test score(0-100): "))
    if user_test_score > 100 or user_test_score < 0:
        print("Invalid")
    if user_test_score >= 93 and user_test_score <= 100:
        print("You got an A good job!")
    if user_test_score >= 86 and user_test_score <= 93:
        print("You got a B thats still pretty good!")
    if user_test_score >= 78 and user_test_score <= 85:
        print("You gat a C thats alright")
    if user_test_score >= 70 and user_test_score <= 77:
        print("Hey at least its not an F")
    if user_test_score < 70:
        print("Hey its okay to fail, it just means your learning just try harder next time.")
    pass

# ---------- Exercise 5 ----------


def ex05():
    """
    Exercise 5 — Logical Operators
    Prompt: Ask if the user has a ticket (y/n) and if they arrived on time (y/n).
            Rules:
              - ticket AND on time  -> "Admitted"
              - ticket AND NOT on time -> "Late check-in"
              - else -> "Denied"
    Constraints:
      - Use and, or, not with booleans derived from y/n.
    Evaluates tasks: 18
    """
    # TODO: Implement per prompt
    user_ticket = input("Do you have a ticket?(y/n): ").upper()
    time = input("Are you on time?(y/n): ").upper()
    if user_ticket == "Y" and time == "Y":
      print("Admitted")
      exit()
    if user_ticket == "Y" and time == "N":
      print("Late check-in")
    else:
      print("Denied")    
    pass
# ---------- Exercise 6 ----------


def ex06():
    """
    Exercise 6 — Input Validation with while
    Prompt: Keep asking for a positive integer until the user enters one. Then print "Thanks! You entered <n>."
    Constraints:
      - Must use a while loop for validation.
    Evaluates tasks: 19
    """
    # TODO: Implement per prompt
    num = -9999999
    while num < 0:
      if num < 0:
        num = int(input("Please enter a positive integer: "))
      if num >= 0:
          print(f"Thanks! you entered {num}")
    pass

# ---------- Exercise 7 ----------


def ex07():
    """
    Exercise 7 — Sentinel Loop & Aggregation
    Prompt: Repeatedly ask for item prices until the user enters 'q'.
            Print the number of items and the average price (2 decimals). If no items were entered, print "No data".
    Constraints:
      - Use a while + sentinel ('q').
      - Track count and sum.
      - 2 decimals can be printed with number:.2f
    Evaluates tasks: 6, 9 lol
    """
    # TODO: Implement per prompt
    user_item_list = [""]
    item_price_list = [""]
    user_item = ""
    while not(user_item == "q"):
      user_item = input("Please enter your items name(hit q to exit): ").lower()
      if user_item == "q":
        try:
          user_item_list.remove("")
          item_price_list.remove("")
          print(f"Average price {(all_item_total/len(item_price_list)):.2f}")
        except UnboundLocalError:
         print("No Data")
         exit()
        print(f"number of items {len(user_item_list)}")
        exit()
      item_price = float(input(f"Please enter the price of {user_item}: "))
      item_price_list.insert(0, item_price)
      all_item_total = 0
      all_item_total += item_price
      user_item_list.insert(0, user_item)


    pass
# ---------- Exercise 8 ----------

def ex08():
    """
    Exercise 8 — for + range
    Prompt: Ask for a positive integer n (≤ 20). Print the squares of 1..n.
    Constraints:
      - Use for in range(1, n+1).
      - If n is out of bounds (0 <= n <= 20) or not an integer (use try/except for ValueError or TypeError), print "Invalid".
      - Make sure to throw (raise the exception) if n is out of bounds or not a number
      - Print appropriate (different) messages based on the error
    Evaluates tasks: 29, 53
    """
    # TODO: Implement per prompt
    user_num = 0
    try:
        user_num = int(input("Please enter a positive number that is below 20: "))
        if not(0 <= user_num <= 20):
            print("out of bounds")
        for num in range(1, user_num + 1):
          print(user_num*num)
          
    except ValueError:
        print("thats not a number?")
    
    pass

# ---------- Exercise 9 ----------


def ex09():
    """
    Exercise 9 — Lists: Build, Index, Membership
    Prompt: Use a loop to have the user enter foods until they type 'q'. Then:
      - Store each food in a list (trim spaces).
      - After 'q', print: first item, last item, list length.
      - Ask for a query food and print whether it's in the list (case-insensitive).
    Constraints:
      - Use .strip(), 'in'.
    Evaluates tasks: 5, 8, 29
    """
    # TODO: Implement per prompt
    user_food_list = [""]
    while True:
      user_food = input("Please enter enter foods: ").lower().strip(" ")
      if user_food == "q":
        user_food_list.remove("")
        print(f"first food item {user_food_list[len(user_food_list)-1].title()}")
        print(f"Last food item {user_food_list[0].title()}")
        print(f"Langth of list {len(user_food_list)}")
        is_food = input("Please enter a food to see if its in your list: ").lower()
        try:  
          if is_food == (user_food_list).remove(is_food):
            print()
        except ValueError:
          print(f"No {is_food.title()} is in your list")
          exit()
        else:
           print(f"Yes {is_food.title()} is in your list")
           exit()
      user_food_list.insert(0, user_food)
    pass
# ---------- Exercise 10 ----------


def ex10():
    """
    Exercise 10 — Dictionaries: Simple Lookup
    Prompt: Create a dictionary of three state abbreviations to capitals (e.g., {"PA": "Harrisburg", ...}).
            Ask the user for a two-letter abbreviation (case-insensitive) and print the capital or "Unknown".
    Constraints:
      - Use dict literal, key normalization with .upper().
      - Use 'in' or .get().
    Evaluates tasks: 3, 7, 10
    """
    # TODO: Implement per prompt
    states = {
      "PA": "Harrisburg",
      "NV": "Carson City",
      "NY": "Albany"
    }
    user_ask = input("Please enter the abbreviation of a state: ").upper()
    if user_ask == "PA":
      print(states["PA"])
    if user_ask == "NV":
      print(states["NV"])
    if user_ask == "NY":
      print(states["NY"])
    else:
       print("Unknown")
    pass

# ---------- Exercise 12 ----------


def ex11():
    """
    Exercise 11 — Basic Error Handling (Try/Except)
    Prompt: Ask for two integers and print their quotient. If the user enters bad data or divides by zero,
            print a friendly error and re-prompt once.
    Constraints:
      - Use try/except (catch ValueError and ZeroDivisionError).
      - Only one retry needed.
    Evaluates tasks: 53
    """
    # TODO: Implement per prompt
    try:
      user_num1 = float(input("Please enter the first number so you can do division: "))
      user_num2 = float(input("Please enter the the second number so you can do division: "))
      print(f"{user_num1}/{user_num2} = {user_num1/user_num2}")
    except ValueError:
      print("Sorry you can't divide letters.")
    except ZeroDivisionError:
       print("Sorry but you can't divide by zero.")
    pass


def main():
    """Call exercises here. Comment out any you’re not ready to run yet."""
    # Uncomment exercises as you complete them:
    ex01()
    ex02()
    ex03()
    ex04()
    ex05()
    ex06()
    ex07()
    ex08()
    ex09()
    ex10()
    ex11()
    pass


if __name__ == "__main__":
    main()
