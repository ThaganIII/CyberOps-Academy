##############################################
# Project: SOC Alert Triage
# Lesson: 04 - Conditional Logic
# Author: Tom Hagan III
# Date: 10/8/26
#
# Purpose:
# Build a program that analyzes SOC alerts and assigns
# a basic security risk level.
##############################################
import ipaddress


while True:
    source_ip = input("Enter the source IP address: ")
    try:
        ipaddress.IPv4Address(source_ip)
        break
    except ValueError:
        print("Invalid IP address. Please enter a valid IP address.")

while True:
    try:
        destination_port = int(input("Enter the destination port: "))
        if destination_port < 0 or destination_port > 65535:
            print("Invalid port. Please enter a number between 0 and 65535.")
        else:
            break
        
    except ValueError:
        print("Invalid input. Please enter a number.")
while True:
    try:
        failed_logins = int(input("Enter the number of failed logins: "))
        if failed_logins < 0:
            print("Invalid number of failed logins. Please enter a non-negative number.")
        else:
            break

    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    try:
        risk_score = float(input("Enter the risk score (as a decimal): "))
        if risk_score < 0 or risk_score > 100:
            print("Invalid risk score. Please enter a number between 0 and 100.")
        else:
            break

    except ValueError:
        print("Invalid input. Please enter a decimal number.")


while True:
    known_ip = input("Is the source IP known? (yes/no): ").lower()

    if known_ip == "yes":
        known_ip = True
        break

    elif known_ip == "no":
        known_ip = False
        break

    else:
        print("Invalid response. Please enter yes or no.")
        
while True:
    malware_detected = input("Is malware detected on the source IP? (yes/no): ").lower()

    if malware_detected == "yes":
        malware_detected = True
        break

    elif malware_detected == "no":
        malware_detected = False
        break

    else:
        print("Invalid response. Please enter yes or no.")
        
while True:
    connection_allowed = input("Is the connection allowed? (yes/no): ").lower()

    if connection_allowed == "yes":
        connection_allowed = True
        break

    elif connection_allowed == "no":
        connection_allowed = False
        break

    else:
        print("Invalid response. Please enter yes or no.")
        
        
if risk_score >= 80 and connection_allowed and malware_detected:
    classification = "CRITICAL"
elif risk_score >= 80 and (not known_ip or failed_logins >= 10):
    classification = "HIGH"
elif risk_score >= 50 or failed_logins >= 5:
    classification = "MEDIUM"
else:
    classification = "LOW"

if classification == "CRITICAL":
    action = "Escalate immediately"
elif classification == "HIGH":
    action = "Begin investigation"
elif classification == "MEDIUM":
    action = "Review alert"
else:
    action = "Continue monitoring"
    
print("========== SOC Alert ==========")   
print()

print(f"Source IP: {source_ip}")
print(f"Destination Port: {destination_port}")
print(f"Failed Logins: {failed_logins}")
print(f"Risk Score: {risk_score}")
print(f"Known IP: {known_ip}")
print(f"Malware Detected: {malware_detected}")
print(f"Connection Allowed: {connection_allowed}")

print()
print(f"Alert Classification: {classification}")
print(f"Recommended Action: {action}")
print()

print("================================") 