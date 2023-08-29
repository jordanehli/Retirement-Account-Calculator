#Author: Jordan Ehlinger
#Assignment Number & Name: HW3 Retirement Account
#Due Date: N/A
#Program Description: Calculate retirement account balances



##INPUT VALIDATION USING WHILE LOOPS
#while loop for annual savings input validation
annual_savings=-1 #intentional bad value
while annual_savings<0:
    annual_savings=input("Enter your annual savings: ")
    if annual_savings == "":
        annual_savings=-1 #intentional bad value
    else:
        annual_savings=float(annual_savings)
    if annual_savings<0:
        print("Error: Your annual savings must be a positive number.")

#while loop for starting year input validation
start_year=2010 #intentional bad value
while start_year<2020 or start_year>2100:
    start_year=input("Enter your desired starting year for saving: ")
    if start_year == "":
        start_year=2010 #intentional bad value
    else:
        start_year=int(start_year)
    if start_year<2020 or start_year>2100:
        print("Error: The starting year must be between 2020 - 2100.")

#while loop for ending year input validation
end_year=2010 #intentional bad value
while end_year<2020 or end_year>2100:
    end_year=input("Enter your desired final year for saving: ")
    if end_year == "":
        end_year=2010 #intentional bad value
    else:
        end_year=int(end_year)
    if end_year<2020 or end_year>2100 or end_year<start_year:
        print("Error: The final year must be between 2020 - 2100 and come the same year or after your starting year.")
        end_year=2010 #intentional bad value

#while loop for retirement year input validation
retire_year=2010 #intentional bad value
while retire_year<2020 or retire_year>2100:
    retire_year=input("Enter your desired retirement year: ")
    if retire_year == "":
        retire_year=2010 #intentional bad value
    else:
        retire_year=int(retire_year)
    if retire_year<2020 or retire_year>2100 or retire_year<end_year:
        print("Error: Your retirement year must be between 2020 - 2100 and come the same year or after your final savings year.")
        retire_year=2010 #intentional bad value
        
#while loop for interest rate input validation
interest_rate=-1 #intentional bad value
while interest_rate<1 or interest_rate>15:
    interest_rate=input("Enter the interest rate: ")
    if interest_rate == "":
        interest_rate=-1 #intentional bad value
    else:
        interest_rate=float(interest_rate)
    if interest_rate<1 or interest_rate>15:
        print("Error: The interest rate must be between 1 - 15.")
#convert interest rate to percentage
interest_rate=interest_rate/100



##DISPLAY TABLE HEADER
print(format("Year", "15"),end='')
print(format("Savings", "20"),end='')
print(format("Interest", "20"),end='')
print("Total")
print("------------------------------------------------------------")



##TABLE CALCULATIONS USING FOR LOOP
#initialize accumulator
total=0
interest=0
#for loop to calculate year, savings, interest, and total
for i in range(start_year,retire_year+1,1):
    if start_year<=end_year:
        additional_savings=annual_savings
    if start_year>end_year:
        additional_savings=0
    interest=(total+additional_savings)*interest_rate
    total+=(additional_savings+interest)
    #print table contents and space them properly
    print(format(start_year, "d"),format(additional_savings, "17,.0f"),format(interest, "20,.0f"),format(total, "16,.0f"))
    #increase year in table
    start_year+=1
