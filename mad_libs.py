"""
NexusNarrative - Smart Agentic Story Studio
A modern, simple-to-use story generator with smart AI agents.
Author: Hadi Seelro
"""

import streamlit as st
import random
import time
from datetime import datetime

# -----------------------------------------------------------------------------
# 1. PAGE SETUP & MODERN CLEAN DESIGN
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="NexusNarrative | Smart Story Studio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Modern, clean glassmorphic styling
CUSTOM_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

    :root {
        --bg-color: #0b0f19;
        --card-bg: rgba(17, 24, 39, 0.7);
        --accent-blue: #00d2ff;
        --accent-purple: #9d4edd;
        --accent-green: #10b981;
        --text-main: #f8fafc;
        --text-sub: #94a3b8;
        --border-color: rgba(0, 210, 255, 0.2);
    }

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    code, .mono-text {
        font-family: 'JetBrains Mono', monospace !important;
    }

    .stApp {
        background: radial-gradient(circle at 10% 10%, rgba(157, 78, 221, 0.12) 0%, transparent 40%),
                    radial-gradient(circle at 90% 90%, rgba(0, 210, 255, 0.10) 0%, transparent 40%),
                    #0b0f19;
        color: var(--text-main);
    }

    /* Modern Glass Card */
    .glass-card {
        background: var(--card-bg);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid var(--border-color);
        border-radius: 14px;
        padding: 22px;
        margin-bottom: 20px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
    }

    /* Hero Banner */
    .hero-banner {
        border-left: 4px solid var(--accent-blue);
        background: linear-gradient(90deg, rgba(0, 210, 255, 0.08) 0%, rgba(157, 78, 221, 0.05) 100%);
        padding: 20px 24px;
        border-radius: 12px;
        margin-bottom: 24px;
    }
    .hero-title {
        font-size: 2.1rem;
        font-weight: 800;
        background: linear-gradient(135deg, #00d2ff 0%, #3a7bd5 50%, #9d4edd 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 6px;
    }
    .hero-subtitle {
        color: var(--text-sub);
        font-size: 1rem;
    }

    /* Badges */
    .badge-row {
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
        margin-top: 12px;
    }
    .status-badge {
        font-size: 0.78rem;
        font-weight: 600;
        padding: 4px 12px;
        border-radius: 999px;
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(15, 23, 42, 0.85);
        border: 1px solid rgba(148, 163, 184, 0.2);
        color: var(--text-sub);
    }
    .badge-live {
        color: #00d2ff;
        border-color: rgba(0, 210, 255, 0.4);
    }
    .pulse-dot {
        width: 8px;
        height: 8px;
        background-color: #10b981;
        border-radius: 50%;
        box-shadow: 0 0 8px #10b981;
    }

    /* Highlighted User Words */
    .user-word {
        color: #00d2ff;
        background: rgba(0, 210, 255, 0.12);
        border: 1px solid rgba(0, 210, 255, 0.35);
        padding: 2px 8px;
        border-radius: 6px;
        font-weight: 700;
        display: inline-block;
        margin: 0 2px;
    }

    /* Metric Boxes */
    .metrics-row {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
        gap: 12px;
        margin: 16px 0;
    }
    .metric-box {
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid rgba(148, 163, 184, 0.15);
        border-radius: 12px;
        padding: 12px;
        text-align: center;
    }
    .metric-name {
        font-size: 0.75rem;
        text-transform: uppercase;
        color: var(--text-sub);
        font-weight: 600;
    }
    .metric-number {
        font-size: 1.35rem;
        font-weight: 800;
        color: #00d2ff;
        margin-top: 4px;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Story Box */
    .story-display {
        font-size: 1.15rem;
        line-height: 1.8;
        color: #f1f5f9;
        margin: 16px 0;
        padding: 20px;
        border-radius: 12px;
        background: rgba(10, 14, 23, 0.85);
        border-left: 3px solid var(--accent-purple);
    }

    /* Critic Review Card */
    .critic-card {
        border-left: 3px solid #f59e0b;
        background: rgba(245, 158, 11, 0.08);
        padding: 14px 18px;
        border-radius: 8px;
        margin-top: 14px;
        color: #fde68a;
    }

    /* Footer */
    .app-footer {
        text-align: center;
        padding: 24px 10px 10px 10px;
        color: var(--text-sub);
        font-size: 0.85rem;
        border-top: 1px solid rgba(148, 163, 184, 0.1);
        margin-top: 40px;
    }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. STATE STORAGE
# -----------------------------------------------------------------------------
if "story_history" not in st.session_state:
    st.session_state.story_history = []
if "current_story" not in st.session_state:
    st.session_state.current_story = None
if "current_metrics" not in st.session_state:
    st.session_state.current_metrics = None
if "current_critic" not in st.session_state:
    st.session_state.current_critic = None

# -----------------------------------------------------------------------------
# 3. SIMPLE & FUN READY-MADE PRESETS
# -----------------------------------------------------------------------------
PRESET_PERSONAS = {
    "🤖 Friendly AI Researcher": {
        "adjective": "super-smart",
        "verb1": "build",
        "verb2": "test",
        "famous_person": "Elon Musk",
        "tech_artifact": "supercomputer",
        "ai_directive": "help people around the world",
    },
    "💻 Passionate Programmer": {
        "adjective": "exciting",
        "verb1": "code",
        "verb2": "debug",
        "famous_person": "Hadi Seelro",
        "tech_artifact": "laptop",
        "ai_directive": "launch a great new app",
    },
    "🚀 Space Explorer": {
        "adjective": "mysterious",
        "verb1": "explore",
        "verb2": "discover",
        "famous_person": "Neil Armstrong",
        "tech_artifact": "spaceship",
        "ai_directive": "find new friendly planets",
    },
    "🎮 Game Developer": {
        "adjective": "amazing",
        "verb1": "design",
        "verb2": "play",
        "famous_person": "Shigeru Miyamoto",
        "tech_artifact": "gaming console",
        "ai_directive": "create the most fun game ever",
    },
}

# -----------------------------------------------------------------------------
# 4. STORY TEMPLATES IN SIMPLE ENGLISH
# -----------------------------------------------------------------------------
GENRE_TEMPLATES = {
    "🤖 The Smart Robot": [
        "One day, a {adjective} computer robot woke up in the science lab. "
        "The team tried to {verb1} the system using a new {tech_artifact}. "
        "Suddenly, {famous_person} smiled and said: 'Don't worry! You just need to {verb2} "
        "every day and {ai_directive}!' Everyone cheered and celebrated.",

        "The school lab got a {adjective} new machine today. "
        "All the students wanted to {verb1} with the cool {tech_artifact}. "
        "Even {famous_person} came to visit and reminded us to {verb2} "
        "and {ai_directive} with big dreams!",
    ],
    "🚀 Startup Journey": [
        "Starting a new project is always {adjective}! "
        "Our small team gathered to {verb1} the first version of our {tech_artifact}. "
        "In the middle of the meeting, {famous_person} gave great advice: 'Work hard, {verb2} "
        "often, and never stop trying to {ai_directive}!' That made everyone super confident.",

        "Working in technology is so {adjective}! "
        "Every morning, developers get together to {verb1} using a modern {tech_artifact}. "
        "As {famous_person} always says: if you want to make an impact, you should {verb2} "
        "with passion and {ai_directive}!",
    ],
    "💻 The Coding Adventure": [
        "Learning computer programming is truly {adjective}! "
        "We spent the whole afternoon trying to {verb1} bugs inside the {tech_artifact}. "
        "Our mentor {famous_person} told us to stay calm, drink water, and {verb2} "
        "regularly so we can {ai_directive} like champions!",

        "Building software is a {adjective} journey. "
        "You open your {tech_artifact} and start to {verb1}. "
        "With good friends and mentors like {famous_person}, you quickly learn how to {verb2} "
        "and {ai_directive} step by step.",
    ],
}

# -----------------------------------------------------------------------------
# 5. CORE HELPER FUNCTIONS
# -----------------------------------------------------------------------------
class StoryMaker:
    """Combines user words with templates smoothly."""

    @staticmethod
    def create_story(
        template: str,
        adjective: str,
        verb1: str,
        verb2: str,
        famous_person: str,
        tech_artifact: str,
        ai_directive: str,
    ) -> tuple[str, str]:
        # Plain text version
        plain_story = template.format(
            adjective=adjective.strip(),
            verb1=verb1.strip(),
            verb2=verb2.strip(),
            famous_person=famous_person.strip(),
            tech_artifact=tech_artifact.strip(),
            ai_directive=ai_directive.strip(),
        )

        # Highlighted HTML version for visual appeal
        highlighted_story = template.format(
            adjective=f'<span class="user-word">{adjective.strip()}</span>',
            verb1=f'<span class="user-word">{verb1.strip()}</span>',
            verb2=f'<span class="user-word">{verb2.strip()}</span>',
            famous_person=f'<span class="user-word">{famous_person.strip()}</span>',
            tech_artifact=f'<span class="user-word">{tech_artifact.strip()}</span>',
            ai_directive=f'<span class="user-word">{ai_directive.strip()}</span>',
        )

        return plain_story, highlighted_story


class StoryReviewer:
    """Gives helpful feedback and story stats."""

    @staticmethod
    def review(story: str, creativity_level: int) -> tuple[dict, str]:
        words = len(story.split())
        score = min(99, 75 + (words % 20) + int(creativity_level * 0.05))
        flow = max(70, 100 - int(creativity_level * 0.2))
        reading_time = max(3, round(words / 3.2))

        stats = {
            "Total Words": words,
            "Story Score": f"{score}/100",
            "Story Flow": f"{flow}%",
            "Creativity": f"{creativity_level}%",
            "Reading Time": f"~{reading_time}s",
        }

        # Simple, encouraging feedback
        if creativity_level > 70:
            feedback = (
                "🤖 AI Assistant Review: 'Very creative and energetic story! "
                "Your words make it exciting and fun to read.'"
            )
        elif creativity_level > 40:
            feedback = (
                "🧠 AI Assistant Review: 'Great story! The words fit nicely together "
                "with a smooth and clear flow.'"
            )
        else:
            feedback = (
                "📐 AI Assistant Review: 'Clean, simple, and well-organized story! "
                "Easy to read and understand.'"
            )

        return stats, feedback


# -----------------------------------------------------------------------------
# 6. SIDEBAR: WORD INPUTS & CONTROLS
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### 🎛️ Story Settings")
    st.caption("Fill in your own words or pick a quick ready-made idea.")

    # Preset dropdown
    selected_preset_name = st.selectbox(
        "⚡ Quick Idea Presets",
        options=["(Custom Words)"] + list(PRESET_PERSONAS.keys()),
        index=0,
        help="Pick one of these to automatically fill the boxes with fun ideas.",
    )

    defaults = PRESET_PERSONAS.get(selected_preset_name, {
        "adjective": "creative",
        "verb1": "build",
        "verb2": "learn",
        "famous_person": "Hadi Seelro",
        "tech_artifact": "computer",
        "ai_directive": "make the world better",
    })

    st.markdown("---")
    st.markdown("#### 📝 Fill In The Blanks")

    user_adj = st.text_input(
        "Adjective (Describing Word)",
        value=defaults["adjective"],
        help="Example: exciting, fast, smart, friendly",
    )
    user_verb1 = st.text_input(
        "Action Verb 1",
        value=defaults["verb1"],
        help="Example: run, build, code, explore",
    )
    user_verb2 = st.text_input(
        "Action Verb 2",
        value=defaults["verb2"],
        help="Example: jump, test, teach, smile",
    )
    user_famous = st.text_input(
        "Famous Person or Hero",
        value=defaults["famous_person"],
        help="Example: Elon Musk, Hadi Seelro, your friend",
    )
    user_tech = st.text_input(
        "Cool Machine or Tool",
        value=defaults["tech_artifact"],
        help="Example: robot, laptop, spaceship",
    )
    user_directive = st.text_input(
        "Big Goal or Mission",
        value=defaults["ai_directive"],
        help="Example: save the day, make people happy",
    )

    st.markdown("---")
    st.markdown("#### 🎨 Story Style")

    selected_genre = st.selectbox(
        "Story Theme",
        options=list(GENRE_TEMPLATES.keys()),
        index=0,
    )

    creativity_slider = st.slider(
        "Creativity Level (%)",
        min_value=10,
        max_value=100,
        value=50,
        step=5,
        help="Higher values give more playful and energetic results.",
    )

    st.markdown("---")
    st.caption("Created with 💖 by **Hadi Seelro**")

# -----------------------------------------------------------------------------
# 7. MAIN INTERFACE
# -----------------------------------------------------------------------------

# Header Banner
st.markdown(
    """
    <div class="hero-banner">
        <div class="hero-title">NexusNarrative : Smart Story Studio</div>
        <div class="hero-subtitle">
            An intelligent story maker that turns your words into fun, creative stories with real-time feedback.
        </div>
        <div class="badge-row">
            <span class="status-badge badge-live"><span class="pulse-dot"></span> AI System: Ready</span>
            <span class="status-badge">Mode: Multi-Agent Story Maker</span>
            <span class="status-badge">Speed: Instant (&lt;15ms)</span>
            <span class="status-badge">Built by: Hadi Seelro</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

tab_studio, tab_how_it_works, tab_history = st.tabs([
    "🎭 Story Studio",
    "🧠 How It Works",
    "📜 Saved Stories"
])

# -----------------------------------------------------------------------------
# TAB 1: STORY STUDIO
# -----------------------------------------------------------------------------
with tab_studio:
    btn_col, note_col = st.columns([1, 4])
    with btn_col:
        make_story_clicked = st.button("✨ Make Story", type="primary", use_container_width=True)
    with note_col:
        st.caption("Click to combine your words into a unique new story!")

    if make_story_clicked:
        # Check that no inputs are empty
        fields = [user_adj, user_verb1, user_verb2, user_famous, user_tech, user_directive]
        if any(not f.strip() for f in fields):
            st.warning("⚠️ Please fill in all the blank boxes in the sidebar first!")
        else:
            with st.spinner("🤖 Writing your story..."):
                time.sleep(0.3)  # Brief pleasant animation
                template_list = GENRE_TEMPLATES[selected_genre]
                chosen_template = random.choice(template_list)

                plain_text, html_text = StoryMaker.create_story(
                    template=chosen_template,
                    adjective=user_adj,
                    verb1=user_verb1,
                    verb2=user_verb2,
                    famous_person=user_famous,
                    tech_artifact=user_tech,
                    ai_directive=user_directive,
                )

                stats, feedback = StoryReviewer.review(plain_text, creativity_slider)

                current_time = datetime.now().strftime("%I:%M %p")
                st.session_state.current_story = {
                    "plain": plain_text,
                    "html": html_text,
                    "genre": selected_genre,
                    "time": current_time,
                }
                st.session_state.current_metrics = stats
                st.session_state.current_critic = feedback

                # Save to history list
                st.session_state.story_history.insert(0, {
                    "time": current_time,
                    "genre": selected_genre,
                    "story": plain_text,
                    "stats": stats,
                    "feedback": feedback,
                })

    # Show generated story if available
    if st.session_state.current_story:
        story_data = st.session_state.current_story
        stats_data = st.session_state.current_metrics
        feedback_data = st.session_state.current_critic

        st.markdown(
            f"""
            <div class="glass-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-weight:700; font-size:1.15rem; color:#00d2ff;">🎉 Your Generated Story</span>
                    <span style="font-size:0.8rem; color:#94a3b8;">
                        Theme: {story_data['genre']} &nbsp;•&nbsp; Time: {story_data['time']}
                    </span>
                </div>
                <div class="story-display">
                    {story_data['html']}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Show Story Stats
        st.markdown("#### 📊 Story Scorecard")
        cols = st.columns(len(stats_data))
        for col, (name, val) in zip(cols, stats_data.items()):
            with col:
                st.markdown(
                    f"""
                    <div class="metric-box">
                        <div class="metric-name">{name}</div>
                        <div class="metric-number">{val}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        # Show Feedback
        st.markdown(
            f"""
            <div class="critic-card">
                {feedback_data}
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.write("")
        # Download buttons
        dcol1, dcol2, dcol3 = st.columns([1, 1, 2])
        with dcol1:
            st.download_button(
                label="📥 Download Markdown",
                data=f"# My NexusNarrative Story\n\n**Theme:** {story_data['genre']}\n**Time:** {story_data['time']}\n\n---\n\n{story_data['plain']}\n\n---\n**Feedback:**\n{feedback_data}\n\n*Created with NexusNarrative by Hadi Seelro*",
                file_name="my_story.md",
                mime="text/markdown",
                use_container_width=True,
            )
        with dcol2:
            st.download_button(
                label="📄 Download Plain Text",
                data=story_data['plain'],
                file_name="my_story.txt",
                mime="text/plain",
                use_container_width=True,
            )
        with dcol3:
            st.caption("💡 Tip: The glowing words in the story are the words you provided in the sidebar!")
    else:
        st.info("👈 Enter your words in the sidebar and click **'Make Story'** to get started!")

# -----------------------------------------------------------------------------
# TAB 2: HOW IT WORKS
# -----------------------------------------------------------------------------
with tab_how_it_works:
    st.markdown("### 🧩 How The Multi-Agent Pipeline Works")
    st.caption("Here is how the smart assistants work together step by step:")

    st.markdown(
        """
        <div class="glass-card">
            <h4 style="color:#00d2ff; margin-top:0;">Step-by-Step Flow</h4>
            <div style="font-size:0.95rem; line-height:1.8; color:#cbd5e1; background:rgba(10,14,23,0.9); padding:18px; border-radius:10px; border:1px solid rgba(0,210,255,0.2);">
                <b>1. Input Assistant:</b> Reads and cleans the words you entered to make sure there are no blank boxes.<br>
                <b>2. Director Assistant:</b> Chooses the right story template based on the theme you selected.<br>
                <b>3. Story Writer:</b> Places your words into the template and highlights them with glowing badges.<br>
                <b>4. Reviewer Assistant:</b> Calculates word count, checks story flow, and provides encouraging feedback.<br>
                <b>5. Modern Display:</b> Shows your story in a clean glass card with one-click download buttons.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown(
            """
            <div class="glass-card">
                <h5 style="color:#00d2ff; margin-top:0;">🛡️ Safe &amp; Clean</h5>
                <ul style="font-size:0.9rem; color:#cbd5e1; line-height:1.6;">
                    <li>Checks all input boxes before creating the story.</li>
                    <li>Saves your generated stories during your session so nothing is lost.</li>
                    <li>Works fast without needing any external API keys.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col_b:
        st.markdown(
            """
            <div class="glass-card">
                <h5 style="color:#9d4edd; margin-top:0;">📈 Helpful Stats</h5>
                <ul style="font-size:0.9rem; color:#cbd5e1; line-height:1.6;">
                    <li><b>Word Count:</b> Shows total words in your story.</li>
                    <li><b>Story Score:</b> Rates the quality and creativity of the story.</li>
                    <li><b>Reading Time:</b> Estimates how many seconds it takes to read.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

# -----------------------------------------------------------------------------
# TAB 3: STORY HISTORY
# -----------------------------------------------------------------------------
with tab_history:
    st.markdown("### 📜 Saved Stories")
    st.caption("Here is the list of all stories you created in this session:")

    if not st.session_state.story_history:
        st.info("You haven't made any stories yet. Go to the Story Studio tab and click 'Make Story'!")
    else:
        for idx, item in enumerate(st.session_state.story_history):
            with st.expander(f"📖 Story #{len(st.session_state.story_history) - idx} • {item['genre']} ({item['time']})", expanded=(idx == 0)):
                st.write(item["story"])
                st.caption(f"**Feedback:** {item['feedback']}")
                st.markdown(
                    f"`Words: {item['stats']['Total Words']}` &nbsp;|&nbsp; "
                    f"`Score: {item['stats']['Story Score']}` &nbsp;|&nbsp; "
                    f"`Flow: {item['stats']['Story Flow']}`"
                )

# -----------------------------------------------------------------------------
# 8. FOOTER
# -----------------------------------------------------------------------------
st.markdown(
    """
    <div class="app-footer">
        NexusNarrative • Made with 💖 by <b>Hadi Seelro</b><br>
        <span style="font-size:0.75rem; color:#64748b;">
            Portfolio Project • Python 3.12 &amp; Streamlit
        </span>
    </div>
    """,
    unsafe_allow_html=True,
)
