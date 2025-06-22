import streamlit as st
from PIL import Image
import base64
import os

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Sanele Mabhedula | Profile",
    page_icon=":bar_chart:",
    layout="wide"
)

# ---- COLOR SCHEME ----
PRIMARY = "#1f77b4"
ACCENT = "#39C1C8"
LIGHT_BG = "#F6FAFB"
DARK_BG = "#141A22"
WHITE = "#ffffff"
BLACK = "#121212"
DARK_PANEL = "#202837"
LIGHT_PANEL = "#ffffff"
LIGHT_TEXT = "#212B36"
DARK_TEXT = "#F6FAFB"

def get_mode():
    return st.get_option("theme.base") or "dark"

mode = get_mode().lower()
if "light" in mode:
    BG = LIGHT_BG
    PANEL = LIGHT_PANEL
    TEXT = LIGHT_TEXT
    SUBTITLE = PRIMARY
    HEADER = PRIMARY
    CARD_BG = "#EAF3FA"
    BUTTON_BG = WHITE
    BUTTON_COLOR = PRIMARY
    BUTTON_BORDER = PRIMARY
else:
    BG = DARK_BG
    PANEL = DARK_PANEL
    TEXT = DARK_TEXT
    SUBTITLE = ACCENT
    HEADER = ACCENT
    CARD_BG = "#1f2733"
    BUTTON_BG = WHITE
    BUTTON_COLOR = PRIMARY
    BUTTON_BORDER = PRIMARY

# ---- CUSTOM CSS ----
st.markdown(
    f"""
    <style>
    html, body, .stApp {{
        background-color: {BG} !important;
        margin: 0;
        padding: 0;
    }}
    .main-content {{
        background: {PANEL};
        border-radius: 18px;
        box-shadow: 0 4px 28px rgba(31,119,180,0.13);
        padding: 3vw 4vw 2vw 4vw;
        margin: auto;
        max-width: 900px;
        margin-top: 3vw;
        margin-bottom: 3vw;
    }}
    .profile-header {{
        display: flex;
        flex-direction: row;
        align-items: flex-start;
        gap: 4vw;
        margin-bottom: 16px;
        flex-wrap: wrap;
    }}
    .profile-img {{
        border: 6px solid {ACCENT};
        border-radius: 50%;
        width: 160px;
        height: 160px;
        object-fit: cover;
        box-shadow: 0 4px 12px rgba(48, 57, 80, 0.11);
        background: #fff;
        margin-bottom: 10px;
        margin-top: 6px;
        display: block;
    }}
    .main-title {{
        font-size: min(7vw, 40px);
        font-weight: bold;
        color: {HEADER};
        margin-bottom: 6px;
        margin-top: 0;
    }}
    .subtitle {{
        font-size: min(4vw, 20px);
        color: {SUBTITLE};
        margin-bottom: 10px;
        font-weight: 600;
    }}
    .location {{
        font-size: min(3.5vw, 17px);
        color: {ACCENT};
        margin-bottom: 12px;
        font-weight: 500;
    }}
    .contact-btn {{
        background-color: {BUTTON_BG};
        color: {BUTTON_COLOR} !important;
        border: 2px solid {BUTTON_BORDER};
        border-radius: 5px;
        padding: 11px 32px;
        font-size: min(4vw, 19px);
        font-weight: 600;
        margin-bottom: 12px;
        text-decoration: none;
        transition: background 0.2s, color 0.2s;
        display: inline-block;
        margin-top: 10px;
        box-shadow: 0 2px 6px rgba(31,119,180,0.13);
    }}
    .contact-btn:hover {{
        background-color: {PRIMARY};
        color: #fff !important;
        border: 2px solid {PRIMARY};
    }}
    .icon {{
        height: 22px;
        width: 22px;
        vertical-align: bottom;
        margin-right: 7px;
    }}
    .contact-info {{
        font-size: min(3.8vw, 17px);
        color: {TEXT};
        margin-bottom: 12px;
        margin-top: 4px;
    }}
    .section-title {{
        color: {HEADER};
        font-size: min(5vw, 23px);
        font-weight: 700;
        margin-top: 22px;
    }}
    .about-text, .skills-text {{
        font-size: min(4vw, 18px);
        color: {TEXT};
        margin-bottom: 0.9em;
    }}
    .quote {{
        background: {CARD_BG};
        margin: 36px 0 16px 0;
        padding: 16px 22px;
        font-style: italic;
        font-size: min(4vw, 18px);
        color: {PRIMARY};
        border-radius: 10px;
        border-left: 5px solid {ACCENT};
        font-weight: 500;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ---- MAIN CONTENT ----
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# ---- HEADER & PROFILE ----
st.markdown('<div class="profile-header">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 3], gap="large")

with col1:
    try:
        image = Image.open("profile.jpg")
        st.markdown(
            f'<img src="data:image/jpeg;base64,{base64.b64encode(open("profile.jpg", "rb").read()).decode()}" class="profile-img"/>',
            unsafe_allow_html=True
        )
    except Exception:
        st.info("Add your image as profile.jpg in this directory for best appearance.")

with col2:
    st.markdown(f'<div class="main-title">Sanele Mabhedula</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="subtitle">Data Science in Training | Helping People Make Smarter Decisions with Data</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div class="location"><span style="font-size:18px;">📍</span> Johannesburg, South Africa | Passionate about impact through insight</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<a href="#contact" class="contact-btn">Contact Me</a>',
        unsafe_allow_html=True
    )
    st.markdown(
        f"""
        <div class="contact-info" id="contact">
            <img class="icon" src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/svg/2709.svg"/> <b>Email:</b> sichothosanele@gmail.com<br>
            <img class="icon" src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/svg/1f4f1.svg"/> <b>Cell/WhatsApp:</b> +27 78 981 6814
        </div>
        """,
        unsafe_allow_html=True
    )
st.markdown('</div>', unsafe_allow_html=True)

# ---- ABOUT ME ----
st.markdown('<div class="section-title">About Me</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="about-text">
    I’m Sanele, a passionate and purpose-driven data science student in training.<br>
    I help individuals, small businesses, NGOs, and community organizations understand their data — not just to collect it, but to use it for better decisions.<br><br>
    Whether it’s showing trends through dashboards, spotting problems early through analysis, or finding answers through data storytelling, I bring curiosity, empathy, and problem-solving to the table. My goal is simple: help people move with confidence, backed by insights.<br><br>
    I believe every organization is unique, so I specialize in <b>customizing solutions to fit your exact needs</b>. If you have a vision or special requirements, I’m always excited to build something that works for you.<br><br>
    I am currently studying <b>Applied Data Science</b> at <b>WorldQuant University</b> and <b>Economics & Management</b> at <b>UNISA</b>, while building real-world projects that matter — from interactive dashboards to language-based mental health tools.
    </div>
    """, unsafe_allow_html=True
)

