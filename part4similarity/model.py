from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import part4similarity.segment as segment

def genermodel():
    segment.seg()
    # 由于训练的模型每次都有所不同，我们已经经过多次训练生成一个比较好的模型，并且放在文件夹下了
    # 如果想要训练新的模型，可以将下面代码的注释去掉
    # f=open('output/bilibili_seg.txt', 'rb')
    # model = Word2Vec(LineSentence(f),sg=1,size=100,window=10,min_count=1,workers=15,sample=1e-3)
    # model.save('wordvec_bilibili.word2vec')
    # print('训练完成')

