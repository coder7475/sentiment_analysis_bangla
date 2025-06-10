# Investigating the Impact of Sentiment Label Imbalance on Model Performance in Bangla Sentiment Analysis

## Research Problem

Sentiment analysis models often suffer from degraded performance when trained on datasets with imbalanced class distributions, where certain sentiment labels (e.g., Positive, Negative, or Neutral) dominate. In the context of the Bangla Sentiment Dataset, which includes diverse sources like newspapers, social media, and blogs, such imbalances are likely due to the real-world nature of the data (e.g., social media may skew Negative due to criticism). This issue is particularly pronounced in low-resource languages like Bangla, where limited labeled data exacerbates the challenge, yet little research has explored effective mitigation strategies for Bangla sentiment analysis.

## Research Aim

To investigate the impact of class imbalance on the performance of sentiment classification models using the Bangla Sentiment Dataset and to evaluate the effectiveness of techniques such as oversampling, undersampling, and weighted loss functions in improving model accuracy and robustness across diverse Bangla text sources.

## Research Question

How does class imbalance in the Bangla Sentiment Dataset affect sentiment classification performance, and can techniques like oversampling (e.g., SMOTE), undersampling, or weighted loss functions mitigate these effects to improve model accuracy and generalization?



### Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)

- [Contributing](#contributing)
- [License](#license)

### Installation

To set up the project, clone the repository and run the `folder_structure_setup.sh` script to create the necessary directories and files.

To install virtual environment:

```bash
python3 -m venv venv
```

To activate the Python virtual environment, navigate to the project directory in your terminal and run the following command:

```bash
source venv/bin/activate
export PYTHONPATH=~/your_path_to_directory/directory_name
```

To install all packages from requirements.txt, run the following command:

```bash
pip install -e .
```

### Usage

First run the the setup python file to initialize:

```bash
python3 setup.py
```

### Directory Structure

```bash
├── data-source
├── src
│   ├── __init__.py
│   ├── components
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_monitoring.py
│   │   └── model_trainer.py
│   ├── exception.py
│   ├── logger.py
│   ├── pipelines
│   │   ├── __init__.py
│   │   ├── prediction_pipeline.py
│   │   └── training_pipeline.py
│   └── utils.py
├── .gitignore
├── main.py
├── app.py
├── EDA.ipynb
├── README.md
├── requirements.txt
├── folder_structure_setup.sh
├── test-logging-integration.py
└── test-request.py
```
