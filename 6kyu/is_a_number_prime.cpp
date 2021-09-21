#include <iostream>

bool isPrime(int n) {
    if (n < 2) {
        return false;
    } else if (n < 4) {
        return true;
    } else if (n % 2 == 0 || n % 3 == 0) {
        return false;
    } else {
        for (int i = 5; i * i <= n; i += 6) {
	        if (n % i == 0 || n % (i + 2) == 0) {
		        return false;
	        }
	    }
    }
    return true;
}
