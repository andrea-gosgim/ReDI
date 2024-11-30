#Here I'll try stuff and modify the code. Only the most recent and working code will remain.

class Category:
    def __init__(self, name, max_allowed_spending,spending_limit_for_alert):
        self.name = name
        self.max_allowed_spending = max_allowed_spending
        self.spending_limit_for_alert = spending_limit_for_alert
        # TODO: change this so the amount spent can be updated when accessed in the dictionary
        self.amount_spent = 0

    def track_amount_spent(self, new_amount):
        self.amount_spent += new_amount
        if self.amount_spent > self.max_allowed_spending:
            print(f"Watch out! Your expenses went over your maximum allowed spending limit for your '{self.name}' category.")

    def get_category_info(self):
        return f"Category's name: '{self.name}'. Maximum allowed spending: {self.max_allowed_spending} €.\n Spending limit alert at: {self.spending_limit_for_alert} €. Amount spent: {self.amount_spent} € \n"

#INFO#this stays#I created the class <Budget> to store the different categories
class Budget:
    def __init__(self):
        self.budget = {}

    def add_category(self, category):
        self.budget[category.name] = category

    def display_info_budget(self): #it will display everything in the budget
        if self.budget:
            print("Categories in your budget: ")
            for name, category in self.budget.items():
                print(category.get_category_info())
        else:
            print("You haven't any categories.")

    def get_info_category(self, name):  #to get the category's info by the name
        if name in self.budget:
            print(self.budget[name].get_category_info())
        else:
            print(f"There is no category named '{name}'")

    def track_expense(self, category_name_containing_expense, expense_amount):
        # access the category
        if category_name_containing_expense in self.budget:
            self.budget[category_name_containing_expense].track_amount_spent(expense_amount)

        else:
            print(f"There is no category named '{category_name_containing_expense}'.")
        # add that amount to the existing amount_spent


def set_categories(budget_input):
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

def search_category(budget_input):
    while True:
        category_name_search = input("Enter the name of the category you want to check(type 'stop' if you are done): ")

        if category_name_search.lower() == "stop":
            print("You typed 'stop', you're done with checking categories!")
            break
        else:
            budget_input.get_info_category(category_name_search)

def set_categories_for_testing(budget):
    category1 = Category("groceries", 45, 10)
    category2 = Category("test_category", 45, 10)
    budget.add_category(category1)
    budget.add_category(category2)


if __name__ == "__main__":
    budget = Budget()
    # set_categories(budget)
    print("Set categories for testing:")
    set_categories_for_testing(budget)
    # search_category(budget)
    print("Track expenses 'groceries'")
    budget.track_expense("groceries", 20)
    print("Track expenses 'test_category'")
    budget.track_expense("test_category", 4500)
    print("Display info budget")
    budget.display_info_budget()

# budget.update_budget(name)

#Info for me#doesn't stay
#always need the name and something else (to track smtg)
#Class is a template (cookie cutter), objet (=category1) (cookie)
#define an objet based on the data user gives me
#class tells you the data and functionalty (methods)
#class == saying there is a value x
#data from arguments in the constructor




#THINGS TO DO
#DONE create a method to store the categories in budget in a dictionary
#DONE MÁS O MENOS to track an expense, use dictionary to connect key:name of category. value: object itself(category itself)
#DONE figure out how I'm going to get the data (input with name, max and alert) [Create an object of the class category]
#extend my budget class
#think about other things the user will give me and create corresponding functions in budget
#DONE modify class Category
# See how to access the each category's attribute


#ADD TO THINGS TO IMPROVE: YOU'VE ALREADY HAVE THAT NAME, BE ABLE TO LOOK FOR EACH DETAIL IN EACH CATEGORY
#make it a float
#make it so it gets an error if it's not an integer (max, alert, spent)