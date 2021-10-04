#include <string>

std::string add(const std::string& a, const std::string& b) {
    std::string l = a, s = b;
    if (a.length() < b.length())
        swap(l, s);
    std::string reversed_sum = "";
    int lenl = l.length(), lens = s.length();
    int d = lenl - lens, carry = 0;
    for (int i = lens - 1; i >= 0; i--) {
       int tmp = (l[i + d] -'0') + (s[i] - '0') + carry;
       reversed_sum += (tmp%10 + '0');
       carry = tmp / 10;
    }
    for (int i = d - 1; i >= 0; i--) {
        int tmp = (l[i] - '0') + carry;
        reversed_sum += (tmp%10 + '0');
        carry = tmp/10;
    }
    if (carry)
        reversed_sum += (carry + '0');
    std::string sum = "";
    for (int i = reversed_sum.length() - 1; i >= 0; i--)
        sum += reversed_sum[i];
    return sum;
}
