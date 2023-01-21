import random as rand
generated = []
while True:
    global check_sum
    check_sum = [
        [4, rand.randint(0,9), rand.randint(0,9), rand.randint(0,9), rand.randint(0,9)],
        [rand.randint(0,9), rand.randint(0,9), rand.randint(0,9), rand.randint(0,9), rand.randint(0,9)],
        [rand.randint(0,9), rand.randint(0,9), rand.randint(0,9), rand.randint(0,9), 5],
        [rand.randint(0,9), rand.randint(0,9), rand.randint(0,9), rand.randint(0,9), rand.randint(0,9)],
        [0, rand.randint(0,9), rand.randint(0,9), rand.randint(0,9), rand.randint(0,9)]
        ]
    for i in generated:
        if i == check_sum:
            continue
    generated.append(check_sum)
    for i in check_sum:
        print(i)
    print()

    if sum([check_sum[0][0], check_sum[1][0], check_sum[2][0], check_sum[3][0], check_sum[4][0]]) == 14 and sum(
        [check_sum[0][1], check_sum[1][1], check_sum[2][1], check_sum[3][1], check_sum[4][1]]) == 28 and sum(
        [check_sum[0][2], check_sum[1][2], check_sum[2][2], check_sum[3][2], check_sum[4][2]]) == 24 and sum(
        [check_sum[0][3], check_sum[1][3], check_sum[2][3], check_sum[3][3], check_sum[4][3]]) == 28 and sum(
        [check_sum[0][4], check_sum[1][4], check_sum[2][4], check_sum[3][4], check_sum[4][4]]) == 14 and sum(

        [check_sum[0][0], check_sum[0][1], check_sum[0][2], check_sum[0][3], check_sum[0][4]]) == 29 and sum(
        [check_sum[1][0], check_sum[1][1], check_sum[1][2], check_sum[1][3], check_sum[1][4]]) == 10 and sum(
        [check_sum[2][0], check_sum[2][1], check_sum[2][2], check_sum[2][3], check_sum[2][4]]) == 21 and sum(
        [check_sum[3][0], check_sum[3][1], check_sum[3][2], check_sum[3][3], check_sum[3][4]]) == 24 and sum(
        [check_sum[4][0], check_sum[4][1], check_sum[4][2], check_sum[4][3], check_sum[4][4]]) == 24:
            break
for i in check_sum:
    print(i)


