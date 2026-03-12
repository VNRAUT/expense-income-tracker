class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category):
        self.expenses.append({'amount': amount, 'category': category})

    def total_expenses(self):
        return sum(expense['amount'] for expense in self.expenses)

    def get_expenses(self):
        return self.expenses

    def get_expenses_by_category(self, category):
        return [expense for expense in self.expenses if expense['category'] == category]