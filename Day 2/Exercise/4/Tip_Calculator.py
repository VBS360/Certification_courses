Bill_Amount = float(input("what is the total bill ? \n"))
Tip_Percent = float(input("What percentage tip would you like to give ? \n"))
People = input("How many people to split the bill ? \n")

Tip_Amount = float((Bill_Amount*Tip_Percent)/100)

Total_bill = float(Bill_Amount+Tip_Amount)
Amount_Per_Person = float(float(Total_bill)/int(People))
Amount_Per_Person_Round = round(Amount_Per_Person,2)

print(f"Each person has to pay {Amount_Per_Person_Round}")
