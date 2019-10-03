from errant import Checker

original_tokenized_sentences = ['This are a great sentences .', 'Can you seen the sea from where you live .',
                                'Let us discuss about all the softwares problems you \'ve been having recently .',
                                'This sentence contains no errors .']
corrected_tokenized_sentences = ['This is a great sentence .', 'Can you see the sea from where you live ?',
                                 'Let us discuss all the software problems you \'ve been having recently .',
                                 'This sentence contains no errors .']

checker = Checker()
for (original_tokenized_sentence, corrected_tokenized_sentence) in zip(original_tokenized_sentences,
                                                                       corrected_tokenized_sentences):
    errors, edits = checker.convert(original_tokenized_sentence, corrected_tokenized_sentence)
    if errors:
        print('original: ' + original_tokenized_sentence + ' - corrected: ' + corrected_tokenized_sentence +
              ' - errors: ' + str(errors) + ' - edits: ' + str(edits))
    else:
        print('original: ' + original_tokenized_sentence + ' - corrected: ' + corrected_tokenized_sentence +
              ' - errors: none')