# ---- DEMO VIDEO SECTION: SMALLER & ASIDE USING COLUMNS ----
gdrive_video_url = "https://drive.google.com/file/d/10MHrx6g3t9q-CVF23BR3cRhpc2MQeqny/view?usp=sharing"

st.markdown('<div class="section-title">Demo Video</div>', unsafe_allow_html=True)
vid_col, txt_col = st.columns([1, 4])
with vid_col:
    st.video(gdrive_video_url)
    with txt_col:
        st.markdown(
            """
            <div style="font-size:18px; font-weight:600; margin-bottom:0.5em;">
                Getting honest feedback is hard.<br>
                And making sense of it? Even harder.
            </div>
            <div style="font-size:16px; margin-bottom:0.5em;">
                Imagine seeing every comment, every rating, every trend—all in one place.<br><br>
                My dashboard makes it easy: clear visuals, powerful insights, and simple tools to help you turn opinions into action.<br><br>
                <b>What you'll see in this demo:</b>
                <ul>
                    <li>Instantly view your average rating, feedback trends, and recent comments</li>
                    <li>Filter results, export detailed reports, and track what’s working</li>
                    <li>Collect new feedback with a simple link or QR code—any device, any time</li>
                    <li>See your true impact and make smarter decisions, faster</li>
                </ul>
                <b>This is just a glimpse!</b> There’s so much more behind the scenes, and I can <b>custom-build features and dashboards based on your unique needs and interests</b>.<br><br>
                If you have an idea or want something special, let’s chat — I’m always up for building what matters to you.<br><br>
                Ready to discover what people really think? <b>Click play</b> and see how simple understanding your impact can be!
            </div>
            """,
            unsafe_allow_html=True
        )

# ---- DATA QUOTE ----
st.markdown(
    f"""
    <div class="quote">
        "Without data, you're just another person with an opinion." – W. Edwards Deming
    </div>
    """, unsafe_allow_html=True
)

# ---- SKILLS & TOOLS ----
st.markdown('<div class="section-title">Key Skills & Tools</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="skills-text">
    <ul>
        <li><b>Data Analysis:</b> Python (Pandas, NumPy)</li>
        <li><b>Dashboards & Reporting:</b> Streamlit</li>
        <li><b>Web Apps:</b> Streamlit (multi-page, user-authentication, CSV-based apps)</li>
        <li><b>Machine Learning:</b> Currently learning classification, regression, and NLP techniques</li>
        <li><b>Visualization:</b> Matplotlib, Seaborn, Plotly</li>
        <li><b>Soft Skills:</b> Problem-solving, data storytelling, collaboration, emotional intelligence</li>
    </ul>
    </div>
    """, unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)  # end main-content

# ---- FOOTER ----
st.markdown(
    f"""
    <div style="text-align:center; color:{SUBTITLE if 'light' in mode else ACCENT}; margin-top:36px; font-size:14px;">
        &copy; 2025 Sanele Mabhedula | Data-driven decisions for a smarter world.
    </div>
    """, unsafe_allow_html=True
)