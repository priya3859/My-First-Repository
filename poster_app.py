import streamlit as st

# Page config
st.set_page_config(page_title="Machine Learning Poster", layout="wide")

# Background + Box Styling
st.markdown("""
<style>
.stApp {
    background-color: #0f2027;
    background-image: linear-gradient(315deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
    color: white;
}

.box {
    background-color: #1f3b4d;
    padding: 15px;
    border-radius: 15px;
    margin-bottom: 15px;
}

h1, h2, h3 {
    text-align: center;
    color: #00e5ff;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>🤖 MACHINE LEARNING</h1>", unsafe_allow_html=True)
st.markdown("<h3>Overview, Types, Applications & Advantages</h3>", unsafe_allow_html=True)

# Layout
col1, col2, col3 = st.columns(3)

# INTRODUCTION
with col1:
    st.markdown("""
    <div class="box">
    <h3>INTRODUCTION</h3>
    <ul>
    <li>Machine Learning is a part of Artificial Intelligence.</li>
    <li>It allows systems to learn from data.</li>
    <li>Works without explicit programming.</li>
    <li>Improves performance with experience.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ADVANTAGES
with col2:
    st.markdown("""
    <div class="box">
    <h3>ADVANTAGES</h3>
    <ul>
    <li>Automation of tasks</li>
    <li>Handles large amount of data</li>
    <li>Improves decision making</li>
    <li>Wide range of applications</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# LIMITATIONS
with col3:
    st.markdown("""
    <div class="box">
    <h3>LIMITATIONS</h3>
    <ul>
    <li>Needs large amount of data</li>
    <li>Data labeling is costly</li>
    <li>High computational cost</li>
    <li>Risk of bias</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# TYPES OF ML
st.markdown("""
<div class="box">
<h3>TYPES OF MACHINE LEARNING</h3>
<ul>
<li><b>Supervised Learning</b> – Classification, Regression</li>
<li><b>Unsupervised Learning</b> – Clustering, Association</li>
<li><b>Reinforcement Learning</b> – Reward based learning</li>
</ul>
</div>
""", unsafe_allow_html=True)

# APPLICATIONS
st.markdown("""
<div class="box">
<h3>REAL LIFE APPLICATIONS</h3>
<ul>
<li>Image Recognition</li>
<li>Speech Recognition</li>
<li>Medical Diagnosis</li>
<li>Recommendation Systems</li>
<li>Fraud Detection</li>
</ul>
</div>
""", unsafe_allow_html=True)

# FOOTER
st.markdown("""
<div class="box">
<p style="text-align:center;">
<b>Done By:</b> Your Name <br>
<b>Subject:</b> Artificial Intelligence & Machine Learning
</p>
</div>
""", unsafe_allow_html=True)
