#include <iostream>
using namespace std;

int main()
{
  int x, y;
  cin >> x >> y;
  if ((x == 1 && y == 10) || (y == 1 && x == 10))
  {
    cout << "YES";
  }
  else if (x - 1 == y || y - 1 == x)
  {
    cout << "YES";
  }
  else
  {
    cout << "NO";
  }
}

// A - Edge Checker
