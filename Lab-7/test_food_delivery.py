
from hypothesis import given, strategies as st
from food_delivery import parse_order, delivery_eta, coupon_discount


# Test 1: Fuzz testing parse_order()
@given(st.text() | st.none())
def test_parse_order_no_crash(s):
    try:
        parse_order(s)
    except Exception as e:
        assert False, f"parse_order crashed with input {s!r}: {e}"


# Test 2: Fuzz testing delivery_eta()
@given(st.text() | st.none())
def test_delivery_eta_no_crash(s):
    try:
        delivery_eta(s)
    except Exception as e:
        assert False, f"delivery_eta crashed with input {s!r}: {e}"


# Test 3: Fuzz testing coupon_discount()
@given(st.text() | st.none())
def test_coupon_discount_no_crash(s):
    try:
        coupon_discount(s)
    except Exception as e:
        assert False, f"coupon_discount crashed with input {s!r}: {e}"
