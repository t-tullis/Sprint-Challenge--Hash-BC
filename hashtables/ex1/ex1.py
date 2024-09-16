#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    #if the length is less than 2 return None
    if length < 2:
        return None
    
    #for item in range of length
    for item in range(length):
        #insert into the hashtable weights with key of index[x], and a value of x
        hash_table_insert(ht, weights[item], item)

    # Loop through weights again and check to see if limit - weight = KEY where KEY is in the hashtable.
    for item in range(length):
        #check to see if the hash table contains an entry for [limit - weight]
        check_number = limit - weights[item]
        #set index of weight = ht w/ a key of "check_number"
        index_of_weight = hash_table_retrieve(ht, check_number)
        if index_of_weight:
        #if index of weight is > n 
            if index_of_weight > item:
                #return index of weight
                return (index_of_weight, item)
            else:
                return (item, index_of_weight)


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))