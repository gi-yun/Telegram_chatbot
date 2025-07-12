# 🤖 기봇 (Gibot) – Telegram 기반 멀티기능 챗봇

기봇(Gibot)은 Python으로 구현된 텔레그램 챗봇으로, **학교 식단 정보 안내**, **영화 및 음악 순위 제공**, **운세 뽑기**, **Gemini AI 대화 기능** 등을 통합한 **멀티 서비스 챗봇**입니다. 사용자는 챗봇 명령어나 키워드 입력을 통해 다양한 정보를 쉽게 받아볼 수 있으며, 매일 정오에는 자동으로 한미락 식단이 그룹 채팅방에 전송됩니다.


---
## 시연 사진
<img width="1094" height="631" alt="image" src="https://github.com/user-attachments/assets/b7dc8f3c-fd17-4ed0-8ba4-651000b2bda0" />



---
## 📌 주요 기능

### ✅ 1. 명령어 기반 기능

| 명령어         | 기능 설명                                          |
| -------------- | -------------------------------------------------- |
| `/start`       | 봇 시작 인사 메시지 전송                           |
| `/fortune`     | 무작위 운세 카드 1장 전송                          |
| `/lunch`       | 오늘의 한미락 식단 정보 전송                       |
| `/lunchweekly` | 이번 주 한미락 식단 전체 전송                      |
| `/testlunch`   | 개발자 테스트용: 그룹 채팅방에 오늘 식단 강제 전송 |

---

### ✅ 2. 키워드 자동 응답 기능

사용자가 일반 텍스트로 메시지를 보낼 때, 특정 키워드를 포함하면 자동으로 응답합니다.

| 키워드 포함                     | 응답 내용                                               |
| ------------------------------- | ------------------------------------------------------- |
| `"gpt"`                         | Google Gemini API를 통한 AI 응답                        |
| `"영화순위"`                    | 영화진흥위원회(KOBIS) API에서 어제 영화 박스오피스 순위 |
| `"멜론순위"`                    | Melon 웹사이트에서 현재 TOP 20 음악 순위                |
| `"사진줘"`                      | 고정 이미지 전송 (예시용)                               |
| `"안녕"`, `"정보"`, `"기분"` 등 | talk_kgy.py의 트리거 워드에 따른 자동 응답              |

---

### ✅ 3. 자동 전송 기능 (스케줄러)

- `APScheduler` 사용
- 매일 **정오(12:00)** 에 `hanmirak.get_today_menu()` 함수를 실행하여 **지정된 그룹 채팅방**에 식단 정보 자동 전송
- `.env` 파일의 `GROUP_CHAT_IDS` 변수에서 대상 방 ID 관리

---

## 🛠️ 구성 파일 설명

### 1. `bot_v2.py`

- 메인 실행 파일
- 텔레그램 봇 실행, 핸들러 등록, 메시지 분석 및 응답 처리
- 명령어 처리, 키워드 응답, 스케줄 등록 기능 포함

### 2. `hanmirak_u.py`

- 부경대학교 홈페이지에서 “한미락” 식당의 주간 식단 정보를 **셀레니움**으로 크롤링
- `update_cache()` : 크롤링 후 캐시에 저장
- `get_today_menu()` : 오늘 식단 정보 반환
- `get_weekly_menu()` : 월~금 전체 식단 반환

### 3. `cache_util.py`

- 캐시 파일(`hanmirak_cache.json`)을 저장/읽기/경로 출력
- 불필요한 중복 크롤링 방지 및 속도 최적화 목적

### 4. `movie.py`

- 영화진흥위원회(KOBIS) Open API를 통해 어제 기준 영화 박스오피스 순위를 받아 문자열로 반환
- API 키는 `.env`의 `MOVIE_TOKEN`에서 불러옴

### 5. `melon.py`

- 멜론 차트 웹페이지에서 음악 순위 TOP 20을 크롤링
- `requests`와 `BeautifulSoup`을 사용

### 6. `gemini.py`

- Google Gemini AI API 연동
- 사용자가 `gpt`라는 키워드를 포함한 문장을 보내면 AI 응답 생성
- `.env`의 `GOOGLE_GEMINI` 환경변수 필요

### 7. `talk_kgy.py`

- 자동 응답 키워드(`TRIGGER_WORDS`) 정의
- 운세 카드 20종(`FORTUNE_CARDS`) 정의 → `/fortune` 또는 인라인 쿼리 응답용

---

## 🔒 환경 변수 설정 (.env 예시)

```env
TELEGRAM_TOKEN=your_telegram_bot_token
GROUP_CHAT_IDS=-1234567890,-987654321
MOVIE_TOKEN=your_kobis_api_token
GOOGLE_GEMINI=your_google_gemini_api_key
```

---

## ⏱ 실행 방법
<img width="1109" height="625" alt="image" src="https://github.com/user-attachments/assets/0de25c3c-3d27-4cb8-afcd-3a4019c329d5" />

---

```bash
##자동실행 방법##
@echo off
wsl -d Ubuntu-22.04 -- bash -c "cd ~ && source venv1/bin/activate && cd chatbot && python bot_v2.py"
```


---

## 📌 사용 예시

**텔레그램 채팅에서 다음과 같이 사용 가능:**

- `/lunch` → "📅 오늘의 한미락 식단 (07월 12일) …"
- `"영화순위"` → "랭킹 1등은 [범죄도시4] 입니다…"
- `"gpt 마동석이 누구야?"` → Gemini가 마동석관련 답변 생성
- `/fortune` → 무작위 타로 운세 카드 제공

---

## 💬 인라인 기능

- 텔레그램 채팅창에 `@<봇아이디>` 입력 시 **인라인 운세 카드 뽑기 기능** 작동
- 예: `@pkgy_bot` → "✨ 당신의 랜덤 운세 카드 …"

---

## ✅ 향후 개선 아이디어

- 스케줄 성능 개선(정확한 시간에 알람이 울리게)
- 캐시 자동 만료 및 재갱신 로직 강화
- 학교 식당 외 다른 외식 정보도 추가 크롤링
- 날씨 정보 추가
