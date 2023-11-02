# Decription of Program: Program users will be prompted to enter in a year for the Easter Sunday date that they are curious about. The program will then take the inputed year and calculate the month and day that Easter Sunday fell on in that particular year, before printing it out in a sentence.

y = int( input("Enter year: ") )
a = y % 19
b = y // 100
c = y % 100
d = b // 4
e = b % 4
g = (8 * b + 13) // 25
h = (19 * a + b -d -g + 15) % 30
j = c // 4
k = c % 4
m = (a + 11 * h) // 319
r = (2 * e + 2 * j - k - h + m +32) % 7
n = (h - m + r + 90) // 25
p = (h - m + r + n + 19) % 32
print("In", y, "Easter Sunday is on month", n, "and day", p)


