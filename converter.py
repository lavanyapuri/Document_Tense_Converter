import spacy
import pyinflect

nlp = spacy.load('en_core_web_trf')
f = open("C:/ML/NLP/New folder/add_text_here.txt", "r", errors='ignore')
text = f.read()

doc = nlp(text)


print("This is the doc....\n\n")
print(doc)

print("\n.\n.\n.\n.\nThese are the sentences in the doc.....\n\n")
for sent in doc.sents:
    print(sent)

print("\n.\n.\n.\n.\nThese are the tokens in the sentences.....\n\n")

for token in doc[:10]:
    print(token)

print("\n.\n.\n.\n.\nThese are the present and future tense verbs in the doc.......\n\n")

for token in doc:
    if token.tag_ in ['VBP', 'VBZ']:
        print(token)

modified = ""
for token in doc:
    if token.tag_ in ['VBP', 'VBZ']:
        temp = token._.inflect("VBD")
        modified += temp
        modified += token.whitespace_

    else:
        modified += token.text_with_ws

doc1 = nlp(text)
print(modified)



var = ""
flag1 = 0
modified2 = ""
for token in doc1:
    if flag1 == 0:
        if (var == 'will' or var == 'shall') and token.text == 'be':

            modified2 += 'was'
            modified2 += token.whitespace_
        elif(var == 'will' or var == 'shall') and token.text == 'not':
            modified2 += 'did'
            modified2 += token.whitespace_
            modified2 += 'not'
            modified2 += token.whitespace_
            flag1 = 1
        else:
            if token.text in ['will', 'shall']:
                pass
            elif not (token.tag_ in ['VB']) and not (token.text in ['will']):
                modified2 += token.text_with_ws
            if token.tag_ in ['VB']:
                temp = (token._.inflect('VBN'))
                modified2 += temp
                modified2 += token.whitespace_
    elif flag1 == 1:
        modified2 += token.text_with_ws
        flag1 = 0

    var = token.text

print(modified2)
