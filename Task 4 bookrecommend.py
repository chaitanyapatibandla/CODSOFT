import pandas as pd
import numpy as np
print("Book Genres")
print(">Fantasy")
print(">Technology")
print(">Personality Development")
print(">If you prefer Fantasy and Technology books select User1")
print(">If you prefer Fantasy and Personality Development books select User2")
print(">If you prefer Technology and Personality Development books select User3")
print(">If you prefer only Technology books select User4")
print(">If you prefer only Personality Development books select User5")

data = {
    'user_id': ['User1', 'User1', 'User2', 'User3', 'User4', 'User4', 'User5', 'User5'],
    'book_id': ['Book1', 'Book2', 'Book2', 'Book3', 'Book1', 'Book3', 'Book4', 'Book5'],
    'rating': [5, 4, 3, 4, 5, 2, 4, 1]
}

df = pd.DataFrame(data)

user_item_matrix = df.pivot(index='user_id', columns='book_id', values='rating').fillna(0)
user_similarity = np.dot(user_item_matrix, user_item_matrix.T)
user_norms = np.linalg.norm(user_item_matrix, axis=1)
user_norms[user_norms == 0] = 1  # Avoid division by zero
user_similarity /= user_norms[:, None]
user_similarity /= user_norms[None, :]

target_user = input("Enter the Reader's user's ID: ")

if target_user not in user_item_matrix.index:
    print(f"User '{target_user}' not found in the dataset.")
else:
    user_ratings = user_item_matrix.loc[target_user]
    user_predicted_ratings = np.dot(user_similarity, user_ratings)

    user_predicted_ratings[user_ratings > 0] = -1

    n_recommendations = 5
    top_book_indices = np.argsort(user_predicted_ratings)[::-1][:n_recommendations]

    top_books = user_item_matrix.columns[top_book_indices]

    print(f"Top {n_recommendations} book recommendations for {target_user}:")
    print(top_books)
    print("Book's Name")
    print("Book1-The Science of Storytelling")
    print("Book2-AI 2041")
    print("Book3-Narnia")
    print("Book4-Outliers The Story of Success ")
    print("Book5-Crush it!")
