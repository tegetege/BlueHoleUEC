# coding:utf-8
#IBM Watson　API　のNLCを呼び出す

from watson_developer_cloud import NaturalLanguageClassifierV1
from watson_developer_cloud import NaturalLanguageClassifierV1 as NaturalLanguageClassifier



def nlc_0(text):
	#NLC読み込みのためのアカウント情報
	natural_language_classifier = NaturalLanguageClassifierV1(
	  username='f36f2174-aae0-40a0-8b8c-6d138726727d',
	  password='YW5Yu1VBXdKh')
#watson　ID:8d6cd8x123-nlc-3468
	res = natural_language_classifier.classify('dc9c06x147-nlc-469', text)
	ans = res["top_class"]
	return ans