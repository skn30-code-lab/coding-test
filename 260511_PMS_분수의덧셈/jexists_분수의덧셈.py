import math
def solution(numer1, denom1, numer2, denom2):
  # 공통 분모 계산 (최소공배수)
  common_denom = denom1 * denom2 // math.gcd(denom1, denom2)

  # 분자 통분 및 합산
  fnumer1 = numer1 * (common_denom // denom1)
  fnumer2 = numer2 * (common_denom // denom2)

  # 결과 약분
  fc_denom = math.gcd(fnumer1 + fnumer2, common_denom)
  fnum = (fnumer1 + fnumer2) // fc_denom
  fdenom = common_denom // fc_denom

  answer = [fnum , fdenom]
  return answer
