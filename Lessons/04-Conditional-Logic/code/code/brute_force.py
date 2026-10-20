failed_logins = 7

if failed_logins >= 5:
    print("Possible brute-force activity")
else:
    print("Login activity below threshold")
    