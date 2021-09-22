#include <string>
#include <iostream>

std::string decomp(int n) {
    bool primes[n + 1];
    std::fill_n(primes, n + 1, true);
    for (int i = 2; i * i <= n; i++) {
        if (primes[i] == true)
            for (int j = i * 2; j <= n; j += i)
                primes[j] = false;
    }
    std::string s;
    for (int i = 2; i <=n; i++) {
        if (primes[i]) {
            int exp = 0, tmp = n;
            while (tmp) {
                tmp /= i;
                exp += tmp;
            }
            if (exp) {
                if (i != 2)
                    s += " * ";
                s += std::to_string(i);
                if (exp > 1)
                    s += "^" + std::to_string(exp);
            }
        }
    }
    return s;
}
