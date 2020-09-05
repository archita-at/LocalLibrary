from .models import Book, Author, Genre
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def createDataFrames():
    """Create dataframes"""
    #generate dataframes of required tables
    df_author = pd.DataFrame.from_records(
        Author.objects.all().values_list('id','first_name','last_name'), columns = ['id','first_name','last_name'])
    df_book = pd.DataFrame.from_records(
        Book.objects.all().values_list('id','title','author_id','genre'), columns = ['id','title','author_id','genre_id'])
    df_genre = pd.DataFrame.from_records(
        Genre.objects.all().values_list('id','name'), columns = ['id','name'])
    return df_author, df_book, df_genre

#selelct features for similarity calculation
#features = ['author','genre']

author_dict = {}
genre_dict = {}

# Helper Functions
def get_title_from_index(df_book, index):
    return df_book[df_book.index == index]["title"].values[0]

def get_index_from_title(df, title):
    return df[df.title == title]["id"].values[0]

#dictionary of id and name of author
def create_author_dict(df_author):
    global author_dict
    for index, row in df_author.iterrows():
        author_dict[row["id"]] = row["first_name"]+" "+row["last_name"]
    return author_dict

#dictionary of id and name of genre
def create_genre_dict(df_genre):
    global genre_dict
    for index, row in df_genre.iterrows():
        genre_dict[row["id"]] = row["name"]
    return genre_dict

def combine_features(row):
    try:
        return row['author']+" "+row['genre']
    except:
        print ("Error:", row)
        
def prepare_dataframe(df_book):
    """Function to prepare the dataframes"""
    df = pd.DataFrame()
    df["title"] = df_book["title"].unique()
    df["id"] = range(0,df.shape[0])
    
    global author_dict
    author_list = []
    for i in range(0,df.shape[0]):
        author_list.append(author_dict[df_book[df["title"][i] == df_book["title"]]["author_id"].unique()[0]])
    df["author"] = author_list
    
    global genre_dict
    genre_list = []
    for i in range(0,df.shape[0]):
        genre_id_list=[]
        genre_id_list = df_book[df["title"][i] == df_book["title"]]["genre_id"].to_list()
        genre = []
        for genre_id in genre_id_list:
            genre.append(genre_dict[genre_id])
        genre_list.append(",".join(genre))
    df["genre"] = genre_list
    
    df['combined_features'] = df.apply(combine_features, axis=1) #add combined features
    return df

def calculate_similarity(df_book):
    df = prepare_dataframe(df_book)
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df["combined_features"])
    cosine_sim = cosine_similarity(count_matrix)
    return df, cosine_sim

def get_recommendations(book_name):
    df_author, df_book, df_genre = createDataFrames()
    author_dict = create_author_dict(df_author)
    genre_dict = create_genre_dict(df_genre)
    
    df, cosine_sim = calculate_similarity(df_book)
    book_index = get_index_from_title(df, book_name)
    similar_books = list(enumerate(cosine_sim[book_index]))
    sorted_similar_books = sorted(similar_books,key=lambda x:x[1],reverse=True)
    
    recommendations = []
    for book in sorted_similar_books[0:3]:
        search_title = get_title_from_index(df, book[0])
        recommendations.append(Book.objects.get(title = search_title))
    
    return recommendations