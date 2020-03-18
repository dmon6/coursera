
# Steps to problem solving

## Sometimes these steps will be out of order
1. Getting information
2. Finding the root cause
3. Performing the necessary remediation


# Troubleshooting Questions to ask user
1. What were you trying to do?
2. What steps did you follow?
3. What was the expected result?
4. What was the actual result?

# Bisect method(binary search) to find a wrong data input on a 100 line CSV file
```sh
head -50 contacts.csv | tail -25 | tail -12 | head -6 | head -3 | ./import.py
```
## What's going on here? This is continually dividing the csv file in half to pin point the wrong data input 