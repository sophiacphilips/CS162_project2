#Name: Sophia Philips
#GitHub Username: sophiacphilips
#Date: 01/17/23
#This code is designed to take info from a lemonade stand's sales and calculate profits, days open, etc

import unittest
from LemonadeStand import LemonadeStand

class LemonadeStandTest(unittest.TestCase):
    """This is class is to run test cases for lemonadestand.py code"""
    def stand_data(self):
        self.stand = LemonadeStand('Lemons R Us')  # Create a new LemonadeStand called 'Lemons R Us'
        self.item1 = MenuItem('lemonade', 0.5, 1.5)  # Create lemonade as a menu item (wholesale cost 50 cents, selling price $1.50)
        self.stand.add_menu_item(item1)  # Add lemonade to the menu for 'Lemons R Us'
        self.item2 = MenuItem('nori', 0.6, 0.8)  # Create nori as a menu item (wholesale cost 60 cents, selling price 80 cents)
        self.stand.add_menu_item(item2)  # Add nori to the menu for 'Lemons R Us'
        self.item3 = MenuItem('cookie', 0.2, 1)  # Create cookie as a menu item (wholesale cost 20 cents, selling price $1.00)
        self.stand.add_menu_item(item3)  # Add cookie to the menu for 'Lemons R Us'

    # This dictionary records that on day zero, 5 lemonades were sold, 2 cookies were sold, and no nori was sold
    day_0_sales = {
        'lemonade': 5,
        'cookie': 2
    }

    stand.enter_sales_for_today(day_0_sales)  # Record the sales for day zero
    print("lemonade profit = {stand.total_profit_for_menu_item('lemonade')}")  # print the total profit for lemonade so far

    def test_add_menu_item(self): #test case to check if adding a new menu item is working
        item4=MenuItem("cake",0.75, 1.5)
        self.stand.add_menu_item(item4)
        self.AssertEqual(self.stand._menu{"lemonade": self.item1, "nori": self.item2, "cookie": self.item3, "cake": self.item4})

    def test_total_profit_for_menu_item(self): #test to check that total profit is not the same between day 0 and 1
        day_1_sales = {
            'lemonade': 4
            'cookie': 6
            'nori': 1
            'cake': 3
        }
        stand.enter_sales_for_today(day_1_sales)

        self.AssertNotEqual(day_0_sales, day_1_sales)

    def test_total_sales_for_menu_item(self): #testing that total sales for lemonade on day 1 is equivalent to 4
        self.stand.enter_sales_for_today(self.day_1_sales)
        self.AssertEqual(self.stand.total_sales_for_menu_item("lemonade"),4)

    def test_init_for_stand_name(self): #testing that correct name is working for get name function
        self.AssertEqual(self.stand.get_name(),'Lemons R Us')

    def test_total_profit_for_stand(self): #testing for total profit of stand on day 0
        self.stand.total_profit_for_stand(self.day_0_sales)
        self.AssertEqual(self.stand.total_profit(), 3.4)







