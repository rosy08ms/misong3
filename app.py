import streamlit as st

st.set_page_config(page_title="서논술형 자동 채점 시스템", layout="centered")

st.title("📝 효율적인 표현법 서·논술형 자동 채점기")
st.write("학생의 답안을 입력하면 채점 기준에 따라 자동 채점 및 피드백을 제공합니다.")

# 세트 및 문항 선택
set_choice = st.selectbox("학습 세트 선택", ["1세트: 효율적인 표현법 (사회적 촉진/억제)", "2세트: 정전기의 특징", "3세트: 인공 지능 예술"])
question_choice = st.selectbox("문항 선택", ["서·논술형 1 (요약 표)", "서·논술형 2 (설명문 작성)", "서·논술형 3 (영상 기획안)"])

# 학생 답안 입력 폼
st.subheader("✍️ 학생 답안 입력")
if question_choice == "서·논술형 1 (요약 표)":
    ans_1 = st.text_input("(1) 항목 답안 입력")
    ans_2 = st.text_input("(2) 항목 답안 입력")
    ans_3 = st.text_input("(3) 항목 답안 입력")
    student_answer = {"ans_1": ans_1, "ans_2": ans_2, "ans_3": ans_3}
else:
    if question_choice == "서·논술형 2 (설명문 작성)":
        sub_ans_1 = st.text_area("(1) 문장 입력 (설명 방법 괄호 포함)")
        sub_ans_2 = st.text_area("(2) 문장 입력 (설명 방법 괄호 포함)")
    else:  # 서·논술형 3
        sub_ans_1 = st.text_area("(1) 시각 요소 및 효과 입력")
        sub_ans_2 = st.text_area("(2) 청각 요소 및 효과 입력")
    student_answer = {"sub_1": sub_ans_1, "sub_2": sub_ans_2}

