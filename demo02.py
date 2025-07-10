"""
uv run demo02.py
"""
import os
import asyncio
import pathlib
from cognee import config, add, cognify, search, SearchType, prune, visualize_graph
# from cognee.shared.utils import render_graph


async def main():
    data_directory_path = str(
        pathlib.Path(
            os.path.join(pathlib.Path(__file__).parent, ".data_storage")
        ).resolve()
    )
    # Set up the data directory. Cognee will store files here.
    config.data_root_directory(data_directory_path)

    cognee_directory_path = str(
        pathlib.Path(
            os.path.join(pathlib.Path(__file__).parent, ".cognee_system")
        ).resolve()
    )
    # 设置 Cognee 系统目录。Cognee 将在此处存储系统文件和数据库。
    config.system_root_directory(cognee_directory_path)

    # 在运行前修剪数据和系统元数据，仅当我们想要“全新”状态时。
    await prune.prune_data()
    await prune.prune_system(metadata=True)

    text = "来自加拿大的才华横溢的音乐家亨利，最初在著名指挥家玛丽亚·罗德里格斯的指导下接受古典钢琴训练。后来，亨利与他的妹妹露西组建了一支名为“枫叶乐队”的摇滚乐队，露西曾在多伦多大学学习音乐作曲。“枫叶乐队”于 2020 年 8 月 12 日发行了他们的首张专辑《极光》，因其融合了古典与摇滚元素而广受好评。露西还积极参与环保活动，并加入了“清洁地球”组织担任区域大使，在那里她倡导更严格的野生动物保护法。亨利受到露西对慈善事业热情的启发，开始在家乡的当地动物收容所做志愿者。虽然亨利和露西最初在创作上存在分歧，但他们最终在结合露西的古典作品和亨利的摇滚吉他 Riff 中找到了和谐。“枫叶乐队”于 2021 年在欧洲巡演，在巴黎、柏林和罗马等主要城市举办了场场爆满的演出。巡演期间，亨利对国际美食产生了浓厚兴趣，并与当地厨师合作拍摄了一部关于地方烹饪技术的短纪录片。"

    # Add the text data to Cognee.
    await add(text)

    # Cognify the text data.
    await cognify()

    # # Get a graphistry url (Register for a free account at https://www.graphistry.com)
    # url = await render_graph()
    # print(f"Graphistry URL: {url}")

    # Or use our simple graph preview
    graph_file_path = str(
        pathlib.Path(
            os.path.join(pathlib.Path(__file__).parent,
                         ".artifacts/graph_visualization.html")
        ).resolve()
    )
    await visualize_graph(graph_file_path)

    # 使用图数据构建上下文的补全查询。
    graph_completion = await search(query_text="告诉我有关亨利的事", query_type=SearchType.GRAPH_COMPLETION)
    print("Graph completion result is:")
    print(graph_completion)
    # ['亨利是来自加拿大的才华横溢的音乐家，最初在著名指挥家玛丽亚·罗德里格斯的指导下接受古典钢琴训练。后来，他与妹妹露西组建了融合古典与摇滚元素的摇滚乐队“枫叶乐队”，他们于2020年发行首张专辑《极光》，并于2021年在欧洲成功巡演。受妹妹露西对慈善热情的影响，亨利开始在家乡的当地动物收容所做志愿者。']

    # 使用文档块构建上下文的补全查询。
    rag_completion = await search(query_text="告诉我有关亨利的事", query_type=SearchType.RAG_COMPLETION)
    print("Completion result is:")
    print(rag_completion)
    # ['亨利是来自加拿大的才华横溢的音乐家，最初接受古典钢琴训练，后来与妹妹露西组建了“枫叶乐队”，发行了融合古典与摇滚元素的首张专辑《极光》。他受到妹妹投身慈善的影响，参与当地动物收容所志愿服务。2021 年，乐队欧洲巡演期间，他对国际美食产生兴趣，并拍摄了地方烹饪技术短纪录片。']

    # 查询与查询相关的所有摘要。
    summaries = await search(query_text="亨利", query_type=SearchType.SUMMARIES)
    print("Summary results are:")
    for summary in summaries:
        print(summary)

    chunks = await search(query_text="亨利", query_type=SearchType.CHUNKS)
    print("Chunk results are:")
    for chunk in chunks:
        print(chunk)


if __name__ == "__main__":
    asyncio.run(main())
