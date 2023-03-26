/*Team - homework t‰iendatud kood
Koodi t‰iendas Taiger Kala*/

#include <iostream>
using namespace std;

int nums[4] = { 2, 7, 11, 15 };
int target = 26;

//Tahame leida arrayst arvu "arv" ja "arv1" positsioonid, mille v‰‰rtuste summa on kokku 26.
int main() {
    for (int arv = 0; arv < size(nums); arv++) {
        for (int arv1 = 0; arv1 < size(nums); arv1++) {
            if (arv != arv1) {
                //Lisan couti et oleks lihtsam troubleshootida
                if (nums[arv] + nums[arv1] == target) {
                    cout << "Arvu 'arv' positsioon on " << arv << " ja 'arv1' positsioon on " << arv1 << "\n";
                }
            }
        }
    }
    return 0;
}