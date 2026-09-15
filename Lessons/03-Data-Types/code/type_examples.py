################################################################################
# Project: Data Type Examples
# Lesson: 03 - Data Types
# Author: Tom Hagan III
# Date: 07/10/26
#
# Purpose: This program demonstrates the use of different data types in Python.
# Practice using strings, integers, floats, and booleans in Python.
# This will use cybersecurity incident and networking information
# to demonstrate the use of different data types.
################################################################################

source_ip = "192.168.1.1" # String
destination_port = 443 # Integer
risk_score = 87.5 # Float   
connection_allowed = True # Boolean

# include integer input to demonstrate type conversion. If does not convert to an integer, it will throw an error when trying to add 5 to the input value.
failed_logins = int(input("Enter the number of failed login attempts: "))
print(failed_logins + 5) 



print("========== Data Type Examples ==========") 
print(f"Source IP Address: {source_ip} (Type: {type(source_ip)})")
print(f"Destination Port: {destination_port} (Type: {type(destination_port)}) ")
print(f"Risk Score: {risk_score} (Type: {type(risk_score)})")
print(f"Connection Allowed: {connection_allowed} (Type: {type(connection_allowed)})")
