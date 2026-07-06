# https://school.programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):

  users = {}
  text = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
  data = []
  answer = []
  for r in record:
    word = r.split(' ')
    if 'Enter' in word:
        data.append({'name': word[1], 'text': text['Enter']})
    elif 'Leave' in word:
        data.append({'name': word[1], 'text': text['Leave']})

    if len(word) >= 3:
        if users.get(word[1]) == None:
          users[word[1]] = word[2]
        else:
          users[word[1]] = word[2]
    else:
        if users.get(word[1]) == None:
          users[word[1]] = word[2]
  for i, a in enumerate(data):
      answer.append(users[data[i]['name']] + data[i]['text'])

  return answer
