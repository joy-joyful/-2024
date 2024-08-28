import streamlit as st

# 타이틀 설정
st.title('MBTI 기반 성격 분석 및 직업 추천')

# MBTI 유형 입력받기
mbti = st.text_input('당신의 MBTI 유형을 입력해주세요 (예: INFP, ESTJ) : ').upper()

# 버튼 클릭 시 성격 분석 및 직업 추천
if st.button('분석하기'):
    if mbti == 'INFP':
        st.write('INFP - 중재자: 이상주의적이고 가치 지향적인 성격으로, 깊은 감정과 공감을 바탕으로 행동합니다.')
        st.write('추천 직업: 상담사, 작가, 예술가, 심리학자')
    elif mbti == 'ESTJ':
        st.write('ESTJ - 경영자: 체계적이고 조직적이며 현실적입니다. 규칙을 중시하고 리더십을 발휘합니다.')
        st.write('추천 직업: 관리자, 경영자, 군인, 판사')
    elif mbti == 'ENFP':
        st.write('ENFP - 활동가: 창의적이고 열정적이며 타인의 감정을 잘 이해합니다. 새로운 아이디어를 시도하는 것을 좋아합니다.')
        st.write('추천 직업: 마케팅 전문가, 기자, 이벤트 기획자, 배우')
    elif mbti == 'INTJ':
        st.write('INTJ - 전략가: 독립적이고 분석적인 사고를 지니며, 장기적인 계획을 세우는 것을 즐깁니다.')
        st.write('추천 직업: 과학자, 엔지니어, 전략 기획자, 교수')
    else:
        st.write('입력하신 MBTI 유형에 대한 정보가 없습니다. 올바른 MBTI 유형을 입력해주세요.')

# 추가적인 MBTI 유형을 원한다면 elif 블록을 추가하여 다양한 유형을 처리할 수 있습니다.
