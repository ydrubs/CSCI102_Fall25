from random import randint

flip_count = 0
head_count = 0

simulations = 0

for i in range(10):

    while head_count < 3:
        flip_count +=1
        flip_result = randint(0,1)

        if flip_result == 0: # 0 means heads
            head_count +=1
            # print("You flipped heads")
        else:
            head_count = 0

    print(f"It took {flip_count} flips to get 3 heads in a row")



