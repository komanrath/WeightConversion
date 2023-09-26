#Simple weight conversion function

Weight = float(input("Weight: "))
Units = input("(K)g or (L)bs? ")
if Units.upper() == "L": 
    print("Weight in Kg: " + str(Weight / 2.2046))
else:
    print("Weight in Lbs: " + str(Weight * 2.2046))
