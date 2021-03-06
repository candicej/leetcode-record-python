# leetcode-record-python
A record of leetcode ordered by tag in python.

# 数组相关

15.三数之和（medium）**** 

https://leetcode-cn.com/problems/3sum/

考察数组的遍历，双指针，难点是去重，果然medium的题做起来是不一样哈哈哈，必须二刷

26.删除有序数组中的重复项

https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

考察双指针

35.搜索插入位置（easy)

https://leetcode-cn.com/problems/search-insert-position/

考察数组的遍历以及二分法查找

53.最大子序和(easy)

https://leetcode-cn.com/problems/maximum-subarray/

考察贪心算法，动态规划，分治算法。只更新了贪心算法系列，其他的后面再更新

66. 加一(easy)

https://leetcode-cn.com/problems/plus-one/

考察数组的遍历，或者考察数组，字符串，整数的相互转换

80. 删除有序数组中的重复项 II（medium）

https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/

考察双指针，边界条件的判断，和 26.删除有序数组中的重复项 差不多，难一点

136.只出现一次的数字（easy)

https://leetcode-cn.com/problems/single-number/

考察位运算，比较经典

137.只出现一次的数字 II（medium）

https://leetcode-cn.com/problems/single-number-ii/

考察hash表，进阶解法是有限状态机和位运算的高级应用，值得二刷，毕竟是谷歌的笔试题


217.存在重复元素（easy)

https://leetcode-cn.com/problems/contains-duplicate/

考察hash表的应用或者排序然后遍历数组


# 字符串相关
9. 回文数（easy）

https://leetcode-cn.com/problems/palindrome-number/

考察翻转后半部分，停止条件是 原数字小于等于翻转后的数字，最后判断x == reverse or x == reverse // 10 （奇数和偶数不同）

58.最后一个单词的长度（easy)

https://leetcode-cn.com/problems/length-of-last-word/

主要考察字符串的应用，难点是最后几个连续都是空格的情况

14. 最长公共前缀（easy）

https://leetcode-cn.com/problems/longest-common-prefix/

考察字符串是否相等,遍历一个列表，依次进行比较，有难度。值得二刷

415. 字符串相加(easy)

https://leetcode-cn.com/problems/add-strings/

考察模拟加法，难点是两个数不相等的时候需要补0，那么需要用while循环判断i or j >=0 因为，数组会越界，不能作为判断条件


# 链表相关
2. 两数相加 （medium）

https://leetcode-cn.com/problems/add-two-numbers/

考察遍历两个链表，相加，并且创建一个新链表。难点：两个链表长度不一样的情况，进位，如何创建一个链表，以及哑结点的使用

19.删除链表的倒数第 N 个结点（medium）

https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/

考察双指针，其实不难，主要是边界条件的处理，加一个dummy节点就可以了

21.合并两个有序链表（easy)

https://leetcode-cn.com/problems/merge-two-sorted-lists/

考察链表的遍历和递归，也可以用迭代，还没尝试

82.删除排序链表中的重复元素 II（medium）

https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/

考察链表的遍历，添加了dummy节点和两个指针，有一点难度

83.删除排序链表中的重复元素(easy)

https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/

考察链表的遍历，很经典，难度不大

141.环形链表(easy)

https://leetcode-cn.com/problems/linked-list-cycle/

考察链表中是否存在环，快慢指针，有点不好想到，多练习

203.移除链表元素（easy)

https://leetcode-cn.com/problems/remove-linked-list-elements/

考察链表的遍历，难点在于边界点的处理，注意每次循环cur只移动一次，就不会出错

206. 反转链表（easy)

https://leetcode-cn.com/problems/reverse-linked-list/

考察链表的遍历 和递归或者迭代，对于我来说很难，不太明白，主要是看递归返回的结果怎么传到上一层，值得二刷

二刷：用了迭代的方法，两个指针遍历，依次翻转！比递归好理解！！！

234. 回文链表（easy）***

https://leetcode-cn.com/problems/palindrome-linked-list/

考察：寻找链表的中间节点，以及翻转后部分链表，进行比较。难点：cur结束的条件 值得二刷

# 动态规划

5.最长回文子串(medium)

https://leetcode-cn.com/problems/longest-palindromic-substring/

考察如何填dp表，状态转移方程，二维表，有难度

53.最大子序和(easy)

https://leetcode-cn.com/problems/maximum-subarray/

考察动态规划，状态转移，或者可以使用分治（待补充)

62.不同路径（medium）

https://leetcode-cn.com/problems/unique-paths/

考察填表（有点技巧），状态转移，简单哈

