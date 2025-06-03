import os
from dotenv import load_dotenv
from openai import OpenAI

# 🔽 .env 파일의 경로를 명시적으로 지정
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

# 🔽 환경 변수에서 API 키 불러오기
api_key = os.getenv("OPENAI_API_KEY")
print("Loaded key:", api_key)  # ← 확인용 출력

# 🔽 OpenAI 클라이언트 생성
client = OpenAI(api_key=api_key)

# 🔽 예시 요청
response = client.chat.completions.create(
    model="gpt-4.1-2025-04-14",  # 또는 본인이 쓸 모델 이름
    messages=[
        {"role": "user", "content": "왜 강남은 강남이라고 할까요?"}
    ],
    temperature=0.0,
)

print(response.choices[0].message.content)
