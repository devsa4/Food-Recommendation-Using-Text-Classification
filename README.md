# Food-Recommendation-Using-Text-Classification
Restaurants often struggle to accurately predict food demand, leading to overstocking or shortages. This can result in increased costs and customer dissatisfaction. make on paragraph problem statement. In the digital age, the restaurant industry heavily relies on online reviews to understand customer sentiments and preferences, but the sheer volume and complexity of user-generated content pose significant challenges for extracting actionable insights. This project aims to leverage advanced text classification techniques to analyse restaurant reviews, accurately identifying sentiments and extracting mentions of popular food dishes. 
Text classification is the task of assigning one or more categories to a given piece of text from a larger set of possible categories
The code for analyzing restaurant reviews and providing food dish recommendations is designed with a modular approach, leveraging several key components and libraries to achieve its goals. Here's an overview of the architectural design:
1. Data Ingestion and Preprocessing
•	Data Loading: The code starts by loading a CSV dataset containing restaurant reviews using pandas. The user is prompted to input the filename and specify the columns for reviews and ratings.
•	Text Cleaning: A clean_text function is defined to preprocess the review text. This includes converting text to lowercase, removing non-alphabet characters, and filtering out stopwords using nltk.
2. Sentiment Analysis
•	Data Splitting: The dataset is split into training and testing sets using train_test_split from scikit-learn.
•	Text Vectorization: The review text is converted into numerical features using the TF-IDF vectorizer.
•	Model Training and Evaluation: A Multinomial Naive Bayes model is trained on the training data, and its performance is evaluated on the testing data. The accuracy of the model is printed.
3. Food Item Identification and Recommendation
•	Food Item List: A predefined list of common Indian food dishes is used to filter the review text and identify mentioned food items.
•	Food Item Extraction: A filter_food_items function is defined to extract and store food items from the reviews.
•	Frequency Analysis: Positive reviews are filtered, and the frequency of each food item is counted using the Counter class from the collections module.
•	Top Recommendations: The top 10 food dish recommendations based on positive reviews are printed.
![image](https://github.com/user-attachments/assets/19ca5a42-5ec7-4f0a-9ff0-8eca4706811d)

The results of this analysis demonstrate the effectiveness of using Natural Language Processing (NLP) and machine learning techniques to classify sentiments in restaurant reviews and identify popular food dishes. 
The identification of food items from positive reviews provided insightful recommendations for popular dishes. The predefined list of common Indian food items allowed for accurate filtering and counting of mentions in the reviews. 
It is important to consider that the dataset and predefined food list used in this analysis might have influenced the outcomes. For more comprehensive and generalized results, a larger and more diverse dataset, along with an expanded list of food items, could be utilized. Additionally, refining the text cleaning and feature extraction processes could further enhance the model's performance and accuracy.
