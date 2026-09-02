import streamlit as st

st.title("AI天気アプリ")

city = st.selectbox(
    "地域",
    ["東京", "大阪", "札幌"]
)

if st.button("実行"):
    st.write(f"{city}の天気を取得しました")