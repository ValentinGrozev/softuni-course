from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    FIX_INTEREST_RATE = 1.5
    FIX_AMOUNT_OF_LOAN = 2000.0

    def __init__(self):
        super().__init__(self.FIX_INTEREST_RATE, self.FIX_AMOUNT_OF_LOAN)

    def increase_interest_rate(self):
        self.interest_rate += 0.2
