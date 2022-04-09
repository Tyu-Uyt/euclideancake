# Program name -    Euclidean Cake
# Developer -       Albert Banoy
# Date -            9th of April 2022
# Purpose -         To find the number of days it takes to eat a cake that is a perfect square
#                   Part of University of Bloomsberg's 12 of April 2022 Competition

# Test Cases -
#   Case 0 -
#       [Input]
#           Enter dimensions of cake: 30 42
#       [Output]  
#           Cake on day 1: 30 x 42
#           Cake on day 2: 12 x 30
#           Cake on day 3: 12 x 18
#           Cake on day 4: 6 x 12
#           Cake on day 5: 6 x 6
#           Cake on day 6: gone

#   Case 1 -
#       [Input]
#           Enter dimensions of cake: 21 13
#       [Output]
#           Cake on day 1: 13 x 21
#           Cake on day 2: 8 x 13
#           Cake on day 3: 5 x 8
#           Cake on day 4: 3 x 5
#           Cake on day 5: 2 x 3
#           Cake on day 6: 1 x 2
#           Cake on day 7: 1 x 1
#           Cake on day 8: gone

#   Case 2 -
#       [Input]
#           Enter dimensions of cake: 12 36
#       [Output]
#           Cake on day 1: 12 x 36
#           Cake on day 2: 12 x 24
#           Cake on day 3: 12 x 12
#           Cake on day 4: gone

#   Case 3 -
#       [Input]
#           Enter dimensions of cake: 8 12
#       [Output]
#           Cake on day 1: 8 x 12
#           Cake on day 2: 4 x 8
#           Cake on day 3: 4 x 4
#           Cake on day 4: gone

#   Case 4 -
#       [Input]
#           Enter dimensions of cake: 1 1
#       [Output]
#           Cake on day 1: 1 x 1
#           Cake on day 2: gone

#   Case 5 -
#       [Input]
#           Enter dimensions of cake: 1 no
#       [Output]
#           Value error
#       [Input]
#           Enter dimensions of cake: 1 3
#       [Output]
#           Cake on day 1: 1 x 3
#           Cake on day 2: 1 x 2
#           Cake on day 3: 1 x 1
#           Cake on day 4: gone

def euclidean(twoDimension):
    # Initialize the variables
    days = 1
    
    # Sort the dimensions
    twoDimension.sort()

    # Print the inital dimensions
    print("Cake on day 1: " + str(twoDimension[0]) + " x " + str(twoDimension[1]))

    # If the dimensions are not equal, continue
    if twoDimension[0] / twoDimension[1] != 1:
        # While the ratio of the dimensions is not 0.5
        while (twoDimension[0] / twoDimension[1] != 0.5):
            # Add a day
            days += 1
            # Move the second dimension to a temporary variable
            tmpNumber = twoDimension[1]
            # Set the second dimension to the first dimension
            twoDimension[1] = twoDimension[0]
            # Subtract the second dimension from the temporary variable, and add it to the first dimension
            twoDimension[0] = tmpNumber - twoDimension[1]
            # Sort the dimensions
            twoDimension.sort()
            # Print the dimensions with a new day
            print("Cake on day " + str(days) + ": " + str(twoDimension[0]) + " x " + str(twoDimension[1]))
        # Print the dimensions with a new day
        print("Cake on day " + str((days + 1)) + ": " + str(twoDimension[0]) + " x " + str(twoDimension[0]))
        # Print the last day as the cake being gone
        print("Cake on day " + str((days + 2)) + ": gone")
    else:
        # Print the last day as the cake being gone
        print("Cake on day " + str((days + 1)) + ": gone")
    
def main():
    # Gets an input from the user, sort the input as an integer map to a list, and pass it to the function
    parameterValue = list(map(int, input("Enter dimensions of cake: ").split()))
    euclidean(parameterValue)

try:
    main()
except ValueError:
    print("Value Error")
    main()