from google import genai

client = genai.Client(
    api_key="AQ.Ab8RN6Kv8VNlvybATlx-rGdQ4r0kpFrgVLbg85JPzfxcPO46Bg"
)

prompt = """
東京
晴れ
最高気温32℃
降水確率60%

一般向けに50文字程度で解説してください。
"""

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

print(response.text)
