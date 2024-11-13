# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the dataset
file_path = "C:/Users/YourUsername/Downloads/emails.csv"  # Update with your local path
data = pd.read_csv(file_path)

# Display first few rows of the dataset
print("Dataset preview:")
print(data.head())

# Check for missing values and drop any rows with missing data
data = data.dropna()

# Split the dataset into features and target variable
X = data['text']  # Assuming 'text' column has the email content
y = data['spam']  # Assuming 'spam' column is the target, where 1 = spam and 0 = not spam

# Convert text data to numerical data using TF-IDF vectorizer
tfidf = TfidfVectorizer(stop_words='english', max_features=3000)  # Limiting features for simplicity
X = tfidf.fit_transform(X).toarray()

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Support Vector Machine (SVM) classifier
svm_model = SVC(kernel='linear')  # Using a linear kernel for simplicity

# Train the model
svm_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = svm_model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
