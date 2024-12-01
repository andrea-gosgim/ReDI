class Category:
    def __init__(self, name, max_allowed_spending,spending_limit_for_alert):
        self.name = name
        self.max_allowed_spending = max_allowed_spending
        self.spending_limit_for_alert = spending_limit_for_alert
        self.amount_spent = 0

    def track_amount_spent(self, new_amount):
        self.amount_spent += new_amount
        return self.amount_spent <= self.max_allowed_spending

    def get_category_info(self):
        return f"Category's name: '{self.name}'. Maximum allowed spending: {self.max_allowed_spending} €.\n Spending limit alert at: {self.spending_limit_for_alert} €. Amount spent: {self.amount_spent} € \n"

#INFO: I created the class <Budget> to store the different categories
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
        if category_name_containing_expense in self.budget:
            is_within_allowed_spending = self.budget[category_name_containing_expense].track_amount_spent(expense_amount)
            if not is_within_allowed_spending:
                print(f"Watch out! Your expenses went over your maximum allowed spending limit for your '{category_name_containing_expense}' category.")

        else:
            print(f"There is no category named '{category_name_containing_expense}'.")