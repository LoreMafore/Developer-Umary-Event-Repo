#include <stdio.h>
#include <string.h>

// File reading and writing practice
// Getting segfaults, not sure why

#define MAX_LINE 256

int readFile(const char* filename) {
    FILE* file = fopen(filename, "r");
    
    // TODO: check if file is NULL
    
    char line[MAX_LINE];
    while (fgets(line, sizeof(line), file) != NULL) {
        printf("%s", line);
    }
    
    fclose(file);
    return 0;
}

int writeFile(const char* filename, const char* content) {
    FILE* file = fopen(filename, "w");
    
    if (file == NULL) {
        printf("Error opening file\n");
        return 1;
    }
    
    fprintf(file, "%s", content);
    
    // fclose(file);  // forgot to uncomment this
    return 0;
}

// TODO: implement append function
// int appendToFile(const char* filename, const char* content) {
    
// }

int main() {
    const char* testFile = "test.txt";
    
    writeFile(testFile, "Hello, World!\n");
    
    readFile(testFile);
    
    return 0;
}
