def restock_inventory(available_items, inventory_records, current_day):
    '''
 ***********COMPLETE THIS FUNCTION***********
 This function is responsible for updating the stock/restock for a given day.
  ---------------
 Function Input:
 ---------------
 available_items: (integer) Available T-shirts from the previous day.
inventory_records: (List) A list of inventory records until the previous day. Each row contains (day, sales, restocked items, available items).
current_day: (integer) Day number which you want to add as the current day. 

 ----------------
 Function Output:
----------------
 available_items:(integer) This function returns this integer which updates the available items 
 at the current day.

 The function will also update the inventory_records (For restocking) for a given current day. 
    '''
    # Initialize restocked_items to 0
    restocked_items = 0

    # Check if today is a restocking day, being the first day and every 7 days after
    if current_day == 0 or current_day % 7 == 0:
        restocked_items = 2000 - available_items  # Checks
        #how many items need to be restocked
        available_items += restocked_items  # Update available items with the restocked amount

    # Update the inventory records for the current day
    # On restocking days, sales are 0 as there are no sales
    inventory_records.append((current_day, 0, restocked_items, available_items))

    # Return the updated available_items
    return available_items

