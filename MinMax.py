# Description of Program: Users will input random numbers into the program and then type stop when finished. The system will then count and display how many numbers were entered along with what the maximum and minimum values were among the inputed numbers.

def main():
    max1 = 0
    min2 = 0
    count = 0
    stop = str('stop')

    while True:
        numbers = input("Enter an integer or stop' to end: ")

        if numbers != str('stop'):
            count += 1
            numbers = int(numbers)
            if count == 1:
                min2 = int(numbers)
            if numbers > max1:
                max1 = int(numbers)
            if numbers < min2:
                min2 = int(numbers)

        else:
            if count > 0:
                print()
                if count > 1:
                    print("You entered", count, "numbers")
                    
                else:
                    print("You entered", count, "number")
                print("The maximum is", max1)
                print("The minimum is", min2)
                break
                
            else:
                print()
                print("You haven't entered integers")
                break


main()
