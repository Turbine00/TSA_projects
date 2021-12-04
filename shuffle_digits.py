n = 513
ans = []


def shuffler(a, b):

    num = str(a)

    if len(str(a)) == 1:
        if (b+a) not in ans:
            ans.append(b+a)

    else:
        for i in range(len(num)):
            shuffler(num[:i] + num[i+1:], b + num[i])


shuffler(n, "")
print(sorted(ans))
