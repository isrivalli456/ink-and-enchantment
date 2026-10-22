
import streamlit as st
from datetime import datetime
from pathlib import Path
import sys

# Make the CrewAI project importable
PROJECT_DIR = Path(__file__).resolve().parent
SRC_DIR = PROJECT_DIR / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from blog_writing_crew.crew import BlogWritingCrew

st.set_page_config(
    page_title="BlogGenius AI",
    page_icon="✍️",
    layout="centered",
)

st.title("✍️ BlogGenius AI")
st.subheader("Your personal AI blog-writing studio")
st.write(
    "Enter any topic. Your AI Researcher and AI Writer will work together "
    "to create a blog for you."
)

topic = st.text_input(
    "What do you want to write about?",
    placeholder="e.g. The magical world of Harry Potter",
)

if st.button("✨ Generate My Blog", type="primary", use_container_width=True):
    if not topic.strip():
        st.warning("Please enter a topic first.")
    else:
        with st.spinner("Your AI crew is researching and writing..."):
            try:
                inputs = {
                    "topic": topic.strip(),
                    "current_year": str(datetime.now().year),
                }

                BlogWritingCrew().crew().kickoff(inputs=inputs)

                blog_path = PROJECT_DIR / "blog.md"

                if blog_path.exists():
                    blog_content = blog_path.read_text(encoding="utf-8")
                    st.success("Your blog is ready!")
                    st.markdown(blog_content)

                    st.download_button(
                        "⬇️ Download Your Blog",
                        data=blog_content,
                        file_name="generated_blog.md",
                        mime="text/markdown",
                        use_container_width=True,
                    )
                else:
                    st.warning(
                        "The crew finished, but blog.md was not found. "
                        "Check your project output configuration."
                    )

            except Exception as error:
                st.error("Something went wrong while generating your blog.")
                st.exception(error)
