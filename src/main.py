#!/usr/bin/env python3

# represent fixed interest growth
# based on formula: principal * ((1 + rate) ^ years)
def fixedInvestor(principal, rate, years):
    balance = principal
    
    for i in range(years):
        # multiply balance by 1 + rate n years times
        balance *= (1 + rate)
        
    return balance

# calculate compound rate using variable rate per year
def variableInvestor(principal, rateList):
    balance = principal
    
    for rate in rateList:
        balance *= (1 + rate)
        
    return balance

def finallyRetired(balance, expense, rate):
    years = 0
    current_balance = balance
    # safety limit to prevent infinite loops if interest > expense
    while current_balance > 0 and years < 100:
        # add interest
        interest = current_balance * rate
        current_balance += interest
        current_balance -= expense
        years += 1
    return years

def maximumExpensed(balance, rate):
    #Task 4: Use Binary Search to find max sustainable withdrawal.
    years = 30 # assume they retire for 30 years
    low = 0.0
    optimal_withdrawal = 0.0
    high = fixedInvestor(balance, rate, years)

    # Binary Search
    while high - low > 0:
        mid = (low + high) / 2
        temp_balance = balance
        possible = True
        
        for _ in range(int(years)):
            temp_balance += temp_balance * rate
            temp_balance -= mid
            if temp_balance < 0:
                possible = False
                break
            
        if possible and temp_balance >= 0:
            optimal_withdrawal = mid
            low = mid 
        else:
            # ran out of money
            high = mid

        return optimal_withdrawal

if __name__ == "__main__":
    while True:
        print("1. Fixed Growth Simulation")
        print("2. Variable Growth Simulation")
        print("3. Retirement Depletion Simulation")
        print("4. Optimize Withdrawal (Binary Search)")
        print("5. Exit")
        
        try:
            choice = input("Select an option (1-5): ")
            
            match choice:
                case '1':
                    principal = float(input("Enter Principal ($): "))
                    rate = float(input("Enter Interest Rate (e.g 0.03): "))
                    years = int(input("Enter Number of Years: "))
                    # cannot have a negative starting amount and cannot progress by negative years
                    if (principal < 0 or years <= 0):
                        raise ValueError
                    
                    result = fixedInvestor(principal, rate, years)
                    print(f"Balance: ${result:.2f}")
                case '2':
                    principal = float(input("Enter Principal Amount: ($)"))
                    years = int(input("How many years of variable rates? "))
                    rates = []
                    
                    if (principal < 0 or years <= 0):
                        raise ValueError
                    
                    for i in range(years):
                        rate = float(input(f"Enter rate for year {i + 1} (e.g 0.03): "))
                        rates.append(r)
                    result = variableInvestor(principal, rates)
                    print(f"Balance: ${result:.2f}")
                case '3':
                    balance = float(input("Enter Retirement Balance: ($)"))
                    expense = float(input("Enter Annual Expense/Withdrawal: ($)"))
                    rate = float(input("Enter Expected Interest Rate (e.g 0.03): "))
                    result = finallyRetired(balance, expense, rate)
                    
                    print(f"Funds will last for approximately {result} years.")
                case '4':
                    balance = float(input("Enter Retirement Balance: ($)"))
                    rate = float(input("Enter Expected Interest Rate (decimal): "))
                    #years = input("Enter Expected Years in Retirement (leave blank for default of 20): ")
                    
                    result = maximumExpensed(balance, rate)
                    
                    print(f"Optimal Annual Withdrawal over : ${result:.2f}")
                    print(f"(This reduces balance to near zero after 30 years)")
                case '5':
                    print("Exiting...")
                    break
                case _:
                    print("Invalid selection. Try again.")
        except ValueError:
            print("Invalid input")
        except:
            print("An unknown error occurred")
