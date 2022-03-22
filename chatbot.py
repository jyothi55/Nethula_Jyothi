from nltk.chat.util import Chat,reflections
#print(reflections)
pairs=[
    [r'hai',['hai jyothi']],
    [r'how r u',['i am good you?']],
    [r'are you fresher',['yes']]
    ]
chat=Chat(pairs,reflections)
chat.converse()
def quit():
    print("hey i am chatbot")
if __name__=="__main__":
    quit()

