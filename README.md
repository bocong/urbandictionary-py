# urbandictionary-py
Simple Python wrapper for Urban Dictionary API.

## UrbanDef

This module defines an **UrbanDef**, an object to represent each Urban Dictionary definition.
**UrbanDef** has the following accessible attributes:
* **word**: the word being defined,
* **definition**: the word's definition,
* **example**: usage example,
* **upvotes**: number of upvotes on Urban Dictionary,
* **downvotes**: number of downvotes on Urban Dictionary

**UrbanDef** objects have a comparison function based solely on the number of upvotes/downvotes.

## Usage

Import the module:
```python
import urbandictionary as ud
# adding import alias recommended
```

Lookup by word:
```python
defs = ud.define('netflix and chill')

>	[<List of UrbanDef objects>]
```

Lookup random words:
```python
rand = ud.random()

>	[<List of UrbanDef objects>]
```

Read definitions:
```python
for d in defs:
	print d.definition

>	It means that you are going to go over ...
> 	<other Netflix and Chill definitions> ...
```

