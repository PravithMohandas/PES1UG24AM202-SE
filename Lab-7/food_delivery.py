
import math


def parse_order(items_csv):
    if not isinstance(items_csv, str) or not items_csv.strip():
        return {}

    order = {}

    try:
        for item in items_csv.split(','):
            parts = item.split(':')

            if len(parts) != 2:
                return {}

            name = parts[0].strip()
            qty_text = parts[1].strip()

            if not name:
                return {}

            qty = int(qty_text)

            if qty <= 0:
                return {}

            order[name] = qty

    except (ValueError, TypeError):
        return {}

    return order


def delivery_eta(distance_km):
    try:
        distance = float(distance_km)

        if not math.isfinite(distance) or distance < 0:
            return 0

        return int(15 + distance * 4)

    except (ValueError, TypeError, OverflowError):
        return 0


def coupon_discount(code):
    if not isinstance(code, str):
        return 0

    code = code.strip().upper()

    if not code.startswith("SAVE"):
        return 0

    discount_text = code[4:]

    if not discount_text.isdigit():
        return 0

    discount = int(discount_text)

    if discount < 0 or discount > 100:
        return 0

    return discount


def main():
    print("==== Running parse_order ====")
    user_input = input("Enter items as name:qty CSV (e.g. pizza:2,burger:1): ")
    result = parse_order(user_input)
    print("Order:", result)

    print("\n==== Running delivery_eta ====")
    user_input = input("Enter distance in km (e.g. 4.5): ")
    result = delivery_eta(user_input)
    print("ETA in Minutes:", result)

    print("\n==== Running coupon_discount ====")
    user_input = input("Enter a coupon code (e.g. SAVE50): ")
    result = coupon_discount(user_input)
    print("Discount:", result)


if __name__ == "__main__":
    main()
