def solution(record):
    split_record = []   
    dic = {}
    answer = []
    for item in record:         # 문자열 분할 저장 리스트
        split_record.append(item.split())
    
    for r in split_record:      # 딕셔너리로 저장
        if r[0] == 'Enter':
            dic[r[1]] = r[2]
        if r[0] == 'Change':
            dic[r[1]] = r[2]
            
    for y in split_record:      # 변경 사항 모두 저장된 상태에서 입력
        if y[0] == 'Enter':
            answer.append(f'{dic[y[1]]}님이 들어왔습니다.')
        elif y[0] == 'Leave':
            answer.append(f'{dic[y[1]]}님이 나갔습니다.')
            
        
    return answer