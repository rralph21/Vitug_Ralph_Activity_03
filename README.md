# Intermediate Software Development Activity 3

This activity will help to reinforce learning of the Module 3 concepts of:

- Design Patterns

## Author

Ralph Vitug

## Additional Information

Activity 3 demonstrates several key components from Module 3 - Patterns and OOP.
In this activity, we were tasked to learn Strategy pattern to be applied in a bill payment concept.

1. Strategy Pattern
    Strategy Pattern is implemented using PaymentStrategy abstract class and its subclass.
    As well as PartialPaymentStrategy and PenaltyStrategy.

2. Inheritence and Polymorphism
    PartialPaymentStrategy and PenaltyStrategy inherits from PaymentStrategy.
    It allows the same pay_bill method to be called but it behaves differently (Polymorphism).

3. Encapsulation
    BillingAccount class is encapsulated where balances are kept private
    and only for view.


