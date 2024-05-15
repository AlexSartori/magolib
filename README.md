# MAGO-LIB

A Python library to format, parse, and convert numbers from meters to maghi.

## What's this, though?

### Meters (= boring 👎)

> Since 2019, the metre has been defined as the length of the path travelled by light in vacuum during a time interval of 1/299792458 of a second, where the second is defined by a hyperfine transition frequency of caesium.
>> One second is the time that elapses during 9.192631770 x 10E9 cycles of the radiation produced by the transition between two levels of the cesium-133 atom.

What the hell is even that? How could you ever recreate a precise meter if you found yourself in a forest alone or shipwrecked on a desert island? Important questions. But the International System of Units doesn't care about you.

### Maghi (= helpful! 👍)

How do you define a Mago? Simple enough! That's his height:

<p style="text-align:center">
    <img alt="Niccolò Marcon, the reference measure of a Mago" title="Niccolò Marcon, the reference measure of a Mago" src="mago.png" height="400px" />
</p>

Of course, you'll have already figured the advantages of such unit of measurement:

- Simple and immediate definition
- The size of a Niccolò is UNIVERSALLY known on Planet Earth
- This Niccolò has always existed and forever will
- Its length is unchanged since the dawn of time and is extremely stable (contrary to a standard meter) to:
  - Thermal variations
  - Mechanical fatigue
  - Aging and degradation
  - Chemical stress
  - Verbal abuse
  - Intense math classes (up to 8 hours of continued exposure)
  - Electromagnetic radiation
  - Ionizing radiation (under testing)
- If you dip a meter in Nutella it'll be ruined, a Mago will smile and thank you
- Conversion between meters and maghi is very straightforward
- A handy Python library is available to help migrate the world from metric to magic

#### Conventions:

- We denote a mago with the character: ℳ
- One ℳ equals approximately 1.93 meters
- All the standard multiples and submultiples apply:
  | Prefix | Name | Factor |
  |---|---|---|
  | p | pico | 1e-12 |
  | n | nano | 1e-9 |
  | µ, u | micro | 1e-6 |
  | m | milli | 1e-3 |
  | c | centi | 1e-2 |
  | d | deci | 1e-1 |
  |  |  | 1e0 |
  | da | deca | 1e1 |
  | h | etto | 1e2 |
  | k, K | kilo | 1e3 |
  | M | mega | 1e6 |
  | G | giga | 1e9 |
  | T | tera | 1e12 |

## Installation

Ensure you have Python and Pip installed in your system and run:

```
pip install magolib
```

Alternatively, you can clone this repository, `cd` into it, and run `pip install .`

## Usage

First off, import `magolib`:

```python
from magolib import *
```

Next, you can perform all these operations:

#### Convert meters to maghi

```python
>>> "34 meters equal %.2f maghi" % meters_to_maghi(34)
'34 meters equal 17.62 maghi'
```

#### Convert maghi to meters

```python
>>> "One Niccolò is said to be %.2f meters tall" % maghi_to_meters(1)
'One Niccolò is said to be 1.93 meters tall'
```

#### Format maghi as strings

```python
>>> "If you cut a Niccolò in 56 pieces and take 3, you get %s" % format_maghi(3/56)
'If you cut a Niccolò in 56 pieces and take 3, you get 5.36 cℳ  (centimaghi)'
```

#### Convert maghi subunits

```python
>>> "274638 maghi equals %.2f kilomaghi" % convert_maghi(274638, '', 'k')
'274638 maghi equals 274.64 kilomaghi'
```


#### Parse meters from string

```python
>>> "A giraffe hair can be as thick as %f meters" % parse_meters("350 um")
'A giraffe hair can be as thick as 0.000350 meters'
```


#### Parse maghi from string

```python
>>> "0.406 hℳ means %.2f maghi" % parse_maghi('0.406 hℳ')
'0.406 hℳ means 40.60 maghi'

# For simplicity, you can use an uppercase 'M' in place of the symbol 'ℳ
>>> "2.4e5 mM means %.2f maghi" % parse_maghi('2.4e5 mM')
'2.4e5 mM means 240.00 maghi'
```

#### Combine everything!

```python
>>> earth_circumference = parse_meters('40075.017 km')
>>> circ_in_maghi = meters_to_maghi(earth_circumference)
>>> "The Earth's circumference is %s" % format_maghi(circ_in_maghi)
"The Earth's circumference is 20.76 Mℳ  (megamaghi)"
```
