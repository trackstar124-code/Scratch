# LAB EXERCISE 01
num = 25
subject = "Computer Science"
is_active = True
text = "Data Science"
first_char = text[0]
last_char = text[-1]
text_length = len(text)
text_upper = text.upper()
second_word = text.split()[1]
text1 = "Computer Science"
fruits = ["banana", "apple", "orange"]
fruits.append("grapes")
fruits[1] = "mango"
first_item = fruits[0]
last_item = fruits[-1]
spam = "Spam spam Spam spam Spam spam Spam Spam Spam spam spams spams spams spams spams spams spams Spam Spam Spam Spams Spam spam spam Spam spams spams Spam Spam Spam Spams Spam spam spam Spam spams spam spam spams spams"
count_Spam = spam.count("Spam")
count_spam = spam.count("spam")
count_spams = spam.count("spams")
spam_clean = spam.lower().replace("spams", "spam")
count_spam_clean = spam_clean.count("spam")
spam_list = spam_clean.split()
count_items = len(spam_list)
spam_list_sliced = spam_list[:4]
print(spam_list)
