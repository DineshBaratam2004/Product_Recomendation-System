# 🛒 Product Recommendation System

An **AI-powered Product Recommendation System** built using **Streamlit** and **Sentence Transformers** that provides semantic-based product suggestions based on user queries.

This system understands the *meaning* of the search query (not just keywords) and recommends the most relevant products from the dataset.

---

## 🚀 Features

* 🔍 Semantic product search using **NLP**
* 🤖 Powered by **Sentence Transformers (MiniLM)**
* 📊 Supports multiple CSV datasets
* ⚡ Fast performance with **Streamlit caching**
* 🧠 Automatic column detection (product name & description)
* 🎯 Top-N product recommendations
* 💻 Simple and interactive UI

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Pandas**
* **Sentence-Transformers**
* **PyTorch**

---

## 📂 Project Structure

```
📦 Product-Recommendation-System
 ┣ 📄 app.py
 ┣ 📄 Product Dataset.csv
 ┣ 📄 sample-data.csv
 ┣ 📄 requirements.txt
 ┗ 📄 README.md
```

---

## 📊 Dataset Requirements

Your CSV file should contain at least:

* **Product Name column**
  (e.g., `name`, `product_name`, `title`)
* **Product Description column**
  (e.g., `description`, `details`, `product_description`)

The system automatically detects these columns.

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Product-Recommendation-System.git
cd Product-Recommendation-System
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 🧪 How It Works

1. Loads the selected product dataset
2. Combines product name and description
3. Generates embeddings using **MiniLM**
4. Converts user query into an embedding
5. Computes **cosine similarity**
6. Displays top recommended products

---

## 🖥️ User Interface

* Select a dataset from the dropdown
* Enter a product search query
* Click **Recommend**
* View AI-generated recommendations instantly

---

## 📌 Example Use Cases

* E-commerce product search
* Smart product discovery
* Recommendation engines
* NLP learning projects
* AI-powered search systems

---

## 🔮 Future Enhancements

* 🖼️ Product image recommendations
* ⭐ Rating-based filtering
* 🗂️ Category-based recommendations
* 🌐 Deployment on cloud platforms
* 🔐 User login and personalization

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repo and submit a pull request.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🙌 Acknowledgements

* Streamlit
* Sentence-Transformers
* Hugging Face
* Open-source community
