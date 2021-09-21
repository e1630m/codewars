#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int is_valid_ip(const char *addr)
{
    if (!*addr || *addr == '.' || strlen(addr) > 15 || strlen(addr) < 7)
    {
        return 0;
    }
    int num_dots = 0, pos = 0, start = 0, diff = 0;
    char chunk[3] = "";
    while (*addr)
    {
        if (!isdigit(*addr))
        {
            if (*addr != '.')
            {
                return 0;
            }
            else
            {
                num_dots++;
                if ((diff > 1 && addr[-diff] == '0') || diff > 3)
                {
                    return 0;
                }
                strncpy(chunk, addr - diff, diff);
                chunk[diff] = '\0';
                if (atoi(chunk) < 0 || atoi(chunk) > 255)
                {
                    return 0;
                }
                start = pos + 1;
            }
        }
        pos++, addr++;
        diff = pos - start;
    }
    if (num_dots != 3 || diff > 3)
    {
        return 0;
    }
    strncpy(chunk, addr - diff, diff);
    chunk[diff] = '\0';
    if (atoi(chunk) < 0 || atoi(chunk) > 255)
    {
        return 0;
    }
    return 1;
}

int main(void)
{
    printf("%d", is_valid_ip("124.134.12.1245"));
}
