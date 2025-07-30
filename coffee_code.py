
class Delivery:
    def __init__(self, menu_items):
        self.menu_items = menu_items

    def menu(self):
        print (self.menu_items)

    def order(self, coffee_type, quantity):
        coffee_price = quantity * self.menu_items[coffee_type]
        if coffee_price < 10000:
            self.total = coffee_price + 3000
        else:
            self.total = coffee_price
        print (self.total)

    def charge(self, payment):
        if payment >= self.total:
            print(f'Your change is {payment - self.total} won.')
        else:
            print (f'You need to pay {self.total} won.')
    
    def reset_total(self):
        self.total = 0



class ForHere():
    def __init__(self, menu_items):
        self.menu_items = menu_items

    def menu(self):
        print (self.menu_items)

    def charge(self, payment):
        if payment >= self.total:
            print(f'Your change is {payment - self.total} won.')
        else:
            print (f'You need to pay {self.total} won.')
    
    def reset_total(self):
        self.total = 0

    def order(self, coffee_type, quantity):  # overriding method 로 덮어씀
        self.total = quantity * self.menu_items[coffee_type]
        print (self.total)
 


class ComposeCoffee(Delivery, ForHere):
    def __init__(self, service_type, position, menu_items):
        self.service_type = service_type
        self.position = position
        if self.service_type == 'Delivery':
            Delivery.__init__(self, menu_items)
        elif self.service_type == 'For Here':
            ForHere.__init__(self, menu_items)

    def switch_service(self):
        Delivery.reset_total(self)
        ForHere.reset_total(self)
        if self.service_type == 'Delivery':
            self.service_type = 'For Here'
        else:
            self.service_type = 'Delivery'
        
    def menu(self):
        if self.service_type == 'Delivery':
            Delivery.menu(self)
        else:
            ForHere.menu(self)    

    def order(self, coffee_type, quantity):
        if self.service_type == 'Delivery':
            Delivery.order(self, coffee_type, quantity)
        else:
            ForHere.order(self, coffee_type, quantity)
        print(f'your order is {coffee_type}')

    def charge(self, payment):
        if self.service_type == 'Delivery':
            Delivery.charge(self, payment)
        else:
            ForHere.charge(self, payment)

    def tell_position(self):
        print (f'Whelcome to Compose Coffee {self.position}.')

    def reset_total(self):
        if self.service_type == 'Delivery':
            Delivery.reset_total(self)
        else:
            ForHere.reset_total(self)


men_dict = {'americano':3000, 'latte':4000, 'juice':4000}
comcoff = ComposeCoffee('Delivery', 'Madeul', men_dict)
print(1)
comcoff.order('latte', 2)
comcoff.switch_service()
print (2)
comcoff.order('juice', 2)

