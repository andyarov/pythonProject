names = ["Sofia Goggia", "Mikaela Shiffrin", "Wendy Holdener", "Lindsey Vonn", "Frida Hansdotter", "Michelle Gisin", "Ragnhild Mowinckel", "Federica Brignone", "Tina Weirather", "Ester Ledecka"]
medals =[3, 10, 7, 11, 6, 2, 3, 2, 2, 6]

zipped_list = list(zip(names,medals))


dictionary = {i[0]:i[1] for i in zipped_list}
print(dictionary)
