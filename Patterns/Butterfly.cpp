#include <bits/stdc++.h>
using namespace std;


 
int main() {

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    int t;
    cin >> t;
    
    
    while(t--){
        
        int n;
        cin >> n;
        
        if (n == 1){
            cout << "**\n**" << endl;
            continue;
        }
        string main = "", line = "", newline;

        for (int i = 0; i < n * 2; i++){
            main = main + "*";
            if (i == 0 || i == (n*2)-1){
                line = line + "*";
            }
            else {
                line = line + " ";
            }
        }
        newline = line;
        int numStars = 1;
        vector<string> outputs;

        for (int i = n - 1; i > 0; i--){
            cout << newline << "\n";
            outputs.push_back(newline);
            if (i != 1){
                newline = "";
                for (int k = 0; k < numStars + 1;k++){
                    newline = newline + "*";
                }
                
                for (int j = 0; j < 2*n - (2*(numStars + 1)); j++){
                    newline = newline + " ";
                }
                for (int k = 0; k < numStars + 1;k++){
                    newline = newline + "*";
                }
                numStars++;
            }

        }

        cout << main << "\n" << main << endl;

        for (int i = 0; i < n - 1; i++){
            cout << outputs.back() << endl;
            outputs.pop_back();
        }

        
    }

 
    return 0;
}
