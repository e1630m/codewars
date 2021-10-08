#include <list>
#include <iostream>
#include <cmath>

using namespace std;
int last_digit(list<int> array)
{
    int ldigit = 1;
    for (list<int>::iterator i = array.end(); i != array.begin();)
        ldigit = pow(--i == array.begin() ? *i % 10 : *i < 4 ? *i : *i % 4 + 4, ldigit < 4 ? ldigit : ldigit % 4 + 4);
    return ldigit % 10;
}
