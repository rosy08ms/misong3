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
            <b>[자료]</b>[cite: 3]<br>
            기자: 심리학 용어인 '사회적 촉진'과 '사회적 억제'를 일상생활, 특히 우리의 학습에 어떻게 적용할 수 있을까요?<br>
            전문가: 쉬운 과제는 커피숍이나 도서관, 또는 모임을 만들어 함께 하는 것이 좋고, 어렵고 도전이 필요한 과제는 충분히 연습하며 익숙해질 때까지 혼자 집중하는 것이 좋습니다.[cite: 3]
            </div>
            """, unsafe_allow_html=True)
            
            st.write("윗글을 요약한 표의 빈칸 (1), (2), (3)에 들어갈 내용을 각각 입력하시오.[cite: 3]")
            
            st.markdown("""
            <div class="gray-box">
            <b>[채점 조건]</b>[cite: 3]<br>
            📌 지문에 제시된 내용 및 키워드와 정확히 부합해야 함<br>
            📌 지문에 없는 외부 배경지식 활용 시 오답 처리됨
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 (1)] 쉬운 과제 특성**<br>비교적 쉽고 노력이 안 드는 과제:", unsafe_allow_html=True)
            with col2:
                ans_1 = st.text_input("ans1", placeholder="(1) 답안 입력", label_visibility="collapsed")

            st.write("")

            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 (2)] 어려운 과제 환경**<br>지나치게 어렵거나 도전이 필요한 과제 환경:", unsafe_allow_html=True)
            with col2:
                ans_2 = st.text_input("ans2", placeholder="(2) 답안 입력", label_visibility="collapsed")

            st.write("")

            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 (3)] 심리 현상**<br>어려운 과제와 관련된 심리 현상:", unsafe_allow_html=True)
            with col2:
                ans_3 = st.text_input("ans3", placeholder="(3) 답안 입력", label_visibility="collapsed")
            
        elif "서논술형 2" in question_choice:
            st.markdown("""
            <div class="blue-box">
            <b>[자료]</b>[cite: 3]<br>
            기자: 심리학 용어인 '사회적 촉진'과 '사회적 억제'를 일상생활, 특히 우리의 학습에 어떻게 적용할 수 있을까요?<br>
            전문가: 쉬운 과제는 커피숍이나 도서관, 또는 모임을 만들어 함께 하는 것이 좋고, 어렵고 도전이 필요한 과제는 충분히 연습하며 익숙해질 때까지 혼자 집중하는 것이 좋습니다.[cite: 3]
            </div>
            """, unsafe_allow_html=True)
            st.write("주어진 첫 문장에 이어지는 설명문을 조건에 맞추어 작성하시오.[cite: 3]")
            st.markdown("""
            <div class="gray-box">
            <b>[제시문]</b> 과제의 특성과 난이도에 따라 우리의 학습 효율을 높이는 방법은 다르게 적용되어야 한다.[cite: 3]<br><br>
            <b>[채점 조건]</b>[cite: 3]<br>
            🚨 서로 다른 2가지의 설명 방법을 사용하여, (1), (2)에 각각 하나씩 작성할 것<br>
            📌 윗글에 제시된 내용만을 활용하여 문장을 구성할 것<br>
            🚨 각 문장의 끝에 자신이 사용한 설명 방법의 명칭을 괄호에 넣어 표기할 것
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 (1)]** 첫 문장에 이어지는 첫 번째 설명 문장", unsafe_allow_html=True)
            with col2:
                sub_ans_1 = st.text_area("sub1", placeholder="(1) 문장 입력", label_visibility="collapsed")

            st.write("")
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 (2)]** 이어지는 두 번째 설명 문장", unsafe_allow_html=True)
            with col2:
                sub_ans_2 = st.text_area("sub2", placeholder="(2) 문장 입력", label_visibility="collapsed")
                
        else:
            st.markdown("""
            <div class="blue-box">
            <b>[자료]</b>[cite: 3]<br>
            [영상 기획안 주제: 사회적 촉진과 억제를 활용한 스마트한 공부법][cite: 3]
            </div>
            """, unsafe_allow_html=True)
            st.write("장면 2(어려운 과제를 할 때)의 시각/청각 연출 계획과 효과를 작성하시오.[cite: 3]")
            st.markdown("""
            <div class="gray-box">
            <b>[채점 조건]</b>[cite: 3]<br>
            📌 윗글을 참고하여 어려운 과제 때 필요한 환경 특성이 드러나도록 Ⓐ와 Ⓑ에 연출 계획을 세울 것<br>
            🚨 설정한 시각/청각 요소가 글의 내용을 전달하는 데 어떤 효과가 있는지 각각 서술할 것
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 1] 시각 요소(Ⓐ)**<br>어려운 과제 시각 연출 및 효과:", unsafe_allow_html=True)
            with col2:
                sub_ans_1 = st.text_area("sub1", placeholder="(1) 답안 입력", label_visibility="collapsed")

            st.write("")
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 2] 청각 요소(Ⓑ)**<br>어려운 과제 청각 연출 및 효과:", unsafe_allow_html=True)
            with col2:
                sub_ans_2 = st.text_area("sub2", placeholder="(2) 답안 입력", label_visibility="collapsed")

    elif "2세트" in set_choice:
        if "서논술형 1" in question_choice:
            st.markdown("""
            <div class="blue-box">
            <b>[자료]</b><br>
            기자: 겨울철 불청객인 '정전기'란 정확히 무엇인지 설명 부탁드립니다.<br>
            전문가: 정전기란 전하가 정지 상태로 있어 그 분포가 시간적으로 변화하지 않는 전기, 그리고 그로 인한 전기 현상을 말합니다... (중략) ...정전기의 전압은 매우 높지만, 우리가 실생활에서 쓰는 전기와는 다르게 전하가 이동하지 않고 머물러 있어 위험하지는 않습니다.
            </div>
            """, unsafe_allow_html=True)
            st.write("정전기에 대한 요약 표의 빈칸 (1), (2), (3)에 알맞은 내용을 각각 입력하시오.")
            st.markdown("""
            <div class="gray-box">
            <b>[채점 조건]</b><br>
            📌 물의 상태, 전하의 상태, 위험성 여부가 지문 내용과 정확히 대응되어야 함
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 (1)] 물의 상태에 비유**<br>정전기의 비유적 표현:", unsafe_allow_html=True)
            with col2:
                ans_1 = st.text_input("ans1", placeholder="(1) 답안 입력", label_visibility="collapsed")

            st.write("")
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 (2)] 전하의 상태**<br>정전기의 전하 상태:", unsafe_allow_html=True)
            with col2:
                ans_2 = st.text_input("ans2", placeholder="(2) 답안 입력", label_visibility="collapsed")

            st.write("")
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 (3)] 위험성**<br>정전기의 위험성 여부:", unsafe_allow_html=True)
            with col2:
                ans_3 = st.text_input("ans3", placeholder="(3) 답안 입력", label_visibility="collapsed")
                
        elif "서논술형 2" in question_choice:
            st.markdown("""
            <div class="blue-box">
            <b>[자료]</b><br>
            기자: 겨울철 불청객인 '정전기'란 정확히 무엇인지 설명 부탁드립니다... (중략) ...정전기의 전압은 매우 높지만, 우리가 실생활에서 쓰는 전기와는 다르게 전하가 이동하지 않고 머물러 있어 위험하지는 않습니다.
            </div>
            """, unsafe_allow_html=True)
            st.write("주어진 첫 문장에 이어지는 설명문을 조건에 맞추어 작성하시오.")
            st.markdown("""
            <div class="gray-box">
            <b>[제시문]</b> 겨울철에 흔히 겪는 정전기는 우리가 평소 집에서 사용하는 전기와는 다른 뚜렷한 특징이 있다.<br><br>
            <b>[채점 조건]</b><br>
            🚨 (1), (2)에 서로 다른 설명 방법을 1가지 이상 활용하고 명칭을 괄호에 기재할 것<br>
            📌 윗글에 제시된 내용만을 활용하여 문장을 구성할 것<br>
            🚨 (1)과 (2)가 논리적 흐름을 갖고 이어지도록 할 것
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 (1)]** 첫 문장에 이어지는 첫 번째 설명 문장", unsafe_allow_html=True)
            with col2:
                sub_ans_1 = st.text_area("sub1", placeholder="(1) 문장 입력", label_visibility="collapsed")

            st.write("")
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 (2)]** 이어지는 두 번째 설명 문장", unsafe_allow_html=True)
            with col2:
                sub_ans_2 = st.text_area("sub2", placeholder="(2) 문장 입력", label_visibility="collapsed")
        else:
            st.markdown("""
            <div class="blue-box">
            <b>[자료]</b><br>
            [영상 기획안 주제: 전압은 높지만 위험하지 않은 정전기의 비밀]
            </div>
            """, unsafe_allow_html=True)
            st.write("장면 2(정전기)의 시각/청각 연출 계획과 효과를 작성하시오.")
            st.markdown("""
            <div class="gray-box">
            <b>[채점 조건]</b><br>
            📌 정전기의 특성이 잘 드러나도록 Ⓐ와 Ⓑ에 연출 계획을 세울 것<br>
            🚨 연출 효과 서술 시 반드시 윗글의 내용을 근거로 포함할 것
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 1] 시각 요소(Ⓐ)**<br>정전기 시각 연출 및 효과:", unsafe_allow_html=True)
            with col2:
                sub_ans_1 = st.text_area("sub1", placeholder="(1) 답안 입력", label_visibility="collapsed")

            st.write("")
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 2] 청각 요소(Ⓑ)**<br>정전기 청각 연출 및 효과:", unsafe_allow_html=True)
            with col2:
                sub_ans_2 = st.text_area("sub2", placeholder="(2) 답안 입력", label_visibility="collapsed")

    else:
        if "서논술형 1" in question_choice:
            st.markdown("""
            <div class="blue-box">
            <b>[자료]</b><br>
            기자: 최근 생성형 인공 지능이 그린 그림이 미술계에서 큰 화제를 모으고 있습니다... (중략) ...비록 인간과 같은 감정은 없더라도, 기존 미술계에 큰 변화를 가져왔다는 점에서 분명한 의미가 있습니다. 또한 앞으로 우리가 알고 있던 예술의 범주를 확장할 수 있다는 점에서 상징적인 가치를 지닙니다.
            </div>
            """, unsafe_allow_html=True)
            st.write("인공 지능 예술에 대한 요약 표의 빈칸 (1), (2), (3)에 알맞은 내용을 각각 입력하시오.")
            st.markdown("""
            <div class="gray-box">
            <b>[채점 조건]</b><br>
            📌 올림픽 비유, 예술 판단 근거, 예술적 가치가 명확히 드러나야 함
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 (1)] 올림픽 경기에 비유**<br>인공 지능 예술의 비유 대상:", unsafe_allow_html=True)
            with col2:
                ans_1 = st.text_input("ans1", placeholder="(1) 답안 입력", label_visibility="collapsed")

            st.write("")
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 (2)] 예술로 볼 수 있는가**<br>인공 지능 예술에 대한 판단 및 근거:", unsafe_allow_html=True)
            with col2:
                ans_2 = st.text_input("ans2", placeholder="(2) 답안 입력", label_visibility="collapsed")

            st.write("")
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 (3)] 예술로서의 가치**<br>인공 지능 예술의 의의 및 가치:", unsafe_allow_html=True)
            with col2:
                ans_3 = st.text_input("ans3", placeholder="(3) 답안 입력", label_visibility="collapsed")
                
        elif "서논술형 2" in question_choice:
            st.markdown("""
            <div class="blue-box">
            <b>[자료]</b><br>
            기자: 최근 생성형 인공 지능이 그린 그림이 미술계에서 큰 화제를 모으고 있습니다... (중략) ...비록 인간과 같은 감정은 없더라도, 기존 미술계에 큰 변화를 가져왔다는 점에서 분명한 의미가 있습니다.
            </div>
            """, unsafe_allow_html=True)
            st.write("주어진 첫 문장에 이어지는 설명문을 조건에 맞추어 작성하시오.")
            st.markdown("""
            <div class="gray-box">
            <b>[제시문]</b> 인공 지능이 그린 그림이 늘어나는 요즘, 우리는 이 작품들을 어떤 눈으로 바라봐야 할지 올바르게 생각해야 한다.<br><br>
            <b>[채점 조건]</b><br>
            🚨 (1), (2)에 서로 다른 설명 방법을 1가지 이상 활용하고 명칭을 괄호에 기재할 것<br>
            📌 윗글에 제시된 내용만을 활용하여 문장을 구성할 것<br>
            🚨 (1)과 (2)가 논리적 흐름을 갖고 이어지도록 할 것
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 (1)]** 첫 문장에 이어지는 첫 번째 설명 문장", unsafe_allow_html=True)
            with col2:
                sub_ans_1 = st.text_area("sub1", placeholder="(1) 문장 입력", label_visibility="collapsed")

            st.write("")
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 (2)]** 이어지는 두 번째 설명 문장", unsafe_allow_html=True)
            with col2:
                sub_ans_2 = st.text_area("sub2", placeholder="(2) 문장 입력", label_visibility="collapsed")
        else:
            st.markdown("""
            <div class="blue-box">
            <b>[자료]</b><br>
            [영상 기획안 주제: 인간의 감정이 담긴 진정한 예술의 가치]
            </div>
            """, unsafe_allow_html=True)
            st.write("장면 2(마음에 울림을 주는 진정한 예술)의 시각/청각 연출 계획과 효과를 작성하시오.")
            st.markdown("""
            <div class="gray-box">
            <b>[채점 조건]</b><br>
            📌 인간이 만들어내는 예술의 특성이 잘 드러나도록 Ⓐ와 Ⓑ에 연출 계획을 세울 것<br>
            🚨 설정한 시각 및 청각 요소의 연출 효과를 각각 서술하되, 반드시 윗글의 내용을 근거로 포함할 것
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 1] 시각 요소(Ⓐ)**<br>진정한 예술 시각 연출 및 효과:", unsafe_allow_html=True)
            with col2:
                sub_ans_1 = st.text_area("sub1", placeholder="(1) 답안 입력", label_visibility="collapsed")

            st.write("")
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**[문제 2] 청각 요소(Ⓑ)**<br>진정한 예술 청각 연출 및 효과:", unsafe_allow_html=True)
            with col2:
                sub_ans_2 = st.text_area("sub2", placeholder="(2) 답안 입력", label_visibility="collapsed")

    if "서논술형 1" in question_choice:
        student_answer = {"ans_1": ans_1, "ans_2": ans_2, "ans_3": ans_3}
    else:
        student_answer = {"sub_1": sub_ans_1, "sub_2": sub_ans_2}

    def grade_answer(set_idx, q_idx, ans_dict):
        score = 100
        feedback = []
        
        def check_text(text, keywords):
            if not text.strip():
                return 50
            if not any(k in text for k in keywords):
                feedback.append("필수 키워드나 핵심 내용이 누락되었습니다.")
                return 40
            return 0

        if set_idx == 0:
            if q_idx == 0:
                score -= check_text(ans_dict["ans_1"], ["쉽", "취미", "노력"])
                score -= check_text(ans_dict["ans_2"], ["혼자", "집중", "충분"])
                score -= check_text(ans_dict["ans_3"], ["사회적 억제"])
            else:
                score -= check_text(ans_dict["sub_1"], ["과제", "효율"])
                score -= check_text(ans_dict["sub_2"], ["과제", "효율"])
        elif set_idx == 1:
            if q_idx == 0:
                score -= check_text(ans_dict["ans_1"], ["고여", "물"])
                score -= check_text(ans_dict["ans_2"], ["정지", "이동하지", "머물"])
                score -= check_text(ans_dict["ans_3"], ["위험하지 않", "피해"])
            else:
                score -= check_text(ans_dict["sub_1"], ["정전기"])
                score -= check_text(ans_dict["sub_2"], ["정전기"])
        else:
            if q_idx == 0:
                score -= check_text(ans_dict["ans_1"], ["로봇", "피겨", "스케이팅"])
                score -= check_text(ans_dict["ans_2"], ["예술로 보", "어렵", "감정"])
                score -= check_text(ans_dict["ans_3"], ["범주", "확장", "변화"])
            else:
                score -= check_text(ans_dict["sub_1"], ["예술", "감정"])
                score -= check_text(ans_dict["sub_2"], ["예술", "감정"])

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
            st.success("🎉 완벽합니다! 모든 필수 조건이 충족되었습니다.")
        else:
            st.warning("⚠️ 보완이 필요한 부분이 있습니다.")
            for fb in feedback:
                st.write(f"- {fb}")

with tab2:
    st.subheader("📌 오답 문항 맞춤형 복습 가이드")
    
    if 'last_score' not in st.session_state:
        st.info("아직 채점된 문항이 없습니다. [문제 풀이 및 채점] 탭에서 문제를 풀고 채점을 진행해 주세요.")
    elif st.session_state['last_score'] == 100:
        st.success("✨ 만점을 받았습니다! 복습할 내용이 없습니다.")
    else:
        st.write("제시된 지문의 핵심 개념과 조건들을 다시 확인해 보세요.")
