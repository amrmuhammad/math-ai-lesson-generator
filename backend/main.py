import streamlit as st
from ai_model import generate_lesson
from math_utils import plot_quadratic

st.set_page_config(page_title="AI Math Lesson Generator", layout="wide")

st.title("🤖 AI Math Lesson Generator")
st.markdown("""
Enter any high school math topic (e.g. **quadratic equations**, **Pythagorean theorem**, **derivatives**).  
You'll get a short, student-friendly lesson with math typeset in LaTeX and optional visualizations!
"""
)

topic = st.text_input("Enter a math topic:")

if topic:
    with st.spinner("Generating lesson..."):
        lesson, latex_list = generate_lesson(topic)
    st.subheader("AI-Generated Lesson")
    st.markdown(lesson, unsafe_allow_html=True)
    for latex_expr in latex_list:
        st.latex(latex_expr)
    # Example visual: plot quadratic if topic matches
    if "quadratic" in topic.lower():
        st.subheader("Quadratic Graph Example")
        fig = plot_quadratic()
        st.pyplot(fig)