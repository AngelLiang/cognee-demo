# cognee demo

这是一个使用 `cognee` 库进行知识图谱操作的演示项目。

## 项目说明

本项目演示了如何使用 `cognee` 库进行以下操作：
1.  从文本数据中添加信息。
2.  生成知识图谱。
3.  查询知识图谱以获取相关信息。

## 环境准备


首先，确保你已经安装了 `uv`。然后拷贝 .env.example 为 .env ，配置大模型

```
LLM_PROVIDER=custom
LLM_MODEL=
LLM_ENDPOINT=
LLM_API_KEY=
```


## 如何运行

运行 `uv run main.py` 脚本即可查看效果。

