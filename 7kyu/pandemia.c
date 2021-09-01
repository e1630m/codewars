#include <stdio.h>
#include <string.h>

double infected (const char *world)
{
    int infected_continent = 0, sum_infected = 0, zero = 0, one = 0, total = 0;
    int length = strlen(world);
    for (int i = 0; i < length; i++)
    {
        if (world[i] == '0' || world[i] == '1')
        {
            total++;
            if (world[i] == '1')
            {
                infected_continent = 1;
                one++;
            }
            else
            {
                zero++;
            }
        }
        if (world[i] == 'X')
        {
            if (infected_continent)
            {
                sum_infected += zero + one;
            }
            infected_continent = zero = one = 0;
        }
        else if (i + 1 == length)
        {
            if (infected_continent)
            {
                sum_infected += zero + one;
            }
            else
            {
                sum_infected += one;
            }
        }
    }
    if (!total)
        return (float) 0.0;
    return (double) sum_infected / (double) total * 100;
}
