"""This module defines the PenaltyStrategy class."""

__author__ = "Ralph Vitug"
__version__ = "1.0.0"

from typing import List
from billing_account.billing_account import BillingAccount
from payee.payee import Payee
from patterns.strategy.payment_strategy import PaymentStrategy

class PenaltyStrategy(PaymentStrategy):
    """
    PenaltyStrategy applys to penalized payee.
    """

    def __init__(self, penalty_rate: float = 0.10) -> None:
        if penalty_rate < 0:
            raise ValueError("Penalty rate must be non negative")
        
        else:
            self.penalty_rate = penalty_rate

    def process_payment(self, account: BillingAccount, payee: Payee, 
                        amount: float):
        penalty = round(amount * self.penalty_rate, 2)

        total = round(amount + penalty, 2)


        return (
            f"Penalty of ${penalty:.2f} ({self.penalty_rate:.0%}) applied. "
            f"Total of ${total:.2f} paid to {payee.name}."
        )
