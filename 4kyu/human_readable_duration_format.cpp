#include <string>

std::string format_duration(int n) {
    if (n == 0)
        return "now";
    int y = n / 31536000, yr = n % 31536000;
    int d = yr / 86400, dr = yr % 86400;
    int h = dr / 3600, hr = dr % 3600;
    int m = hr / 60, s = hr % 60;
    int time[5] = {y, d, h, m, s};
    std::string duration;
    std::string fmt[5] = {"year", "day", "hour", "minute", "second"};
    int count = -1;
    for (int i = 0; i < 5; i++)
        if (time[i])
            count++;
    bool first = true;
    for (int i = 0; i < 5; i++) {
        if (time[i]) {
            duration += std::to_string(time[i]) + " " + fmt[i];
            if (time[i] > 1)
                duration += 's';
            count--;
            if (count > 0)
                duration += ", ";
            if (!count)
                duration += " and ";
        }
    }
    return duration;
}
