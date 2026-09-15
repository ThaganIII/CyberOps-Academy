# Lesson 3 Notes - Data Types, Networking, and Conditional Logic

## Data Types

A data type tells Python what kind of information is stored in a variable.

The four main data types covered in this lesson are:

| Data Type | Python | Example | Cybersecurity Example |
|---|---|---|---|
| String | `str` | `"hello"` | IP address, username, hostname |
| Integer | `int` | `443` | Port number, failed logins, packet count |
| Float | `float` | `87.5` | Risk score, percentage |
| Boolean | `bool` | `True` / `False` | Connection allowed, account locked |

### String - `str`

Strings contain text.

```python
source_ip = "192.168.1.1"
username = "admin"
protocol = "TCP"
```

Even though an IP address contains numbers, it is normally treated as a string because we are not performing normal math with the IP address.

---

## Integer - `int`

Integers are whole numbers without decimals.

```python
destination_port = 443
packet_count = 123
failed_logins = 8
```

Cybersecurity examples include:

- Port numbers
- Packet counts
- Failed login counts
- Number of alerts

---

## Float - `float`

Floats contain decimal values.

```python
risk_score = 87.5
```

Cybersecurity examples could include:

- Risk scores
- Percentages
- CPU usage
- Response times

User input can be converted to a float:

```python
risk_score = float(input("Enter the risk score: "))
```

---

## Boolean - `bool`

A Boolean can only represent:

```python
True
False
```

Examples:

```python
connection_allowed = True
account_locked = False
```

Booleans are useful when something has two possible states.

Examples:

- Connection allowed or blocked
- Account locked or unlocked
- Malware detected or not detected
- Alert investigated or not investigated

---

# Checking Data Types with `type()`

The `type()` function tells us the data type of a value.

Example:

```python
source_ip = "192.168.1.1"

print(type(source_ip))
```

Output:

```text
<class 'str'>
```

For now, `<class 'str'>` can be understood as:

> This value belongs to the string data type.

Examples:

```python
print(type("192.168.1.1"))
print(type(443))
print(type(87.5))
print(type(True))
```

Output:

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

---

# `input()` Returns a String

An important rule learned in this lesson:

> `input()` returns a string.

Example:

```python
failed_logins = input("Enter failed logins: ")
```

If the user enters:

```text
8
```

Python initially stores:

```python
"8"
```

not:

```python
8
```

That means this will fail:

```python
failed_logins = input("Enter failed logins: ")

print(failed_logins + 5)
```

Python cannot directly add:

```text
"8" + 5
```

because one value is a string and the other is an integer.

---

# Type Conversion

Type conversion changes a value from one data type to another.

## `int()`

Convert a value to an integer:

```python
failed_logins = int(input("Enter failed logins: "))
```

If the user enters `8`:

```text
input() → "8"
int("8") → 8
8 + 5 → 13
```

---

## `float()`

Convert a value to a decimal number:

```python
risk_score = float(input("Enter the risk score: "))
```

User enters:

```text
33.3
```

Python stores:

```python
33.3
```

as a `float`.

---

# Boolean Conversion

Using `bool()` on strings can produce unexpected results.

Examples:

```python
print(bool("yes"))
print(bool("no"))
print(bool(""))
```

Output:

```text
True
True
False
```

Why?

Python does not understand that the English word `"no"` means false.

Instead:

```text
Non-empty string → True
Empty string     → False
```

Therefore:

```python
bool("no")
```

returns:

```python
True
```

This means we should not use this:

```python
connection_allowed = bool(input("Connection allowed? "))
```

when we want `"yes"` and `"no"` to represent Boolean values.

---

# Assignment vs Comparison

## `=` - Assignment

One equal sign assigns a value to a variable.

```python
destination_port = 443
```

Read this as:

> Store `443` inside `destination_port`.

---

## `==` - Comparison

Two equal signs compare values.

```python
destination_port == 443
```

Read this as:

> Is `destination_port` equal to `443`?

A comparison produces a Boolean:

```python
destination_port = 443

print(destination_port == 443)
```

Output:

```text
True
```

---

# Conditional Statements

Conditional statements allow Python programs to make decisions.

## `if`

`if` means:

> If this condition is True, run this code.

Example:

```python
destination_port = 22

if destination_port == 22:
    print("SSH traffic detected")
```

Because:

```text
22 == 22 → True
```

Python runs the `print()` statement.

---

## `else`

`else` means:

