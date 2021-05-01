def matchingStrings(strings, queries):
    otptArr = []
    count = 0
    for query in queries:
        for string in strings:
            if query == string:
                count+=1
        otptArr.append(count)
        count = 0
    return otptArr


if __name__ == '__main__':
    strings = ['def', 'de', 'fgh']
    queries = ['de', 'lmn', 'fgh']
    ans = matchingStrings(strings, queries)
    print(ans)

