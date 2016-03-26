# urbandictionary-py
Simple Python wrapper for Urban Dictionary API.

## Installation

With PyPI:
```
pip install urbandictionary
```

Without PyPI, fork/download, then:
```
python setup.py install
```

## Usage

### UrbanDefinition

This module defines **UrbanDefinition**, an object to represent each Urban Dictionary definition.
**UrbanDefinition** has the following accessible attributes:
* **word**: the word being defined,
* **definition**: the word's definition,
* **example**: usage example,
* **upvotes**: number of upvotes on Urban Dictionary,
* **downvotes**: number of downvotes on Urban Dictionary

### Examples

Import the module:
```python
import urbandictionary as ud
# adding import alias recommended
```

Lookup by word:
```python
defs = ud.define('netflix and chill')

>	[List of UrbanDef objects]
```

Lookup random words:
```python
rand = ud.random()

>	[List of UrbanDef objects]
```

Read definitions:
```python
for d in defs:
	print(d.definition)

>	It means that you are going to go over ...
>	code for two people going to each others ...
> 	<other Netflix and Chill definitions> ...
```

UrbanDefinition string representation:
```python
for d in defs:
	print(d)

>	Netflix and Chill: It means that you are going to go over to your par... (21776, 7750)
>	netflix and chill: code for two people going to each others houses an... (8056, 2622)
>	<word>: <definition trimmed to 50 characters> (<upvotes>, <downvotes>)
```

