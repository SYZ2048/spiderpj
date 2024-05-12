# import part1spider.bilibili as bilibili
# import part2progressbar.drawgraph as drawgraph
# import part3sentiment.sentiment as sentiment
# import part4similarity.similarity as similarity
# import part5wordcloud.wordclouds as wordclouds
# import part5wordcloud.extract as extract
#
# if __name__ == "__main__":
#     print("start spidering...")
#     #bilibili.spider()
#
#     print("graph drawing...")
#     duration = 1175 # 视频总时长为1175秒
#     drawgraph.draw(duration)
#
#     print("sentiment analyzing...")
#     sentiment.genersentiment()
#
#     print("similarity analyzing...")
#     w1 = input("Please input a word:")
#     w2 = input("Please input another word:")
#     similarity.genersimilarity(w1, w2)# 控制台输入
#
#     print("wordcloud generating...")
#     wordclouds.generwordcloud(extract.extract("output/cixing.txt"), "output/wordcloud.png")
#     wordclouds.generwordcloud(extract.extract("output/cixing_a.txt"), "output/wordcloud_a.png")
#     wordclouds.generwordcloud(extract.extract("output/cixing_n.txt"), "output/wordcloud_n.png")
#     wordclouds.generwordcloud(extract.extract("output/cixing_v.txt"), "output/wordcloud_v.png")

import zlib
import binascii
import base64

HEX = '789cad50c9929b400cfd201fc080170e39a89bc5cde2610966b9d160b7d90263ec61f9fa814a662ab75ca2523d3d49af2495fc2d2808b9008b03a9869a9fe0303eb6215b72558215578805b94a1264bd09f3a088baed63df7e7a59f29162935e778faa23fd9bd2fbca14df34762d83d48bf150b8e3ed48b1a4b813a05f13c7d919a58e8146e91154859889afba3576ca6182216ab93837d450ddf0939231b57e5a7af3ae3e1ca7f76b64814b38f8d79d786dfe36f2cd504905afc60cd85701d04235712f4851ca0f277de68afe2e3f7e42469d8d399d84a78d02b5d710fba35f465f567e1a165032d09eee35f25a2a48cc2e24317279d329a50d31eff2fb49686f4baeb85d90355a9984c63d167a66eadb8f4c7459d65c96da8e27faf94ef581515d9b735ced15b765444d3aaa078c94e3708dce6d128e3d9961438a5557bf121f460ba38e1670a4a15ce5e1583b8c370906f6f7eeb0b94c94f7babca9e734945f5e644c5424fb6f4dfa9fa20f47cb47431c9de75c90a704c3c1fcfa05c08f4f15a7c2ce'
result = binascii.unhexlify(HEX)
print(result)
result = zlib.decompress(result)
print(result)
