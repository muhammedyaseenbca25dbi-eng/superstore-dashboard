import streamlit as st

st.title("Muhammed Yaseen")

st.header("About Me", divider="blue")
st.write("I am interested in Python, AI, and Web Development.")
st.header("Skills", divider="green")
st.markdown(
    "- Python\n"
    "- HTML\n"
    "- CSS"
)
st.header("Contact", divider="orange")
st.write("Email: yaseen@gmail.com")
st.subheader("Favourite Snippet")
st.code("""
name = "Yaseen"
print(name)
""", language="python")

st.latex(r'E = mc^{2}')

st.markdown("---")
st.caption("Built with Streamlit")