import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# -------------------------
# Load company names from CSV
# -------------------------
def load_names_from_csv(csv_path):
    df = pd.read_csv(csv_path)
    names = df["Name"].dropna().tolist()
    return names


# -------------------------
# Cluster similar names
# -------------------------
def cluster_similar_names(names, threshold=0.85):
    model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

    embeddings = model.encode(names, convert_to_numpy=True)
    similarity_matrix = cosine_similarity(embeddings)

    visited = set()
    clusters = []

    for i in range(len(names)):
        if i in visited:
            continue

        cluster = [names[i]]
        visited.add(i)

        for j in range(i + 1, len(names)):
            if j in visited:
                continue

            if similarity_matrix[i][j] >= threshold:
                cluster.append(names[j])
                visited.add(j)

        if len(cluster) > 1:
            clusters.append(cluster)

    return clusters


# -------------------------
# Main
# -------------------------
if __name__ == "__main__":
    csv_path = "companies.csv"  # ← غيّر الاسم حسب ملفك
    
    print("Loading names from CSV...")
    names = load_names_from_csv(csv_path)

    print(f"Total names: {len(names)}")
    print("Clustering similar names...")

    clusters = cluster_similar_names(names)

    for idx, cluster in enumerate(clusters, 1):
        print(f"\n=== Cluster {idx} ===")
        for name in cluster:
            print("- " + name)
