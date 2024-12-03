from budget import Category, Budget


def set_categories_from_user_input(budget_input):
    print("Here you can set different categories for your budget. \n NOTE: If you want to re-set a category, type its name again and the new values for it.")
    while True:
        name = input("Enter your new category's name (enter 'stop' if you are done): ")

        if name.lower() == "stop":
            print("You typed 'stop', you're done with entering categories!")
            budget_input.display_info_budget()
            break

        else:
            max_allowed_spending = int(input(f"Enter the maximum amount of money you want to spend in the '{name}' category (€): "))
            spending_limit_for_alert = int(input(f"Enter when do you want to get an alert (spending limit) for the '{name}' category(€): "))

            category = Category(name, max_allowed_spending, spending_limit_for_alert)
            budget_input.add_category(category)

def search_category_from_user_input(budget_input):
    while True:
        category_name_key = input("Enter the name of the category you want to check(type 'stop' if you are done): ")

        if category_name_key.lower() == "stop":
            print("You typed 'stop', you're done with checking categories!")
            break
        else:
            budget_input.get_info_category(category_name_key)

def track_expenses_from_user_input (budget_input):
    while True:
        category_name_key = input("Enter the name of the category you want to update the amount spent from (type 'stop' if you are done): ")

        if category_name_key.lower() == "stop":
            print("You typed 'stop', you're done adding expenses!")
            break
        else:
            expense_amount = int(input(f"Enter the amount you spent in your '{category_name_key}' category (it has to be an integer): "))
            budget_input.track_expense(category_name_key, expense_amount)

if __name__ == "__main__":
    budget = Budget()
    set_categories_from_user_input(budget)
    search_category_from_user_input(budget)
    track_expenses_from_user_input(budget)
    budget.display_info_budget()
