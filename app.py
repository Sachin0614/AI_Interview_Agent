import streamlit as st
from streamlit_mic_recorder import mic_recorder

from modules.pdf_processor import extract_text_from_pdf
from modules.llm_engine import GroqInterviewEngine
from modules.voice_engine import VoiceEngine
from modules.ui_styles import ANIMATED_CSS, get_wave_html

st.set_page_config(
    page_title="AI Interview Agent Pro",
    page_icon="🎙️",
    layout="wide"
)

st.markdown(ANIMATED_CSS, unsafe_allow_html=True)

if "llm" not in st.session_state:
    with st.spinner("Starting Groq AI Interview Engine..."):
        st.session_state.llm = GroqInterviewEngine()
        st.session_state.voice = VoiceEngine()

default_states = {
    "chat_history": [],
    "pdf_context": "",
    "interview_started": False,
    "interview_paused": False,
    "interview_finished": False,
    "score": 0,
    "question_count": 0,
    "last_audio_id": None,
    "last_audio_bytes": None,
    "is_processing": False,
    "report_text": ""
}

for key, value in default_states.items():
    if key not in st.session_state:
        st.session_state[key] = value


def generate_report(role, level, interview_type):
    history_text = ""

    for i, chat in enumerate(st.session_state.chat_history, start=1):
        history_text += f"""
Question/Response {i}
Candidate: {chat['user']}
Interviewer: {chat['assistant']}
"""

    report_prompt = f"""
Generate a professional interview report.

Role: {role}
Difficulty: {level}
Interview Type: {interview_type}
Total Questions Answered: {st.session_state.question_count}

Conversation:
{history_text}

Report format:
1. Candidate Summary
2. Overall Score out of 100
3. Strengths
4. Weaknesses
5. Communication Skills
6. Technical Skills
7. Project Knowledge
8. Final Recommendation: Selected / Rejected / Borderline
9. Improvement Suggestions

Keep it clean and professional.
"""

    report = st.session_state.llm.generate_response(
        system_instruction="You are an expert HR interview evaluator.",
        user_input=report_prompt,
        history=[]
    )

    st.session_state.report_text = report
    st.session_state.interview_finished = True
    return report


st.markdown("""
<div class="hero-card">
    <div class="neon-badge">LIVE AI INTERVIEW SIMULATOR</div>
    <h1>AI Interview Agent Pro</h1>
    <p>3D Voice Interviewer • Resume Based Questions • Groq Powered Brain • Smart Feedback • Real Interview Flow</p>
</div>
""", unsafe_allow_html=True)


with st.sidebar:
    st.markdown("## ⚙️ Interview Setup")

    role = st.text_input("Target Role", "AI/ML Intern")
    level = st.selectbox("Difficulty Level", ["Beginner", "Intermediate", "Advanced"])
    interview_type = st.selectbox(
        "Interview Type",
        ["HR + Technical", "Only HR", "Only Technical", "Project Based"]
    )
    voice_enabled = st.toggle("Voice Output", value=True)

    uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

    if uploaded_file:
        with st.spinner("Reading resume..."):
            st.session_state.pdf_context = extract_text_from_pdf(uploaded_file)
        st.success("Resume uploaded successfully!")

    st.markdown("---")

    if st.button("📄 Generate Report Now", use_container_width=True):
        if len(st.session_state.chat_history) > 0:
            with st.spinner("Generating interview report..."):
                generate_report(role, level, interview_type)
            st.rerun()
        else:
            st.warning("Interview start karo pehle.")

    if st.button("🔄 Reset Interview", use_container_width=True):
        st.session_state.chat_history = []
        st.session_state.pdf_context = ""
        st.session_state.interview_started = False
        st.session_state.interview_paused = False
        st.session_state.interview_finished = False
        st.session_state.score = 0
        st.session_state.question_count = 0
        st.session_state.last_audio_id = None
        st.session_state.last_audio_bytes = None
        st.session_state.is_processing = False
        st.session_state.report_text = ""
        st.rerun()


resume_context = st.session_state.pdf_context[:2500]

system_instruction = f"""
You are an expert AI Interviewer.

Candidate is applying for: {role}
Difficulty level: {level}
Interview type: {interview_type}

Rules:
1. Ask only ONE question at a time.
2. Keep question short and professional.
3. First give short feedback on previous answer.
4. Then ask the next question.
5. Ask resume/project based questions if resume context is available.
6. Do not give long lectures.
7. After every answer, rate the answer out of 10 in one line.
8. Help the candidate improve like a real interviewer.
9. Never continue the interview automatically.
10. Always wait for the candidate's next answer.
11. Do not ask more than one question in one response.

Resume Context:
{resume_context}
"""


left, right = st.columns([1.2, 2])


