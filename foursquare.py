from property import Property

def foursquare():
    prop=Property()
    print("Welcome to the Four Square Calculation Program!\nThis program will use Bigger Pockets\' Four Square method to calculate your ROI percentage.\n We will begin this process by calculating your total monthly income.")
    prop.monthly_income()
    print("Okay, now we will add up all of your monthly expenses on the property.")
    prop.monthly_expenses()
    print("Using your monthly income and expenses, we will now show your monthly and annual cash flow.")
    prop.annual_cash_flow()
    print("We will now determine your total initial investment, and from that your Cash On Cash Return On Investment.")
    prop.cash_on_cash()
    print("Thank you for using the Four Square Calculator!")
foursquare()