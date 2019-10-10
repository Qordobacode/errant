import spacy
from errant import Checker


# nlp = spacy.load("en")
# checker = Checker(nlp)
# or
checker = Checker()

original_sentences = ['This are a great sentences.', 'Can you seen the sea from where you live.',
                      'Let us discuss about all the softwares problems you\'ve been having recently.',
                      'This sentence contains no errors.']
corrected_sentences = ['This is a great        sentence.', 'Can you see the sea from where you live?',
                       'Let us discuss all the software problems you \'ve been having recently.',
                       'This sentence contains no errors.']
for (original_sentence, corrected_sentence) in zip(original_sentences, corrected_sentences):
    errors, edits = checker.check(original_sentence, corrected_sentence)
    if errors:
        print('original: ' + original_sentence + ' - corrected: ' + corrected_sentence +
              ' - errors: ' + str(errors) + ' - edits: ' + str(edits))
    else:
        print('original: ' + original_sentence + ' - corrected: ' + corrected_sentence + ' - errors: none')
