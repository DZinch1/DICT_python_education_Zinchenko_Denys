import math
import sys
import argparse


def calculate_months(principal, monthly_payment, annual_percent):
    annual_rate = annual_percent / 100.0
    monthly_rate = annual_rate / 12.0
    if monthly_rate == 0:
        months = math.ceil(principal / monthly_payment)
    else:
        if monthly_payment <= monthly_rate * principal:
            raise ValueError("Monthly payment too small to cover interest.")
        months = math.ceil(math.log(monthly_payment / (monthly_payment - monthly_rate * principal), 1 + monthly_rate))
    years = months // 12
    remaining_months = months % 12
    return years, remaining_months


def calculate_payment(principal, months, annual_percent):
    annual_rate = annual_percent / 100.0
    monthly_rate = annual_rate / 12.0
    if monthly_rate == 0:
        return math.ceil(principal / months)
    payment = math.ceil(principal * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1))
    return payment


def calculate_principal(payment, months, annual_percent):
    annual_rate = annual_percent / 100.0
    monthly_rate = annual_rate / 12.0
    if monthly_rate == 0:
        return math.ceil(payment * months)
    principal = math.floor(payment / ((monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)))
    return principal


def calculate_diff_payment(principal, months, annual_percent):
    annual_rate = annual_percent / 100.0
    monthly_rate = annual_rate / 12.0
    payments = []
    for m in range(1, months + 1):
        payment = math.ceil(principal / months + monthly_rate * (principal - (principal * (m - 1) / months)))
        payments.append(payment)
    return payments


def calculate_overpayment(principal, total_paid):
    return math.ceil(total_paid - principal)


def main():
    parser = argparse.ArgumentParser(description="Credit Calculator")
    parser.add_argument("--type", choices=["annuity", "diff"], help="Type of payment: 'annuity' or 'diff'")
    parser.add_argument("--principal", type=float, help="Loan principal")
    parser.add_argument("--payment", type=float, help="Monthly payment amount")
    parser.add_argument("--periods", type=int, help="Number of periods (months)")
    parser.add_argument("--interest", type=float, help="Annual interest rate (percent)")
    try:
        args = parser.parse_args()
    except SystemExit:
        print("Incorrect parameters.")
        return
    if args.type is None:
        print("Incorrect parameters.")
        return

    values = [args.principal, args.payment, args.periods, args.interest]

    if values.count(None) != 1:
        print("Incorrect parameters.")
        return

    payment_type = args.type
    principal = args.principal
    periods = args.periods
    interest = args.interest
    payment = args.payment

    if payment_type == "diff" and payment is not None:
        print("Incorrect parameters.")
        return
    if interest is not None and interest < 0:
        print("Incorrect parameters.")
        return
    if principal is not None and principal < 0:
        print("Incorrect parameters.")
        return
    if payment is not None and payment < 0:
        print("Incorrect parameters.")
        return
    if periods is not None and periods < 0:
        print("Incorrect parameters.")
        return
    if payment_type == "diff":
        payments = calculate_diff_payment(principal, periods, interest)
        total_paid = sum(payments)
        overpayment = calculate_overpayment(principal, total_paid)
        for m in range(1, periods + 1):
            print(f"Month {m}: payment is {payments[m - 1]}")
        print(f"Overpayment = {overpayment}")
    elif payment_type == "annuity":
         if payment is None:
             payment = calculate_payment(principal, periods, interest)
             print(f"Your annuity payment = {payment}!")
             overpayment = calculate_overpayment(principal, payment * periods)
             print(f"Overpayment = {overpayment}")
         elif periods is None:
             years, remaining_months = calculate_months(principal, payment, interest)
             if years > 0:
                 year_str = "year" if years == 1 else "years"
                 month_str = "month" if remaining_months == 1 else "months"
                 if remaining_months > 0:
                     print(f"You need {years} {year_str} and {remaining_months} {month_str} to repay this credit!")
                 else:
                     print(f"You need {years} {year_str} to repay this credit!")
             else:
                 print(f"You need {remaining_months} months to repay this credit!")
             total_paid = payment * (years * 12 + remaining_months)
             overpayment = calculate_overpayment(principal, total_paid)
             print(f"Overpayment = {overpayment}")
         elif principal is None:
             principal = calculate_principal(payment, periods, interest)
             print(f"Your credit principal = {principal}!")
             total_paid = payment * periods
             overpayment = calculate_overpayment(principal, total_paid)
             print(f"Overpayment = {overpayment}")
         elif interest is None:
             print("Incorrect parameters.")
             return


if __name__ == "__main__":
    main()
