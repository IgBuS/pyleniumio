---
description: >-
  The command to select an <option> by its index within a <select> dropdown
  element.
---

# select\_by\_index

## Syntax

```python
Element.select_by_index(index: int) -> Element
```

## Usage

{% code title="correct usage" %}
```python
py.get("#dropdown").select_by_index(2)

---or--- # chain an Element command

py.get("#dropdown").select_by_index(0).get_attribute("value")
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, can only perform this command on a <select> dropdown element
py.get("ul > li").select_by_index(1)
```
{% endcode %}

## Arguments

* <mark style="color:purple;">`index (int)`</mark> - The **index** or "position" of the option to select.

## Yields

* <mark style="color:orange;">**Element**</mark> - The current instance of Element so you can chain commands.

## Examples

Given this HTML

```html
<select id="dropdown">
    <option value="" disabled="disabled" selected="selected">Please select an option</option>
    <option value="1">Option 1</option>
    <option value="2">Option 2</option>
</select>
```

We can select any of the options

```python
dropdown = py.get("dropdown")

# Select the first option that is "disabled"
dropdown.select_by_index(0)

# Select Option 1
dropdown.select_by_index(1)

# Select Option 2
dropdown.select_by_index(2)
```

{% hint style="info" %}
Give this a try yourself! [https://the-internet.herokuapp.com/dropdown](https://the-internet.herokuapp.com/dropdown)
{% endhint %}

## See also

* [select\__by\__text](select\_many.md)
* [select\__by\__value](select\_many-1.md)
* [click()](click.md) - If the dropdown is NOT a \<select> element, <mark style="color:purple;">`.click()`</mark> will work
