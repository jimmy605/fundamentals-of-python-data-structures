"""
3.
A standard science experiment is to drop a ball and see how high it bounces. Once the “bounciness” of the ball has been determined, the ratio gives a bounci- ness index. For example, if a ball dropped from a height of 10 feet bounces 6 feet high, the index is 0.6 and the total distance traveled by the ball is 16 feet after one bounce. If the ball were to continue bouncing, the distance after two bounces would be 10ft + 6ft + 6ft + 3.6ft = 25.6ft. Note that distance traveled for each successive bounce is the distance to the floor plus 0.6 of that distance as the ball comes back up. Write a program that lets the user enter the initial height of the ball and the number of times the ball is allowed to continue bouncing. Output should be the total distance traveled by the ball.
"""


def bounce(downPhase):
    """Returns the total of a single bounce"""
    return downPhase + (downPhase * 0.6)


def ballTraveled(ballHeight, bounces):
    """Return the total distance traveled of a ball when bounced x times."""
    # total variable to store the total distance traveled
    totalDistance = 0

    # Use a for loop to iterate through the bounces
    for n in range(bounces):
        totalDistance += bounce(ballHeight)
        ballHeight *= 0.6

    print(f'{totalDistance:.2f}')


ballTraveled(10, 2)
