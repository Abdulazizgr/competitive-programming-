#include <iostream>
using namespace std;

int main()
{
    int x;
    int y;
    int sum = 0;
    cin >> x;
    for (int i = 0; i < x; i++)
    {
        cin >> y;
        if (y > 10)
        {
            y = y - 10;
            sum += y;
        }
    }
    cout << sum;
}

// B - Nuts
