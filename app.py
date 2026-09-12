import streamlit as st

st.set_page_config(page_title="서논술형 자동 채점 시스템", layout="centered")

st.markdown("""
    <style>
    .blue-box {
        background-color: #e8f4fd;
        border-left: 5px solid #2196F3;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 15px;
    }
    .gray-box {
        background-color: #f1f3f5;
        border-left: 5px solid #adb5bd;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 15px;
    }
    .review-box {
        background-color: #fff3cd;
        border-left: 5px solid #ffc107;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("효율적인 표현법 서논술형 자동 채점기")
st.write("학생의 답안을 입력하면 채점 기준에 따라 자동 채점 및 피드백을 제공합니다.")

tab1, tab2 = st.tabs(["📝 문제 풀이 및 채점", "📌 복습할 내용"])

with tab1:
    set_choice = st.selectbox("학습 세트 선택", ["1세트: 효율적인 표현법 (사회적 촉진/억제)", "2세트: 정전기의 특징", "3세트: 인공 지능 예술"], key="set_select")
    question_choice = st.selectbox("문항 선택", ["서논술형 1 (요약 표)", "서논술형 2 (설명문 작성)", "서논술형 3 (영상 기획안)"], key="q_select")

    st.divider()

    ans_1, ans_2, ans_3 = "", "", ""
    sub_ans_1, sub_ans_2 = "", ""

    if "1세트" in set_choice:
        if "서논술형 1" in question_choice:
            st.markdown("""
            <div class="blue-box">
            <b>[자료]</b><br>
            기자: 심리학 용어인 '사회적 촉진'과 '사회적 억제'를 일상생활, 특히 우리의 학습에 어떻게 적용할 수 있을까요?<br>
            전문가: 쉬운 과제는 커피숍이나 도서관, 또는 모임을 만들어 함께 하는 것이 좋고, 어렵고 도전이 필요한 과제는 충분히 연습하며 익숙해질 때까지 혼자 집중하는 것이 좋습니다.
            </div>
            """, unsafe_allow_html=True)
            
            st.write("윗글을 요약하여 정리한 아래 항목별 빈칸에 들어갈 내용을 바로 입력하시오.")
            
            st.markdown("""
            <div class="gray-box">
            <b>[채점 조건]</b><br>
            📌 (1), (2), (3) 각 칸의 핵심 내용과 키워드가 정확히 부합해야 함<br>
            📌 지문에 없는 외부 배경지식 활용 시 오답 처리됨
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 1] 쉬운 과제**<br>과제 특성 및 효율적 방식:", unsafe_allow_html=True)
            with col2:
                ans_1 = st.text_input("ans1", placeholder="(1) 답안 입력", label_visibility="collapsed")

            st.write("")

            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 2] 추천 장소**<br>쉬운 과제 추천 장소/환경:", unsafe_allow_html=True)
            with col2:
                ans_2 = st.text_input("ans2", placeholder="(2) 답안 입력", label_visibility="collapsed")

            st.write("")

            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 3] 어려운 과제**<br>과제 특성 및 집중 방식:", unsafe_allow_html=True)
            with col2:
                ans_3 = st.text_input("ans3", placeholder="(3) 답안 입력", label_visibility="collapsed")
            
        elif "서논술형 2" in question_choice:
            st.markdown("""
            <div class="blue-box">
            <b>[자료]</b><br>
            과제의 특성과 난이도에 따라 우리의 학습 효율을 높이는 방법은 다르게 적용되어야 한다. (이하 생략)
            </div>
            """, unsafe_allow_html=True)
            st.write("윗글을 활용하여 과제 난이도에 따른 효율적인 학습 전략에 대한 설명문을 작성하려 한다. 각 문항별로 조건에 맞는 내용을 바로 작성하시오.")
            st.markdown("""
            <div class="gray-box">
            <b>[채점 조건]</b><br>
            🚨 서로 다른 2가지의 설명 방법을 사용하여, (1), (2)에 각각 하나씩 작성할 것<br>
            📌 윗글에 제시된 내용만을 활용하여 문장을 구성할 것<br>
            🚨 각 문장의 끝에 자신이 사용한 설명 방법의 명칭을 괄호에 넣어 표기할 것<br>
            🔍 개념 설명만 있고 요구한 결론이 누락된 경우 오답 처리함
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 1]** 쉬운 과제와 사회적 촉진 설명 문장", unsafe_allow_html=True)
            with col2:
                sub_ans_1 = st.text_area("sub1", placeholder="(1) 문장 입력", label_visibility="collapsed")

            st.write("")
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 2]** 어려운 과제와 사회적 억제 설명 문장", unsafe_allow_html=True)
            with col2:
                sub_ans_2 = st.text_area("sub2", placeholder="(2) 문장 입력", label_visibility="collapsed")
                
        else:
            st.markdown("""
            <div class="blue-box">
            <b>[자료]</b><br>
            [영상 기획안 주제: 사회적 촉진과 억제를 활용한 스마트한 공부법]
            </div>
            """, unsafe_allow_html=True)
            st.write("윗글을 바탕으로 상황에 맞는 학습 공간 선택법을 설명하는 영상을 제작하려 한다. 각 문항별 연출 계획과 효과를 바로 서술하시오.")
            st.markdown("""
            <div class="gray-box">
            <b>[채점 조건]</b><br>
            📌 윗글을 참고하여 어려운 과제 때 필요한 환경 특성이 드러나도록 연출 계획을 세울 것<br>
            🚨 설정한 시각/청각 요소가 글의 내용을 전달하는 데 어떤 효과가 있는지 각각 서술할 것<br>
            🔍 요소 A(연출)와 요소 B(효과)가 실질적으로 연결되지 않으면 오답 처리함
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 1]** 시각 요소(요소 A) 및 연출/효과(요소 B)", unsafe_allow_html=True)
            with col2:
                sub_ans_1 = st.text_area("sub1", placeholder="(1) 답안 입력", label_visibility="collapsed")

            st.write("")
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 2]** 청각 요소(요소 A) 및 연출/효과(요소 B)", unsafe_allow_html=True)
            with col2:
                sub_ans_2 = st.text_area("sub2", placeholder="(2) 답안 입력", label_visibility="collapsed")

    elif "2세트" in set_choice:
        if "서논술형 1" in question_choice:
            st.markdown("""
            <div class="blue-box">
            <b>[자료]</b><br>
            실생활 전기는 '흐르는 물'이라면 정전기는 '높은 곳에 고여 있는 물'이다. 전하가 이동하지 않고 머물러 있어 위험하지 않다.
            </div>
            """, unsafe_allow_html=True)
            st.write("윗글을 요약하여 정리한 아래 항목별 빈칸에 알맞은 내용을 바로 입력하시오.")
            st.markdown("""
            <div class="gray-box">
            <b>[채점 조건]</b><br>
            📌 물의 상태, 전하의 상태, 위험성 여부가 정확히 대응되어야 함
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 1] 비유적 표현**<br>정전기의 비유적 표현:", unsafe_allow_html=True)
            with col2:
                ans_1 = st.text_input("ans1", placeholder="(1) 답안 입력", label_visibility="collapsed")

            st.write("")
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 2] 전하의 상태**<br>정전기 전하의 상태:", unsafe_allow_html=True)
            with col2:
                ans_2 = st.text_input("ans2", placeholder="(2) 답안 입력", label_visibility="collapsed")

            st.write("")
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 3] 위험성**<br>정전기의 위험성 여부:", unsafe_allow_html=True)
            with col2:
                ans_3 = st.text_input("ans3", placeholder="(3) 답안 입력", label_visibility="collapsed")
                
        elif "서논술형 2" in question_choice:
            st.markdown("""
            <div class="blue-box">
            <b>[자료]</b><br>
            겨울철에 흔히 겪는 정전기는 우리가 평소 집에서 사용하는 전기와는 다른 뚜렷한 특징이 있다.
            </div>
            """, unsafe_allow_html=True)
            st.write("윗글을 활용하여 정전기의 특징에 대한 설명문을 작성하려 한다. 각 문항별로 조건에 맞게 작성하시오.")
            st.markdown("""
            <div class="gray-box">
            <b>[채점 조건]</b><br>
            🚨 (1), (2)에 서로 다른 설명 방법을 1가지 이상 활용하고 명칭을 괄호에 기재할 것<br>
            📌 (1)과 (2)가 논리적 흐름을 갖고 이어지도록 할 것<br>
            🔍 개념 설명만 있고 결론이 누락된 경우 오답 처리함
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 1]** 정전기의 개념 및 비유 설명 문장", unsafe_allow_html=True)
            with col2:
                sub_ans_1 = st.text_area("sub1", placeholder="(1) 문장 입력", label_visibility="collapsed")

            st.write("")
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 2]** 정전기의 안전성 관련 결론 문장", unsafe_allow_html=True)
            with col2:
                sub_ans_2 = st.text_area("sub2", placeholder="(2) 문장 입력", label_visibility="collapsed")
        else:
            st.markdown("""
            <div class="blue-box">
            <b>[자료]</b><br>
            [영상 기획안 주제: 전압은 높지만 위험하지 않은 정전기의 비밀]
            </div>
            """, unsafe_allow_html=True)
            st.write("윗글을 바탕으로 정전기의 특징을 설명하는 영상을 제작하려 한다. 각 문항별 연출 계획과 효과를 바로 서술하시오.")
            st.markdown("""
            <div class="gray-box">
            <b>[채점 조건]</b><br>
            📌 정전기의 특성이 잘 드러나도록 연출 계획을 세울 것<br>
            🚨 연출 효과 서술 시 반드시 윗글의 내용을 근거로 포함할 것<br>
            🔍 요소 A와 요소 B가 실질적으로 연결되지 않으면 오답 처리함
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 1]** 시각 요소(요소 A) 및 연출/효과(요소 B)", unsafe_allow_html=True)
            with col2:
                sub_ans_1 = st.text_area("sub1", placeholder="(1) 답안 입력", label_visibility="collapsed")

            st.write("")
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 2]** 청각 요소(요소 A) 및 연출/효과(요소 B)", unsafe_allow_html=True)
            with col2:
                sub_ans_2 = st.text_area("sub2", placeholder="(2) 답안 입력", label_visibility="collapsed")

    else:
        if "서논술형 1" in question_choice:
            st.markdown("""
            <div class="blue-box">
            <b>[자료]</b><br>
            「에드몽 드 벨라미」는 14~20세기 초상화 1만 5,000점을 토대로 알고리즘과 데이터를 사용해 그려졌다. 예술적 가치와 범주 확장에 기여함.
            </div>
            """, unsafe_allow_html=True)
            st.write("윗글을 요약하여 정리한 아래 항목별 빈칸에 알맞은 내용을 바로 입력하시오.")
            st.markdown("""
            <div class="gray-box">
            <b>[채점 조건]</b><br>
            📌 제작 방식, 예술성 판단 근거, 가치가 명확히 드러나야 함
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 1] 제작 방식**<br>AI 그림의 제작 방식:", unsafe_allow_html=True)
            with col2:
                ans_1 = st.text_input("ans1", placeholder="(1) 답안 입력", label_visibility="collapsed")

            st.write("")
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 2] 예술성 판단**<br>예술성 판단 근거:", unsafe_allow_html=True)
            with col2:
                ans_2 = st.text_input("ans2", placeholder="(2) 답안 입력", label_visibility="collapsed")

            st.write("")
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 3] 의의 및 가치**<br>작품의 의의 및 가치:", unsafe_allow_html=True)
            with col2:
                ans_3 = st.text_input("ans3", placeholder="(3) 답안 입력", label_visibility="collapsed")
                
        elif "서논술형 2" in question_choice:
            st.markdown("""
            <div class="blue-box">
            <b>[자료]</b><br>
            인공 지능이 그린 그림이 늘어나는 요즘, 우리는 이 작품들을 어떤 눈으로 바라봐야 할지 올바르게 생각해야 한다.
            </div>
            """, unsafe_allow_html=True)
            st.write("윗글을 활용하여 인공 지능이 그린 그림을 바라보는 시각에 대한 설명문을 작성하려 한다. 각 문항별로 조건에 맞게 작성하시오.")
            st.markdown("""
            <div class="gray-box">
            <b>[채점 조건]</b><br>
            🚨 서로 다른 설명 방법을 1가지 이상 활용하고 명칭을 괄호에 기재할 것<br>
            📌 인간의 예술과 AI 예술의 차이점 및 가치가 논리적으로 이어질 것<br>
            🔍 결론이 누락된 경우 오답 처리함
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 1]** 인간 예술과 AI 예술의 차이점 설명", unsafe_allow_html=True)
            with col2:
                sub_ans_1 = st.text_area("sub1", placeholder="(1) 문장 입력", label_visibility="collapsed")

            st.write("")
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 2]** AI 예술의 가치와 범주 확장 결론", unsafe_allow_html=True)
            with col2:
                sub_ans_2 = st.text_area("sub2", placeholder="(2) 문장 입력", label_visibility="collapsed")
        else:
            st.markdown("""
            <div class="blue-box">
            <b>[자료]</b><br>
            [영상 기획안 주제: 인간의 감정이 담긴 진정한 예술의 가치]
            </div>
            """, unsafe_allow_html=True)
            st.write("윗글을 바탕으로 인공 지능이 그린 그림을 바라보는 시각을 설명하는 영상을 제작하려 한다. 각 문항별 연출 계획과 효과를 바로 서술하시오.")
            st.markdown("""
            <div class="gray-box">
            <b>[채점 조건]</b><br>
            📌 인공 지능 그림의 제작 방식과 상징적 가치가 드러나도록 연출할 것<br>
            🚨 설정한 시각/청각 요소의 연출 효과를 윗글 근거와 함께 서술할 것<br>
            🔍 요소 A와 요소 B가 실질적으로 연결되지 않으면 오답 처리함
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 1]** 시각 요소(요소 A) 및 연출/효과(요소 B)", unsafe_allow_html=True)
            with col2:
                sub_ans_1 = st.text_area("sub1", placeholder="(1) 답안 입력", label_visibility="collapsed")

            st.write("")
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 2]** 청각 요소(요소 A) 및 연출/효과(요소 B)", unsafe_allow_html=True)
            with col2:
                sub_ans_2 = st.text_area("sub2", placeholder="(2) 답안 입력", label_visibility="collapsed")

    if "서논술형 1" in question_choice:
        student_answer = {"ans_1": ans_1, "ans_2": ans_2, "ans_3": ans_3}
    else:
        student_answer = {"sub_1": sub_ans_1, "sub_2": sub_ans_2}

    def grade_answer(set_idx, q_idx, ans_dict):
        score = 100
        feedback = []
        
        def check_conclusion_and_connection(text_a, text_b, required_keywords_a, required_conclusion):
            penalties = 0
            if not any(k in text_a for k in required_keywords_a):
                feedback.append("요소 A(주장/설정)에 필수 내용이나 핵심 키워드가 누락되었습니다.")
                penalties += 50
            if required_conclusion and not any(c in text_b for c in required_conclusion):
                feedback.append("개념 설명만 존재하고, 조건에서 요구한 결론이 명확히 드러나지 않습니다.")
                penalties += 30
            if not text_a.strip() or not text_b.strip():
                feedback.append("요소 A와 요소 B가 실질적으로 연결되지 않았습니다.")
                penalties += 20
            return max(0, penalties)

        if set_idx == 0:
            if q_idx == 0:
                if not any(k in ans_dict["ans_1"] for k in ["쉬운", "취미", "노력"]):
                    score -= 33; feedback.append("(1) 쉬운 과제 관련 필수 키워드 누락")
                if not any(k in ans_dict["ans_2"] for k in ["커피숍", "도서관", "모임", "함께"]):
                    score -= 33; feedback.append("(2) 함께 공부하는 환경 키워드 누락")
                if not any(k in ans_dict["ans_3"] for k in ["어렵", "혼자", "억제"]):
                    score -= 34; feedback.append("(3) 어려운 과제와 혼자 집중하는 내용 누락")
            elif q_idx == 1:
                score -= check_conclusion_and_connection(ans_dict["sub_1"], ans_dict["sub_2"], ["쉬운", "과제"], ["사회적 촉진", "효율"])
            else:
                score -= check_conclusion_and_connection(ans_dict["sub_1"], ans_dict["sub_2"], ["혼자", "집중", "독서실"], ["사회적 억제", "이해"])
        elif set_idx == 1:
            if q_idx == 0:
                if "고여" not in ans_dict["ans_1"]:
                    score -= 33; feedback.append("(1) '고여 있는 물' 표현 누락")
                if not any(k in ans_dict["ans_2"] for k in ["정지", "머물", "이동하지"]):
                    score -= 33; feedback.append("(2) 전하의 정지 상태 누락")
                if not any(k in ans_dict["ans_3"] for k in ["위험", "피해", "없"]):
                    score -= 34; feedback.append("(3) 위험하지 않다는 결론 누락")
            elif q_idx == 1:
                score -= check_conclusion_and_connection(ans_dict["sub_1"], ans_dict["sub_2"], ["흐르는 물", "고여 있는 물"], ["위험하지 않다", "피해가 없는"])
            else:
                score -= check_conclusion_and_connection(ans_dict["sub_1"], ans_dict["sub_2"], ["고여", "정지"], ["위험하지 않", "안전"])
        else:
            if q_idx == 0:
                if not any(k in ans_dict["ans_1"] for k in ["알고리즘", "데이터", "초상화"]):
                    score -= 33; feedback.append("(1) 데이터/알고리즘 제작 특징 누락")
                if not any(k in ans_dict["ans_2"] for k in ["감정", "철학", "어렵"]):
                    score -= 33; feedback.append("(2) 예술로 보기 어렵다는 판단 누락")
                if not any(k in ans_dict["ans_3"] for k in ["변화", "확장", "상징적"]):
                    score -= 34; feedback.append("(3) 상징적 가치 누락")
            elif q_idx == 1:
                score -= check_conclusion_and_connection(ans_dict["sub_1"], ans_dict["sub_2"], ["노력", "열정", "감정"], ["상징적 가치", "범주 확장"])
            else:
                score -= check_conclusion_and_connection(ans_dict["sub_1"], ans_dict["sub_2"], ["알고리즘", "데이터"], ["상징", "확장", "변화"])

        return max(0, score), list(set(feedback))

    if st.button("🔍 채점 실행하기"):
        s_idx = ["1세트", "2세트", "3세트"].index(set_choice.split(":")[0])
        q_idx = ["서논술형 1", "서논술형 2", "서논술형 3"].index(question_choice.split(" ")[0] + " " + question_choice.split(" ")[1])
        
        score, feedback = grade_answer(s_idx, q_idx, student_answer)
        
        st.session_state['last_score'] = score
        st.session_state['last_feedback'] = feedback
        st.session_state['last_set'] = set_choice
        st.session_state['last_q'] = question_choice
        
        st.subheader("📊 채점 결과")
        st.metric(label="점수", value=f"{score}점 / 100점")
        
        if score == 100:
            st.success("🎉 완벽합니다! 모든 필수 조건과 결론, 요소 간 연계가 충족되었습니다.")
        else:
            st.warning("⚠️ 보완이 필요한 부분이 있습니다.")
            st.write("**[감점 및 오답 안내]**")
            for fb in feedback:
                st.write(f"- {fb}")

