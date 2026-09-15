# Quiz

1. Which data type should store the port number 443?

        A. str
        B. int
        C. bool
        D. float

2. Which data type should store 87.5?

        A. float
        B. int
        C. str
        D. bool

3. Why does this fail?

        failed_logins = input("Failed logins: ")
        print(failed_logins + 5)
        
4. What does int() do?

#

## Answers

1.      B
2.      A
3.      Python assumes everything is a string. input() returns       everything as a string.

4.      int() converts a string containing a whole number into an integer.

# Lesson 3 Quiz PT.2 - Data Types, Networking, and Conditional Logic

## Q1 - Data Types

Given the following network alert:

```text
Source IP:          192.168.1.25
Destination Port:   443
Packet Count:       250
Risk Score:         72.5
Connection Allowed: True
```

What Python data type should be used for each value?

```text
Source IP =
Destination Port =
Packet Count =
Risk Score =
Connection Allowed =
```

---

## Q2 - Understanding `input()`

Why would the following code cause a problem?

```python
failed_logins = input("Enter failed logins: ")
print(failed_logins + 5)
```

What does `input()` return, and how can the problem be fixed?

---

## Q3 - Assignment vs Comparison

Explain the difference between:

```python
destination_port = 443
```

and:

```python
destination_port == 443
```

---

## Q4 - Boolean Behavior

Why does the following return `True` instead of `False`?

```python
bool("no")
```

---

## Q5 - Conditional Logic

In your own words, explain what each of the following does:

```text
if =
elif =
else =
```

---

## Q6 - Loops

Why did we use:

```python
while True:
```

and:

```python
break
```

in the Network Alert program?

---

## Q7 - Input Validation

Why could the following code be dangerous in a cybersecurity tool?

```python
if connection_input == "yes":
    connection_allowed = True
else:
    connection_allowed = False
```

Think about what would happen if the user entered:

```text
banana
```

---

## Q8 - Input Normalization

What problem does `.lower()` solve in the following code?

```python
connection_input = input("Allowed? ").lower()
```

---

## Q9 - Networking

Explain the difference between an **IP address** and a **port**.

Then explain what the following represents:

```text
192.168.1.25:443
```

---

## Q10 - SOC Analysis Scenario

You are investigating the following alert:

```text
Source IP:          10.0.0.25
Destination IP:     172.217.5.110
Destination Port:   443
Failed Logins:      12
Risk Score:         91.7
Connection Allowed: True
```

Answer the following:

1. Which fields should be stored as `str`, `int`, `float`, and `bool`?
2. Which information would immediately catch your attention as a SOC analyst?
3. Based only on the information provided, can you determine that the activity is malicious? Why or why not?
4. What additional information would you investigate before making a final determination?

---

# Answer Section

## Q1 - Answer

```text
Source IP          = String (str)
Destination Port   = Integer (int)
Packet Count       = Integer (int)
Risk Score         = Float (float)
Connection Allowed = Boolean (bool)
```

---

## Q2 - Answer

`input()` always returns user input as a **string**.

If the user enters:

```text
12
```

Python initially stores:

```python
"12"
```

Because `"12"` is a string, Python cannot directly perform:

```python
"12" + 5
```

The input needs to be converted to an integer:

```python
failed_logins = int(input("Enter failed logins: "))
print(failed_logins + 5)
```

Now Python can perform:

```text
12 + 5 = 17
```

### What I Learned

`input()` returns a string. If I need to perform mathematical operations on the value, I may need to convert it to an `int` or `float`.

---

## Q3 - Answer

`=` is the **assignment operator**.

```python
destination_port = 443
```

This means:

> Store the value `443` inside the variable `destination_port`.

`==` is a **comparison operator**.

```python
destination_port == 443
```

This means:

> Check whether the value stored in `destination_port` is equal to `443`.

The comparison will return either:

```python
True
```

or:

```python
False
```

---

## Q4 - Answer

Python considers `"no"` to be `True` because `"no"` is a **non-empty string**.

Python is not interpreting the English meaning of the word `no`.

For example:

```python
bool("yes")    # True
bool("no")     # True
bool("False")  # True
bool("")       # False
```

An empty string is considered false, while a non-empty string is considered true.

---

## Q5 - Answer

### `if`

Checks the first condition.

```python
if destination_port == 22:
    print("SSH")
```

### `elif`

If the previous condition was false, `elif` checks another condition.

```python
elif destination_port == 443:
    print("HTTPS")
```

### `else`

Runs when none of the previous conditions were true.

```python
else:
    print("Other traffic")
```

