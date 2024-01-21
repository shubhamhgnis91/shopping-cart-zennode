import math

# Build cart and simultaneously calculate total price, total quantity, shipping cost and gift wrap fee
def buildCart(cart):

    totalPrice = 0
    toatlQuantity = 0
    giftWrapFee = 0

    while True:
        
        print("Product Name : Price")
        print("Product A : $20")
        print("Product B : $40")
        print("Product C : $50")

        print("Which product do you want to buy? (q to quit)") 
        choice = input().lower()

        if choice not in ['a', 'b', 'c', 'q']:
            print("Invalid choice")
            continue

        if choice == 'q':
            break

        print("Provide quantity: ")
        quantity = int(input())  

        if quantity < 0:
            print("Invalid quantity")
            continue

        print("Do you want to gift wrap this product? (y/n)")
        giftWrap = input().lower()

        if giftWrap == 'y':
            giftWrapFee += quantity

        if choice == 'a':
            totalPrice += 20 * quantity

        elif choice == 'b':
            totalPrice += 40 * quantity

        elif choice == 'c':
            totalPrice += 50 * quantity

        toatlQuantity += quantity
         

        if choice in cart:
            cart[choice] += quantity
        else:
            cart[choice] = quantity

        

    shippingCost = math.ceil(toatlQuantity / 10 ) * 5

    #return set of totalPrice, totalQuantity, shippingCost, giftWrapFee
    return totalPrice, toatlQuantity, shippingCost, giftWrapFee

def calculateDiscount(cart, totalPrice, totalQuantity):

    discounts = []

    '''"flat_10_discount": If cart total exceeds $200, apply a flat $10 discount on the cart total.'''
    if totalPrice > 200:
        discounts.append(('flat_10_discount',totalPrice * 0.1))


    '''"bulk_5_discount": If the quantity of any single product exceeds 10 units, apply a 5% discount on that item's total price.'''
    for product in cart:
        quantity = cart[product]

        if quantity > 10:
            if product == 'a':
                discounts.append(('bulk_5_discount',20 * quantity * 0.05))
            elif product == 'b':
                discounts.append(('bulk_5_discount',40 * quantity * 0.05))
            elif product == 'c':
                discounts.append(('bulk_5_discount',50 * quantity * 0.05))

    '''"bulk_10_discount": If total quantity exceeds 20 units, apply a 10% discount on the cart total.'''
    if totalQuantity > 20:
        discounts.append(('bulk_10_discount',totalPrice * 0.1))


    '''"tiered_50_discount": If total quantity exceeds 30 units & any single product quantity greater than 15, then apply a 50% discount on products which are above  15 quantity. The first 15 quantities have the original price and units above 15 will get a 50% discount.'''
    if totalQuantity > 30:
        for product in cart:
            quantity = cart[product]

            if quantity > 15:
                if product == 'a':
                    discounts.append(('tiered_50_discount',20 * 15 * 0.5))
                elif product == 'b':
                    discounts.append(('tiered_50_discount',40 * 15 * 0.5))
                elif product == 'c':
                    discounts.append(('tiered_50_discount',50 * 15 * 0.5))

    if len(discounts) == 0:
        return ('no_discount', 0)
    
    discount, discountName = max(discounts, key=lambda x: x[1]), max(discounts, key=lambda x: x[0])

    #return set of discount, discountName
    return discount, discountName


# show products in cart along with their total
def showCart(cart):
    for product in cart:
        print("Product: ", product.upper())
        print("Quantity: ", cart[product])
        
        if product == 'a':
            print("Price: ", 20 * cart[product])
        elif product == 'b':
            print("Price: ", 40 * cart[product])
        elif product == 'c':
            print("Price: ", 50 * cart[product])


print("-------------------------------------------")

'''"cart" is a dictionary that stores the product and its quantity'''
cart = {}

cartSet = buildCart(cart)
totalPrice = cartSet[0]
totalQuantity = cartSet[1]
shippingCost = cartSet[2]
giftWrapFee = cartSet[3]

discountSet = calculateDiscount(cart, totalPrice, totalQuantity)
discount = discountSet[0][1]
discountName = discountSet[1][0]

print("-------------------------------------------")
showCart(cart)

print("\nSubtotal: ", totalPrice)
print("Discount Name: ", discountName)
print("Discount: ", discount)
print("\nShipping Cost: ", shippingCost)
print("Gift Wrap Fee: ", giftWrapFee)

print("\nTotal: ", totalPrice - discount)
