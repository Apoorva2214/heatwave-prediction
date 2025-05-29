import streamlit as st

# Configure Streamlit page
st.set_page_config(page_title="Heatwave Forecast App", layout="wide")

# Custom CSS for a wide desktop layout
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        background-color: #fff8f5;
    }

    .main-container {
        max-width: 1200px;
        margin: 5rem auto;
        background: #ffffffee;
        padding: 3.5rem 4rem;
        border-radius: 24px;
        box-shadow: 0 12px 40px rgba(0,0,0,0.1);
        text-align: center;
    }

    h1 {
        font-weight: 700;
        font-size: 3.5rem;
        margin-bottom: 1rem;
        color: #c0392b;
        text-shadow: 1px 1px 6px rgba(192, 57, 43, 0.2);
    }

    h2 {
        font-weight: 500;
        font-size: 1.6rem;
        color: #333;
        margin-bottom: 2rem;
    }

    ul {
        list-style-type: none;
        padding-left: 0;
        font-size: 1.2rem;
        line-height: 2rem;
        margin-bottom: 2rem;
    }


    hr {
        margin: 2rem auto;
        border-top: 2px solid #ddd;
        width: 80%;
    }

    footer {
        margin-top: 2rem;
        font-size: 1rem;
        color: #777;
    }

    header, .block-container {
        padding-top: 1rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# Render homepage content
st.markdown("""
<div class="main-container">
    <h1>☀️ Heatwave Early Warning System</h1>
    <h2>Welcome! Use the sidebar to:</h2>
    <ul>
        <li>🔮 Predict heatwaves for selected dates</li>
        <li>📈 Visualize temperature forecast using ARIMA for the next 7 days</li>
    </ul>
    <hr>
    <p><strong>Apoorva</strong> | IIIT Lucknow | CRO Internship</p>
</div>
<footer>© 2025 Apoorva - Heatwave Forecast App</footer>
""", unsafe_allow_html=True)
