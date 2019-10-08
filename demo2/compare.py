from errant import CompareM2

original = 'demo2/gt.m2'
regular = 'demo2/regular.m2'
word2vec = 'demo2/word2vec.m2'

CompareM2.compare(regular, original, detection_spans=True, score_category=3)
CompareM2.compare(word2vec, original, detection_spans=True, score_category=3)
