# Lesson 04 — Conditional Logic & Security Decisions

## Learning Objectives

- Understand comparison operators.
- Use `if`, `elif`, and `else` to make decisions.
- Combine conditions using `and`, `or`, and `not`.
- Group conditions using parentheses.
- Validate user input.
- Handle errors using `try` and `except`.
- Apply conditional logic to SOC alert triage.

## 1. Comparison Operators

Comparison operators compare two values and produce a Boolean result.

| Operator | Meaning | Example |
|---|---|---|
| `==` | Equal to | `risk_score == 80` |
| `!=` | Not equal to | `port != 443` |
| `>` | Greater than | `failed_logins > 5` |
| `<` | Less than | `risk_score < 50` |
| `>=` | Greater than or equal to | `risk_score >= 80` |
| `<=` | Less than or equal to | `risk_score <= 100` |

**Important:** `=` assigns a value, while `==` compares values.

## 2. Conditional Statements

Conditional statements allow a program to make decisions.

```python
risk_score = 85

if risk_score >= 80:
    print("HIGH")
elif risk_score >= 50:
    print("MEDIUM")
else:
    print("LOW")
```

Python evaluates the conditions from top to bottom. Once a matching branch is found, the remaining branches in that chain are skipped.

## 3. Boolean Operators

### AND

Both conditions must be True.

```python
if risk_score >= 80 and malware_detected:
    print("Critical alert")
```

### OR

At least one condition must be True.

```python
if risk_score >= 50 or failed_logins >= 5:
    print("Review alert")
```

### NOT

Reverses a Boolean value.

```python
known_ip = False

if not known_ip:
    print("Unknown IP")
```

`not False` evaluates to `True`.

## 4. Parentheses and Compound Conditions

Parentheses group conditions and clarify how a rule should be evaluated.

```python
if risk_score >= 80 and (malware_detected or not known_ip):
    print("Escalate alert")
```

The risk score must be at least 80, and at least one condition inside the parentheses must be True.

Parentheses are not required simply because a statement contains three conditions.

## 5. Input Validation

Input validation checks whether entered data meets the program's requirements.

```python
while True:
    try:
        destination_port = int(input("Enter destination port: "))

        if destination_port < 0 or destination_port > 65535:
            print("Invalid port.")
        else:
            break

    except ValueError:
        print("Please enter a valid number.")
```

This checks both data type and allowed range.

Port numbers range from 0 to 65535. Port 0 is reserved and is not normally used as a destination service port.

## 6. Exception Handling

`try` attempts to execute code.

`except ValueError` handles a value-related error, such as converting text into an integer.

```python
try:
    failed_logins = int(input("Enter failed logins: "))
except ValueError:
    print("Invalid number.")
```

Exception handling prevents certain expected errors from terminating the program unexpectedly.

## 7. Loops and Break

`while True` creates a loop that continues until it encounters `break` or another exit.

This is useful when repeatedly asking an analyst for valid input.

## 8. IPv4 Validation

An IPv4 address contains four octets, each ranging from 0 to 255.

Python includes the `ipaddress` module.

```python
import ipaddress

while True:
    source_ip = input("Enter IPv4 address: ")

    try:
        ipaddress.IPv4Address(source_ip)
        break
    except ValueError:
        print("Invalid IPv4 address.")
```

This verifies IPv4 syntax. It does not establish whether an IP address is trusted, malicious, or appropriate for use on a specific