#Name: Sophia Philips
#GitHub Username: sophiacphilips
#Date: 01/17/23
#This code is designed to take info from a lemonade stand's sales and calculate profits, days open, etc

class MenuItem:

    def __init__(self, name, wholesale_cost, selling_price):
        """Initializes menu item's wholesale cost and selling price"""
        self._name= name
        self._wholesale_cost= wholesale_cost
        self._selling_price= selling_price

    def get_name(self): #get method for name of menu item
        return self._name
    #
    def get_wholesale_cost(self): #get method for wholesale cost of item
        return self._wholesale_cost
    #
    def get_selling_price(self): #get method for selling price of item
        return self._selling_price
    #

class SalesForDay:

    def __init__(self, no_of_days, sales_dict):
        """Initializes number of days the stand has been operating and its sales dictionary"""
        self._no_of_days= no_of_days
        self._sales_dict= sales_dict

    def get_no_of_days(self): #get method for days shop has been open
        #
        return self._no_of_days

    def get_sales_dict(self): #get method for shop's sales dictionary
        #
        return self._sales_dict

class InvalidSalesItemError(Exception):
    """creates exception so code can run if a menu item is tested that does not exist in dictionary(menu)"""
    pass

class LemonadeStand:
    """creates a class for the lemonade stand and will initialize stand's name, days of operation, menu and sales"""
    def __init__(self, name):
        self._name=name
        self._no_of_days= 0
        self._menu={}
        self._sales_record=[]

    def get_name(self): #get method for stand name
        return self._name

    def add_menu_item(self, menu_item): #get method for adding new menu item
        self._menu[menu_item.get_name()] = menu_item

    def enter_sales_for_today(self, sales_dict): #creates sales dictionary of daily sales and raises exception if something is "sold" that is not a menu item
        try:
            for s in sales_dict:
                if s not in self._menu:
                    raise InvalidSalesItemError

                sales_for_day= SalesForDay(self._no_of_days, sales_dict)
                self._sales_record.append(sales_for_day)
                self._no_of_days =+ 1
        except InvalidSalesItemError:
            print("Item not listed on menu.")

    def sales_of_menu_item_for_day(self, day): #method for finding sales by menu item for a day
        for sr in self._sales_record:
            if sr._get_day() == day:
                return sr.get_sales_dict()

    def total_sales_for_menu_item(self,item_name): #method for finding total sales of a specific menu item
        total_sales=0
        for s in self._sales_record:
            sales_dict= s.get_sales_dict()
            if item_name in sales_dict:
                total_sales += sales_dict[item_name]

    def total_profit_for_menu_item(self, item_name): #method to calc total profit a menu item has made
        total_sales = self.total_sales_for_menu_item(item_name)
        item = self._menu[item_name]
        total_item_profit = total_sales * (item.get_selling_price() - item.get_wholesale_cost())
        return total_item_profit

    def total_profit_for_stand(self): #method to calc total profit for the stand
        total_stand_profit=0
        for i in self._menu:
            total_stand_profit += self.total_profit_for_menu_item(i)
            return total_stand_profit


if __name__ == '__main__':
    stand = LemonadeStand('Lemons R Us')  # Create a new LemonadeStand called 'Lemons R Us'
    item1 = MenuItem('lemonade', 0.5, 1.5)  # Create lemonade as a menu item (wholesale cost 50 cents, selling price $1.50)
    stand.add_menu_item(item1)  # Add lemonade to the menu for 'Lemons R Us'
    item2 = MenuItem('nori', 0.6, 0.8)  # Create nori as a menu item (wholesale cost 60 cents, selling price 80 cents)
    stand.add_menu_item(item2)  # Add nori to the menu for 'Lemons R Us'
    item3 = MenuItem('cookie', 0.2, 1)  # Create cookie as a menu item (wholesale cost 20 cents, selling price $1.00)
    stand.add_menu_item(item3)  # Add cookie to the menu for 'Lemons R Us'

    # This dictionary records that on day zero, 5 lemonades were sold, 2 cookies were sold, and no nori was sold
    day_0_sales = {
        'lemonade': 5,
        'cookie': 2
    }
    try: #exception specified for invalid item entry
        stand.enter_sales_for_today({"chicken nuggets": 3})
    except InvalidSalesItemError:
        print("Item not listed on menu.")
    #stand.enter_sales_for_today(day_0_sales)  # Record the sales for day zero
    #print("lemonade profit is:", {stand.total_profit_for_menu_item('lemonade')}# print the total profit for lemonade so far

