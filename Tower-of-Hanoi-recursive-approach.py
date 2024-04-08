# Initialise the values of variables 

"""
	-> There are three different rods for this puzzle 
	-> The first is the 'source rod' <- This is the rod where the disks are first placed
	-> The 'target rod' <- This is the rod where we aim to move the disks 
	-> The 'auxillary rod' <- This is the intermediary rod which the disks are placed on
	-> This second function defined allows us to move the disks between these rods 
	-> More information about this is found in the project problem-solving thought process notes 
"""

NUMBER_OF_DISKS = 5
A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []

#  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Defining a function which allows us to move disks between rods 
def move(n, source, auxiliary, target):

"""
    -> We are implementing the Tower of Hanoi puzzle 
    -> The disks are starting all on one rod, from small at the top, to large at the bottom 
    -> Rules of the puzzle: 
            -> Only one disk can be moved at a time
            -> Each move consists of taking the top disk from one stack and placing it onto another stack
            -> No disk may be placed on top of a smaller disk
    -> The lists represent the different rods 
        -> All of the disks initially occupy rod A 
    -> The `move` function is defined, to move the disks between the rods: 
        -> n is the number of disks we want to move 
        -> A, B and C are the source, auxiliary and target rods for this
    -> In this .py file, we are following a recursive approach - to move the disks from the source to the target rod
    -> The base case for this is n <= 0 <- In this case, we run the function, without doing anything 
    -> The function is then printing out the number of disks on each rod after every move 
    -> Then after the algorithm has finished executing, it outputs the sequence of moves required to solve the puzzle 
        with the input number of disks
"""

    if n <= 0:
        return
    # move n - 1 disks from source to auxiliary, so they are out of the way
    move(n - 1, source, target, auxiliary)
        
    # move the nth disk from source to target
    target.append(source.pop())
        
    # display our progress
    print(A, B, C, '\n')
        
    # move the n - 1 disks that we left on auxiliary onto target
    move(n - 1,  auxiliary, source, target)
              
# initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, A, B, C)

#  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%