def solution(strings, n):
    # 1. [s[n] + s] 형태로 변형: n번째 문자가 맨 앞으로 오도록 만듦
    # 예: "sun", n=1 -> "usun"
    prepared = [s[n] + s for s in strings]
    
    # 2. 정렬
    prepared.sort()
    
    # 3. [s[1:]] 슬라이싱으로 원래 문자열 복구: 맨 앞의 임시 문자 제거
    return [s[1:] for s in prepared]

// def solution(strings, n):
//     keys = [(x[n], x) for x in strings]
//     sorted_key = sorted(keys)
//     result = [i[1] for i in sorted_key]
//     return result

# 유효 기간 알 수 없음
# 람다 적용 예상 테스트 10문제
# https://gemini.google.com/share/c6769a266b2b
