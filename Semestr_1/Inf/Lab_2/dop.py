while True:
    num = input("Введите набор:")
    if num.count('0') + num.count('1') != len(num):
        print('Введите правильный набор! Он должен содержать только 0 и 1:')
    else:
        S = ''
        for i in range(len(num)):
            if (i+1)&i == 0:
                s = 0
                for j in range(i, len(num), 2*(i+1)):
                    s += num[j:j+i+1].count('1')
                S = str(s%2) + S

        error = int(S, 2)
        num1 = ''
        print("Ошибка:", error)
        for i in range(len(num)):
            if error-1 == i:
                num1 += str(int(not(bool(num[i]))))
            else:
                num1 += num[i]

        ans = ''
        for i in range(len(num1)):
            if (i+1)&i != 0:
                ans += num1[i]
        
        print(ans)
        break


        

