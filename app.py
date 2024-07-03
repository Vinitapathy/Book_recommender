import streamlit as st
import pandas as pd
import pickle as pkl
import numpy as np

def MyBG_colour(wch_colour):
	my_colour=f"<style>.stApp{{background-color:{wch_colour};}}</style>"
	st.markdown(my_colour,unsafe_allow_html=True)

MyBG_colour("orange")

Ratings=pd.read_pickle('ratings.pkl')
Similarity=pd.read_pickle('similarity.pkl')
final_df=pd.read_pickle('final_df.pkl')
popular=pd.read_pickle('popular.pkl')
books=pd.read_pickle('Books.pkl')

st.title("Book recommender system")
with st.sidebar:
	st.title("Popularbooks:")

for index,row in popular.iterrows():
	with st.sidebar:	
		st.write(row["Book-Title"])
		st.write("by",row["Book-Author"])
		st.image(row["Image-URL-M"])

def recommend(book_name):
	index=np.where(Ratings.index==book_name)[0][0]
	similar_items=sorted(list(enumerate(Similarity[index])),key=lambda x:x[1],reverse=True)[1:6]
	data=[]
	for i in similar_items[1:6]:
		item = []
		temp_df = books[books['Book-Title'] == Ratings.index[i[0]]]
		item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
		item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
		item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

		data.append(item)
	return data
	

	


book_name=st.selectbox("Type a Book name",final_df['Book-Title'].unique())
if st.button("Get recommendation"):
	recommendation=recommend(book_name)
	for i in recommendation:
		st.write(i[0],"BY",i[1])
		st.image(i[2])
		
	

	
		

	














