int divide(int dividend, int divisor) {
    int sign = 1;

    if ((dividend < 0) ^ (divisor < 0)) {
        sign = -1;
    }

    long long dvd = dividend;
    long long dvs = divisor;

    if (dvd < 0) {
        dvd = -dvd;
    }

    if (dvs < 0) {
        dvs = -dvs;
    }

    long long quotient = 0;

    while (dvd >= dvs) {
        long long temp = dvs;
        long long multiple = 1;

        while (dvd >= (temp << 1)) {
            temp <<= 1;
            multiple <<= 1;
        }

        dvd -= temp;
        quotient += multiple;
    }

    if (sign == -1) {
        quotient = -quotient;
    }

    if (quotient > 2147483647) {
        return 2147483647;
    }

    if (quotient < -2147483648LL) {
        return -2147483648LL;
    }

    return (int)quotient;
}