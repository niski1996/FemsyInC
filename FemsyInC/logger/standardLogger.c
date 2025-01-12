#include <stdio.h>
#include <time.h>
#include "logger.h"
#include <stdarg.h>


char *LogName = "log.log";

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

    fprintf(file, "\nDatetime: %04d-%02d-%02d %02d:%02d:%02d ",
            t->tm_year + 1900, t->tm_mon + 1, t->tm_mday,
            t->tm_hour, t->tm_min, t->tm_sec);
    fclose(file);
}

void logMessage(const char *format, ...) {
    logDatetime();
    FILE *file = fopen(LogName, "a");
    if (file == NULL) {
        perror("Error opening log file");
        return;
    }

    va_list args;
    va_start(args, format);
    fprintf(file, "Message: ");
    vfprintf(file, format, args);
    fprintf(file, "\n");
    va_end(args);

    fclose(file);
}

void logGlsVector(const gsl_vector *vector, FILE *file) {
    fprintf(file, "Vector: x: %lf, y: %lf, z: %lf", gsl_vector_get(vector, 0), gsl_vector_get(vector, 1), gsl_vector_get(vector, 2));
}