# leetcode-record-python
A record of leetcode ordered by tag in python.

# 数组相关
1.两数之和（easy)

https://leetcode-cn.com/problems/two-sum/

15.三数之和（medium）

https://leetcode-cn.com/problems/3sum/

考察数组的遍历，双指针，难点是去重，果然medium的题做起来是不一样哈哈哈

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

169.多数元素 （easy）

https://leetcode-cn.com/problems/majority-element/

考察hash表的应用或者先排序后选择

206. 反转链表（easy)

https://leetcode-cn.com/problems/reverse-linked-list/

考察链表的遍历 和递归或者迭代，对于我来说很难，不太明白，主要是看递归返回的结果怎么传到上一层，值得二刷

217.存在重复元素（easy)

https://leetcode-cn.com/problems/contains-duplicate/

考察hash表的应用或者排序然后遍历数组


# 字符串相关

58.最后一个单词的长度（easy)

https://leetcode-cn.com/problems/length-of-last-word/

主要考察字符串的应用，难点是最后几个连续都是空格的情况

14. 最长公共前缀（easy）

https://leetcode-cn.com/problems/longest-common-prefix/

考察字符串是否相等,遍历一个列表，依次进行比较


# 链表相关

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


# 动态规划

5.最长回文子串(medium)

https://leetcode-cn.com/problems/longest-palindromic-substring/

考察如何填dp表，状态转移方程

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

1143. 最长公共子序列（medium） ***

https://leetcode-cn.com/problems/longest-common-subsequence/

考察二维的动态规划，非常经典！！！！思想也很好，自底向上实现，必看

# 其他（栈、）

155. 最小栈(easy) **

https://leetcode-cn.com/problems/min-stack/

考察 栈 用列表来模拟

239. 滑动窗口最大值 (hard) *****

https://leetcode-cn.com/problems/sliding-window-maximum/

考察双向队列，队首元素存储最大元素，很难理解


# 树

144. 二叉树的前序遍历 (easy) **

https://leetcode-cn.com/problems/binary-tree-preorder-traversal/

94. 二叉树的中序遍历  (easy) ***

https://leetcode-cn.com/problems/binary-tree-inorder-traversal/

145. 二叉树的后序遍历 (easy) ****

https://leetcode-cn.com/problems/binary-tree-postorder-traversal/submissions/

二叉树主要考察递归和迭代，递归相对简单，迭代利用栈的特性来实现，目前还不太掌握

104. 二叉树的最大深度 (easy) **

https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/

考察深度搜索，递归实现就可以, 难点应该是子问题和问题的联系，就是+1

112. 路径总和(easy) **

https://leetcode-cn.com/problems/path-sum/

考察递归, 不用sum直接递归下一个子问题








 to do list:
 
 27 4 92.63.123.118
 
 102. 107

 
