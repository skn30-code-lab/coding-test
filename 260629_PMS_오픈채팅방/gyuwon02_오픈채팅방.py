def solution(record):
    answer = []
    user_dict = {}  # 유저 아이디와 최종 닉네임 저장(Dictionary)
    
    # 기록 하나씩 보면서 유저의 최종 닉네임 파악
    for log in record:
        # 공백 기준으로 문자열 나누기
        parts = log.split()
        command = parts[0]  # Enter, Leave, Change 중 1
        user_id = parts[1]      # 유저 아이디
        
        # Enter/Change => 닉네임 ㅇ
        if command == "Enter" or command == "Change":
            nickname = parts[2]
            user_dict[user_id] = nickname  # 딕셔너리(아이디:닉네임) 저장
            
    # 최종 닉네임으로 메시지 생성
    for log in record:
        parts = log.split()
        command = parts[0]
        user_id = parts[1]
        
        # user_dict[user_id] => 유저의 최종 닉네임
        if command == "Enter":
            answer.append(f"{user_dict[user_id]}님이 들어왔습니다.")
        elif command == "Leave":
            answer.append(f"{user_dict[user_id]}님이 나갔습니다.")
            # Change 명령어는 메시지를 안 남기므로 무시
            
    return answer
