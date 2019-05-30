# We will be iterating over nested lists and/or dictionaries

list_data = [1, 2, 3]
embedded_list = [[1, 2, 3], [7, 8, 9]]
dict_data = {
    1: {
        "name": "James",
        "money": "£30,000"
        },
    2: {
        'name': 'Isabella',
        'money': '£330,001'
        },
    3: {
        'name': 'Philip',
        'money': '£3,000'
        }
}

# for data in embedded_list:
#     print(data)
#     for embed in data:
#         print(embed)

for data in dict_data:
    print(data)
    hash = dict_data[data]

    for embed in hash:
        print(embed + ':', hash[embed])

