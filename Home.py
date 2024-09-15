import plotly.express as px
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans, DBSCAN
import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="./ionio.png",
    layout='wide'
)

st.write("# Καλώς ήρθατε στην εφαρμογή οπτικοποίησης και ανάλυσης δεδομένων :bar_chart:")
st.title("Υλοποίηση 2D & 3D οπτικοποίησεων δεδομένων βασισμένες στους αλγορίθμους PCA & UMAP")
st.write('\n')
st.write('\n')
st.write('\n')
st.write("Σε αυτή την εφαρμογή χρησιμοποιώ τον αλγόριθμο **Random Forest** and **Extra Trees** "
         "ως 'Feature selection' αλγορίθμους για να με βοηθήσουν να μικρύνω το μέγεθος του dataset")
st.write("**Made By: Σούρλας Ιωάννης Π2016102**")
st.image("ionio.png", caption="Ionian University department of Informatics")

st.sidebar.success("Select a function above.")
















