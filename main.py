from Tax import Vehicle

vehicle1 = Vehicle("80AB001",900,2022)
vehicle2 = Vehicle("80CC001",1400,2020)
vehicle3 = Vehicle("34AL545",1800,1998)
vehicle4 = Vehicle("46DD987",1600,2015)
vehicle5 = Vehicle("01SE582",2500,2018)

total_tax = 0
for vehicle in [vehicle1,vehicle2,vehicle3,vehicle4,vehicle5]:
    total_tax += vehicle.tax_price

print("Total:{}TL".format(total_tax))

"""
Örnek çıktılar:
80AB001,3,3000TL
80CC001,3,4500TL
34AL545,1,2000TL
46DD987,2,3000TL
01SE582,3,7500TL
Total:20000TL
"""