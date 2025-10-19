"""This module defines the PartialPaymentStrategy class."""

__author__ = "Ralph Vitug"
__version__ = "1.0.0"

from typing import List
from patterns.strategy.payment_strategy import PaymentStrategy
from billing_account.billing_account import BillingAccount
from payee.payee import Payee

class PartialPaymentStrategy(PaymentStrategy):
    """
    PartialPaymentStrategy only pays partial
    of the total amount owing.

    """

    def __init__(self, percentage: float = 0.5) -> None:
        self.percentage = max(0.0, min(percentage, 1.0))

    def process_payment(self, account: BillingAccount, payee: Payee,
                        amount: float) -> str:
        amount_to_pay = round(amount * self.percentage, 2)
        account.deduct_balance(payee, amount_to_pay)
        
        remaining = round(amount - amount_to_pay, 2)
        return(f"Partial payment of ${amount_to_pay:.2f} made to {payee.name}."
               f"Remaining balance: ${remaining:.2f}")