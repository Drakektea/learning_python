first_demension = [x + 1 for x in range(10)]
print(f'first_demension =')
print(*first_demension, '\n')

second_demension = [[j * 3 + k + 1 for k in range(3)] for j in range(3)]
print(f'second_demension =')
for j in range(len(second_demension)):
    for k in range(len(second_demension[j])):
        print(second_demension[j][k], end=' ')
    print()
print()

third_demension = [[[j * 9 + k * 3 + i + 1 for i in range(3)] for k in range(3)] for j in range(3)]
print(f'third_demension =')
for j in range(len(third_demension)):
    for k in range(len(third_demension[j])):
        for i in range(len(third_demension[j][k])):
            print(third_demension[j][k][i], end=' ')
        print()
    print()
