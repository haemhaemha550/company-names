# 🧩 Company Name Clustering Script

This project helps you **automatically detect similar or duplicate company names** using **sentence embeddings** and **cosine similarity**.
It is useful when cleaning datasets, merging records, or identifying repeated company names with small variations in spelling or wording.

---

## 🚀 Features

* Load company names from a CSV file
* Generate multilingual embeddings using **SentenceTransformer**
* Compute similarity scores using **cosine similarity**
* Cluster names that are highly similar based on a custom threshold
* Print out all discovered clusters

---

## 📁 Project Structure

```
project/
│
├── companies.csv
├── cluster_names.py
└── README.md
```

---

## 📦 Installation

### 1. Install Python dependencies

```bash
pip install pandas sentence-transformers scikit-learn
```

---

## 📄 CSV File Format

Your CSV must contain a column named **Name**, for example:

| Name                |
| ------------------- |
| Apple Inc           |
| Apple Corporation   |
| Samsung Electronics |
| Sam Sung Co         |

Save the file as:

```
companies.csv
```

(You can rename it, but update the path in the script.)

---

## ▶️ How to Run

In your terminal:

```bash
python cluster_names.py
```

---

## ⚙️ Configuration

### Similarity Threshold

By default:

```python
threshold = 0.85
```

You can adjust this in the call:

```python
clusters = cluster_similar_names(names, threshold=0.80)
```

A **higher threshold** → fewer, stricter clusters.
A **lower threshold** → more clusters with looser matching.

---

## 🔍 Example Output

```
Loading names from CSV...
Total names: 120
Clustering similar names...

=== Cluster 1 ===
- Apple Inc
- Apple Corporation
- Apple Company

=== Cluster 2 ===
- Samsung Electronics
- Sam Sung Co
```

---

## 🧠 How It Works

1. The script loads names from CSV
2. Embeds each name using:

```
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
```

3. Computes cosine similarity between all names
4. Groups names into clusters when similarity ≥ threshold
5. Prints every cluster that contains more than one item

---

## 📝 Code Reference

Your main script:

```python
# [Code from your message included verbatim]
```

---

## 🙋‍♂️ Need Enhancements?

I can help you add:

* Export clusters to CSV
* Fast clustering (HDBSCAN / FAISS)
* Streamlit UI
* Duplicate-finder API
* Arabic-optimized models
