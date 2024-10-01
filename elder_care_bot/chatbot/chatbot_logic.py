import nltk  
from nltk.tokenize import word_tokenize  
from nltk.corpus import stopwords  
from sklearn.feature_extraction.text import TfidfVectorizer  
from sklearn.metrics.pairwise import cosine_similarity  
import numpy as np  
from .models import Disease, BlogPost  

nltk.download('punkt')  
nltk.download('stopwords')  

stop_words = set(stopwords.words('russian'))  

def preprocess_text(text):  
    tokens = word_tokenize(text.lower())  
    return ' '.join([token for token in tokens if token not in stop_words])  

def get_most_similar_response(user_input):  
    diseases = Disease.objects.all()  
    blog_posts = BlogPost.objects.all()  

    corpus = [preprocess_text(d.description + ' ' + d.care_instructions) for d in diseases] + \
             [preprocess_text(p.content) for p in blog_posts]  
    
    vectorizer = TfidfVectorizer()  
    tfidf_matrix = vectorizer.fit_transform(corpus + [preprocess_text(user_input)])  
    
    cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()  
    most_similar_idx = np.argmax(cosine_similarities)  
    
    if most_similar_idx < len(diseases):  
        return f"Информация о заболевании {diseases[most_similar_idx].name}:\n{diseases[most_similar_idx].description}\n\nРекомендации по уходу:\n{diseases[most_similar_idx].care_instructions}"  
    else:  
        blog_post = blog_posts[most_similar_idx - len(diseases)]  
        return f"Из нашего блога:\n{blog_post.title}\n\n{blog_post.content[:300]}..."  

def process_user_input(user_input):  
    if 'привет' in user_input.lower():  
        return "Здравствуйте! Я чат-бот, который может помочь вам с информацией о старческих заболеваниях и уходе за пожилыми людьми. Чем я могу вам помочь?"  
    elif 'пока' in user_input.lower():  
        return "До свидания! Если у вас возникнут еще вопросы, обращайтесь."  
    else:  
        return get_most_similar_response(user_input)