63.不同路径II (medium)

https://leetcode-cn.com/problems/unique-paths-ii/

考察填表，但是这个填表稍微有一点难搞，要考虑dp[0,0]的特殊性，还有边界条件的处理

64.最小路径和（medium）

https://leetcode-cn.com/problems/minimum-path-sum/

考察二维数组的初始化和状态转移方程，跟62很像，不难哈

70.爬楼梯（easy)

https://leetcode-cn.com/problems/climbing-stairs/

最经典的动态规划，本质是斐波那契数列，不错

121.买卖股票的最佳时机（easy）

https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/

考察动态规划的基本思想，刚开始没想到解法，其实就是将大问题的解变成小问题的解，更新状态就可以了

122.买卖股票的最佳时机 II（medium)

https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/

考察思维，怎么能够最大收益？不就是有涨就买入

139.单词拆分（medium）

https://leetcode-cn.com/problems/word-break/

考察动态规划，但是我刚开始用的双指针，没有考虑前缀相同的情况，会有部分测试样例没法通过，这道题应该是先遍历i，再遍历j，这样不会漏掉情况。

198.打家劫舍（medium）

https://leetcode-cn.com/problems/house-robber/

考察特例判断和状态转移方程，思想就是动态规划的基本思想：大问题转化为小问题

300. 最长递增子序列 （medium）

https://leetcode-cn.com/problems/longest-increasing-subsequence/

考察第i个状态和前面状态的关系，状态转移方程不好想，值得二刷

1143. 最长公共子序列（medium） ***

https://leetcode-cn.com/problems/longest-common-subsequence/

考察二维的动态规划，非常经典！！！！思想也很好，自底向上实现，必看

# 哈希表

1.两数之和（easy) **

https://leetcode-cn.com/problems/two-sum/

考察利用hashtable来减少时间，难点在于字典的键值怎么设置，以及enumerate函数的使用

128. 最长连续序列（medium）****

https://leetcode-cn.com/problems/longest-consecutive-sequence/

考察利用set来判断元素是否出现过，首先是去重，然后遍历（便利条件的处理）值得二刷，思想不太好想

146. LRU 缓存（medium） ****

https://leetcode-cn.com/problems/lru-cache/

考察的太多了！！！我觉得太难了，考察了hash表，双链表，链表里存储了key和value两个值，太难了，必须二刷

169.多数元素 （easy）*

https://leetcode-cn.com/problems/majority-element/

考察hash表的应用或者先排序后选择


# 栈和队列

20. 有效的括号 （easy） ***

https://leetcode-cn.com/problems/valid-parentheses/

考察栈的使用，优化：通过字典来优化

155. 最小栈(easy) **

https://leetcode-cn.com/problems/min-stack/

考察 栈 用列表来模拟

232. 用栈实现队列（easy）****

https://leetcode-cn.com/problems/implement-queue-using-stacks/

考察 队列的性质，先进先出，那么就需要两个栈来实现，我个人觉得很难，尤其是这种需要init函数的，值得二刷。多熟练就好了

# 树

144. 二叉树的前序遍历 (easy) **

https://leetcode-cn.com/problems/binary-tree-preorder-traversal/

考察树的遍历，迭代和递归

94. 二叉树的中序遍历  (easy) ***

https://leetcode-cn.com/problems/binary-tree-inorder-traversal/

考察树的遍历，迭代和递归

145. 二叉树的后序遍历 (easy) ****

https://leetcode-cn.com/problems/binary-tree-postorder-traversal/submissions/

二叉树主要考察递归和迭代，递归相对简单，迭代利用栈的特性来实现，目前还不太掌握

104. 二叉树的最大深度 (easy) **

https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/

考察深度搜索，递归实现就可以, 难点应该是子问题和问题的联系，就是+1

112. 路径总和(easy) **

https://leetcode-cn.com/problems/path-sum/

考察递归, 不用sum直接递归下一个子问题



# 滑动窗口

239. 滑动窗口最大值 (hard) *****

https://leetcode-cn.com/problems/sliding-window-maximum/

考察双向队列，队首元素存储最大元素，很难理解

# 二分查找

35.搜索插入位置（easy)

https://leetcode-cn.com/problems/search-insert-position/

考察数组的遍历以及二分法查找

69. x 的平方根(easy)

https://leetcode-cn.com/problems/sqrtx/

考察二分查找

704. 二分查找(easy)

https://leetcode-cn.com/problems/binary-search/

最基础的二分查找，关键是循环停止条件 l<=r


to do list:
27 4 92.63.123.118 102. 107
 
top 100 to do:
88 





 
