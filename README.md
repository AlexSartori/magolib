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
import magolib
```

Next, you can perform all these operations:

#### Convert meters to maghi

```python
>>> magolib.meters_to_maghi(1.0)
0.5181347150259068
>>> magolib.meters_to_maghi(-0.58)
-0.3005181347150259
>>> magolib.meters_to_maghi(2.3e4)
11917.098445595855
```

#### Convert maghi to meters

```python
>>> magolib.maghi_to_meters(1.0)
1.93
>>> magolib.maghi_to_meters(-42.5)
-82.02499999999999
>>> magolib.maghi_to_meters(1.9e-2)
0.03667
```

#### Format maghi as strings

```python
>>> magolib.format_maghi(1.0)
'1.00 ℳ  (maghi)'
>>> magolib.format_maghi(3.4e-10)
'340.00 pℳ  (picomaghi)'
>>> magolib.format_maghi(23e6)
'23.00 Mℳ  (megamaghi)'
```

#### Convert maghi subunits

```python
>>> magolib.convert_maghi(1.0, '', 'k')
0.001
>>> magolib.convert_maghi(5, 'h', '')
500.0
>>> magolib.convert_maghi(7.2, 'm', 'u')
7200.000000000001
```


#### Parse meters from string

```python
>>> magolib.parse_meters('-2e3 km')
-2000000.0
>>> magolib.parse_meters('1 m')
1.0
>>> magolib.parse_meters('.3 dm')
0.03
>>> magolib.parse_meters('-2e3 km')
-2000000.0
```


#### Parse maghi from string

```python
>>> magolib.parse_maghi('1ℳ')
1.0
>>> magolib.parse_maghi('1M')
1.0
>>> magolib.parse_maghi('3 mM')
0.003
```

*Note: here for simplicity you can use an uppercase 'M' in place of the symbol 'ℳ'*
