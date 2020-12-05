#include <iostream>
#include <unordered_set>

using namespace std;

// PYTHON IS TOO SLOW D=

int main() {    

    unordered_set<int> seen;
    unsigned int r0 = 0, r2 = 0, r3 = 0, r5 = 0;

start:
    r5 = r3 | (1 << 16);
    r3 = 15028787;
inner:
    r2 = r5 & 255;
    r3 += r2;
    r3 = (r3 * 65899) % (1 << 24);

    if (r5 >= 256) {
        r2 = 0;
        while ((r2 + 1) * 256 <= r5) { // hand analysis of assembly shows that this is equivalent
            r2++;
        }
        r5 = r2;
        goto inner;
    }
    else {
        if (seen.count(r3) > 0) {
            cout << "REPEATED DETECTED! " << r3 << endl; // take the value just before repeat as the answer
            return 0;
        }
        else {
            seen.insert(r3);
            cout << r3 << endl;
        }
        goto start;
    }

    return 0;
}