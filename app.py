import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer, util

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Product Recommendation System",
    layout="wide"
)

st.title("🛒 Product Recommendation System")
st.write("AI-based semantic product recommendation")

# ---------------- DATASET SELECTION ----------------
dataset_option = st.selectbox(
    "Select Dataset",
    ["Product Dataset.csv", "sample-data.csv"]
)

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data(file_name):
    df = pd.read_csv(file_name, encoding="latin1")
    df.columns = df.columns.str.lower().str.strip()
    return df

df = load_data(dataset_option)

st.write("📄 Dataset Columns:", list(df.columns))

# ---------------- COLUMN AUTO-DETECTION ----------------
def detect_columns(df):
    name_candidates = ['name', 'product_name', 'title']
    desc_candidates = ['description', 'desc', 'details', 'product_description']

    name_col = next((c for c in name_candidates if c in df.columns), None)
    desc_col = next((c for c in desc_candidates if c in df.columns), None)

    return name_col, desc_col

name_col, desc_col = detect_columns(df)

if name_col is None or desc_col is None:
    st.error("❌ Required columns not found in dataset.")
    st.stop()

df = df[[name_col, desc_col]].dropna()
df['combined'] = df[name_col] + " " + df[desc_col]

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model_and_embeddings(texts):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(texts, convert_to_tensor=True)
    return model, embeddings

model, embeddings = load_model_and_embeddings(df['combined'].tolist())

# ---------------- RECOMMEND FUNCTION ----------------
def recommend_products(query, model, embeddings, df, top_n=5):
    query_embedding = model.encode(query, convert_to_tensor=True)
    scores = util.cos_sim(query_embedding, embeddings)[0]
    top_indices = scores.argsort(descending=True)[:top_n]
    return df.iloc[top_indices.cpu().numpy()]

# ---------------- UI ----------------
query = st.text_input("🔍 Enter your product search query")

if st.button("Recommend"):
    if not query.strip():
        st.warning("Please enter a search query.")
    else:
        results = recommend_products(query, model, embeddings, df)
        st.subheader("✅ Recommended Products")

        for _, row in results.iterrows():
            st.markdown(f"### {row[name_col]}")
            st.write(row[desc_col])
            st.divider()
