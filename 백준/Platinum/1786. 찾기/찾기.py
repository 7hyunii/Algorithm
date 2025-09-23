import sys
input = sys.stdin.readline

def LPS(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0      # 이전의 가장 긴 접두사-접미사 길이
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:   # 일치 O
            length += 1
            lps[i] = length
            i += 1
        else:                               # 일치 X
            if length != 0:
                length = lps[length - 1]    # 이전 인덱스 lps 값으로 돌아가서 비교
            else:
                lps[i] = 0
                i += 1
    
    return lps

def KMP(text, pattern):
    n = len(text)
    m = len(pattern)
    
    # LPS 배열 생성
    lps = LPS(pattern)
    
    i = 0  # text의 인덱스
    j = 0  # pattern의 인덱스
    result = []  # 매칭된 시작 위치들
    
    while i < n:
        if text[i] == pattern[j]:  # 문자가 일치
            i += 1
            j += 1
        
        if j == m:                  # 패턴을 모두 찾았을 때
            result.append(i - j)    # 시작 위치 저장
            j = lps[j-1]            # 다음 매칭을 위해 j 조정
        
        elif i < n and text[i] != pattern[j]:   # 불일치
            if j != 0:
                j = lps[j-1]        # LPS를 이용해 j 조정
            else:
                i += 1              # j가 0이면 i만 증가
    
    return result

T = input().rstrip()
P = input().rstrip()

matches = KMP(T, P)

print(len(matches))
for pos in matches:
    print(pos + 1)