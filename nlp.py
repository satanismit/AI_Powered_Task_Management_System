import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# nltk.download('punkt_tab')
# nltk.download('punkt')
# print("Punkt tokenizer downloaded.")
# nltk.download('stopwords')
# print("Stopwords downloaded.")
# nltk.download('wordnet')
# print("WordNet downloaded.")


# Load the dataset
df = pd.read_csv('F:\\Internship\\AI powered task management system\\task_management_dataset.csv')


# Initialize lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    # 1. Lowercase
    text = text.lower()
    
    # 2. Remove special characters and digits
    text = re.sub(r'[^a-z\s]', '', text)
    
    # 3. Tokenize
    tokens = word_tokenize(text)
    
    # 4. Remove stopwords
    tokens = [word for word in tokens if word not in stop_words]
    
    # 5. Lemmatize
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    # Return processed text
    return ' '.join(lemmatized_tokens)


df['Processed_Task'] = df['Task'].apply(preprocess_text)
df['Processed_Task'].head(5)

# Save the processed dataset
df.to_csv('processed_task_management_dataset.csv', index=False)

