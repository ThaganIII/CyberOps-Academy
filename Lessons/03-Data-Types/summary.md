# Lesson 3 Summary - Data Types, Networking, and Conditional Logic

## Lesson Overview

Lesson 3 focused on understanding Python data types and applying them to cybersecurity and networking data.

The lesson started with basic data types and developed into a Network Alert Data Checker that collects information from an analyst, converts values into appropriate data types, validates user input, and uses conditional logic to make decisions.

---

# Learning Objectives

By completing this lesson, I learned how to:

- Identify common Python data types
- Use strings, integers, floats, and Booleans
- Check a value's data type using `type()`
- Convert user input using `int()` and `float()`
- Understand how `input()` handles user input
- Use `if`, `elif`, and `else`
- Understand the difference between `=` and `==`
- Create a basic `while` loop
- Exit a loop using `break`
- Validate user input
- Normalize user input using `.lower()`
- Understand the basic difference between IP addresses and ports
- Apply Python concepts to network alert information

---

# Python Data Types

The four main data types covered were:

| Data Type | Python Type | Example |
|---|---|---|
| String | `str` | `"192.168.1.10"` |
| Integer | `int` | `443` |
| Float | `float` | `87.5` |
| Boolean | `bool` | `True` |

Different types of cybersecurity information require different data types.

Example:

```python
source_ip = "192.168.1.10"
destination_port = 443
risk_score = 87.5
connection_allowed = True
```

---

# User Input and Type Conversion

One of the most important concepts from this lesson was learning that:

> `input()` returns a string.

For example:

```python
failed_logins = input("Enter failed logins: ")
```

If the user enters `12`, Python initially treats it as:

```python
"12"
```

To perform mathematical operations, the value can be converted:

```python
failed_logins = int(input("Enter failed logins: "))
```

Other conversions used in this lesson included:

```python
int()
float()
```

---

# Checking Data Types

The `type()` function can be used to inspect the data type of a value.

Example:

```python
print(type(destination_port))
```

Possible output:

```text
<class 'int'>
```

This was useful while testing and debugging the Network Alert program.

---

# Boolean Values

Booleans represent two states:

```python
True
False
```

One important discovery was that Python considers non-empty strings truthy.

For example:

```python
bool("yes")   # True
bool("no")    # True
bool("")      # False
```

Python does not understand the English meaning of `"no"` when converting a string to a Boolean.

Because of this, the program needed conditional logic to correctly convert `"yes"` and `"no"` into Boolean values.

---

# Assignment vs Comparison

The assignment operator:

```python
=
```

stores a value.

Example:

```python
destination_port = 443
```

The comparison operator:

```python
==
```

checks whether two values are equal.

Example:

```python
destination_port == 443
```

A comparison produces a Boolean result:

```text
True
```

or:

```text
False
```

---

# Conditional Logic

Conditional statements allow a program to make decisions.

Example:

```python
if destination_port == 22:
    print("SSH traffic detected")
elif destination_port == 443:
    print("HTTPS traffic detected")
else:
    print("Other network traffic")
```

The basic logic is:

```text
if
↓
Check first condition

elif
↓
Check another condition

else
↓
Handle everything else
```

Conditional logic is especially useful in cybersecurity automation because security tools frequently need to make decisions based on collected data.

---

# Loops

The program used:

```python
while True:
```

to repeatedly ask the user for input.

The loop continues until:

```python
break
```

is reached.

Example:

```python
while True:
    connection_input = input("Is the connection allowed? (yes/no): ").lower()

    if connection_input == "yes":
        connection_allowed = True
        break

    elif connection_input == "no":
        connection_allowed = False
        break

    else:
        print("Invalid response. Please enter yes or no.")
```

---

# Input Validation

Input validation prevents unexpected information from being treated as valid data.

Originally, logic such as:

```python
if connection_input == "yes":
    connection_allowed = True
else:
    connection_allowed = False
```

would treat anything other than `"yes"` as `False`.

That meant:

```text
no     → False
banana → False
hello  → False
```

This was a problem because invalid information was being treated as legitimate data.

The program was improved by specifically validating both `"yes"` and `"no"`.

