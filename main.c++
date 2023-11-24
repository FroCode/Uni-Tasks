#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main() {

  vector<int> v = {1, 2, 3, 4, 5};
  vector<int>::iterator it = v.begin() + 1;
  for (int i = 0 ; v.begin() + i != v.end(); i++) {
    cout << "ele : " << *(v.begin() + i) << endl;
  
  }
  cout << "first ele : " << *it << endl;
  
  return 0;

}