# 6.8 (Parking Charges) A parking garage charges a $2.00 minimum fee to park for up to three
# hours. The garage charges an additional $0.50 per hour for each hour or part thereof in excess of three
# hours. The maximum charge for any given 24-hour period is $10.00. Assume that no car parks for
# longer than 24 hours at a time. Write an application that calculates and displays the parking charges
# for each customer who parked in the garage yesterday. You should enter the hours parked for each
# customer. The program should display the charge for the current customer and should calculate and
# display the running total of yesterday’s receipts. It should use the method calculateCharges to
# determine the charge for each customer

class Car_park_charges_calculator:
    hours_parked = 0
    fee = 0.50

    def set_hours_parked(self, hours_parked):
        self.hours_parked = hours_parked

    def get_hours_parked(self):
        return self.hours_parked

    def set_fee_for_hours_parked(self, fee):
        if self.hours_parked == 3:
            self.fee = 2.00
        else:
            self.fee = fee

    def get_fee_for_hours_parked(self):
        return self.fee

    def calculate_charges(self,hours_parked,fee):
