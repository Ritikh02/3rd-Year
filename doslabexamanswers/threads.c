// Question 4: Program to create threads and use semaphores to control execution order.

#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>

sem_t semA, semB, semC;

void* printA(void* arg) {
    for (int i = 1; i <= 7; i += 3) {
        sem_wait(&semA);
        printf("A%d ", i);
        sem_post(&semB);
    }
    return NULL;
}

void* printB(void* arg) {
    for (int i = 2; i <= 8; i += 3) {
        sem_wait(&semB);
        printf("B%d ", i);
        sem_post(&semC);
    }
    return NULL;
}

void* printC(void* arg) {
    for (int i = 3; i <= 9; i += 3) {
        sem_wait(&semC);
        printf("C%d ", i);
        sem_post(&semA);
    }
    return NULL;
}

int main() {
    pthread_t threadA, threadB, threadC;

    sem_init(&semA, 0, 1);
    sem_init(&semB, 0, 0);
    sem_init(&semC, 0, 0);

    pthread_create(&threadA, NULL, printA, NULL);
    pthread_create(&threadB, NULL, printB, NULL);
    pthread_create(&threadC, NULL, printC, NULL);

    pthread_join(threadA, NULL);
    pthread_join(threadB, NULL);
    pthread_join(threadC, NULL);

    sem_destroy(&semA);
    sem_destroy(&semB);
    sem_destroy(&semC);

    return 0;
}
