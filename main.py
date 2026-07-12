from apps.git_load import fetch_commit_history
from apps.git_load import connect_git_api
from utils.file import save_raw_data
from apps.git_load import fetch_pull_req
from apps.git_load import fetch_issue_threads
from apps.process import load_json
from apps.process import clean_commit_data
from apps.process import clean_pull_request_data
from apps.process import clean_issue_data
from apps.process import *
from utils.file import save_raw_data
from  apps.embedding import load_docu
from apps.embedding import *
from apps.vector import *
from apps.retriever import load_faiss_index,load_metadata,embed_query,search_documents,retrieve_context
from apps.gene import gene_ans, build_prompt,load_llm
from apps.embedding import generate_embeddings



def main():
    '''session = connect_git_api()

    response = session.get("https://api.github.com/repos/fastapi/fastapi")

    print(response.status_code)'''

    '''commits = fetch_commit_history()

    save_raw_data(commits,"data/raw/commits.json")

    print("commits saved successfully")'''

    '''prs = fetch_pull_req()

    save_raw_data(prs,"data/raw/pull_requests.json")

    print("Pull Requests Saved")'''

    '''issues = fetch_issue_threads()
    save_raw_data(issues,"data/raw/issues.json")
    print("Issues saved successfully")'''

    '''commits = fetch_commit_history()
    save_raw_data(commits,"data/raw/commits.json")

    print(f"Downloaded{len(commits)} commits")'''


    '''prs = load_json("data/raw/pull_requests.json")
    cleaned_prs = clean_pull_request_data(prs)
    
    print(cleaned_prs[0])'''

    '''issues = load_json("data/raw/issues.json")
    cleaned = clean_issue_data(issues)

    print(cleaned[0])'''

    '''commits = load_json("data/raw/commits.json")
    prs = load_json("data/raw/pull_requests.json")
    issues = load_json("data/raw/issues.json")

    clean_commits = clean_commit_data(commits)
    clean_prs = clean_pull_request_data(prs)
    clean_issues = clean_issue_data(issues)

    documents = merge_docu(
        clean_commits,
        clean_prs,
        clean_issues
    )

    save_raw_data(documents, "data/processed/documents.json")

    print("Total Documents :", len(documents))'''



    '''documents = load_docu("data/processed/documents.json")

    print("Total Documents:", len(documents))

    model = load_embedding_model()

    vector = create_embedding(model, documents[0])

    print("Embedding Dimension:", len(vector))
    print(vector[:10]) ''' 

    documents = load_docu(
        "data/processed/documents.json"
    )
    documents = documents[:100]

    embeddings = generate_embeddings(documents)

    save_embeddings(embeddings)

    embeddings = load_embeddings()

    vectors, metadata = extract_vectors(
        embeddings
    )
    save_metadata(metadata)

    print(vectors.shape)

    index = create_faiss_index(
        vectors.shape[1]
    )

    add_vector(index, vectors)

    save_index(index)

    print("FAISS Index Created")


    '''index = load_faiss_index()

    metadata = load_metadata()

    question = input("Ask Question: ")

    query_vector = embed_query(question)

    distances, indices = search_documents(
        index,
        query_vector,
        top_k=5
    )
    if len(indices)==0:
        print("item not found")
        return
    
   


    docs = retrieve_context(
        [indices],
        metadata
    )

    print()

    for doc in docs:

        print("="*80)

        print(doc["title"])

        print()

        print(doc["content"])

        print()'''
    


    '''print("=" * 70)
    print("PatchContext - FastAPI Repository RAG")
    print("=" * 70)

    # Load FAISS index
    index = load_faiss_index()

    # Load metadata
    metadata = load_metadata()

    while True:

        question = input("\nAsk Question (type 'exit' to quit): ")

        if question.lower() == "exit":
            print("Goodbye!")
            break

        # Convert question into embedding
        query_vector = embed_query(question)

        # Search similar documents
        distances, indices = search_documents(
            index=index,
            query_vector=query_vector,
            top_k=5
        )

        # No documents found
        if len(indices) == 0:
            print("\nNo relevant documents found.\n")
            continue

        # Retrieve metadata
        docs = retrieve_context(indices, metadata)

        print("\nRetrieved Documents\n")

        for i, doc in enumerate(docs, start=1):

            print("=" * 80)

            print(f"Document {i}")

            print(f"Type   : {doc.get('type','Unknown')}")

            print(f"Title  : {doc.get('title','')}")

            print()

            print(doc.get("content",""))

            print()

        # Generate final answer
        answer = gene_ans(question, docs)

        print("\n" + "=" * 80)
        print("Gemini Answer")
        print("=" * 80)

        print(answer)'''

    commits = load_json("data/raw/commits.json")
    pull_requests = load_json("data/raw/pull_requests.json")
    issues = load_json("data/raw/issues.json")

    # Clean the data
    cleaned_commits = clean_commit_data(commits)
    cleaned_prs = clean_pull_request_data(pull_requests)
    cleaned_issues = clean_issue_data(issues)

    # Merge into one document list
    documents = merge_docu(
        cleaned_commits,
        cleaned_prs,
        cleaned_issues
    )

    print(f"Total Documents: {len(documents)}")

    # Save processed documents
    save_raw_data(
        documents,
        "data/processed/documents.json"
    )

    print("documents.json regenerated successfully!")


    '''documents = load_json("data/processed/documents.json")

    embeddings = generate_embeddings(documents)

    save_embeddings(
        embeddings,
        "data/embeddings/embeddings.pkl"
    )

    print("Embeddings saved successfully!")'''






if __name__ == "__main__":
    main()
