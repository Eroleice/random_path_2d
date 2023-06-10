# random_path_2d
有在看YouTube主播[Ava - 凛](https://www.youtube.com/@AvaLab)制作的[游戏](https://youtu.be/JRL-hyeU7P0)，正好想试一试随机生成游戏地图的方法，于是做了一个简单的deemo出来。
参考了[戴克斯特拉算法](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)的思路~

# 运行
直接运行就可以了，会print出来整个地图（默认10x10，可修改），矩阵中的S代表起点，E代表终点，星号代表这是路线。示例：
```
0  0  0  0  0  0  0  0  0  0
0  0  0  0  *  *  *  *  0  0
0  0  0  0  S  0  0  *  0  0
0  0  0  0  0  0  0  *  0  0
0  0  0  0  0  0  0  *  0  0
0  0  0  0  0  0  *  *  0  0
0  0  0  0  0  0  *  0  0  0
0  0  0  0  0  0  *  *  *  0
0  0  0  0  0  0  0  0  *  0
0  0  0  0  0  0  0  0  E  0
```

# 逻辑
生成10x10的矩阵后，把所有坐标记录到一个list中，打乱顺序（等效随机抽取）
随机抽一个坐标，看看删掉这个坐标后S还能不能走到E，若能，就删了；若不能，把这个坐标记录为必要坐标
当整个矩阵的坐标删除的只剩必要坐标的时候，说明只剩下了一条路

## 如何判断S到E能否走通
从S点开始，找到S点相邻的坐标点并记录，这时候我们有5个坐标点（假设4个相邻坐标没有撞墙或者移除）
5个坐标点再召相邻坐标点，记录
直到找到E点，或者无法找到新的相邻坐标点。过程演示：
![image](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#/media/File:Dijkstras_progress_animation.gif)
