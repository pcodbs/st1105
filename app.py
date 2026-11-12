import streamlit as st

st.title("10주차 스트림릿 연습 채유니.")

st.info("안녕하세요. 소개페이지..")
st.error("빨간 박스")
st.success("초록 박스")
st.warning("노란 박스")

st.header("메인페이지")
st.subheader("그 다음 중제목")
st.write("모든 내용 다 쓰기 가능")
st.markdown("이것은 **텍스트** 쓰기")
st.latex("ax^2+bx+c=0")
st.code("print('hello teachers')")
st.write("---")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("image1.jpg", use_container_width=True)

st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTj5ANoZdAmcssAoXT8ejHfJOIGGRPxmr7PSH3_YseA3A&s=10")
st.subheader("나 유신우예요!! >_<")
st.video("https://www.youtube.com/watch?v=8XDI2kk6qQU")

st.link_button("데스모스 행렬 계산기 바로가기", "https://www.desmos.com/matrix?lang=ko")
st.components.v1.iframe("https://www.desmos.com/matrix?lang=ko", height=500)