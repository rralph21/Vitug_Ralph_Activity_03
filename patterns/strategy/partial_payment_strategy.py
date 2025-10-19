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

    def process_payment(self, account: BillingAccount, payee: Payee,
                        amount: float) -> str:
        """
        Applies the payment to the correct bill
        """
        amount = float(amount)

        account.deduct_balance(payee, amount)

        new_balance = account.get_balance(payee)

        if new_balance is not None and new_balance <= 0.0:
            return (f"Processed payment of ${amount:.2f}. "
            + "New balance: $0.00. ")
        
        shown_balance = 0.0 if new_balance is None else new_balance
        return (
            f"Partial payment of ${amount:.2f} accepted. "
            f"New balance: ${shown_balance:.2f}. ")