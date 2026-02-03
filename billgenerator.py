grocerys_price = {
    "rice" : 50,
    "wheat" : 40,
    "oil" : 140
}


total_items = int(input("enter the total grocerys item : "))
print("Total items : ", total_items)

grocerys = []
user_picked_grocery ={}
billed_items = []

for itr in range(total_items):
    grocery_name = input("enter the grocery item name : " + str(itr))
    grocerys.append(grocery_name)


    weight = float(input("weight of " + grocery_name + " "))
    user_picked_grocery[grocery_name] = weight * grocerys_price.get(grocery_name, 0)



    billed_result = (
                     grocery_name,
                     weight,
                     grocerys_price.get(grocery_name,0),
                     user_picked_grocery.get(grocery_name)
                     )
                     



    billed_items.append(billed_result)

print("Grocerys collected : ", user_picked_grocery)

for item in(billed_items):
    print(item)
