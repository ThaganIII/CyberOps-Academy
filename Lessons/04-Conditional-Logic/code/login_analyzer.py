##############################################
# Project: Failed Login Analyzer
# Lesson: 04 - Conditional Logic
# Author: Tom Hagan III
# Date: 09/15/26
#
# Purpose:
# Analyze failed login attempts and assign
# a basic security risk level.
##############################################


risk_score = float(input("Enter the risk score: "))
while True:
    connection_input = input("Is the connection allowed? (Yes/No): ").lower()

    if connection_input == "yes":
        connection_allowed = True
        break

    elif connection_input == "no":
        connection_allowed = False
        break

    else:
        print("Invalid response, Try Again")

if risk_score >= 80 and connection_allowed:
    print("Critical")

elif risk_score >= 50 and connection_allowed:
    print("Suspicious")

else:
    print("Low risk")
        
        