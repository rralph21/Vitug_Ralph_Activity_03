"""This module defines the PaymentStrategy class."""

__author__ = "Ralph Vitug"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from typing import List
from billing_account.billing_account import BillingAccount
from payee.payee import Payee


class PaymentStrategy(ABC):
    """
    PaymentStrategy is to maintain all possible ways
    in which payments are processed.

    """

    @abstractmethod
    def process_payment(
        self, account: BillingAccount, payee: Payee, 
        acoumt: float
    ) -> str:
        pass


    """
    PaymentStrategy is the interface.

    It defines a rule that every payment method must have 
    a process_payment() function.

    Other classes like PartialPaymentStrategy or PenaltyStrategy
    follow this rule and provide their own versions of 
    process_payment().

    Strategy Pattern allows different payment method to 
    switch methods easily because they all use this interface.
    
    """  