with left:
    st.markdown("""
    <div class="avatar-container">
        <div class="avatar-ring"></div>
        <div class="avatar-ring two"></div>
        <div class="avatar-ring three"></div>
        <div class="voice-avatar-3d">AI</div>
    </div>
    """, unsafe_allow_html=True)

    m1, m2, m3 = st.columns(3)

    with m1:
        st.markdown(f"""
        <div class="status-card">
            <h3>QUESTIONS</h3>
            <p>{st.session_state.question_count}</p>
        </div>
        """, unsafe_allow_html=True)

    with m2:
        st.markdown(f"""
        <div class="status-card">
            <h3>SCORE</h3>
            <p>{st.session_state.score}</p>
        </div>
        """, unsafe_allow_html=True)

    with m3:
        st.markdown(f"""
        <div class="status-card">
            <h3>LEVEL</h3>
            <p>{level}</p>
        </div>
        """, unsafe_allow_html=True)

    if not st.session_state.interview_started:
        if st.button("🚀 Start Interview", use_container_width=True):
            st.session_state.interview_started = True
            st.session_state.interview_paused = False
            st.session_state.interview_finished = False

            first_prompt = "Greet the candidate and ask the first interview question only."
            reply = st.session_state.llm.generate_response(
                system_instruction=system_instruction,
                user_input=first_prompt,
                history=[]
            )

            st.session_state.chat_history.append({
                "user": "Start interview",
                "assistant": reply
            })

            if voice_enabled:
                st.session_state.voice.text_to_speech(reply)

            st.rerun()


with right:
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    st.markdown("### 💬 Interview Console")

    if st.session_state.interview_started and not st.session_state.interview_finished:

        if st.session_state.interview_paused:
            st.warning("You have completed 5 questions. Do you want to continue the interview?")

            c1, c2 = st.columns(2)

            with c1:
                if st.button("✅ Continue Interview", use_container_width=True):
                    st.session_state.interview_paused = False

                    continue_prompt = "Candidate wants to continue. Ask the next interview question only."
                    reply = st.session_state.llm.generate_response(
                        system_instruction=system_instruction,
                        user_input=continue_prompt,
                        history=st.session_state.chat_history[-10:]
                    )

                    st.session_state.chat_history.append({
                        "user": "Continue interview",
                        "assistant": reply
                    })

                    if voice_enabled:
                        st.session_state.voice.text_to_speech(reply)

                    st.rerun()

            with c2:
                if st.button("🛑 Stop & Generate Report", use_container_width=True):
                    with st.spinner("Generating final report..."):
                        generate_report(role, level, interview_type)
                    st.rerun()

        else:
            audio_col, text_col = st.columns([1, 3])

            user_input = ""

            with audio_col:
                audio_data = mic_recorder(
                    start_prompt="🎙️ Speak",
                    stop_prompt="🛑 Stop",
                    key="voice_input"
                )

            with text_col:
                typed_text = st.chat_input("Type your answer here...")

            if not st.session_state.is_processing:

                if typed_text:
                    user_input = typed_text.strip()

                elif audio_data and "bytes" in audio_data:
                    current_audio_bytes = audio_data["bytes"]
                    current_audio_id = str(hash(current_audio_bytes))

                    if current_audio_id != st.session_state.last_audio_id:
                        st.session_state.last_audio_id = current_audio_id
                        st.session_state.last_audio_bytes = current_audio_bytes

                        st.markdown(get_wave_html(), unsafe_allow_html=True)

                        with st.spinner("Converting voice to text..."):
                            user_input = st.session_state.voice.speech_to_text(current_audio_bytes)

            if user_input and user_input.strip() != "":
                st.session_state.is_processing = True

                with st.spinner("AI Interviewer is thinking..."):
                    reply = st.session_state.llm.generate_response(
                        system_instruction=system_instruction,
                        user_input=user_input,
                        history=st.session_state.chat_history[-10:]
                    )

                st.session_state.chat_history.append({
                    "user": user_input,
                    "assistant": reply
                })

                st.session_state.question_count += 1
                st.session_state.score += 1

                if st.session_state.question_count > 0 and st.session_state.question_count % 5 == 0:
                    st.session_state.interview_paused = True

                if voice_enabled:
                    st.session_state.voice.text_to_speech(reply)

                st.session_state.is_processing = False
                st.rerun()

    elif st.session_state.interview_finished:
        st.success("Interview completed. Report generated below.")

    else:
        st.info("Upload resume, select settings, then click Start Interview.")

    st.markdown("</div>", unsafe_allow_html=True)


if st.session_state.report_text:
    st.markdown("## 📄 Interview Report")

    st.markdown(
        f"""
        <div class="glass-panel">
            {st.session_state.report_text.replace(chr(10), "<br>")}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.download_button(
        label="⬇️ Download Report",
        data=st.session_state.report_text,
        file_name="interview_report.txt",
        mime="text/plain",
        use_container_width=True
    )


st.markdown("## 🧾 Conversation History")

for chat in reversed(st.session_state.chat_history):
    st.markdown(
        f"""
        <div class="chat-bubble-user">
            <b>You:</b><br>{chat["user"]}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="chat-bubble-ai">
            <b>AI Interviewer:</b><br>{chat["assistant"]}
        </div>
        """,
        unsafe_allow_html=True
    )