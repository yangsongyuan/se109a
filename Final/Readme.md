# 用python實作希爾排序法(shell sort)

# 原理
希爾排序是把記錄按下標的一定增量分組，對每組使用直接插入排序算法排序；隨著增量逐漸減少，每組包含的關鍵詞越來越多，當增量減至1時，整個文件恰被分成一組，算法便終止。
# 參考資料
https://blog.csdn.net/ggdhs/article/details/90613577