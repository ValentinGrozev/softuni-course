from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    FIX_INTEREST_RATE = 3.5
    FIX_AMOUNT_OF_LOAN = 50000.0

    def __init__(self):
        super().__init__(self.FIX_INTEREST_RATE, self.FIX_AMOUNT_OF_LOAN)

    def increase_interest_rate(self):
        self.interest_rate += 0.5
