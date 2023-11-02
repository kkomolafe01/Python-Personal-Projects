# Description of Program: Using Zeller's Congruenece to calculate the day of the week for any Gregorian calendar date

def main():
    # Function defines the starting point for the program

    # Accept the year from the user and convert it to an int.
    Y = int( input("\nEnter year (e.g., 2008): "))
    # If the year is not greater than 1752, print an error
    # message and exit the program. 
    if (Y < 1753):
        print("Year must be > 1752. Illegal year entered:", Y, "\n")
        return

    # handle the month similarly
    m = int(input("\nEnter month (1-12): "))
    if m == 1 or m == 2:
        m = m + 12
        Y = Y - 1
    elif(m < 1):
        print("Month must be between 1 and 12. Illegal month entered:", m, "\n")
        return
    else:
        m = m

    # handle the day of the month similarly
    d = int(input("\nEnter the day of the month (1-31): "))
    if (d < 1 or d > 31 ):
        print("Day must be between 1 and 31. Illegal day entered:", d, "\n")
        return
    else:
        d = d

    # Compute the other variables, including h
    K = Y % 100
    J = Y // 100
    h = ( d + (13 * (m + 1))//5 + K + K//4 + J//4 + 5*J ) % 7

    # Compute the name of the day from h
    # print the day of week message
    if h == 0:
        print("\nDay of the week is Saturday")
    elif h == 1:
        print("\nDay of the week is Sunday")
    elif h == 2:
        print("\nDay of the week is Monday")
    elif h == 3:
        print("\nDay of the week is Tuesday")
    elif h == 4:
        print("\nDay of the week is Wednesday")
    elif h == 5:
        print("\nDay of the week is Thursday")
    elif h == 6:
        print("\nDay of the week is Friday")
        return

# You'll need this to run your main program. 
main()  
