def bread_price(n):
    price=3.49
    discount=0.06
    price_old=n*price
    discount_amount= discount*price_old
    total_price=price_old-discount_amount
    return price_old , discount_amount , total_price
def user():
    n=float(input("enter n. loaves: "))
    while n < 0:
         print("invalid , try again")
         n=float(input("enter n. loaves: "))
    price_old , discount_amount , total_price =bread_price(n)
    print(f"regular price for the {n} loaves={price_old}")
    print(f"the discount because it is a day old={discount_amount}")
    print(f"the total price={total_price}")
user()