import streamlit as st
from apps.retriever import (
    load_faiss_index,
    load_metadata,
    embed_query,
    search_documents,
    retrieve_context
)


def load_css():
    with open("assests/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style",
            unsafe_allow_html=True
        )

load_css()      





@st.cache_resource
def load_resources():
    index = load_faiss_index()
    metadata = load_metadata()
    return index, metadata


index, metadata = load_resources()

from apps.gene import gene_ans

st.set_page_config(
    page_title="PatchContext",
    page_icon="🤖",
    layout="wide"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.markdown("---")

    st.write("Repository")

    st.success("FastAPI")

    st.markdown("---")

    st.write("Powered By")

    st.info("Gemini + FAISS")

st.markdown("""
<div class="header-card">

<h1>🤖 PatchContext</h1>

<p>
AI-Powered GitHub Repository Assistant
</p>

<p>
Chat with commits, pull requests, issues and repository history.
</p>

</div>
""", unsafe_allow_html=True)


 #Repo Statistics 

commit_count = sum(1 for doc in metadata if doc["type"] == "commit")

pr_count = sum(1 for doc in metadata if doc["type"] == "pull_request")

issue_count = sum(1 for doc in metadata if doc["type"] == "issue")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📜 Commits", commit_count)

with col2:
    st.metric("🔀 Pull Requests", pr_count)

with col3:
    st.metric("🐞 Issues", issue_count)



st.markdown('## Example Question')

col1,col2= st.columns(2)

with col1:
    st.button("show recent commits")
    st.session_state.example_question="What changed in the latest release?"

    
    if st.button("🚀 Latest release changes"):
        st.session_state.example_question = "What changed in the latest release?"

with col2:

    if st.button("🔐 Authentication changes"):
        st.session_state.example_question = "Show authentication related commits"

    if st.button("📚 Documentation updates"):
        st.session_state.example_question = "Summarize documentation updates"










for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
    
question  = st.chat_input("ask something about the repo..")

if question:
        st.session_state.messages.append({
            "role":"user",
            "content":question
        })
        
        with st.chat_message("user"):
            st.markdown(question)
        
        with st.chat_message("assistant"):
            with st.spinner("Searching Repo..."):




                query_vector = embed_query(question)

            

                distances, indices = search_documents(
                    index,
                    query_vector,
                    top_k=5
                )

                docs = retrieve_context(indices, metadata)

                answer = gene_ans(question, docs)

                st.markdown(answer)  

            with st.expander("Retrieved Documents"):

               for doc in docs:

                st.markdown(f"### {doc["title"]}")

                
                st.write(f"{doc['author']}")
                st.write(f"{doc['date']}")
                st.markdown(f"[open on Github]({doc['url']})")
                st.divider()

                

            st.session_state.messages.append({
                "role":"assistant",
                "content": answer
            })    




        if st.button("Clear Chat"):
            st.session_state.message = []
            st.rerun()
 

        st.markdown("---")
        st.caption("PatchContext v1.0 | Biult with streamlit - Gemini - FAISS - Lnagchain")