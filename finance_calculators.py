import math

user_wants_investment = ("INVESTMENT")
user_wants_bond = ("BOND")
user_choice_investment_or_bond = input(f"""\nChoose either '{user_wants_investment}' or '{user_wants_bond}' from the menu below to proceed:\n 
\v  Investment - to calculate the amount of interest that you will earn on your investment
\v  Bond       - to calculate the amount you will have to pay on your home loan\v
  Type in your choice here : """)
user_choice_investment_or_bond = user_choice_investment_or_bond.lower()

if user_choice_investment_or_bond == "investment" :
    print("\vThank you choosing the INVESTMENT calculaton")
elif user_choice_investment_or_bond == "bond" :
    print("\vThank you choosing the BOND calculaton")
else :
    print("\v !!ISSUE ENCOUNTERED!! You may have mistyped your selection. Please restart the program and try again. Please check your spelling of INVESTMENT or BOND.")

if user_choice_investment_or_bond == "investment" :
    
    investment_amount = input("\vHow much of your money would you like to invest : ")
    investment_amount = float(investment_amount)

    investment_interest_rate = input("\vHow much interest are you recieving on your investment :  ")
    investment_interest_rate = float(investment_interest_rate)
    
    investment_length = input("\vHow many years would you like to invest for : ")
    investment_length = float(investment_length)

    investment_interest_simple = ("SIMPLE")
    investment_interest_compound = ("COMPOUND")
    investment_choice_simple_or_compound = input(f"\vWould you like {investment_interest_simple} OR {investment_interest_compound} interest :  ")
    investment_choice_simple_or_compound = investment_choice_simple_or_compound.lower()
    
    interest = str()
    if investment_choice_simple_or_compound == "simple" :
        interest = "simple"    
    if investment_choice_simple_or_compound == "compound" :
        interest = "compound"
   
    #  A = P*(1 + r*t)

    if interest == "simple" :
       
        investment_interest_payout = (investment_amount) * (1 + (investment_interest_rate) * (investment_length))
        investment_interest_payout = float(investment_interest_payout)
        investment_interest_payout = round(investment_interest_payout, 2)
        print(f"\nThis is the amount you should receive at the end of your INVESTMENT : R {investment_interest_payout} with SIMPLE interest \n")

    # A = P * math.pow((1+r),t)

    elif interest == "compound" :
        
        investment_interest_payout = (investment_amount) * math.pow((1 + investment_interest_rate), investment_length)
        investment_interest_payout = float(investment_interest_payout)
        investment_interest_payout = round(investment_interest_payout, 2)
        print(f"\vThis is the amount you should receive at the end of your INVESTMENT : R {investment_interest_payout} with COMPOUND interest \n")

if user_choice_investment_or_bond == "bond" :
            
            bond_amount = input("\vHow much would you like to borrow for your house : ")
            bond_amount = float(bond_amount)       
            
            bond_interest_rate = input("\vHow much is the annual interest rate on your bond :  ")
            bond_interest_rate = float(bond_interest_rate)   

            bond_loan_length = input("\vOver how many months do you wish to borrow : ")
            bond_loan_length = float(bond_loan_length)

# repayment = (i * P)/(1 - (1 + i)**(-n))

            P = bond_amount
            i = ((bond_interest_rate/12)/100)
            n = bond_loan_length
            

            bond_monthly_repayment = (i*P)/(1-(1 + i)**(-n))

            bond_monthly_repayment = round(bond_monthly_repayment, 2)

            print((f"\nThis is the amount you repay per month for the BOND : {bond_monthly_repayment} \n"))