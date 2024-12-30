def apply_discount(discount_percentage):
    def decorator(func):
        def wrapper(*args, **kwargs):
            total = func(*args, **kwargs)
            discount = total * (discount_percentage / 100)
            total_after_discount = total - discount
            print(f"Applying a discount of {discount_percentage}%...")
            return total_after_discount
        return wrapper
    return decorator
