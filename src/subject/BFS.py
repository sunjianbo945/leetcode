
'''
BFS模板
模板1

void search(...)
{
    queue q;
    q.push(startRoot);
    while (!q.empty()) {
        // 按照节点处理
        curNode = q.front();
        q.pop();

        if (...) {
            // 处理curNode,并把curNode的相邻Nodes加入队列
        }
    }

}


模板2

void search(...)
{
    queue q;
    q.push(startRoot);
    while (!q.empty()) {
        // 按照层次处理
        size = q.size();
        for (i = 0; i < size; i++) {
            curNode = q.front();
            q.pop();

            if (... ) {
                // 处理curNode,并把curNode的相邻Nodes加入队列
            }
        }
    }

}
---------------------
作者：renwotao2009
来源：CSDN
原文：https://blog.csdn.net/renwotao2009/article/details/52993277
版权声明：本文为博主原创文章，转载请附上博文链接！


'''
