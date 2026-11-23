import streamlit as st

def style_background_home():
    st.markdown("""
        <style>
            .stApp {
                background: #5865F2 !important
            }

            .stApp div[data-testid="stColumn"]{
                background-color: #E0E3FF !important;
                padding: 2.5rem !important;
                border-radius: 5rem !important;
            }

            .stApp h1,
            .stApp h2,
            .stApp h3,
            .stApp h4,
            .stApp p {
                color: #31333F 
            }
        </style>
""",unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background: #E0E3FF !important
            }

            .stApp h1,
            .stApp h2,
            .stApp h3,
            .stApp h4,
            .stApp p,
            .stApp label {
                color: #31333F 
            }
        </style>
""",unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

                .stApp h1,
                .stApp h2,
                .stApp h3,
                .stApp h4,
                .stApp h5,
                .stApp h6,
                .stApp p,
                .stApp label,
                .stApp [data-testid="stMarkdownContainer"],
                .stApp [data-testid="stWidgetLabel"] {
                    color: #31333F 
                }

                /*Hide Top Bar of streamlit*/
            
                #MainMenu, header, footer {
                    visibility: hidden;
                }

                .block-container {
                    padding-top: 1.5rem !important;
                }

                h1 {
                    font-family: 'Climate Crisis', sans-serif !important;
                    font-size: 3.5rem !important;
                    line-height: 0.9 !important;
                    margin-bottom: 0rem !important;
                }

                h2 {
                    font-family: 'Climate Crisis', sans-serif !important;
                    font-size: 2rem !important;
                    line-height: 1.1 !important;
                    margin-bottom: 0rem !important;
                }

                h3, h4, p {
                    font-family: 'Outfit', sans-serif;
                }

                /* =====================================
                STREAMLIT BUTTON STYLING
                ===================================== */

                /* Primary buttons */
                .stApp div[data-testid="stButton"] button[kind="primary"],
                .stApp button[data-testid="stBaseButton-primary"] {
                    background-color: #5865F2 !important;
                    color: #FFFFFF !important;
                    border: none !important;
                    border-radius: 1.5rem !important;
                    padding: 10px 20px !important;
                }

                /* Force button text and icons to white */
                .stApp div[data-testid="stButton"] button[kind="primary"] *,
                .stApp button[data-testid="stBaseButton-primary"] * {
                    color: #FFFFFF !important;
                    fill: #FFFFFF !important;
                    -webkit-text-fill-color: #FFFFFF !important;
                }

                /* Secondary buttons */
                .stApp div[data-testid="stButton"] button[kind="secondary"],
                .stApp button[data-testid="stBaseButton-secondary"] {
                    background-color: #EB459E !important;
                    color: #FFFFFF !important;
                    border-radius: 1.5rem !important;
                    border: none !important;
                }

                .stApp div[data-testid="stButton"] button[kind="secondary"] * {
                    color: #FFFFFF !important;
                    fill: #FFFFFF !important;
                }

                /* Tertiary buttons */
                .stApp div[data-testid="stButton"] button[kind="tertiary"] {
                    background-color: #000000 !important;
                    color: #FFFFFF !important;
                    border-radius: 1.5rem !important;
                    border: none !important;
                }

                .stApp div[data-testid="stButton"] button[kind="tertiary"] * {
                    color: #FFFFFF !important;
                    fill: #FFFFFF !important;
                }

                /* Hover */
                .stApp div[data-testid="stButton"] button:hover {
                    transform: scale(1.05);
                }
        
        </style>
""",unsafe_allow_html=True)
    
    