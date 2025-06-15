# Preprocessed Bangla Sentiment Dataset

This folder contains all the necessary files for training and evaluating sentiment classification models using Bangla text data.

## Contents
- **`cleaned_dataset.csv`**: Original dataset with an additional cleaned text column (`Tense_Cleaned`).
- **`tfidf_matrix.npz`**: Full sparse TF-IDF matrix for all samples.
- **`tfidf_train.npz`**, **`tfidf_val.npz`**, **`tfidf_test.npz`**: Sparse TF-IDF matrices for the training, validation, and test sets respectively.
- **`labels_train.csv`**, **`labels_val.csv`**, **`labels_test.csv`**: Sentiment labels corresponding to each data split.
- **`bert_input_ids.npy`**: Tokenized input IDs generated using the `BanglaBERT` tokenizer.
- **`bert_attention_masks.npy`** *(optional if generated)*: Attention masks for BERT inputs.
- **`text_train.csv`**, **`text_val.csv`**, **`text_test.csv`**: Cleaned Bangla text for each split.
- **`split_indices.csv`**: Index mapping of samples to their respective dataset split (Train/Val/Test).

## Notes
- Labels are encoded as: `0 = Negative`, `1 = Positive`, `2 = Neutral`
- All text has been preprocessed using BNLP and regex cleaning techniques.
- BERT tokens are padded to a maximum length of 128.
- TF-IDF features are saved in SciPy's `.npz` sparse format for efficient loading.
