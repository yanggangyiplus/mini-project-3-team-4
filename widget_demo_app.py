import streamlit as st
import pandas as pd
from datetime import datetime

st.title("🎛️ Streamlit 위젯 데모")

# ========== 탭으로 구분 ==========
tab1, tab2, tab3, tab4 = st.tabs(["📝 입력", "📊 데이터", "🎨 레이아웃", "💬 메시지"])

# ========== 탭 1: 입력 위젯 ==========
with tab1:
    st.header("입력 위젯")
    
    # 텍스트 입력
    st.subheader("텍스트 입력")
    text = st.text_input("이름을 입력하세요", placeholder="홍길동")
    text_area = st.text_area("자기소개", placeholder="여기에 입력하세요...")
    
    if text:
        st.success(f"안녕하세요, {text}님!")
    
    # 숫자 입력
    st.subheader("숫자 입력")
    col1, col2 = st.columns(2)
    
    with col1:
        number = st.number_input("나이", min_value=0, max_value=120, value=25)
        st.write(f"입력한 나이: {number}세")
    
    with col2:
        slider = st.slider("점수", 0, 100, 50)
        st.write(f"슬라이더 값: {slider}점")
    
    # 선택
    st.subheader("선택")
    option = st.selectbox("좋아하는 과일", ["🍎 사과", "🍌 바나나", "🍊 오렌지"])
    st.write(f"선택: {option}")
    
    multi = st.multiselect("관심 분야", ["🎨 디자인", "💻 개발", "📊 데이터", "🎮 게임"])
    if multi:
        st.write(f"선택한 항목: {', '.join(multi)}")
    
    # 날짜/시간
    st.subheader("날짜 및 시간")
    date = st.date_input("날짜 선택")
    time = st.time_input("시간 선택")
    st.write(f"선택한 날짜: {date}")
    st.write(f"선택한 시간: {time}")
    
    # 체크박스와 라디오
    st.subheader("체크박스 & 라디오")
    check = st.checkbox("약관에 동의합니다")
    radio = st.radio("성별", ["남성", "여성", "기타"])
    
    if check:
        st.success("✅ 동의하셨습니다!")

# ========== 탭 2: 데이터 표시 ==========
with tab2:
    st.header("데이터 표시")
    
    # 샘플 데이터
    df = pd.DataFrame({
        '이름': ['철수', '영희', '민수'],
        '나이': [25, 30, 28],
        '점수': [85, 92, 78]
    })
    
    st.subheader("📋 데이터프레임")
    st.dataframe(df)
    
    st.subheader("📊 정적 테이블")
    st.table(df)
    
    st.subheader("📈 메트릭")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="평균 나이", value="27.7세", delta="2.3세")
    
    with col2:
        st.metric(label="평균 점수", value="85점", delta="-3점")
    
    with col3:
        st.metric(label="총 인원", value="3명", delta="1명")
    
    st.subheader("🔢 JSON")
    st.json({
        '이름': '홍길동',
        '나이': 30,
        '취미': ['독서', '운동']
    })

# ========== 탭 3: 레이아웃 ==========
with tab3:
    st.header("레이아웃")
    
    st.subheader("컬럼 나누기")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("첫 번째 컬럼")
    
    with col2:
        st.success("두 번째 컬럼")
    
    with col3:
        st.warning("세 번째 컬럼")
    
    st.subheader("Expander (접기/펼치기)")
    with st.expander("클릭하여 자세히 보기"):
        st.write("여기에 숨겨진 내용이 있어요!")
        st.write("긴 설명이나 추가 정보를 넣을 수 있습니다.")
    
    st.subheader("컨테이너")
    container = st.container()
    container.write("컨테이너 안의 내용")
    container.info("컨테이너를 사용하면 레이아웃을 더 자유롭게!")

# ========== 탭 4: 메시지 ==========
with tab4:
    st.header("메시지 및 알림")
    
    st.info("ℹ️ 정보 메시지입니다")
    st.success("✅ 성공적으로 완료되었습니다!")
    st.warning("⚠️ 주의가 필요합니다")
    st.error("❌ 에러가 발생했습니다")
    
    st.subheader("버튼 인터랙션")
    
    if st.button("🎈 풍선 날리기"):
        st.balloons()
        st.success("축하합니다! 🎉")
    
    if st.button("❄️ 눈 내리기"):
        st.snow()
        st.info("눈이 내립니다! ⛄")

# ========== 사이드바 ==========
st.sidebar.title("🎛️ 사이드바")
st.sidebar.write("여기는 사이드바입니다!")

sidebar_option = st.sidebar.selectbox(
    "메뉴 선택",
    ["홈", "데이터", "설정"]
)

st.sidebar.info(f"선택된 메뉴: {sidebar_option}")

if st.sidebar.button("정보 보기"):
    st.sidebar.success("버튼이 클릭되었습니다!")