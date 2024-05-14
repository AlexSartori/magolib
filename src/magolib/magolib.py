from typing import List
import re


# Constants
CONVERSION_FACTOR = 1.93
UNIT_SYMBOL = u"ℳ"

class Subunit:
    def __init__(self, factor: float, symbol: str|List[str], name: str) -> None:
        self.factor: float = factor

        if type(symbol) is not list:
            self.symbols: List[str] = [symbol]
        else:
            self.symbols: List[str] = symbol
       
        self.name: str = name


# Conversion factors
subunits = [
    Subunit(1e-12, 'p', "picomaghi"),
    Subunit(1e-9, 'n', "nanomaghi"),
    Subunit(1e-6, ['µ', 'u'], "micromaghi"),
    Subunit(1e-3, 'm', "millimaghi"),
    Subunit(1e-2, 'c', "centimaghi"),
    Subunit(1e-1, 'd', "decimaghi"),
    Subunit(1e0, '', "maghi"),
    Subunit(1e1, 'da', "decamaghi"),
    Subunit(1e2, 'h', "ettomaghi"),
    Subunit(1e3, ['k', 'K'], "kilomaghi"),
    Subunit(1e6, 'M', "megamaghi"),
    Subunit(1e9, 'G', "gigamaghi"),
    Subunit(1e12, 'T', "teramaghi")
]


def meters_to_maghi(meters: float|int) -> float:
    '''
    Convert meters to maghi.

    Args:
        meters: The value in meters to convert.

    Returns:
        The value in maghi.

    Raises:
        TypeError: If the input is not a number.

    Example:
        >>> meters_to_maghi(1)
        0.52
    '''

    if isinstance(meters, (int, float)):
        return meters / CONVERSION_FACTOR
    else:
        raise TypeError("Invalid input type: " + str(type(meters)))


def maghi_to_meters(maghi: float|int) -> float:
    '''
    Convert maghi to meters.

    Args:
        maghi: The value in maghi to convert.
    
    Returns:
        The value in meters.

    Raises:
        TypeError: If the input is not a number.

    Example:
        >>> maghi_to_meters(1)
        1.93
    '''

    if isinstance(maghi, (int, float)):
        return maghi * CONVERSION_FACTOR
    else:
        raise TypeError("Invalid input type: " + str(type(maghi)))


# TODO: Negative numbers probably break this function
def format_maghi(maghi: float|int) -> str:
    '''
    Format a maghi value as a string.

    Args:
        maghi: The value in maghi to format.
    
    Returns:
        A string representation of the maghi value.

    Raises:
        TypeError: If the input is not a number.

    Example:
        >>> format_maghi(1)
        '1.00 ℳ  (maghi)'
    '''

    if not isinstance(maghi, (int, float)):
        raise TypeError("Invalid input type: " + str(type(maghi)))
    
    val, unit_prefix, unit_name = None, None, None
    for idx, subunit in enumerate(sorted(subunits, key=lambda x: x.factor)):
        if idx == len(subunits) - 1 or maghi < subunits[idx+1].factor:
            val = maghi / subunit.factor
            unit_prefix = subunit.symbols[0]
            unit_name = subunit.name
            break
    
    return "%.2f %s  (%s)" % (val, unit_prefix + UNIT_SYMBOL, unit_name)


def convert_maghi(val: float|int, from_unit: str, to_unit: str) -> int:
    '''
    Convert a value from one maghi unit to another.

    Args:
        val: The value to convert.
        from_unit: The unit to convert from.
        to_unit: The unit to convert to.

    Returns:
        The converted value.

    Raises:
        TypeError: If the input types are invalid.
        ValueError: If the input units are invalid.

    Example:
        >>> convert_maghi(1, 'm', 'k')
        0.001
    '''
    
    if not isinstance(val, (int, float)):
        raise TypeError("Invalid input type for 'val': " + str(type(val)))
    if not isinstance(from_unit, str):
        raise TypeError("Invalid input type for 'from_unit': " + str(type(from_unit)))
    if not isinstance(to_unit, str):
        raise TypeError("Invalid input type for 'to_unit': " + str(type(to_unit)))

    unit1, unit2 = None, None
    for subunit in subunits:
        if from_unit in subunit.symbols:
            unit1 = subunit
        if to_unit in subunit.symbols:
            unit2 = subunit
        if unit1 is not None and unit2 is not None:
            break
    
    if unit1 is None:
        raise ValueError("Unknown starting unit: " + from_unit)
    if unit2 is None:
        raise ValueError("Unknown desired unit: " + to_unit)
    
    factor = unit1.factor / unit2.factor
    return val * factor


def parse_meters(s: str) -> float:
    '''
    Parse a string representing meters into a float.

    Args:
        s: The string to parse.

    Returns:
        The float representation of the input string.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input string is not in the correct format.

    Example:
        >>> parse_meters("1 m")
        1.0
    '''
    
    if not isinstance(s, str):
        raise TypeError("Invalid input type: " + str(type(s)))
    
    reg_res = re.match(r"(-?[0-9]*\.?[0-9]+(?:e-?[0-9]+)?) ?(.*m)", s.strip())
    if reg_res is None:
        raise ValueError("Invalid format: '" + s + "'")
    
    val, unit = reg_res.groups()
    try:
        val = float(val)
        unit = unit[:-1]
    except:
        raise ValueError("Could not parse string: '" + s + "'")
    
    for subunit in subunits:
        if unit in subunit.symbols:
            return val * subunit.factor
    
    raise ValueError("Invalid unit: '" + unit + "'")


def parse_maghi(s: str) -> float:
    '''
    Parse a string representing maghi into a float.

    Args:
        s: The string to parse.

    Returns:
        The float representation of the input string.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input string is not in the correct format.

    Example:
        >>> parse_maghi("1 ℳ")
        1.0
    '''
    
    if not isinstance(s, str):
        raise TypeError("Invalid input type: " + str(type(s)))
    
    reg_res = re.match(r"(-?[0-9]*\.?[0-9]+(?:e-?[0-9]+)?) ?(.*[" + UNIT_SYMBOL + "|M])", s.strip())
    if reg_res is None:
        raise ValueError("Invalid format: '" + s + "'")
    
    val, unit = reg_res.groups()
    try:
        val = float(val)
        unit = unit[:-1]
    except:
        raise ValueError("Could not parse string: '" + s + "'")
    
    for subunit in subunits:
        if unit in subunit.symbols:
            return val * subunit.factor
    
    raise ValueError("Invalid unit: '" + unit + "'")
