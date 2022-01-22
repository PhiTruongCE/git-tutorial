#include <iostream>

using namespace std;

/*Test github*/

void swap(int &a,int &b){
    a = a + b;
    b = a - b;
    a = a - b;
}

int main(){
    int a = 3;
    int b = 4;
    swap(a,b);
    cout<<a<<" "<<b;
    return 0;
}