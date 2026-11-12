import array
import io
import math
import wave

import streamlit as st

classcode = "1234"
code = st.text_input("강의코드를 입력해주세요")

# 입력이 없으면 안내, 1234이면 "환영합니다", 아니면 "코드가 일치하지 않습니다"
if code.strip() == "":
    st.warning("코드를 입력하세요")
elif code == classcode:
    st.success("환영합니다")
else:
    st.error("코드가 일치하지 않습니다")


st.subheader("다양한 인풋")

# 객관식(라디오버튼, 체크박스), 주관식 (숫자만 입력, 텍스트 입력), 슬라이더, 파일 업로드

# A가 답이다.


agree = st.checkbox("신합니다.")
if agree:
    st.success("신하셨습니다.")
else:
    st.error("신하지 않으셨습니다.")

answer2 = st.text_input("이름을 입력해주세요.", placeholder="홍길동")
answer3 = st.number_input("숫자를 입력해주세요.", 
min_value=0,
max_value=100,
step=5,
value=50)

st.write(answer3*20)

if st.button("확인"):
    st.success("확인되었습니다.") 

# 라디오버튼 문제에 대한 정답 제출하기 버튼 -> 피드백
answer = st.radio("일차방정식 2x+1=15를 풀어보세요.", ["5", "6", "7", "8"])
if st.button("제출"):
    if answer == "7":
        st.success("정답입니다")
    elif answer == "8":
        st.warning("8은 오답입니다")
    else:
        st.error("다시 풀어보세요.")


@st.cache_data
def twinkle_wav() -> bytes:
    rate = 22050
    notes = [
        261.63, 261.63, 392.00, 392.00, 440.00, 440.00, 392.00,
        349.23, 349.23, 329.63, 329.63, 293.66, 293.66, 261.63,
    ]
    samples = array.array("h")
    for index, freq in enumerate(notes):
        count = int(rate * (0.7 if index in (6, 13) else 0.35))
        for t in range(count):
            fade = min(1.0, t / 250, (count - t) / 700)
            samples.append(int(11000 * fade * math.sin(2 * math.pi * freq * t / rate)))
        samples.extend([0] * int(rate * 0.05))

    buffer = io.BytesIO()
    with wave.open(buffer, "wb") as song:
        song.setnchannels(1)
        song.setsampwidth(2)
        song.setframerate(rate)
        song.writeframes(samples.tobytes())
    return buffer.getvalue()


st.subheader("노래 재생")
if st.button("노래 재생"):
    st.audio(twinkle_wav(), format="audio/wav", autoplay=True)

st.subheader("영상 재생")
if st.button("영상 재생"):
    st.video(
        "https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4",
        autoplay=True,
    )

