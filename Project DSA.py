#!/usr/bin/env python
# coding: utf-8

# # Project DSA
# 19B-001-CS(A)
# 19B-020-CS(A)

# In[1]:


class HashTable():
    def __init__(self,size):
        self.size = size
        self.capacity = [None for i in range(self.size)]
        self.indexing = [None]*self.size
        self.next = 0
        print(self.indexing)
        
    # HF = hash function
    def HF(self,key):
        HashFunc = key % self.size
        return HashFunc
    
    # RHF = re-hash function
    def RHF(self,key):
        ReHashFunc = (key + 1) % self.size
        return ReHashFunc
    
    # insert data in hash table by using key & value
    def Insert_Data(self, key, value):
        if self.next == self.size:
            raise Exception ("Array is over flow")
        HashFunc = key % self.size 
        if self.indexing[HashFunc] == None:
            self.capacity[HashFunc] = key
            self.indexing[HashFunc] = value
            self.next += 1
            return self.indexing
        else:
            HashFunc = self.RHF(HashFunc)
             
            while self.capacity[HashFunc] != None:
                HashFunc = self.RHF(HashFunc)
            self.capacity[HashFunc] = key
            self.indexing[HashFunc] = value
            self.next += 1
            return  self.indexing
        
    # print the data
    def Print(self):
        print (self.indexing)
        
    # searching the data by using key
    def Search_Data(self,key):
        hashtable = self.HF(key)
        while self.capacity[hashtable] is not  None:
            if self.capacity[hashtable] == key:
                return self.indexing[hashtable]
            hash1 = hashtable + 1 
            hash2 = hash1 % self.size
            if self.capacity[hash2] == key:
                return self.indexing[hash2]
        raise Exception ("Key is not found")
    
    # delete data by using key
    def Delete_Data(self,key):
        hashtable = self.HF(key)
        if self.capacity[hashtable] != key:
            count = 0
            hashtable = self.RHF(hashtable)
            while self.capacity[hashtable] != key and count != self.size:
                hashtable = self.ReHash(hashtable)
                count += 1

            if self.size == count:
                raise Exception ("Key not in the data")
            else:
                item = self.indexing[hashtable]
                self.indexing[hashed] = None
                self.capacity[hashed] = None
                return self.indexing
            
print("Before entering the data")

# Enter the data
# I am entering the data of some students of UIT (19B-CS(A))

CS = HashTable(10)             
(CS.Insert_Data(1,'Burhan Al Haq'))
(CS.Insert_Data(20,'Sameer Khan'))
(CS.Insert_Data(9,'Hammad'))
(CS.Insert_Data(4,'Fahama'))
(CS.Insert_Data(6,'Mohammad Hassan Ejaz'))
(CS.Insert_Data(5,'Dabeer Ahmed'))
(CS.Insert_Data(8,'Faris Shah'))
(CS.Insert_Data(7,'Rafay Khan'))
(CS.Insert_Data(3,'Hashir'))
(CS.Insert_Data(2,'Madni Raza'))

print("")
print("After entering the data")
CS.Print()

#Search any student by using key
print("")
print("Searching any name")
print(CS.Search_Data(20))

#Deleting those names who left UIT
print("")
print("Delete names those who left UIT")
CS.Delete_Data(2)
CS.Delete_Data(7)
CS.Print()

