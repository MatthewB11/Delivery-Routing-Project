# Creating Hashmap with insert function that takes package IDs as input and inserts:
# delivery address
# delivery deadline
# delivery city
# delivery zip code
# package weight
# delivery status (i.e., at the hub, en route, or delivered), including the delivery time
# Citing source: WGU code repository W-2_ChainingHashTable_zyBooks_Key-Value_CSV_Greedy.py

class MyHashMap:

    # sets size of map to an array of 40
    def __init__(self, initial_capacity=40):
        # initialize the hash table with empty bucket list
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def search(self, key):
        # gets bucket list base of hash function
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                return kv[1]  # value
        return None

    # add function to add values into Hashmap
    # also updates key value pairs
    def insert(self, key, item):

        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])
