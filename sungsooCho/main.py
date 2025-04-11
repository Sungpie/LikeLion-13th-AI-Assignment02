import os  # OS(운영체제)와 상호작용하기 위해 os 모듈을 불러옵니다. 
from dotenv import load_dotenv  # .env 파일에 저장된 환경 변수를 불러오기 위해 load_dotenv 함수를 임포트합니다.
from openai import OpenAI  # OpenAI API를 사용하기 위해 OpenAI 클래스를 임포트합니다.

load_dotenv()  # .env 파일에 설정된 환경 변수를 현재 환경에 불러옵니다.

API_KEY = os.environ["API_KEY"]  # 'API_KEY'를 가져옵니다.
SYSTEM_MESSAGE = os.environ["SYSTEM_MESSAGE"]  # 환경 변수 중 'SYSTEM_MESSAGE'를 가져옵니다.

BASE_URL = "https://api.together.xyz"  # Together 플랫폼의 API 요청을 위한 기본 URL입니다.
MODEL = "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo" 

# OpenAI 객체를 생성하여 API 키와 base_url을 설정합니다.
client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

# 메시지 리스트를 정의합니다. 
messages = [
    {"role": "system", "content": SYSTEM_MESSAGE}
]

print("챗봇을 시작합니다! (종료하려면 'exit' 입력)")  # 챗봇 시작 안내 메시지를 출력합니다.

while True:  # 무한 루프를 사용하여 사용자의 입력을 계속 받습니다.
    user_input = input("You: ")  # 사용자에게서 입력을 받습니다.
    if user_input.lower() in ["exit", "quit"]:  # 사용자 입력이 'xit 또는 quit이면 종료 안내 메시지를 출력하고 while 루프를 빠져나옵니다.
        print("챗봇을 종료합니다.")  
        break  

    # 사용자가 입력한 내용을 messages 리스트에 추가합니다.
    messages.append({"role": "user", "content": user_input})

    # OpenAI API를 사용하여 챗봇의 응답을 생성합니다.
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.8  # 창의성을 높여 더 자연스럽고 풍부한 답변을 생성하도록 설정합니다.
    )

    # API로부터 받은 응답(response)에서 실제 챗봇 답변 텍스트를 추출합니다.
    chatbot_reply = response.choices[0].message.content
    print("Chatbot:", chatbot_reply)  # 추출한 챗봇의 답변을 콘솔솔에 출력합니다.

    # 방금 생성된 챗봇의 답변도 messages 리스트에 추가합니다. -> 대화 기억
    messages.append({"role": "assistant", "content": chatbot_reply})


# --- 아이디어 작성 ---
# 이 챗봇을 어디에 응용할 수 있을까요?
# 알고리즘을 자세하고 쉽게 설명해주는 AI 비서를 만드는데 사용할 수 있을 것 같습니다.
