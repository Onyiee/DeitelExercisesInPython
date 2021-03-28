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
    charges_per_hour = 0.50
    total_charges = 0

    def set_hours_parked(self, hours_parked):
        self.hours_parked = hours_parked

    def get_hours_parked(self):
        return self.hours_parked

    def set_fee_for_hours_parked(self, charges_per_hour):
        self.charges_per_hour = charges_per_hour

    def get_fee_for_hours_parked(self):
        return self.charges_per_hour

    def calculate_charges(self, hours_parked):
        # total_charges = hours_parked * self.charges_per_hour
        # customers = []
        # self.set_fee_for_hours_parked()
        if hours_parked == 3:
            self.total_charges = 2.00
            print(self.total_charges)
            return self.total_charges

        if hours_parked < 3:
            self.charges_per_hour = 0.67
            self.total_charges = hours_parked * self.charges_per_hour
            return self.total_charges

        if hours_parked > 3 and hours_parked < 24:
            extra_hours_parked = hours_parked - 3
            self.total_charges = 2.00
            self.charges_per_hour = 0.5
            extra_fee = extra_hours_parked * self.charges_per_hour
            self.total_charges = extra_fee + self.total_charges
            return self.total_charges
        if hours_parked == 24:
            self.total_charges = 10.00
            return self.total_charges

    def get_charges(self):
        return self.total_charges
        # self.get_fee_for_hours_parked()
        # self.set_hours_parked(4)
        # self.get_fee_for_hours_parked()
        # total_charges = hours_parked * self.charges_per_hour
        # print(total_charges)

        # charges_per_hour = 0.50
        # for i in customers:
        # hours_parked = int(input("Enter the number of hours the car was parked for: "))
        # total_charges = hours_parked * self.charges_per_hour
        # print(f"the total charges to be paid is {total_charges}")
