#!/usr/bin/env python
# -*- coding: utf-8 -*-


from gensim.models import word2vec
import logging
from gensim.models.phrases import Phrases
# 主程序
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

model = word2vec.Word2Vec.load("wordvec.model")# python

#model = word2vec.Word2Vec.load_word2vec_format("wordvec_c.model", binary=True)#c 文件
# 计算两个词的相似度/相关程度

y1 = model.similarity(u"主席", u"习近平")
print "【主席】和【习近平】的相似度为："+ str(y1)
print "--------\n"

# 计算某个词的相关词列表
y2 = model.most_similar(u"主席", topn=20)  # 20个最相关的
print "和【主席】最相关的词有：\n"
for item in y2:
    print str(item[0])+ str(item[1])
print "--------\n"

# 寻找对应关系
#vector（小米）- vector（苹果）+ vector（乔布斯）近似于 vector（雷军）
print u"与 ‘习近平 中国’相近，并排除 ‘主席’ 相关的词  "
y3 = model.most_similar([u'习近平', u'中国'], [u'主席'], topn=3)
for item in y3:
    print str(item[0])+ str(item[1])
print "--------\n"

# 寻找不合群的词
y4 = model.doesnt_match(u"习近平 中国  发展 手机".split())
print "'习近平 中国  发展 手机' 不合群的词："+y4
print "--------\n"





#中国的词向量
print (model[u"中国"])

#model.train("我爱中国", total_words=None, word_count=0, total_examples=None, queue_factor=2, report_delay=1.0)
#词的信息Vocab(count:16, index:7, sample_int:936985059)
print (model.vocab[u"习近平"])

#print model.similarity(model.wv[u"中国"], model.wv[u"中国"])

if __name__ == "__main__":
    pass