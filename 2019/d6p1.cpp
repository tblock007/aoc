#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

class Node {
public:
  vector<Node*> children;
  int desc;
  Node() : desc(-1) {}
  int numDescs() {
    int result = 0;
    if (desc != -1) return desc;
    for (auto* c : children) {
      result += (1 + c->numDescs());
    }
    return desc = result;
  }
};



int main() {

  unordered_map<string, Node*> map;
  string s;
  while (cin >> s) {
    string first = s.substr(0, 3);
    string second = s.substr(4, 3);
    if (map.count(first) == 0) map.emplace(first, new Node());
    if (map.count(second) == 0) map.emplace(second, new Node());
    if (s[3] == ')') {
      map[first]->children.push_back(map[second]);
    }
    if (s[3] == '(') {
      map[second]->children.push_back(map[first]);
    }
  }

  int result = 0;
  for (auto kv : map) {
    result += (kv.second)->numDescs();
  }
  cout << result;

  return 0;
}