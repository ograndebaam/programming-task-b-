import random

def daily_sales(available_items, inventory_records, current_day):
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the sales for a given day.
---------------
Function Input:
---------------
available_items: (integer) Available Tshirts from the previous day.
inventory_records: (List) A list of inventory records until the previous day. Each row contains (day, sales, restocked items, available items)
current_day: (integer) Day number which you want to add as the current day. 

----------------
Function Output:
----------------
available_items:(integer) This function returns this integer which updates the available items at the current day.

The function will also update the inventory_records (For restocking) for a  given current day. 

    '''
    # sets restocked_items back to 0 since there is no restocking on non-restocking days
    restocked_inventory = 0

    # Random generates the number of sold tshirts and keeps it less than the total of available items and less than 200
    # Randomly generate the number of T-shirts sold, ensuring it's <= available items and <= 200
    sales = random.randint(0, min(200, available_items))
    
    # Update available_items by the sales
    available_items -= sales

    # Update the inventory log for the day
    inventory_records.append((current_day, sales, restocked_inventory, available_items))

    return available_items

