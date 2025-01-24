import pandas as pd

#Sample inventory data for a Kirana store
data={
    'Item':['Rice(kg)','Atta(kg)','Dal(kg)','Sugar(kg)','Oil(liter)','Spices(pkt)','Tea(pkt)','Biscuits(pkt)'],
    'Quantity':[100,80,50,50,30,50,50,120],
    'Price':[60,40,120,45,180,30,80,20]
}
inventory=pd.DataFrame(data)

# Function to update inventory after a sale
def update_inventory(item,quantity):
    if item in inventory['Item'].values:
        index=inventory[inventory['Item']==item].index[0]
        if inventory.loc[index,'Quantity']>=quantity:
            inventory.loc[index,'Quantity']>=quantity
            print(f"{quantity}{item}sold.")
        else:
            print(f"Not enough {item} in stock.") 
    else:
        print("{Item} not found in inventory.")

# Function to generate a bill
def generate_bill(item,quantities):
    total_bill=0
    print("-----Bill-----")
    for item,quantity in zip(item,quantities):
        if item in inventory['Item'].values:
            index= inventory[inventory['Item']==item].index[0]
            price=inventory.loc[index,'Price']
            cost=price*quantity
            print(f"{item}x{quantity}={cost:.2f}")
            total_bill+=cost
        else:
            print(f"{item} not found in inventory.")
    print(f"Total:{total_bill:.2f}") 

# Example usage
update_inventory(' Rice(kg)',10)  
update_inventory(' Dal(kg)',25)
update_inventory(' Oil(liter)',5)  

generate_bill(['Rice(kg)','Oil(liter)','Spices(pkt)'],[5,2,3])

# Check for low stock (e.g.,below 20 units)
low_stock_items=inventory[inventory['Quantity']<20]['Item'].tolist()
if low_stock_items:
    print("\nLow stock alert:")
    for item in low_stock_items:
        print(f"{item}is running low.")
else:
    print("\nAll items are sufficiently stocked.")    

