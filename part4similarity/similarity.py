from gensim.models import Word2Vec
import part4similarity.model as models

def genersimilarity(w1, w2):
    models.genermodel()
    model = Word2Vec.load('wordvec_bilibili.word2vec')
    #w1="毕业"
    y= model.wv.most_similar([w1])
    print("和【%s】最相似度排名"%w1)
    for x in y:
        print(x[0],x[1])
    #w2 ="泪目"
    x=model.wv.similarity(w1,w2)
    print("【%s】和【%s】相似度是%f"%(w1,w2,x))

