class Property:
    def __init__(self, income=0, cashflow=0, expenses=0, total_investment=0):
        self.income=income
        self.cashflow=cashflow
        self.expenses=expenses
        self.total_investment=total_investment
        self.roi=0
    def __str__(self):
        return f"Monthly Income: ${self.income}\nAnnual Cash Flow: ${self.cashflow}\nMonthly Expenses: ${self.expenses}\nCash on Cash Return on Investment: {self.roi}%"
    def monthly_income(self):
        self.income+=float(input("How much is this property's monthly rent?\n $"))
        self.income+=float(input("How much will the tenants pay for laundry?\n $"))
        self.income+=float(input("How much will the tenants pay you for storage services?\n $"))
        self.income+=float(input("How much miscellaneous income will you be recieving from the property per month? \n$"))
        print(f"Your total monthly income on this property is ${self.income}")
    def monthly_expenses(self):
        self.expenses+=float(input("How much will you be paying in property taxes per month? \n$"))
        self.expenses+=float(input("How much is insurance on the property per month? \n$"))
        self.expenses+=float(input("How much will you be paying for water and/or sewer services for the property per month? \n$"))
        self.expenses+=float(input("How much will you be paying for garbage services for the property per month? \n$"))
        self.expenses+=float(input("How much do you expect to pay for electricity per month on the property? \n$"))
        self.expenses+=float(input("How much will you be paying for gas on the property per month? \n$"))
        self.expenses+=float(input("How much will you be paying in HOA fees on the property per month? \n$"))
        self.expenses+=float(input("How much will you be paying for lawn care and/or snow removal services per month? \n$"))
        self.expenses+=float(input("How much do you expect the average monthly repair costs to be? \n$"))
        self.expenses+=float(input("How much will you be setting aside for capital expenditures per month? \n$"))
        self.expenses+=float(input("How much do you expect to pay in Property Management per month? \n$"))
        self.expenses+=float(input("How much is the mortgage on the property per month? \n$"))
        print(f"Your expected monthly expenses total up to ${self.expenses}")
    def annual_cash_flow(self):
        self.cashflow=(self.income-self.expenses)
        print(f"With a monthly income of ${self.income} and monthly expenses of ${self.expenses}, your monthly cash flow amounts to ${self.cashflow}")
        self.cashflow=self.cashflow*12
        print(f"Your annual cash flow totals up to ${self.cashflow}")
    def cash_on_cash(self):
        self.total_investment+=float(input("How much are you paying for your down payment? \n$"))
        self.total_investment+=float(input("What are the total closing costs? \n$"))
        self.total_investment+=float(input("What is your property Rehab Budget? \n$"))
        self.total_investment+=float(input("How much will you be paying for any other miscellaneous costs? \n$"))
        print(f"Your total initial investment is expected to be ${self.total_investment}")
        self.roi=(self.cashflow/self.total_investment)*100
        print(f"Your Cash on Cash Return on Investment will be {self.roi}%")