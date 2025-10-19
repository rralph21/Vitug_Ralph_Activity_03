"""This module defines the Payment class."""

__author__ = "Ralph Vitug"
__version__ = "1.0.0"

from billing_account.billing_account import BillingAccount
from payee.payee import Payee
from patterns.strategy.payment_strategy import PaymentStrategy

class PaymentProcess:
    """
    PaymentProcess uses a strategy to execute payments
    without knowing details of any other strategy.
    """

    def __init__(self, strategy: PaymentStrategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy) -> None:
        self._strategy = strategy

    def pay_bill(self, account: BillingAccount, payee: Payee,
                amount: float) -> str:
        return self._strategy.process_payment(account, payee, amount)