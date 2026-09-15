# Lesson 3 Reflections - Data Types and Networking

## 1. What was the most important Python concept you learned in this lesson?

The most important concept I learned was that data types define how Python interprets and works with values. The programmer must make sure they are using the correct data type so that values are processed and used properly.

## 2. What was something that confused you at first but makes more sense now?

I was confused about how Python recognizes different data types and how I could verify whether a value was using the correct data type.

I learned that Python recognizes types such as strings, integers, floats, and Booleans. I can use the `type()` function to check the data type of a value while testing or debugging my code.

## 3. Why is input validation important when creating cybersecurity tools?

Input validation is important because it ensures that the end user provides an appropriate response to the prompt they are being asked.

For example, if a program asks the user a yes-or-no question, input validation prevents an invalid answer such as `"banana"` from being treated as a legitimate response.

This helps prevent incorrect data from being processed by the program.

## 4. What did you learn about IP addresses and ports?

An IP address identifies a host or network interface on a network, while a port identifies the service or application involved in the network communication.

For example, an IP address could identify the destination host while port `443` could indicate that the traffic is communicating with a service commonly associated with HTTPS.

## 5. What did the SOC scenario teach you about determining whether activity is malicious?

The SOC scenario taught me that the information in an alert alone may not be enough to determine whether activity is malicious.

The information can provide enough evidence to justify further investigation, but an analyst should investigate and gather additional evidence before making a final determination.

## 6. How could you use what you learned in this lesson in a real SOC or cybersecurity environment?

I could use what I learned to create a small network alert ticketing tool that asks an analyst for information about an alert.

The program could collect values such as source IP, destination IP, destination port, packet count, risk score, and whether the connection was allowed. The program could then validate and process that information using the correct data types.

## 7. What part of Lesson 3 do you think you still need more practice with?

I still need more practice with `if`, `elif`, and `else` statements.

I understand the basic idea, but I want more experience using conditional statements and understanding when they should be used. I would also like to see more cybersecurity use cases so I can understand how conditional logic can be applied in real scripts and security automation.