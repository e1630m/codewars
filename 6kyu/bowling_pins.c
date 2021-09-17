#include <stdio.h>

char *bowling_pins (size_t length, const int removed_pins[length], char *pins_string)
{
    static const char pins[] = 
        "%c %c %c %c" "\n"
        " %c %c %c "  "\n"
        "  %c %c  "   "\n"
        "   %c   ";
    char p[] = "IIIIIIIIII";
    for (size_t i = 0; i < length; i++)
    {
        p[removed_pins[i] - 1] = ' ';
    }
    sprintf(pins_string, pins,
        p[6], p[7], p[8], p[9],
          p[3], p[4], p[5],
            p[1], p[2],
              p[0]);
    return pins_string;
}