with tab2:
    st.subheader("📌 오답 문항 맞춤형 복습 가이드")
    
    if 'last_score' not in st.session_state:
        st.info("아직 채점된 문항이 없습니다. [문제 풀이 및 채점] 탭에서 문제를 풀고 채점을 진행해 주세요.")
    elif st.session_state['last_score'] == 100:
        st.success("✨ 직전에 제출한 문항에서 만점을 받았습니다! 복습할 오답 내용이 없습니다.")
    else:
        review_data = {
            "1세트": {
                "서논술형 1": "쉬운 과제는 여럿이 할 때 효율이 높아지는 '사회적 촉진', 어려운 과제는 혼자 집중해야 하는 '사회적 억제' 개념을 정확히 매칭해야 합니다.",
                "서논술형 2": "과제 난이도에 따른 효율 변화를 서술할 때, 단순 현상 설명에 그치지 않고 학습 효율이 달라지는 '결론'까지 논리적으로 연결해야 합니다.",
                "서논술형 3": "어려운 과제 상황에서 '사회적 억제'가 적용되도록 혼자 집중하는 환경(시각)과 차분한 분위기 조성(청각)이 효과와 실질적으로 연계되어야 합니다."
            },
            "2세트": {
                "서논술형 1": "실생활 전기(흐르는 물)와 정전기(고여 있는 물)의 비유 및 전하의 정지 상태, 그리고 '위험하지 않다'는 결론의 대응 관계를 파악해야 합니다.",
                "서논술형 2": "정전기의 특징을 비유와 인과 관계를 활용해 설명하되, 전압이 높음에도 피해가 없는 이유라는 결론이 문장에 명확히 드러나야 합니다.",
                "서논술형 3": "고여 있는 물이라는 비유적 특성이 시각 요소에 반영되고, 전하가 이동하지 않아 안전하다는 근거가 효과와 연결되어야 합니다."
            },
            "3세트": {
                "서논술형 1": "인공 지능 그림의 제작 방식(알고리즘·데이터), 예술로 보기 어려운 이유(감정·철학 부재), 그리고 상징적 가치(범주 확장)를 구분해 요약해야 합니다.",
                "서논술형 2": "인간 예술(내외부적 요소)과 AI 예술의 차이를 대조하고, 감정이 없더라도 미술계에 주는 변화와 확장이라는 가치 결론을 포함해야 합니다.",
                "서논술형 3": "AI의 데이터 기반 제작 방식과 예술 범주 확장이라는 상징적 가치가 시청각 연출 및 효과 서술에 유기적으로 녹아들어야 합니다."
            }
        }
        
        current_set = st.session_state['last_set'].split(":")[0]
        current_q = st.session_state['last_q']
        current_feedback = st.session_state['last_feedback']
        
        st.markdown(f"""
        <div class="review-box">
        <b>🚨 취약 문항: [{st.session_state['last_set']}] - {current_q}</b><br>
        획득 점수: <b>{st.session_state['last_score']}점</b>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("### 🔍 내 답안의 부족한 부분")
        for fb in current_feedback:
            st.write(f"- {fb}")
            
        st.write("### 💡 핵심 복습 포인트")
        point = review_data.get(current_set, {}).get(current_q, "핵심 개념을 다시 교재와 대조하여 확인해 보세요.")
        st.info(point)

    st.divider()

    col_msg, col_btn = st.columns([4, 1])
    with col_msg:
        st.markdown(
            "<span style='font-size: 13px; color: #555;'>"
            "모든 문제를 제출하면 복습할 내용 탭에서 틀린 개념을 확인할 수 있어요. "
            "답안을 초기화하고 처음부터 다시 풀고 싶다면 다음의 버튼을 누르세요."
            "</span>", 
            unsafe_allow_html=True
        )
    with col_btn:
        if st.button("처음부터 다시 풀기", type="primary"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