# 자동 채점 로직 함수
def grade_answer(set_num, q_type, ans_dict):
    score = 0
    max_score = 100
    feedback = []
    
    # ---------------- 1세트 채점 로직 ----------------
    if set_num == 0:
        if q_type == 0:  # 1번
            score = 100
            if not any(k in ans_dict["ans_1"] for k in ["쉬운", "취미", "노력"]):
                score -= 33; feedback.sypend("(1) 쉬운 과제 또는 노력less 관련 키워드 누락")
            if not any(k in ans_dict["ans_2"] for k in ["커피숍", "도서관", "모임", "함께"]):
                score -= 33; feedback.append("(2) 함께 공부하는 환경(커피숍, 도서관 등) 키워드 누락")
            if not any(k in ans_dict["ans_3"] for k in ["어렵", "혼자", "억제"]):
                score -= 34; feedback.append("(3) 어려운 과제와 혼자 집중하는 내용 누락")
        elif q_type == 1:  # 2번
            score = 100
            if "사회적 촉진" not in ans_dict["sub_1"] or "예시" not in ans_dict["sub_1"]:
                score -= 50; feedback.append("(1) '사회적 촉진' 개념 또는 '예시' 표기 누락")
            if not any(k in ans_dict["sub_2"] for k in ["사회적 억제", "대조", "인과"]):
                score -= 50; feedback.append("(2) '사회적 억제' 개념 또는 설명 방법 표기 누락")
        else:  # 3번
            score = 100
            if not any(k in ans_dict["sub_1"] for k in ["혼자", "집중", "독서실", "억제"]):
                score -= 50; feedback.append("(1) 시각 요소에 '사회적 억제' 환경(혼자 집중) 연출 미흡")
            if not any(k in ans_dict["sub_2"] for k in ["백색소음", "안정", "소음", "분위기"]):
                score -= 50; feedback.append("(2) 청각 요소에 학습 분위기 조성 효과 미흡")

    # ---------------- 2세트 채점 로직 ----------------
    elif set_num == 1:
        if q_type == 0:  # 1번
            score = 100
            if "고여" not in ans_dict["ans_1"]:
                score -= 33; feedback.append("(1) '고여 있는 물' 비유 표현 누락")
            if not any(k in ans_dict["ans_2"] for k in ["정지", "머물", "이동하지"]):
                score -= 33; feedback.append("(2) 전하의 정지/비이동 상태 누락")
            if not any(k in ans_dict["ans_3"] for k in ["위험", "피해", "없"]):
                score -= 34; feedback.append("(3) 위험하지 않다는 결론 누락")
        elif q_type == 1:  # 2번
            score = 100
            if "비유" not in ans_dict["sub_1"] and "비교와 대조" not in ans_dict["sub_1"]:
                score -= 50; feedback.append("(1) 적절한 설명 방법 명칭 괄호 표기 누락")
            if "위험하지" not in ans_dict["sub_2"] or ("인과" not in ans_dict["sub_2"] and "대조" not in ans_dict["sub_2"]):
                score -= 50; feedback.append("(2) 인과적 결론 또는 설명 방법 표기 누락")
        else:  # 3번
            score = 100
            if not any(k in ans_dict["sub_1"] for k in ["고여", "정지", "댐", "물탱크"]):
                score -= 50; feedback.append("(1) 시각 요소에 고여 있는 물/정지 상태 연출 누락")
            if not any(k in ans_dict["sub_2"] for k in ["효과음", "적막", "고요", "안전"]):
                score -= 50; feedback.append("(2) 청각 요소에 안전성/비이동 특성 연계 누락")

    # ---------------- 3세트 채점 로직 ----------------
    else:
        if q_type == 0:  # 1번
            score = 100
            if not any(k in ans_dict["ans_1"] for k in ["알고리즘", "데이터", "초상화"]):
                score -= 33; feedback.append("(1) 알고리즘/데이터 기반 제작 특징 누락")
            if not any(k in ans_dict["ans_2"] for k in ["감정", "철학", "이야기", "어렵"]):
                score -= 33; feedback.append("(2) 예술로 보기 어렵다는 판단 근거 누락")
            if not any(k in ans_dict["ans_3"] for k in ["변화", "확장", "상징적"]):
                score -= 34; feedback.append("(3) 상징적 가치 및 범주 확장 누락")
        elif q_type == 1:  # 2번
            score = 100
            if not any(k in ans_dict["sub_1"] for k in ["노력", "열정", "감정", "철학"]):
                score -= 50; feedback.append("(1) 인간 예술의 내외부적 요소(감정·철학 등) 누락")
            if not any(k in ans_dict["sub_2"] for k in ["상징적 가치", "변화", "확장"]) or not any(m in ans_dict["sub_2"] for m in ["대조", "예시"]):
                score -= 50; feedback.append("(2) AI 예술의 상징적 가치 또는 설명 방법 누락")
        else:  # 3번
            score = 100
            if not any(k in ans_dict["sub_1"] for k in ["알고리즘", "데이터", "그림"]):
                score -= 50; feedback.append("(1) 시각 요소에 AI 제작 방식(데이터/알고리즘) 반영 누락")
            if not any(k in ans_dict["sub_2"] for k in ["범주", "확장", "변화", "상징"]):
                score -= 50; feedback.append("(2) 청각 요소에 상징적 가치/예술 범주 확장 효과 누락")

    return max(0, score), feedback

# 채점 실행 버튼
if st.button("🔍 채점 실행하기"):
    score, feedback = grade_answer(
        ["1세트", "2세트", "3세트"].index(set_choice.split(":")[0]),
        ["서·논술형 1", "서·논술형 2", "서·논술형 3"].index(question_choice.split(" ")[0] + " " + question_choice.split(" ")[1]),
        student_answer
    )
    
    st.divider()
    st.subheader("📊 채점 결과")
    st.metric(label="점수", value=f"{score}점 / 100점")
    
    if score == 100:
        st.success("🎉 완벽합니다! 모든 필수 조건과 키워드가 충족되었습니다.")
    else:
        st.warning("⚠️ 보완이 필요한 부분이 있습니다.")
        st.write("**[감점 요인 및 피드백]**")
        for fb in feedback:
            st.write(f"- {fb}")