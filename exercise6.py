s = input("enter string: ")
method = int(input("method 1 or 2: "))

if method == 1:
    cnt = {}
    for i in range(len(s)):
        c = s[i]
        if c in cnt:
            cnt[c] = cnt[c] + 1
        else:
            cnt[c] = 1
    ans = -1
    for i in range(len(s)):
        if cnt[s[i]] == 1:
            ans = i
            break
    print(ans)

elif method == 2:
    from collections import OrderedDict
    d = OrderedDict()
    for i in range(len(s)):
        c = s[i]
        if c in d:
            d[c][1] = d[c][1] + 1
        else:
            d[c] = [i, 1]
    ans = -1
    for c in d:
        if d[c][1] == 1:
            ans = d[c][0]
            break
    print(ans)
