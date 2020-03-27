# input:
# 8
# 12 2 51 4 9 1 20 7

# output:
# 2 4 12 51 1 7 9 20


#include <bits/stdc++.h>
using namespace std;
int main() {
    int a, b, c, d, e, f, t;
    scanf("%d", &t);
    while (t--) {
        scanf("%1d%1d%1d%1d%1d%1d", &a, &b, &c, &d, &e, &f);
        if (a + b + c != d + e + f)
            printf("Wish you good luck.\n");
        else printf("You are lucky!\n");
    }
    return 0;
