# shopping-cart-zennode

## Here is a catalogue with 3 products.

Product Name : Price
Product A : $20
Product B : $40
Product C : $50

## Discount Rules:
"flat_10_discount": If cart total exceeds $200, apply a flat $10 discount on the cart total.
"bulk_5_discount": If the quantity of any single product exceeds 10 units, apply a 5% discount on that item's total price.
"bulk_10_discount": If total quantity exceeds 20 units, apply a 10% discount on the cart total.
"tiered_50_discount": If total quantity exceeds 30 units & any single product quantity greater than 15, then apply a 50% discount on products which are above  15 quantity. The first 15 quantities have the original price and units above 15 will get a 50% discount.
Note: Only one rule can be applied per purchase. If multiple discounts are applicable, the program calculates the discount amount for each rule and applies the most beneficial one for customer.

## Fees:
Gift wrap fee: $1 per unit.
Shipping fee: 10 units can be packed in one package, and the shipping fee for each package is $5.

## Program
The program will ask the quantity of each product. The program will also ask if that product is wrapped as a gift?

Then the program will show / output below details.
The product name, quantity & total amount of that product.
Subtotal
The discount name applied & the discount amount.
The shipping fee & the gift wrap fee.
Total
