#include <stdbool.h>
#include <string.h>

bool isValidWalk(const char *walk) {
    int n = 0, e = 0, s = 0, w = 0;
    for (unsigned long i = 0; i < strlen(walk); i++)
    {
        switch(walk[i])
        {
            case 'n':
                n++;
                break;
            case 'e':
                e++;
                break;
            case 's':
                s++;
                break;
            case 'w':
                w++;
                break;
        }
    }
    if (strlen(walk) == 10 && n == s && e == w)
        return true;
    return false;
}
