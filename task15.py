class Passport:
    def __init__(self, first_name, last_name, date_of_birth, country, number):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.country = country
        self.number = number

    def print_info(self):
        print("First name: ", self.first_name, "\n", "Last name: ", self.last_name, "\n",
              "Date of birth: ", self.date_of_birth, "\n", "Country: ", self.country, "\n", "Passport №: ", self.number)


class ForeignPassport(Passport):
    def __init__(self, first_name, last_name, date_of_birth, country, number, visa):
        super().__init__(first_name, last_name, date_of_birth, country, number)
        self.visa = visa

    def print_info(self):
        super().print_info()
        print("Visa: ", self.visa)
