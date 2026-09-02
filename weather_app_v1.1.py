import streamlit as st
from google import genai

# ===== Gemini APIキー =====
API_KEY = "AQ.Ab8RN6Kv8VNlvybATlx-rGdQ4r0kpFrgVLbg85JPzfxcPO46Bg"

client = genai.Client(api_key=API_KEY)

st.set_page_config(
    page_title="AI天気アプリ",
    page_icon="??"
)

st.title("?? AI天気アプリ")

city = st.selectbox(
    "地域を選択してください",
    ["東京", "大阪", "札幌", "さいたま"]
)

if st.button("AI解説生成"):

    # 仮の天気データ
    weather_data = {
        "東京": {
            "weather": "晴れ",
            "temp": 32,
            "rain": 60
        },
        "大阪": {
            "weather": "曇り",
            "temp": 34,
            "rain": 40
        },
        "札幌": {
            "weather": "雨",
            "temp": 25,
            "rain": 80
        },
        "さいたま": {
            "weather": "曇り",
            "temp": 25,
            "rain": 50
        }
    }

    data = weather_data[city]

    prompt = f"""
    次の天気情報を一般向けに50文字程度で説明してください。

    地域: {city}
    天気: {data['weather']}
    気温: {data['temp']}℃
    降水確率: {data['rain']}%
    """

    with st.spinner("AIが解説中..."):

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

    st.subheader("天気情報")

    st.write(f"地域 : {city}")
    st.write(f"天気 : {data['weather']}")
    st.write(f"気温 : {data['temp']}℃")
    st.write(f"降水確率 : {data['rain']}%")

    st.subheader("AIコメント")

    st.success(response.text)
