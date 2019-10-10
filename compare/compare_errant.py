from errant import Checker
import json
from collections import Counter
import glob


checker = Checker()

path = 'compare/resources/*.json'
for filename in glob.glob(path):
    output = open(filename + '-difference-v1.2.4.txt', 'w')
    total_count = 0
    difference_count = 0
    with open(filename, 'r') as h:
        data = json.load(h)
        for item in data:
            edits = item['edits']
            errors190_counter = Counter([edit[2] for edit in edits])
            original_sentence = item['sentence_gt']
            corrected_sentence = item['sentence']
            errors221, edits221 = checker.check(original_sentence, corrected_sentence)
            errors221_counter = Counter([error.name for error in errors221])
            if errors190_counter != errors221_counter:
                output.write('1.9.0: ' + str(errors190_counter) + '\n')
                output.write('2.2.1: ' + str(errors221_counter) + '\n')
                output.write(str(item) + '\n')
                output.write('===================================================' + '\n')
                difference_count += 1
            total_count += 1
    print('Finished processing file: ' + filename +
          ' - total: ' + str(total_count) +
          ' - difference: ' + str(difference_count) +
          ' ({0:.0f}%)'.format(difference_count/total_count * 100))
    output.close()