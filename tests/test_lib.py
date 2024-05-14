import pytest
from magolib import (
    maghi_to_meters,
    meters_to_maghi,
    format_maghi,
    convert_maghi,
    parse_meters,
    parse_maghi
)


# Constants
CONVERSION_FACTOR = 1.93


def test_meters_to_maghi():
    test_vals = [321.65, 122.28, 86.66, 468.75, 331.38, -62.44, -165.25, -108.52, 207.36, -104.49, -102.28, -473.5, -456.47, 110.09, 497.75, 251.24, -427.78, 234.24, -433.2, -479.59]
    for v in test_vals:
        assert meters_to_maghi(v) == pytest.approx(v / CONVERSION_FACTOR, 0.001)


def test_meters_to_maghi_error():
    with pytest.raises(TypeError):
        meters_to_maghi("swag")


def test_maghi_to_meters():
    test_vals = [321.65, 122.28, 86.66, 468.75, 331.38, -62.44, -165.25, -108.52, 207.36, -104.49, -102.28, -473.5, -456.47, 110.09, 497.75, 251.24, -427.78, 234.24, -433.2, -479.59]
    for v in test_vals:
        assert maghi_to_meters(v) == pytest.approx(v * CONVERSION_FACTOR, 0.001)


def test_maghi_to_meters_error():
    with pytest.raises(TypeError):
        maghi_to_meters("swag")


def test_format():
    assert format_maghi(1) == "1.00 ℳ  (maghi)"
    assert format_maghi(0.1) == "1.00 dℳ  (decimaghi)"
    assert format_maghi(0.005) == "5.00 mℳ  (millimaghi)"
    assert format_maghi(500) == "5.00 hℳ  (ettomaghi)"
    assert format_maghi(4390) == "4.39 kℳ  (kilomaghi)"
    assert format_maghi(3.4e6) == "3.40 Mℳ  (megamaghi)"
    assert format_maghi(75e12) == "75.00 Tℳ  (teramaghi)"


def test_convert():
    test_vals = [
        (1, '', 'm', 1e3),
        (3.14, 'k', '', 3140),
        (42, 'u', 'd', 4.2e-4),
        (600, 'h', 'M', 0.06),
        (0.02476, 'n', 'p', 24.76),
        (2.34e9, 'k', 'T', 2.34)
    ]

    for v, f, t, r in test_vals:
        assert convert_maghi(v, f, t) == pytest.approx(r, 0.001)


def test_convert_error():
    with pytest.raises(ValueError):
        convert_maghi(1, 'm', 'z')

    with pytest.raises(ValueError):
        convert_maghi(1, 'z', 'm')
    
    with pytest.raises(TypeError):
        convert_maghi("swag", 'm', 'k')
        convert_maghi(1, 1, 'k')
        convert_maghi(1, 'm', 1)


def test_parse_meters():
    test_vals = [
        ("1m", 1),
        ("3.0 m", 3),
        ("1e-2 cm", 0.0001),
        ("40 km", 40000),
        (".7e3 um", 0.0007),
    ]

    for v, r in test_vals:
        assert parse_meters(v) == pytest.approx(r, 0.001)


def test_parse_meters_error():
    with pytest.raises(ValueError):
        parse_meters("1.2.3 m")

    with pytest.raises(ValueError):
        parse_meters("1.2.3")

    with pytest.raises(ValueError):
        parse_meters("abc m")
    
    with pytest.raises(TypeError):
        parse_meters([1.2])


def test_parse_maghi():
    test_vals = [
        ("1ℳ", 1),
        ("3.0 ℳ", 3),
        ("1e-2 dℳ", 0.001),
        ("40 kℳ", 40000),
        (".7e3 µℳ", 0.0007),
    ]

    for v, r in test_vals:
        assert parse_maghi(v) == pytest.approx(r, 0.001)


def test_parse_maghi_error():
    with pytest.raises(ValueError):
        parse_maghi("1.2.3 ℳ")

    with pytest.raises(ValueError):
        parse_maghi("1.2.3")

    with pytest.raises(ValueError):
        parse_maghi("abc ℳ")
    
    with pytest.raises(TypeError):
        parse_maghi([1.2])
