# customeFeedbackAnalysis
使用 Python 分析用户反馈
## 使用方法
- 准备用户反馈数据源（表格）
- 安装 openpyxl
  ``` python
  pip install openpyxl
  ```
- 安装 snownlp
  ``` python
  pip install snownlp
  ```
- 将脚本中 `cixing` 方法的第 1 个参数换成本地的数据源表格地址，第 2 个参数换成表格中用户反馈数据所在列
- `wbcixing.save()`中替换为导出表格的地址
- 运行脚本
- 筛选名词 n、形容词 a、动词 v 分析用户反馈核心讨论点