---

# Input Normalization

The `.lower()` method was introduced to handle different capitalization.

Example:

```python
connection_input = input("Is the connection allowed? (yes/no): ").lower()
```

This converts:

```text
YES → yes
Yes → yes
yEs → yes
```

This makes input validation easier and more reliable.

---

# Networking Fundamentals

## IP Addresses

An IP address identifies a host or network interface involved in network communication.

Example:

```text
192.168.1.25
```

IP addresses were stored as strings in the program.

```python
source_ip = "192.168.1.25"
```

## Ports

A port identifies a service or application involved in network communication.

Examples:

```text
22  → commonly SSH
443 → commonly HTTPS
```

The IP address and port work together to help identify where network communication is occurring and which service is involved.

A simple analogy is:

```text
IP Address = Apartment building address
Port       = Apartment number
```

---

# Cybersecurity Analysis

The lesson also reinforced an important SOC concept:

> Suspicious activity does not automatically mean malicious activity.

An alert containing:

```text
Failed Logins:      12
Risk Score:         91.7
Connection Allowed: True
Destination Port:   443
```

may justify further investigation, but it does not provide enough evidence by itself to determine that malicious activity occurred.

An analyst may need to investigate:

- Authentication logs
- Network logs
- User activity
- Source and destination systems
- Destination IP/domain reputation
- Timeline of events
- Successful connections
- Downloads or execution
- Additional indicators of compromise

Another important lesson was:

> HTTPS does not automatically mean traffic is trustworthy.

HTTPS normally provides encrypted communication, but both legitimate and malicious applications can use encrypted connections.

---

# Project - Network Alert Data Checker

The main project for Lesson 3 was a Python Network Alert Data Checker.

The program collects:

- Source IP address
- Destination IP address
- Destination port
- Packet count
- Risk score
- Whether the connection was allowed

The project combines:

```text
User Input
    ↓
Type Conversion
    ↓
Input Validation
    ↓
Conditional Logic
    ↓
Formatted Network Alert
```

This project helped connect basic Python programming concepts with a realistic cybersecurity use case.

---

# Lessons Learned

## Technical Lesson

Data types affect how Python interprets and processes information.

I also learned that user input cannot always be trusted to be in the format that a program expects. Type conversion, validation, and normalization can help make programs more reliable.

Conditional statements allow programs to make decisions based on the information being processed.

## Cybersecurity Lesson

Security automation requires accurate data.

Invalid information should not silently become legitimate security data simply because the program was able to continue running.

I also learned that individual indicators should be investigated in context before determining whether activity is malicious.

## Personal Lesson

I understand the basic idea behind `if`, `elif`, and `else`, but I want more practice using conditional statements.

Future projects should continue using conditional logic so I can become more comfortable deciding when and how to use it instead of only memorizing the syntax.

---

# Skills Practiced

### Python

- Variables
- `str`
- `int`
- `float`
- `bool`
- `input()`
- `type()`
- `int()`
- `float()`
- `if`
- `elif`
- `else`
- `while`
- `break`
- `.lower()`
- Comparison operators
- Input validation

### Networking

- IP addresses
- Ports
- Basic network traffic interpretation
- HTTPS/443
- SSH/22

### Cybersecurity

- Network alert information
- Input integrity
- Alert investigation
- Evidence gathering
- Suspicious vs malicious activity
- SOC analyst decision-making

---

# Areas for Continued Practice

The main area I want to continue practicing is conditional logic.

I want additional experience using:

```python
if
elif
else
```

in different cybersecurity scenarios.

Rather than only being shown the completed code, I want to practice determining what conditions should be checked and writing the logic myself.

Networking terminology will also continue to be reinforced in future lessons.

---

# Lesson 3 Completion

Lesson 3 expanded the CyberOps Academy project from basic variables into programs that can store different types of information and make basic decisions.

The biggest progression was moving from:

```python
print("Something")
```

and storing variables to thinking about:

```text
What information did I receive?
        ↓
What data type should it be?
        ↓
Is the input valid?
        ↓
What condition is true?
        ↓
What should my program do?
```

This creates the foundation for more advanced cybersecurity automation.