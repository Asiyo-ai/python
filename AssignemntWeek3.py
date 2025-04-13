def calculate_discount(price, discount_percent):
   
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price

# Example usage
if __name__ == "__main__":
    original_price = float(input("Enter the original price: "))
    discount = float(input("Enter the discount percentage: "))
    final_price = calculate_discount(original_price, discount)
    print(f"Final price: ${final_price:.2f}")
2