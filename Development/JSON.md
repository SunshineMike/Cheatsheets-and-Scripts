# JSON in Python Cheatsheet

A quick guide to working with JSON in Python, including setting, getting, and navigating nested structures.

## Table of Contents
1. [Introduction](#introduction)
2. [Importing the JSON Library](#importing-the-json-library)
3. [Parsing JSON](#parsing-json)
4. [Outputting JSON](#outputting-json)
5. [Working with JSON Data](#working-with-json-data)

---

## Introduction

JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate.

---

## Importing the JSON Library

To work with JSON in Python, you'll first need to import the `json` module:

```python
import json
```

---

## Parsing JSON

To convert a JSON string into a Python object:

```python
data = '{"name": "John", "age": 30, "city": "New York"}'
parsed_data = json.loads(data)
```

---

## Outputting JSON

To convert a Python object into a JSON string:

```python
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
json_string = json.dumps(data)
```

---

## Working with JSON Data

### Get Value

To retrieve a value from a JSON object (which becomes a dictionary in Python):

```python
age = parsed_data["age"]  # Returns 30
```

### Set Value

To set a value in a JSON object:

```python
parsed_data["age"] = 31
```

### Get Nested Values

For nested JSON objects:

```python
nested_data = '{"employee": {"name": "Anna", "age": 25, "department": {"id": 1, "name": "HR"}}}'
parsed_nested_data = json.loads(nested_data)

department_name = parsed_nested_data["employee"]["department"]["name"]  # Returns "HR"
```

### Set Nested Values

To set a value in a nested JSON object:

```python
parsed_nested_data["employee"]["department"]["name"] = "Finance"
```

---
