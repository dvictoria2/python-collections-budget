
from . import Expense

# Class that extends list type
class BudgetList():
    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []
    
    def __len__(self):
        return (len(self.expenses) + len(self.overages))

    # implement append so that it only appends to self if total < budget
    def append(self, item):
        # TODO Check if item is a number
        if (self.sum_expenses+item < self.budget):
            self.expenses.append(item)
            self.sum_expenses += item
        # Otherwise append to the overages list and add to the overage total
        else:
            self.overages.append(item)
            self.sum_overages+=item


