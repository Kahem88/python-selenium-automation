# name = input('kahem patrick')
# print(f'Hello {name} how are you?')


#
# name = input('enter your name: ')
# print(f' hello {name} how are you today? ')
#
#

# x = 6
#
# if x >= 20:
#     print('the number is too high')
# else:
#     print('Thank you')
#

#
# grade = 85
#
# if grade > 90:
#     print('you\'ve got an A!')
#
# elif grade > 80:
#     print('you\'ve got an b!')
# elif grade > 70:
#     print('you\'ve got an b!')
# elif grade > 60:
#     print('you\'ve got an d!')
# else:
#     print('you\'ve got an F!')
#
#
# result = 'great'
# print(result[3])
#
# result2 = "great job!"
# print(result2[-6])
#
# result3 = "what a great job you've done my friend!"
# print(len(result3))
#

#
# operation = 'concatenation'
# print(operation[3:6])
#
# place = "Atlanta, Georgia"
# print(place[0:7])
#

#
# word_1 = "Amazing!"
# print(word_1[0:8:2])
#
# string_2 = "indexing"
# print(string_2[::-1])

#
# name = "kahem"

# for letters in name:
#     print(letters)
#
# for f in range(3):
#     print(name)

# seconds = 10



# def function_1(number):
#     if number > 50:
#         return number + 100
#     else:
#         return number / 100
#
# print(function_1(60))
#
# def weight_convertor(pounds):
#     return pounds / 2.2
#
# print(weight_convertor(5))
#
# grocery_list = ['water', 'cheese', 'bread', 'milk', 'cheese']
# del grocery_list[0]
# print(grocery_list)

# grocery_list = ['water', 'cheese', 'bread', 'milk', 'cheese']
# grocery_list.append('grapes')
# print(grocery_list)

# grocery_list = ['water', 'cheese', 'bread', 'milk', 'cheese']
# grocery_list.pop(1)
# print(grocery_list)

# grocery_list_1 = ['milk', 'cheese', 'cookies', 'peanut butter', 'salt']
# grocery_list_2 = ['juices','oranges', 'cheese', 'ham', 'cookies']
# for item in grocery_list_1:
#         if item in grocery_list_2:
#             print(f"A meeting of minds, you both want {item}")
#
# test_scores = {
#     "james": "83",
#     "julie": "91",
#     "Ryan" : "90",
#     "maria": "80"
#
# }
# for keys, value in test_scores.items():
#     print(keys, value)


class Webpage:

    def __int__(self, url, title):
        self.url = url
        self.title = title
        