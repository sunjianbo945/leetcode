# OA1: debug，小土刀看一遍就行。其实我当时做的时候压根没看，都很简单的。C++基本就是while死循环，for少括号导致有行没执行，sort<>符号写反等等
#
# OA2: 照着这个链接准备就行，看地里别人汇报全职的挺准的，我这intern的两道题也都遇上了 https://leetcode.com/discuss/interview-question/344650/Amazon-Online-Assessment-Questions
# 我的两道题分别是Most Common Word和Find Pair With Given Sum，都是标记了intern的两星高频题
# 第一题Most Common Word跟原题略有变化，要求如果频率一样return list。有俩test case没过，不知道为啥，不过OA还是过了。
# 第二题则是two sum变种，需要注意的是一个corner case，即遇到都符合条件的无脑选靠后的，非常智障的test case。
#
# OA3: 不管work simulation还是逻辑题都跟小土刀基本一致，建议仔细看看 https://wdxtub.com/interview/14520850399861.html
# 逻辑题不难但是要快，可以提前拿出纸笔并写好a-z，这样找规律时方便写写画画，安排座位时也方便画个图
#
#
# 240，1129
#
#
# Favorite Genre
# Subtree of another tree
#
# 1. Number of Clusters，200。
# 2. Days for updating servers。僵尸矩阵的变形，只有1，0。 1是好server，0是坏server。好server会修复相邻（上下左右）坏server，问最少几天全修好。BFS解的，有1个test case没过，不知道是哪种edge case。
#
# merge 2 sorted list   和 subtree
#
#
# Subtree of another tree
#
# 复习的就是https://leetcode.com/discuss/interview-question/344650/Amazon-Online-Assessment-Questions里面的八道new grad题
#
# 关于两个难题
# critical connections在leetcode上有，我follow的是discussion的这个https://leetcode.com/problems/critical-connections-in-a-network/discuss/382632/Java-implementation-of-Tarjan-Algorithm-with-explanation，里面有两个视频讲解算法的特别有帮助。另外很多人都提到结果的pair必须是有顺序的，不然会有test case过不了
#
# genre应该是唯一一个没有正确参考答案的题了，帖子里的参考答案会有runtime error。这里有一个test case全过的lz参考https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=567423&extra=page%3D2%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3046%5D%5Bvalue%5D%3D5%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311%26orderby%3Ddateline
#
# 如果遇到难题似乎test case有两个没过也不影响后续面试
#
#
# 都是原题，面经里面都有
# printPattern evenoddpattern 1
# sortArray 2
# countOccurrence 3
# reverseArray 4
# replaceValue 5
# printcharacterpattern 6
# removeElement 7
#
# replaceValue, sortArray, checkGrade, printCharacterPattern, countOccurence, manchester, EvenOddPattern.
#
# 1.2sum,有找不到等于sum的case,要返回空list,试了好久才找到2.k closest,直接用priorityqueue就过了
#
# topN  和 路由器
#
#
# 卡车运货 K cloest points to origin
# K distinct chars in string with size K
#
# 1. longest palindrome是lc原题 完全一样 2. Altitude那道题 就是那几道题里 Path With Maximum Score
#
#
# https://docs.google.com/document/d/1veEFozbWpPjKmHkuYgpKVpgTvsJp3eMUZH8CsoVKjPA/edit
#
#
# 猎头来找，说来个OA就onsite，我说好吧，事先在lc上看了看大概什么题。
# 第一题是那个topN竞争对手的，就是hashmap，hashset，priority queue都用得上那题，结果测试有一个不过。
# 也不知道是什么情况不过，move on到下一题。是那个矩阵有0和1，问多久相邻的0全变1。bfs可解。结果又是
# 有一个test不过，也看不出来怎么就不过了。估计是什么特殊情况处理地不对，因为题目也没说如果输入非法
# 返回什么，我是返回-1了。本来题都看过，觉得时间应该挺富裕，结果就剩2-3分钟才提交，每个都没全对。
#
#
#
# ... For each type of truck, they have different space units. For each package, they will be occupying different space units. Your job is to find exactly TWO products that fit into the truck. You will also implement an interval rule that the truck has to reserve exactly 30 space units for safety purposes.
# Assumption
# You will pick up exactly 2 packages.
# Can't pick up one package twice.
# If you have multiple pairs, select the pair witht the largest package. （一开始我这个条件理解错了，后来觉得他的意思就是选那个带有最大的包裹的pair ）
# e.g. truckSpace = 90, packagesSpace = [1,10,25,35,60] return: [2,3]
# e.g. truckSpace = 220, packagesSpace = [40,150,180,10,50]. return: [2,3] instead of [0,1] because of the biggest package thing...
#
#
#
# 第二个就是常规的maximize minimum path. 大家写的时候注意的edge cases where num_col = 0 or num_row =0.
#
#
# 一个是找list of quotes 里面match keyword的quote. 我用hashmap 做的
#
#
#
# 1. Top K Competitors. 有n个toys，和m条quote(string list)。quote里会提到这些toys名称。找出被提到最多 前k位的toys。
# 思路：就是HashMap+priorityqueue来解。不过有两个test case没过。还是lz太菜鸡了
# 2. Critical routers. 就是articulation points，用Tarjan解的
#
# 1. Top N Toys. 就是Top N competitors.. 不过list 里面加了标点我估计我string没处理好 21个test只过了14个...
# 2. Update Servers. 就是zombie in matrix，1是更新过的server，0是没更新的server.. 多少天全部更新完...  17过了16....
#
# 解释代码，性格测试。
