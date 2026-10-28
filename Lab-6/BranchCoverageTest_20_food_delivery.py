
import pytest
from food_delivery import delivery_charge, apply_coupon, estimated_time


# Delivery charge tests
def test_nearby_small_order():
    assert delivery_charge(2, 200, False) == 20


def test_no_delivery_charge_for_large_order():
    assert delivery_charge(5, 500, False) == 0


def test_medium_distance_charge():
    assert delivery_charge(5, 200, False) == 40


def test_long_distance_charge():
    assert delivery_charge(10, 200, False) == 60


def test_rain_adds_extra_charge():
    assert delivery_charge(2, 200, True) == 50


def test_large_order_in_rain():
    assert delivery_charge(5, 500, True) == 30


def test_zero_distance_rejected():
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(0, 200, False)


def test_negative_distance_rejected():
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(-1, 200, False)


def test_distance_over_limit_rejected():
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(16, 200, False)


def test_exact_maximum_distance():
    assert delivery_charge(15, 200, False) == 60


# Coupon tests
def test_no_coupon():
    assert apply_coupon(300, None, False) == 300


def test_save50_coupon():
    assert apply_coupon(300, "SAVE50", False) == 250


def test_welcome_coupon_for_first_order():
    assert apply_coupon(300, "WELCOME", True) == 200


def test_invalid_coupon_rejected():
    with pytest.raises(ValueError, match="invalid coupon"):
        apply_coupon(300, "INVALID", True)


def test_welcome_coupon_rejected_for_repeat_order():
    with pytest.raises(ValueError, match="coupon only for first order"):
        apply_coupon(300, "WELCOME", False)


def test_coupon_not_applied_below_minimum_order():
    assert apply_coupon(150, "SAVE50", False) == 150


def test_coupon_applied_at_minimum_order():
    assert apply_coupon(200, "SAVE50", False) == 150


# Estimated delivery time tests
def test_normal_delivery_time():
    assert estimated_time(5, False, False) == 35


def test_peak_hour_adds_time():
    assert estimated_time(5, True, False) == 45


def test_busy_restaurant_adds_time():
    assert estimated_time(5, False, True) == 50


def test_peak_hour_and_busy_restaurant():
    assert estimated_time(5, True, True) == 65


def test_zero_distance_estimated_time():
    assert estimated_time(0, False, False) == 15
