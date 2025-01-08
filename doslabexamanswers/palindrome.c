// Question 2: Write a C program to create a child process to reverse a string
// and check if it's a palindrome.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void reverseString(char* str, char* reversed) {
    int len = strlen(str);
    for (int i = 0; i < len; i++) {
        reversed[i] = str[len - i - 1];
    }
    reversed[len] = '\0';
}

int main() {
    char input[100], reversed[100];
    printf("Enter a string: ");
    scanf("%s", input);

    pid_t pid = fork();
    if (pid < 0) {
        perror("Fork failed");
        return 1;
    } else if (pid == 0) {
        // Child process
        reverseString(input, reversed);
        printf("Reversed String: %s\n", reversed);
        exit(0);
    } else {
        // Parent process
        wait(NULL);
        reverseString(input, reversed);
        if (strcmp(input, reversed) == 0) {
            printf("The string is a palindrome.\n");
        } else {
            printf("The string is not a palindrome.\n");
        }
    }

    return 0;
}

