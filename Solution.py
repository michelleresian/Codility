# Function to calculate the final balance of an account at the end of the year 2020
def solution(A, D):
#everything in the bank at the begining is 0
    card_payments = 0
    card_payment_total = 0
    account_balance = 0

    #Track of card payments by month
    card_payments_by_month = {}

    # transactions using the amount and dates
    for amount, date in zip(A, D):
        # now split the dates into the year, month,date,
        year, month, _ = date.split('-')
# If the transaction is an incoming transfer
        if amount < 0:  
        #Take the current value of account_balance, add the value of amount to it, and then assign the result back to account_balance
            account_balance += amount
        else:  # If it's a card payment
            account_balance += amount - 5  # Deduct 5 for card payment
            card_payments += 1
            card_payment_total += amount
            # Update card payments by month
            if month in card_payments_by_month:
                card_payments_by_month[month] += 1
            else:
                card_payments_by_month[month] = 1

    # unless there were at least 3 payments made by a card for a total cost of atleast 100
    if card_payments >= 3 and card_payment_total >= 1000:
        for month, num_payments in card_payments_by_month.items():
            if num_payments >= 3:
                account_balance -= 5  # Deduct $5 for each month with 3 or more card payments

    return account_balance

print(solution([100, 100, 100, -10], ["2020-12-31", "2020-12-22", "2020-12-03", "2020-12-29"]))