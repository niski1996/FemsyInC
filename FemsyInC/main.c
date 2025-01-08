#include <stdio.h>
#include "Test.h"

// Dyrektywa preprocesora dla debug/release
#ifdef DEBUG
    #define DEBUG_PRINT() printf("hello debug\n")
#else
    #define DEBUG_PRINT() printf("hello rel\n")
#endif
void Run() {
    DEBUG_PRINT(); // Wypisuje odpowiedni komunikat w zależności od trybu
}

int main() {
#ifdef NDEBUG
    printf("hello rel\n");  // Tryb Release
#else
    printf("hello debug\n");  // Tryb Debug
#endif
    printf("Hello, World!\n");
    RunAllTests();

    // Wywołanie funkcji z odpowiednim komunikatem
    Run();

    return 0;
}
int RunTask() {
    char path = "/home/kali/Desktop/cybersec/sem1/programowanie/Femsy/FemsyInC/input/example";
    printf("start task from location: %s\n", path);

}

