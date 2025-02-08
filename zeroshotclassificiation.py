from transformers import pipeline
from pypdf import PdfReader
import glob, os

classifier = pipeline("zero-shot-classification", model="MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7")

def get_all_files_from_folder(subfolder="docs"):
    all_texts = []
    file_names = glob.glob(os.path.join(subfolder, "**", "*.pdf"), recursive=True)
    for file_name in file_names:
        print(f"Reading file: {file_name}")
        reader = PdfReader(file_name)
        page_texts = [page.extract_text() for page in reader.pages]
        all_texts.append({ "file_name" : file_name, "text" : " ".join(page_texts)})
        print("File read successfully")
    return all_texts

labels = ["Sport", "Politik", "Wirtschaft", "Kultur", "Wissenschaft", "Technik", "Gesundheit", "Reisen", "Essen"]

all_texts = get_all_files_from_folder()
for entry in all_texts:
    text = entry["text"]
    filename = entry["file_name"]
    result = classifier(text, labels)

    print(f"File: {filename}")
    print("Klassifikationen:")
    for label, score in zip(result["labels"], result["scores"]):
        print(f"{label}: {score:.3f}")

    print("\n-----------------------------------\n")
