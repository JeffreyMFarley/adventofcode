import io

# ------------------------------------------------------

def main():
    with io.open('input1.txt','r', encoding='utf-8') as f:
        a = [l.strip() for l in f]

    width = len(a[0])
    gamma_rate = 0
    epsilon_rate = 0

    for i in range(width):
        ones = 0
        zeros = 0
        for j, _ in enumerate(a):
            x = int(a[j][i])
            if x == 1:
                ones += 1
            else:
                zeros += 1

        gamma_rate = gamma_rate << 1
        epsilon_rate = epsilon_rate << 1
        if ones > zeros:
            gamma_rate += 1
        else:
            epsilon_rate += 1

        print(ones, zeros, gamma_rate, epsilon_rate)

    print(gamma_rate * epsilon_rate)




if __name__ == '__main__':
    main()
