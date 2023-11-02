# Description of Program: Program takes user inputs to calculate a bowler's average and handicap after three bowling games

name = input("Enter bowler's name: ")
game_one = int(input("Enter Game 1: "))
game_two = int(input("Enter Game 2: "))
game_three = int(input("Enter Game 3: "))

average = int((game_one + game_two + game_three) / 3)
handicap = int( (200 - average) * 0.8 )
handicap = max( 0, handicap )

print()
print("Handicap report for",name + ":")
print("  ",name, "'s average is: ", average)
print("  ",name, "'s handicap is: ", handicap)
print()
print("It's time to Bowl!")
print()

