class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.all_customers.append(self)

    def set_given_name(self, given_name):
        self.given_name = given_name

    def set_family_name(self, family_name):
        self.family_name = family_name

    def get_given_name(self):
        return self.given_name

    def get_family_name(self):
        return self.family_name



    def get_full_name(self):
        return self.given_name + ' ' + self.family_name

    @classmethod
    def get_all_customers(cls):
        return cls.all_customers
    

    # Create some customer instances
customer1 = Customer("Mike", "Smith")
customer2 = Customer("Angela", "Johnson")

# Test the get_given_name() and get_family_name() methods
print(customer1.get_given_name())  # Output: Mike
print(customer1.get_family_name())  # Output: Smith

# Test the set_given_name() and set_family_name() methods
customer2.set_given_name("Angel")
customer2.set_family_name("Brown")
print(customer2.get_given_name())  # Output: Angel
print(customer2.get_family_name())  # Output: Brown

# Test the get_full_name() method
print(customer1.get_full_name())  # Output: Mike Smith
print(customer2.get_full_name())  # Output: Angel Brown

# Test the get_all_customers() class method
all_customers = Customer.get_all_customers()
for customer in all_customers:
    print(customer.get_full_name())

# Output:
# Mike Smith
# Angel Brown



           