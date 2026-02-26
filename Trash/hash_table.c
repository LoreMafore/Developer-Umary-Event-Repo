#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Hash table implementation - work in progress
// Collisions not handled properly yet

#define TABLE_SIZE 100

typedef struct Entry {
    char* key;
    int value;
    struct Entry* next;  // for chaining
} Entry;

typedef struct HashTable {
    Entry* table[TABLE_SIZE];
} HashTable;

unsigned int hash(const char* key) {
    unsigned int hash = 0;
    while (*key) {
        hash = (hash * 31) + *key;
        key++;
    }
    return hash % TABLE_SIZE;
}

HashTable* createHashTable() {
    HashTable* ht = (HashTable*)malloc(sizeof(HashTable));
    for (int i = 0; i < TABLE_SIZE; i++) {
        ht->table[i] = NULL;
    }
    return ht;
}

void insert(HashTable* ht, const char* key, int value) {
    unsigned int index = hash(key);
    
    Entry* newEntry = (Entry*)malloc(sizeof(Entry));
    newEntry->key = strdup(key);
    newEntry->value = value;
    newEntry->next = NULL;
    
    // TODO: handle collision with chaining
    if (ht->table[index] == NULL) {
        ht->table[index] = newEntry;
    } else {
        // FIXME: this overwrites instead of chaining
        ht->table[index] = newEntry;
    }
}

// TODO: implement search function
// int search(HashTable* ht, const char* key) {
//     unsigned int index = hash(key);
    
// }

// TODO: implement delete function
// void delete(HashTable* ht, const char* key) {
//     
// }

void printHashTable(HashTable* ht) {
    for (int i = 0; i < TABLE_SIZE; i++) {
        if (ht->table[i] != NULL) {
            printf("Index %d: %s -> %d\n", i, ht->table[i]->key, ht->table[i]->value);
        }
    }
}

int main() {
    HashTable* ht = createHashTable();
    
    insert(ht, "apple", 5);
    insert(ht, "banana", 7);
    insert(ht, "orange", 3);
    
    printHashTable(ht);
    
    // TODO: free memory
    
    return 0;
}
