################################################################### 
# Lesson 3: Data Types and Networking
# Author: Tom Hagan III
# Date: 07/10/26
# 
# Purpose: This program collects and displays network alert information
# and stores them using different data types in Python.
########################################################################

source_ip = input("Enter the source IP address: ") # String
destination_ip = input("Enter the destination IP address: ") # String
destination_port = int(input("Enter the destination port: ")) # Integer
packet_count = int(input("Enter the packet count: ")) # Integer
risk_score = float(input("Enter the risk score (as a decimal): ")) # Float
# connection_allowed = input("Is the connection allowed? (yes/no): ")

# Adding in if/else statement
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

print()
print("========== Network Alert ==========")
print(f"Source IP:          {source_ip}")
print(f"Destination IP:     {destination_ip}")
print(f"Destination Port:   {destination_port}")
print(f"Packet Count:       {packet_count}")
print(f"Risk Score:         {risk_score}")
print(f"Connection Allowed: {connection_allowed}")

#This was used to check the value type of a variable.
print(type(connection_allowed))
print(type(destination_port))

#This was used to view how Python views True/False values 
print(bool("yes"))
print(bool("no"))
print(bool(""))

#This will print out the results of the if/else statement
print(type(connection_allowed))