//
// Created by kali on 1/10/25.
//

#ifndef LOGGER_H
#define LOGGER_H
#include <gsl/gsl_matrix.h>
extern char *LogName;
void logMatrix(const gsl_matrix *matrix);
void logDatetime();
void logMessage(const char *format, ...) ;

#endif //LOGGER_H
