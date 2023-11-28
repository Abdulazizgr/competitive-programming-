#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int x;
    cin >> x;
    vector<int> y(x);
    vector<int> an;
    int z = x;
    for (int i = 0; i < x; i++)
    {
        cin >> y[i];
        if (z > 0)
        {
            an.push_back(z);
            z = z - 1;
        }
    }
    sort(y.begin(), y.end(), greater<int>());

    if (y == an)
    {
        cout << "Yes";
    }
    else
    {
        cout << "No";
    }

    return 0;
}
// C - Swappable