def inputWord(arr, w):
    while 1:
        word = input().strip()
        if word == w:
            break
        arr.append(word)
    return arr
# -, #을 입력받기 전까지 리스트 입력을 받음
wordList = inputWord([], '-')
puzzleList = inputWord([], '#')

for puzzle in puzzleList:
    dict = {}
    # puzzle 알파벳의 사용 갯수를 세기 위해 딕셔너리 생성
    for i in set(puzzle):
        dict[i] = 0
    # 모든 단어에 대해
    for word in wordList:
        possible = True
        # puzzle 알파벳들로 해당 단어를 만들 수 있는지 검사
        for w in word:
            if w not in puzzle or word.count(w) > puzzle.count(w):
                possible = False
                break
        # 해당 단어를 puzzle로 만들 수 있으면
        if possible:
            # 각 puzzle 알파벳들에 대해
            for i in set(puzzle):
                cnt = 0
                # 해당 알파벳이 사용되었으면 +1
                if i not in word:
                    continue
                dict[i] += 1

    # 완성된 딕셔너리 cnt 순으로 정렬
    sortedDict = sorted(dict.items(), key=lambda x: x[1])
    # 최소 cnt, 최대 cnt 지정
    minCnt, maxCnt = sortedDict[0][1], sortedDict[-1][1]
    minArr, maxArr = [], []
    # 각 단어의 사용 횟수가 최소 cnt와 같으면 minArr에 추가
    # 최대 cnt와 같으면 maxArr에 추가
    for word, cnt in sortedDict:
        if cnt == minCnt:
            minArr.append(word)
        if cnt == maxCnt:
            maxArr.append(word)

    print("".join(sorted(minArr)), minCnt, "".join(sorted(maxArr)), maxCnt)

# 총평:
# 문제에 논리적으로 접근하는데에는 어렵지 않았다.
# 분명 모든 테스트케이스는 맞았는데
# 약간의 자잘한 실수가 있었기에 계속해서 정답을 받지 못했다.
# 분명 쉬운데 꽤나 오래걸린 문제였으니 어렵다고 보는게 맞는걸지도 모르겠다.