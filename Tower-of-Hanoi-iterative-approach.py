# Initialise the values of variables 
NUMBER_OF_DISKS = 4
number_of_moves = 2 ** NUMBER_OF_DISKS - 1
    # Initialise a dictionary which contains the 'rods' for the puzzle 
rods = {
    'A': list(range(NUMBER_OF_DISKS, 0, -1)),
    'B': [],
    'C': []
}

#  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

"""
	-> This is the first function which we define for this project 
	-> This encodes the rules of the Hanoi tower puzzle
	-> For more information about these rules, refer to the project problem-solving thought process notes 
"""

def make_allowed_move(rod1, rod2):    
    forward = False
    if not rods[rod2]:
        forward = True
    elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
        forward = True  

    if forward:
        # Print results as f string literals 
        print(f'Moving disk {rods[rod1][-1]} from {rod1} to {rod2}')
        rods[rod2].append(rods[rod1].pop())

    else:
        # Print results as f string literals 
        print(f'Moving disk {rods[rod2][-1]} from {rod2} to {rod1}')
        rods[rod1].append(rods[rod2].pop())
    
    # Display our progress
    print(rods, '\n')

#  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

"""
	-> There are three different rods for this puzzle 
	-> The first is the 'source rod' <- This is the rod where the disks are first placed
	-> The 'target rod' <- This is the rod where we aim to move the disks 
	-> The 'auxillary rod' <- This is the intermediary rod which the disks are placed on
	-> This second function defined allows us to move the disks between these rods 
	-> More information about this is found in the project problem-solving thought process notes 
"""

# Defining a function which allows us to move disks between rods 
def move(n, source, auxiliary, target):
    # Display starting configuration
    print(rods, '\n')
    for i in range(number_of_moves):
        remainder = (i + 1) % 3

        # Depending on the number of disks we have left on a specific rod
        if remainder == 1:

            if n % 2 != 0:
                # Print results as f string literals 
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)

            else:
                # Print results as f string literals 
                print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                make_allowed_move(source, auxiliary)

        elif remainder == 2:
            if n % 2 != 0:
                # Print results as f string literals 
                print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                make_allowed_move(source, auxiliary)
            else:
                # Print results as f string literals 
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)

        elif remainder == 0:
            print(f'Move {i + 1} allowed between {auxiliary} and {target}')
            make_allowed_move(auxiliary, target)           

# Initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, 'A', 'B', 'C')