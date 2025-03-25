def calc_emi (loan_amount,annual_interest,loan_tenure_months):
    monthly_interest=(annual_interest/100)/12
    if monthly_interest == 0:
        return loan_amount/loan_tenure_months
    
    emi=(loan_amount*monthly_interest*(1+monthly_interest)**loan_tenure_months)/((1+monthly_interest)**loan_tenure_months-1)
    
    return emi

loan_amount=float(input("Enter the loan amount: "))
annual_interest=float(input("Enter annual interest rate: "))
loan_tenure_years=int(input("Enter Loan Tenure years: "))
loan_tenure_months=int(loan_tenure_years*12)

emi=calc_emi(loan_amount,annual_interest,loan_tenure_months)

print(f"Your EMI for Loan amount of RS {loan_amount} for annual interest rate of {annual_interest} for loan tenure months of {loan_tenure_months} is {emi}")

