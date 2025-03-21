// 234. Palindrome Linked List

#include <iostream>

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;

        // Slow stop at the first node of the second half in even case
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* prev = nullptr;
        ListNode* curr = slow;
        while (curr != nullptr) {
            ListNode* nextNode = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nextNode;
        }
        ListNode* left = head;
        ListNode* right = prev;
        while (right != nullptr) {
            if (left->val != right->val) {
                return false;
            }
            left = left->next;
            right = right->next;
        }

        return true;
    }
};

int main() {
    ListNode n5(1);
    ListNode n4(3, &n5);
    ListNode n3(5, &n4);
    ListNode n2(3, &n3);
    ListNode n1(2, &n2);

    Solution sol;
    bool result = sol.isPalindrome(&n1);
    std::cout << result;
}