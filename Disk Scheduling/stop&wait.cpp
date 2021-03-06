#include<iostream>
using namespace std;

int main()
{
  srand(time(0));
  string data = "ghoshIsGay";
  int timeout = 4;

  int dataSize = data.size();
  string dataReceived;
  cout << "Data to be sent: " << data;
  for (int i = 0; i < dataSize; i++)
  {
    cout << "\n\nSending "
         << data[dataSize - i - 1];

    int RanAckTime = rand() % 6;
    if (RanAckTime < timeout)
    {
      cout << "\nReceived and acknowledged! ";
      dataReceived = data[dataSize - i - 1] + dataReceived;
      cout << "\nData received so far: " << dataReceived;
    }
    else
    {
      int ranlost = rand() % 2;
      if (ranlost == 1)
        cout << "\nAcknowledgement has been lost!";
      else
        cout << "\nAcknowledgement has been delayed! ";
      cout << "\nSending again...";
      i--;
    }
  }
  return 0;
}