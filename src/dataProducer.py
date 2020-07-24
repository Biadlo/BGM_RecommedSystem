import random

with open('origin_data.txt', 'a+') as f:
    for i in range(1, 10):
        for j in range(1500):
            line = str(i)
            sales = random.randint(1000, 10000)
            line += ',' + str(sales)

            music = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            class2 = random.randint(0, 9)
            class3 = random.randint(0, 9)
            music[i] = random.uniform(0.5, 0.95)
            while class2 == i:
                class2 = random.randint(0, 9)
            if class2 != class3:
                music[class2] = random.uniform(0, 1 - music[i])
                music[class3] = 1 - music[i] - music[class2]
            else:
                music[class2] = 1 - music[i]

            for k in range(10):
                line += ','+str(music[k])

            views = sales * random.randint(100, 200)
            stars = sales * random.randint(10, 20)

            line += ',' + str(views) + ',' + str(stars)+'\n'

            f.write(line)
