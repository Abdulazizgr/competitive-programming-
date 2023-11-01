#include <iostream>
using namespace std;

int main()
{
    int x, y, z;
    cin >> x >> y >> z;

    while (true)
    {
        if (z < y)
        {
            int a = 1;
            z = a * z;
            if ((z > x) && (z < y))
            {
                cout << z;
                break;
            }
            a += 1;
        }

        else
        {
            cout << -1;
            break;
        }
    }
}

// A - Find Multiple
