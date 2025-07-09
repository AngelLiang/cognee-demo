import os
import dotenv
dotenv.load_dotenv()


import cognee
import asyncio


print(os.getenv('LLM_ENDPOINT'))

async def main():
    # Add text to cognee
    await cognee.add("来自加拿大的才华横溢的音乐家亨利，最初在著名指挥家玛丽亚·罗德里格斯的指导下接受古典钢琴训练。后来，亨利与他的妹妹露西组建了一支名为“枫叶乐队”的摇滚乐队，露西曾在多伦多大学学习音乐作曲。“枫叶乐队”于 2020 年 8 月 12 日发行了他们的首张专辑《极光》，因其融合了古典与摇滚元素而广受好评。露西还积极参与环保活动，并加入了“清洁地球”组织担任区域大使，在那里她倡导更严格的野生动物保护法。亨利受到露西对慈善事业热情的启发，开始在家乡的当地动物收容所做志愿者。虽然亨利和露西最初在创作上存在分歧，但他们最终在结合露西的古典作品和亨利的摇滚吉他 Riff 中找到了和谐。“枫叶乐队”于 2021 年在欧洲巡演，在巴黎、柏林和罗马等主要城市举办了场场爆满的演出。巡演期间，亨利对国际美食产生了浓厚兴趣，并与当地厨师合作拍摄了一部关于地方烹饪技术的短纪录片。")

    # Generate the knowledge graph
    await cognee.cognify()

    # Query the knowledge graph
    results = await cognee.search("告诉我有关亨利的事")

    print()
    print('===output===')
    for result in results:
        print(result)
    print('===output end===')


if __name__ == '__main__':
    asyncio.run(main())
