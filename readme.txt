Hash table:
Hash table are a type of data structures in which we can stores key-value pair same as python dictionary.The order of data elements in a dictionary is not fixed. In python we emplement hash table in different ways, the two most common methods are as follow;
1) linear probing
2) chaining method
Implementation of the code is done by linear probing. In Linear probing we have a pre defined size of the table in which we store data. The function insert is used to enter the data and the predefined system formula of lonear probing 
KEY%SIZE is used to determine the position of the object to be stored. The determination of the table size is important as if the table is full and we try to store the data the error would occur,known as error overflow. The search function in the
code is used to search the element stored in the table and the delete function is used to delete the function which is little bit tricky while implementing the hash table.