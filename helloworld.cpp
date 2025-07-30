#include <iostream>
using namespace std;

string send_msg = "Hello, world!";
string receive_msg = "Hi";

string send() {
    cin >> send_msg;
    cout << "Me:" << send_msg << endl;
}
string receive() {
    cin >> receive_msg;
    cout << "My Proverbs 31 Girl ❤️:" << receive_msg << endl;
}
int main() {
    send();
    receive();
    cout << "Would you like to end convo?" << endl;
    return 0;
}