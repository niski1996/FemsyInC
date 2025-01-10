#include <stdio.h>
#include <time.h>
#include "logger.h"

void logDatetime() {
    FILE *file = fopen(LogName, "a");
    if (file == NULL) {
        perror("Error opening log file");
        return;
    }

    time_t now = time(NULL);
    struct tm *t = localtime(&now);
    if (t == NULL) {
        perror("Error getting local time");
        fclose(file);
        return;
    }

    fprintf(file, "Datetime: %04d-%02d-%02d %02d:%02d:%02d ",
            t->tm_year + 1900, t->tm_mon + 1, t->tm_mday,
            t->tm_hour, t->tm_min, t->tm_sec);
    fclose(file);
}

void logMessage(const char *message) {
    logDatetime();
    FILE *file = fopen(LogName, "a");
    if (file == NULL) {
        perror("Error opening log file");
        return;
    }
    fprintf(file, "Message: %s\n", message);
    fclose(file);
}