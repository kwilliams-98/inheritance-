import PersonExercise as p 

def main():
    name = 'John'
    address = '123 Test Blvd'
    phone = '123-456-7890'
    cust_number = 1234
    on_list = True

    person1 = p.Person(name, address, phone)

    customer1 = p.Customer(name, address, phone, cust_number, on_list)

    person1.print_person()

    customer1.print_person()