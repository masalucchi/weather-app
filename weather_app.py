import streamlit as st
from google import genai
import requests

# ===== Gemini APIキー =====
API_KEY = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=API_KEY)


def get_weather(city):

    city_data = {
        "東京": (35.68, 139.76),
        "大阪": (34.69, 135.50),
        "札幌": (43.06, 141.35)
    }

    lat, lon = city_data[city]

    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}"
        f"&longitude={lon}"
        f"&current=temperature_2m"
    )

    response = requests.get(url)

    return response.json()


st.set_page_config(
    page_title="AI天気アプリ",
    page_icon="??"
)

st.title("?? AI天気アプリ")

city = st.selectbox(
    "地域を選択してください",
    ["東京", "大阪", "札幌"]
)

if st.button("AI解説生成"):

    data = get_weather(city)

    temp = data["current"]["temperature_2m"]

    prompt = f"""
    次の天気情報を一般向けに50文字程度で説明してください。

    地域: {city}
    気温: {temp}℃
    """

    with st.spinner("AIが解説中..."):

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

    st.subheader("現在の天気情報")

    st.write(f"地域 : {city}")
    st.write(f"現在気温 : {temp}℃")

    st.subheader("AIコメント")

    st.success(response.text)