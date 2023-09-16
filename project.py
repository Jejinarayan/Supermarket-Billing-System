from datetime import datetime

name = input("Enter your name: ")

lists = ''' 
Rice    rs 50/kg
sugar   rs 30/kg
salt    rs 20/kg
oil     rs 100/kg
paneer  rs 400/kg
Maggie  rs 100/kg
Boost   rs 60/pt
colgate rs 95/each
'''
items = {"rice":50,"sugar":30,"salt":20,"oil":100,
         "paneer":400,"maggie":100,"boost":60,"colgate":95}

price = 0
pricelist = []
item2 = []
qua2 = []
price2 = []
total = 0
final_amt = 0
 

menu = int(input("For list of items press 1:"))
if menu == 1:
    print("------------------------")
    print(lists)
    print("------------------------")
for i in range(len(items)):
    option = int(input("To buy products press 1,for exit press 2: "))
    if option == 2:
        print("Thank you!")
        break
    if option == 1:
        item = (input("Enter item: "))
        qua = int(input("Enter quantity: "))
        if item in items.keys():
            price = qua*items[item]
            pricelist.append((item,qua,items,price))
            item2.append(item)
            qua2.append(qua)
            price2.append(price)
            total = total + price
            gst = (total*5)/100
            final_amt = total + gst
        else:
            print("sorry, entered item is not available.")
    else:
        print("Please enter valid option")
    
    inp = input("Can i bill the item? - yes or no: ")
    if inp == "yes":
        pass
        if final_amt != 0:
            print(50*"=","Amma supermarket",50*"=")
            print(55*" ","Tenali")
            print(118*"-")
            print("Date:",datetime.now(),60*" ","Name:",name)
            print(118*"-")
            print("SNO:",22*" ","Items:",25*" ","Quantity:",10*" ","Price:")
            for i in range(len(pricelist)):
                print(i,25*" ",item2[i],27*" ",qua2[i],17*" ",price2[i])
            print(118*"-")
            print("Total: ",total)
            print(118*"-")
            print("Gst: ",gst)
            print(118*"-")
            print("Final Amount: ",final_amt)
            print(50*"=","Thank you for visiting",44*"=")
            break
        else:
            print("Please add items")
    elif inp == "no":
        pass
    else:
        print("Invalid option")






        
        



