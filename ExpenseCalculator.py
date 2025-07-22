amount =[]
category =[]
while True :
    category.append(input("Enter the category of expense and if you Want total enter '=' "))
    if category[-1] == "=" or category[-1] == "" or category[-1] == " te":
        break
    amount.append(eval(input("Enter the amount ")))
enpenses_with_amount = dict(zip(category,amount))    
if len(category) >1:    
    for i,j in zip(category,amount):
        print("Expenses of ",i," = ", j)
    print("Total Amount =",sum(amount))
else:     
    print("Total Amount =",0)            