> If the previous condition was not True, do this instead.

Example:

```python
destination_port = 443

if destination_port == 22:
    print("SSH traffic detected")
else:
    print("Traffic is not SSH")
```

---

## `elif`

`elif` means:

> Else if another condition is True, do this.

Example:

```python
if connection_input == "yes":
    connection_allowed = True

elif connection_input == "no":
    connection_allowed = False

else:
    print("Invalid response")
```

This allows the program to check multiple possibilities.

---

# While Loops

A `while` loop repeats code while a condition remains True.

Example:

```python
while True:
    print("This keeps running")
```

`while True:` creates a loop that will continue until something tells Python to stop.

---

# `break`

`break` tells Python to immediately exit a loop.

Example:

```python
while True:
    answer = input("Enter yes: ")

    if answer == "yes":
        break
```

The program continues asking until the user enters:

```text
yes
```

---

# Input Validation

Input validation checks whether user-provided information meets the requirements of the program.

Our Network Alert program needs the user to enter either:

```text
yes
```

or:

```text
no
```

We added:

```python
while True:
    connection_input = input("Is the connection allowed? (yes/no): ")

    if connection_input == "yes":
        connection_allowed = True
        break

    elif connection_input == "no":
        connection_allowed = False
        break

    else:
        print("Invalid response. Please enter yes or no.")
```

The logic is:

```text
yes
 ↓
True
 ↓
break

no
 ↓
False
 ↓
break

anything else
 ↓
invalid response
 ↓
ask again
```

This prevents invalid information such as `"banana"` from silently being stored as a legitimate answer.

---

# Input Normalization

Python strings are case-sensitive.

For example:

```python
"YES" == "yes"
```

returns:

```text
False
```

The `.lower()` string method can convert user input to lowercase:

```python
connection_input = input(
    "Is the connection allowed? (yes/no): "
).lower()
```

This allows:

```text
YES
Yes
yes
```

to all become:

```text
yes
```

Likewise:

```text
NO
No
no
```

becomes:

```text
no
```

This is called normalizing input.

---

# Networking Fundamentals

## IP Address

An IP address identifies a host/network interface on a network.

Example:

```text
192.168.1.1
```

In Python, an IP address is commonly stored as a string:

```python
source_ip = "192.168.1.1"
```

---

## Port

A port identifies a service or application communicating on a host.

Example:

```text
22 → SSH
443 → HTTPS
```

A port number is normally stored as an integer:

```python
destination_port = 443
```

### Simple Analogy

Think of an IP address as the address of an apartment building.

The port is the apartment number.

The IP gets traffic to the correct host.

The port helps get the traffic to the correct service on that host.

---

# Network Alert Data Checker

During Lesson 3, I created a program that collects:

- Source IP address
- Destination IP address
- Destination port
- Packet count
- Risk score
- Whether the connection was allowed

The program uses several different Python data types:

```text
Source IP          → str
Destination IP     → str
Destination Port   → int
Packet Count       → int
Risk Score         → float
Connection Allowed → bool
```

The program was then improved with conditional logic and input validation so invalid yes/no answers are rejected.

---

# Debugging Techniques

I used `type()` to inspect variables while troubleshooting the program.

Example:

```python
print(type(connection_allowed))
```

Temporary debugging statements are useful while developing a program but can be removed or commented out once the program works correctly.

I also learned that testing unexpected values is important.

Instead of testing only:

```text
yes
no
```

I deliberately tested invalid values to verify that the validation worked.

---

# Cybersecurity Connection

Correct data types and input validation matter in cybersecurity automation because inaccurate data can lead to inaccurate analysis.

For example, automatically treating an invalid answer as:

```python
connection_allowed = False
```

could cause a security tool to record information that the analyst never actually provided.

Validation helps protect the integrity and reliability of the data being processed.

---

# Key Takeaways

- `str` stores text.
- `int` stores whole numbers.
- `float` stores decimal numbers.
- `bool` stores `True` or `False`.
- `type()` identifies the type of a value.
- `input()` returns a string.
- `int()` and `float()` perform type conversion.
- Non-empty strings are truthy, even `"no"`.
- `=` assigns a value.
- `==` compares values.
- `if`, `elif`, and `else` allow programs to make decisions.
- `while` allows code to repeat.
- `break` exits a loop.
- Input validation prevents invalid data from being accepted.
- `.lower()` can normalize text input.
- IP addresses and ports identify different parts of network communication.