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
    if isinstance(meters, (int, float)):
        return meters / CONVERSION_FACTOR
    else:
        raise TypeError("Invalid input type: " + str(type(meters)))


def maghi_to_meters(maghi: float|int) -> float:
    if isinstance(maghi, (int, float)):
        return maghi * CONVERSION_FACTOR
    else:
        raise TypeError("Invalid input type: " + str(type(maghi)))


def format_maghi(maghi: float|int) -> str:
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
    if not isinstance(s, str):
        raise TypeError("Invalid input type: " + str(type(s)))
    
    reg_res = re.match(r"([0-9]*\.?[0-9]+(?:e-?[0-9]+)?) ?(.*m)", s.strip())
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
    if not isinstance(s, str):
        raise TypeError("Invalid input type: " + str(type(s)))
    
    reg_res = re.match(r"([0-9]*\.?[0-9]+(?:e-?[0-9]+)?) ?(.*" + UNIT_SYMBOL + ")", s.strip())
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
