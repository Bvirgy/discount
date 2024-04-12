def calculate_discount(price,calculate_discount_price):
    if discount_percent>=20:
        discounted_price=price-(price*(discount_percent/100))
        return discounted_price
        else:
            return price
        
            orginal_price=float(input("Enter the orginal price:"))
            discount= float(input("Enter the discount percentage:"))
            discounted_price=calculate_discount(original_price,discount)
            if final_price !=original_price:
                printf("The finsl price after applying the discount is":,final_price)
                else:
                    printf("No discount applied. The original price is:",original_price)