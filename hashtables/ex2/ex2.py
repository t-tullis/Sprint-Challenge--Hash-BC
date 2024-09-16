#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for item in range(length):
        ticket = tickets[item]
        hash_table_insert(ht, ticket.source, ticket.destination)
    '''
    Loop through our hash table and go from the desintation that has the source of NONE 
    to the destination ticket that is NONE
    '''
    current_index = 0
    #set ticket destination in hashtable w/ key "None"
    ticket_destination = hash_table_retrieve(ht, "NONE")
    while True:
        #route[index] is equal to ticket destination
        route[current_index] = ticket_destination
        #increment the current index by 1
        current_index += 1
        #and set ticket_destination to value recieved from ht
        ticket_destination = hash_table_retrieve(ht, ticket_destination)
        #if the ticket destination is NONE
        if ticket_destination == "NONE":
            #set the route[current_index] to None
            route[current_index] = "NONE"
            break

    return route
