from errant import ParallelToM2
from errant import M2ToM2
from errant import CompareM2

# from command line
# python errant/parallel_to_m2.py -orig demo/orig.txt -cor demo/cor1.txt demo/cor2.txt -out manhal.m2
# python errant/m2_to_m2.py -gold demo/out.m2 -out demo/out.m2.m2
# python errant/compare_m2.py -hyp demo/out.m2 -ref demo/out2.m2 -ds -cat 3


# ParallelToM2 example
original_file = 'demo/orig.txt'
corrected_files = ['demo/cor1.txt']
output_file1 = 'demo/out1.m2'
ParallelToM2.convert(original_file, corrected_files, output_file1)

corrected_files = ['demo/cor2.txt']
output_file2 = 'demo/out2.m2'
ParallelToM2.convert(original_file, corrected_files, output_file2)


# M2ToM2 example
m2_file = output_file1
output_file = 'demo/out1.m2.m2'
edit_type = 'gold'
M2ToM2.convert(m2_file, output_file, edit_type)


# CompareM2 example
res = CompareM2.compare(output_file1, output_file2, detection_spans=True, score_category=3)