Together:

```python
if destination_port == 22:
    print("SSH")
elif destination_port == 443:
    print("HTTPS")
else:
    print("Other traffic")
```

---

## Q6 - Answer

`while True:` creates a loop that continues running until something explicitly stops it.

```python
while True:
```

We used it so the program would continue asking the user for an answer if invalid information was entered.

`break` exits the loop.

Example:

```python
while True:
    connection_input = input("Is the connection allowed? (yes/no): ")

    if connection_input == "yes":
        connection_allowed = True
        break
```

Once valid input is received, `break` stops the loop and allows the program to continue.

---

## Q7 - Answer

The problem is that every value other than `"yes"` would automatically be treated as `False`.

For example:

```text
yes     → True
no      → False
banana  → False
hello   → False
```

`banana` should not mean `False`.

It should mean that the user entered invalid information.

The improved version checks specifically for both valid answers:

```python
if connection_input == "yes":
    connection_allowed = True

elif connection_input == "no":
    connection_allowed = False

else:
    print("Invalid response. Please enter yes or no.")
```

### Security Lesson

Invalid input should not silently be converted into legitimate security data.

A program running without errors does not necessarily mean that the data being processed is accurate.

---

## Q8 - Answer

`.lower()` converts uppercase letters into lowercase letters.

For example:

```text
YES → yes
Yes → yes
yEs → yes
yes → yes
```

This allows the program to compare different capitalization styles against one value:

```python
if connection_input == "yes":
```

This is an example of **input normalization**.

`.lower()` handles capitalization, but it does not correct spelling or remove spaces.

---

## Q9 - Answer

An **IP address** identifies a host or network interface involved in network communication.

A **port** identifies a service or application involved in the communication.

A simple analogy is:

```text
IP Address = Apartment building address
Port       = Apartment number
```

The port does **not** represent the route that the network traffic took.

Therefore:

```text
192.168.1.25:443
```

represents communication involving the host:

```text
192.168.1.25
```

and port:

```text
443
```

Port `443` is commonly associated with HTTPS.

---

## Q10 - Answer

### 1. Data Types

```text
Source IP          = str
Destination IP     = str
Destination Port   = int
Failed Logins      = int
Risk Score         = float
Connection Allowed = bool
```

### 2. Information That Deserves Investigation

Several pieces of information would catch my attention:

```text
Failed Logins:      12
Risk Score:         91.7
Connection Allowed: True
Destination Port:   443
```

The failed login attempts and high risk score would especially justify further investigation.

The fact that the connection was allowed is also important because I would want to understand what happened after the connection was permitted.

### 3. Is the Activity Malicious?

There is not enough information to determine that the activity is malicious based only on this alert.

The activity contains suspicious indicators, but:

> Suspicious does not automatically mean malicious.

Port `443` is commonly associated with HTTPS.

HTTPS generally means the communication is encrypted. It does **not** automatically mean the communication is safe or trustworthy.

Legitimate applications and malicious software can both communicate using HTTPS.

### 4. Additional Investigation

Before making a final determination, I would investigate:

- When the failed login attempts occurred
- Whether the attempts happened close together or over a longer period
- Which user was associated with the activity
- Whether the user expected the activity
- Authentication logs
- Network logs
- The destination IP/domain
- Whether the connection was successful
- What happened after the connection
- Whether anything suspicious was downloaded or executed
- Additional indicators of compromise

A final determination should be based on the evidence collected during the investigation rather than one individual indicator.

---

# Quiz Results

**Score: 8/10**

## Strengths

- Python data types
- Type conversion
- Assignment and comparison
- Boolean concepts
- Conditional logic
- Loops
- Input normalization
- Basic SOC investigation methodology

## Areas to Continue Improving

- Remembering that `input()` returns a string
- Input validation
- Precise networking terminology
- Understanding the relationship between IP addresses and ports
- Understanding that encrypted traffic is not automatically trusted
- Separating suspicious activity from confirmed malicious activity

---

# Key Lessons

1. `input()` returns a string unless the value is converted.

2. `=` assigns a value while `==` compares values.

3. Non-empty strings are considered truthy in Python.

4. `if`, `elif`, and `else` allow programs to make decisions.

5. `while` loops repeat code and `break` can stop the loop.

6. Input validation prevents bad data from being treated as legitimate data.

7. Input normalization makes user input easier to process consistently.

8. IP addresses identify hosts/network interfaces while ports identify services or applications.

9. HTTPS encryption does not automatically mean network activity is trustworthy.

10. Suspicious activity requires investigation before it should be classified as malicious.