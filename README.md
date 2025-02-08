# Document Classification

This is a simple sample for me to use a zero-shot classification model to classify the content of PDF documents into predefined categories.

For this project, we will use the [mDeBERTa-v3-base-xnli-multilingual-nli-2mil7 model](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7) from Hugging Face.

## Requirements

To install the required dependencies, run:

```sh
pip install -r requirements.txt
```

Be sure that you have installed Pytorch on your system.

## Usage
1. Place your PDF documents in the docs folder.
2. Run the zeroshotclassificiation.py script:

```sh
python zeroshotclassificiation.py
```

The script will read all PDF files in the docs folder, extract their text, and classify the content into the following categories:

- Sport
- Politik
- Wirtschaft
- Kultur
- Wissenschaft
- Technik
- Gesundheit
- Reisen
- Essen

You can adjust the labels accordingly to your use case as needed.

## Script Details
The main script is zeroshotclassificiation.py. It performs the following steps:

1. Uses the transformers library to load a zero-shot classification model.
2. Reads all PDF files in the docs folder using pypdf.
3. Extracts text from each PDF file.
4. Classifies the extracted text into predefined categories.
5. Prints the classification results.

## License
This project is licensed under the MIT License. See the LICENSE file for details.