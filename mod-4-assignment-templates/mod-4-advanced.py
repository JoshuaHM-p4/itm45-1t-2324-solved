'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''
import importlib

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    15 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    status = ""

    # Retreive from and to member follows data
    from_member_follows = social_graph.get(from_member, {}).get("following", [])
    to_member_follows = social_graph.get(to_member, {}).get("following", [])

    # Check if to_member is a folllower of from_member
    if to_member in from_member_follows:
        status = "follower"

    # Check if from_member follows to_member -> followed by or if both are followers -> "friends"
    if from_member in to_member_follows:
        if status == "follower":
            status = "friends"
        else:
            status = "followed by"

    if not status:
        status = "no relationship"

    return status


def tic_tac_toe(board):
    '''Tic Tac Toe.
    15 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    # Board is equal on both sides, thus we iterate
    for ind, row in enumerate(board):
        # Check Row Winners
        if len(set(row)) == 1 and row[0] != '':
            return row[0]

        # Check for column
        column = [board[val][ind] for val in range(len(board))]
        if len(set(column)) == 1 and column[0] != '':
            return board[0][ind]

    # Check for diagonals
    l_diagonal = [board[x][x] for x in range(len(board))]
    r_diagonal = [board[x][len(board)-1-x] for x in range(len(board))]

    if len(set(l_diagonal)) == 1 and l_diagonal[0] != 0:
        return l_diagonal[0]
    if len(set(r_diagonal)) == 1 and r_diagonal[0] != 0:
        return r_diagonal[1]

    # Return no winner after no one has won
    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA.
    20 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    if (first_stop, second_stop) in route_map:
        return route_map[(first_stop, second_stop)]["travel_time_mins"]

    current_stop = first_stop
    total_time = 0

    while current_stop != second_stop:
        next_stop_found = False
        for key, value in route_map.items():
            if key[0] == current_stop:
                total_time += value["travel_time_mins"]
                current_stop = key[1]
                next_stop_found = True
                break  # Stop the loop once the next stop is found

        if not next_stop_found:
            return -1

    return total_time

# sample_data = importlib.import_module("mod-4-advanced-sampledata")

# def main():
#     member_one = input("Enter your username: ")
#     member_two = input("Enter the other person's username: ")
#     print(relationship_status(member_one, member_two, sample_data.social_graph))

#     print(tic_tac_toe(sample_data.board6))

#     print(eta("a1", "b1", sample_data.legs2))


# if __name__ == "__main__":
#     main()