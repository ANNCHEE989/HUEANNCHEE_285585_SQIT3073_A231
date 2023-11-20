import os
os.system ('cls')

#check eligibility
def check_eligible(dsr,threshold): 
    if dsr < threshold:
         return "Yes"
    else:
         return "No"
    
#display calcultions
def display_calculations(calculations): 
    print("Previous Calculations:")
    for i, calculation in enumerate(calculations, start=1):
        print(f"{i}")
        for j,k in calculation.items():
             print(f"{j}:{k}")
        print()

#delete calculation
def delete_calculation(calculations): 
    display_calculations(calculations)
    index = int(input("Enter the number of the calculation to delete: ")) - 1
    if 0 <= index < len(calculations):
            del calculations[index]
            print("Calculation deleted successfully.")
    else:
            print("Invalid calculation number.")
    
#modify threshold
def modify_dsr_threshold(): 
    global dsr_threshold
    dsr_threshold = float(input("Enter the new DSR threshold: "))
    print("DSR threshold modified successfully.")
    return dsr_threshold

save_calculations = []

#main menu 
def main(): 
    global dsr_threshold
    dsr_threshold = 70
    while True:
        print("Loan Eligibility Calculator")
        print("1. Calculate a New Loan")
        print("2. Display Previous Loan Calculations")
        print("3. Delete a Previous Calculation")
        print("4. Modify DSR Threshold")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        #Calculate loan, input all the information.

        if choice == "1": 
            
            principal= float(input('Please input amount of loan: RM '))
            num_years = int(input('Please input years of loan: '))
            interest_rate = float(input('Please input Annual interest rate: '))
            monthly_expenses = float(input('Enter monthly expenses: RM '))
            monthly_income = float(input('Enter monthly income: RM '))

            r= interest_rate/100/12
            n= num_years*12
            payment= round(principal*((r*(1+r)**n)/    #monthy installment formula
                        (((1+r)**n)-1)),2)
            amount= payment*n                          #total amount formula

            def calculate_dsr(monthly_expenses,payment, monthly_income):

                dsr = round(((monthly_expenses + payment) / monthly_income) * 100,2)   #dsr formula
                return dsr
            
            dsr= calculate_dsr(monthly_expenses,payment,monthly_income)
            eligible= check_eligible(dsr,dsr_threshold)

            
            print('Total amount: RM'+format(amount, ",.2f")) 
            print('Monthly Payment : RM',payment) 
            print(f'Debt Service Ratio (DSR): {dsr}%')
            print(f"Eligible for the loan: {eligible}") 

            #save all calculations
            save_calculations.append({"Monthly Payment" : payment, "Total amount" : amount,"Debt Service Ratio(DSR)" : dsr,
                                      "Eligible" : eligible})    
     
        #display previous calculations

        elif choice == "2":
                display_calculations(save_calculations)   
                
        #delete previous calculations

        elif choice == "3":
                delete_calculation(save_calculations)    

        #modify threshold

        elif choice == "4":
            dsr_threshold = modify_dsr_threshold()

        #Exit
        
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
