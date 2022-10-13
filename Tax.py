"""
Ad soyad:
Okul no:
"""

class Vehicle:
    """Vehicle tax price calculator class"""


    def __init__(self,alisence_plate:str,aengine_size:int,amodel_year:int) -> None:
        """Vehicle constructor it assigns start values of a vehicle. 
        Calls methods by order:

        calculate_tax_factor()
        calculate_tax_price()
        print()

        Args:
            alisence_plate (str): lisence plate number of a vehicle
            aengine_size (int): engine size of a vehicle (in cm3)
            amodel_year (int): model year of a vehicle
        """

    
    def calculate_tax_factor(self):
        """Calculate tax factor by model year
        model_year<2013, tax_factor=1
        model_year<2018, tax_factor=2
        model_year>=2018, tax_factor=3
        """

    
    def calculate_tax_price(self):
        """Calculate tax price by tax_factor and engine size
        engine_size<1001, tax_price = tax_factor * 1000
        engine_size<1601, tax_price = tax_factor * 1500
        engine_size<2001, tax_price = tax_factor * 2000
        engine_size>2000, tax_price = tax_factor * 2500
        """


    def print(self):
        """Print vehicle lisence plate no, tax factor, tax price
        ex:
        80AB001,3,3000TL
        """

        
