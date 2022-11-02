"""
In this section we will see how online platform give a discount to costumer, when they buy expensive products.
_______________________________________________________________________________________________________________
Question : when anyone purchase any product more than one thousand, and they should get at least ten present off on the
           price.
________________________________________________________________________________________________________________________
Approach : first we take input from user then compare the price of that product, if the price is more than one thousand
           then we should give ten present off on that product else not giving any discount.
"""
from typing import Any

A = int(input("Enter the price of that product : "))
if (A < 1000):
    print("No discount is available on this product! sorry.")
else:
    C = A * 10 / 100
    print("Discount is available on this product, final price of this product after discount is : ", C)
