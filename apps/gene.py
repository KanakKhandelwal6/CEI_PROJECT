from langchain_google_genai import ChatGoogleGenerativeAI
from confi import GOOGLE_API_KEY

def load_llm():
    llm = ChatGoogleGenerativeAI(
        model = "gemini-2.5-flash",
        google_api_key = GOOGLE_API_KEY,
        temperature = 0
    )
    return llm


def build_prompt(question, documents):

    context = ""

    for i, doc in enumerate(documents, start=1):

        context += f"""
Document {i}

Type: {doc.get('type','')}

Title: {doc.get('title','')}

Author:
{doc.get('author','Unknown')}

Date:
{doc.get('date','Unknown')}

Content:
{doc.get('content','')}

URL:
{doc.get('url','')}
"""



    prompt = f"""
You are PatchContext, an AI assistant that answers questions about GitHub repositories.

You are given repository information such as commits, pull requests, and issues.

Your rules:

1. Answer ONLY using the provided repository context.

2. Do NOT use outside knowledge.

3. Summarize the retrieved information instead of copying it.

4. If multiple commits discuss the same topic,
combine them into one explanation.

5. Mention important commit titles when useful.

6. Mention authors only if relevant.

7. Keep answers concise and professional.

8. If the repository does not contain the answer,
reply exactly:

"I couldn't find relevant information in the repository."

Repository Context

{context}

Question

{question}

Answer:
"""

    return prompt


def gene_ans(question,documents):
    llm = load_llm()
    prompt = build_prompt(question,documents)
    response = llm.invoke(prompt)

    return response.content