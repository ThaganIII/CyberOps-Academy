# Lesson 04 — Summary

**Lesson:** Conditional Logic & Security Decisions  
**Project:** SOC Alert Triage Tool  
**Status:** Completed  
**Quiz Score:** 85%

## Lesson Overview

During Lesson 4, I learned how to use conditional statements and Boolean operators to make decisions in Python.

I applied these concepts by developing a SOC Alert Triage Tool that accepts security-related information, validates user input, classifies alerts, and recommends actions.

## Project: SOC Alert Triage Tool

### Purpose

The purpose of this project was to simulate how a security analyst could use Python to support alert triage.

### Information Collected

- Source IPv4 address
- Destination port
- Number of failed logins
- Risk score
- Known or unknown IP status
- Malware detection status
- Connection allowed or blocked status

### Features Implemented

1. User input collection.
2. Integer, float, and Boolean conversions.
3. Input validation with loops.
4. IPv4 address validation using the `ipaddress` module.
5. Error handling with `try` and `except ValueError`.
6. Alert classification using `if`, `elif`, and `else`.
7. Recommended actions based on alert severity.
8. Formatted SOC alert reporting using f-strings.

### Alert Classifications

| Severity | Recommended action |
|---|---|
| CRITICAL | Escalate immediately |
| HIGH | Begin investigation |
| MEDIUM | Review alert |
| LOW | Continue monitoring |

The classifications are based on the project's defined conditions.

## Testing and Troubleshooting

I tested the program using valid and invalid inputs.

Tests included:

- Entering letters instead of numeric values.
- Entering invalid IPv4 addresses.
- Entering port numbers outside the accepted range.
- Entering negative failed-login counts.
- Entering risk scores outside the 0–100 range.
- Entering invalid yes/no responses.
- Testing all four alert classifications.

The program successfully rejected the invalid inputs tested and continued requesting valid information.

## Lessons Learned

### Technical Skills

I learned how to structure conditional statements, combine multiple conditions using Boolean operators, and use parentheses to control how expressions are grouped.

I also learned how to use loops, exception handling, and validation to make a Python program more reliable.

### Cybersecurity Skills

I learned how Python can support SOC investigations by evaluating security indicators and assigning alert priorities.

The project demonstrated how automation can help analysts make consistent decisions based on predefined rules.

### Personal Development

I became more confident writing Python code independently without constantly referencing previous examples.

I also improved my ability to troubleshoot errors, understand program behavior, and explain the purpose of my code.

## Challenges

The biggest challenge was structuring conditional statements containing multiple conditions.

I needed additional practice understanding parentheses, Boolean operators, and how Python evaluates compound expressions.

I also learned that invalid user input can cause errors and that validation is important when building reliable automation tools.

## Future Improvements

Potential future enhancements include:

- Reading security alerts from CSV or JSON files.
- Processing multiple alerts automatically.
- Recording alert results in log files.
- Adding automated tests.
- Integrating the tool with simulated SIEM data.
- Improving classification rules to account for more security indicators.

## Final Reflection

Lesson 4 helped me move beyond writing basic Python statements and toward creating a functional cybersecurity tool.

I learned how to combine Python programming fundamentals with practical SOC workflows.

The most important improvement