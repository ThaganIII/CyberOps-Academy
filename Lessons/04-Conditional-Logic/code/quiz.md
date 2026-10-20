# Lesson 04 — Conditional Logic & Security Decisions

## Python & SOC Analyst Knowledge Quiz

**Topic:** Conditional Logic, Boolean Operators, Input Validation, and SOC Alert Triage  
**Total Questions:** 10  
**Difficulty:** Beginner / Junior SOC Analyst

---

## Quiz Questions

### Question 1 — Comparison Operators

What does the following Python expression evaluate to?

```python
risk_score = 75
print(risk_score >= 80)
```

A. True  
B. False  
C. 75  
D. Error

### Question 2 — Assignment vs. Comparison

Explain the difference between the following statements:

```python
failed_logins = 5
failed_logins == 5
```

Why would you use each one?

### Question 3 — AND Operator

Review the following code:

```python
malware_detected = True
connection_allowed = False

if malware_detected and connection_allowed:
    print("Critical Alert")
else:
    print("Investigate Further")
```

What will Python print, and why?

### Question 4 — OR Operator

A SOC analyst wants an alert to be reviewed if either the risk score is at least 60 or there are at least 10 failed login attempts.

Given:

```python
risk_score = 45
failed_logins = 12
```

Write a Python conditional statement that prints `"Review Alert"` when the rule is satisfied.

### Question 5 — NOT Operator

Given:

```python
known_ip = False
```

What will the following code print?

```python
if not known_ip:
    print("Unknown Source IP")
else:
    print("Known Source IP")
```

Explain what the `not` operator does.

### Question 6 — Compound Conditions

Review the following code:

```python
risk_score = 90
malware_detected = False
known_ip = False

if risk_score >= 80 and (malware_detected or not known_ip):
    print("Escalate")
else:
    print("Monitor")
```

What will Python print?

Explain how the parentheses affect the conditional statement.

### Question 7 — Exception Handling

A security analyst enters `"hello"` when prompted for a destination port.

```python
try:
    destination_port = int(input("Enter destination port: "))
except ValueError:
    print("Invalid port number")
```

What happens, and why does the program behave this way?

### Question 8 — Input Validation

A program needs to accept destination port numbers from 0 through 65535.

Complete the missing condition:

```python
destination_port = int(input("Enter port: "))

if __________________________:
    print("Invalid port")
else:
    print("Valid port")
```

### Question 9 — IPv4 Validation

Which of the following are valid IPv4 addresses? Select all that apply.

A. `192.168.10.5`  
B. `10.0.0.999`  
C. `172.16.0.100`  
D. `192.168.1`

Explain why the invalid addresses are incorrect.

### Question 10 — SOC Alert Classification

A SOC Alert Triage Tool receives the following information:

```python
risk_score = 95
failed_logins = 3
known_ip = True
malware_detected = True
connection_allowed = True
```

The tool uses these rules:

```python
if risk_score >= 80 and connection_allowed and malware_detected:
    classification = "CRITICAL"

elif risk_score >= 80 and (not known_ip or failed_logins >= 10):
    classification = "HIGH"

elif risk_score >= 50 or failed_logins >= 5:
    classification = "MEDIUM"

else:
    classification = "LOW"
```

What classification will be assigned?

Explain why Python chooses that classification.

---

# Answer Section

### Answer 1 — Comparison Operators

**Correct Answer: B. False**

The risk score is 75, which is below 80.

The `>=` operator checks whether the left value is greater than or equal to the right value.

### Answer 2 — Assignment vs. Comparison

`=` assigns a value to a variable.

```python
failed_logins = 5
```

`==` compares two values and returns either `True` or `False`.

```python
failed_logins == 5
```

Assignment is used to store information. Comparison is used when evaluating conditions.

### Answer 3 — AND Operator

**Correct Answer: Investigate Further**

The `and` operator requires both conditions to be True.

Although `malware_detected` is True, `connection_allowed` is False.

Therefore, the condition fails and Python executes the `else` block.

### Answer 4 — OR Operator

```python
if risk_score >= 60 or failed_logins >= 10:
    print("Review Alert")
```

The `or` operator requires at least one condition to be True.

The risk score is below 60, but 12 failed logins exceeds the threshold of 10.

Therefore, the alert is reviewed.

### Answer 5 — NOT Operator

**Correct Answer: Unknown Source IP**

The `not` operator reverses a Boolean value.

Since `known_ip` is False, `not known_ip` evaluates to True.

Python executes the first `print()` statement.

### Answer 6 — Compound Conditions

**Correct Answer: Escalate**

The risk score is 90, satisfying the first requirement.

Inside the parentheses:

- `malware_detected` is False.
- `not known_ip` is True.

Because the `or` condition is True, the entire expression evaluates to True.

Parentheses group the conditions to make the intended logic clear.

### Answer 7 — Exception Handling

**Correct Answer: Invalid port number**

Python attempts to convert `"hello"` into an integer.

Because `"hello"` is not a valid integer, Python raises a `ValueError`.

The `except ValueError` block catches the error and prints the message instead of allowing the exception to terminate the program.

### Answer 8 — Input Validation

**Correct Answer:**

```python
if destination_port < 0 or destination_port > 65535:
```

This rejects any number outside the accepted port range.

The condition uses `or` because either an excessively low or excessively high number is invalid.

### Answer 9 — IPv4 Validation

**Correct Answers: A and C**

- A. `192.168.10.5` — Valid.
- B. `10.0.0.999` — Invalid because 999 exceeds 255.
- C. `172.16.0.100` — Valid.
- D. `192.168.1` — Invalid because it contains only three octets.

A valid IPv4 address contains four octets, each between 0 and 255.

### Answer 10 — SOC Alert Classification

**Correct Answer: CRITICAL**

The first conditional statement evaluates to True because:

- The risk score is 95, meeting the threshold of 80.
- The connection is allowed.
- Malware was detected.

Python assigns the classification `"CRITICAL"`.

Because the first condition succeeds, Python skips the remaining `elif` and `else` statements.

---

## Key Lessons Reviewed

1. Comparison operators evaluate relationships between values.
2. Conditional statements control how Python makes decisions.
3. Boolean operators combine multiple conditions.
4. Parentheses help group logical expressions.
5. Input validation checks that values meet defined requirements.
6. Exception handling allows programs to respond to expected errors.
7. IPv4 validation helps reject incorrectly formatted addresses.
8. SOC alert triage can use predefined rules to recommend investigation priorities.

## Lesson 04 — Quiz Complete