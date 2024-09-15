import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
import plotly.express as px
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA

@st.cache_data
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')

def impPlot(imp, name):
    figure = px.bar(imp,
                    x=imp.values,
                    y=imp.keys(), labels = {'x':'Importance Value', 'index':'Columns'},
                    text=np.round(imp.values, 2),
                    title=name + ' Feature Selection Plot',
                    width=1000, height=600)
    figure.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })
    st.plotly_chart(figure)


def randomForest(x, y):
    model = RandomForestClassifier()
    model.fit(x, y)
    feat_importances = pd.Series(model.feature_importances_, index=x.columns).sort_values(ascending=False)
    st.subheader('Random Forest Classifier:')
    impPlot(feat_importances, 'Random Forest Classifier')
    #st.write(feat_importances)
    st.write('\n')
    st.write(feat_importances)
    st.write('\n')


def extraTress(x, y):
    model = ExtraTreesClassifier()
    model.fit(x, y)
    feat_importances = pd.Series(model.feature_importances_, index=x.columns).sort_values(ascending=False)
    st.subheader('Extra Trees Classifier:')
    impPlot(feat_importances, 'Extra Trees Classifier')
    st.write('\n')
    st.write(feat_importances)
    st.write('\n')




uploaded_file = st.file_uploader("Φορτώστε ένα αρχείο CSV ή Excel", type=["csv", "xlsx"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(5))
    x = df.iloc[:, :-1]  # Using all column except for the last column as X
    y = df.iloc[:, -1]  # Selecting the last column as Y
    randomForest(x, y)
    extraTress(x, y)
    
    
    model = RandomForestClassifier()
    model.fit(x, y)
    feat_importances1 = pd.Series(model.feature_importances_, index=x.columns).sort_values(ascending=False)
    
    model = ExtraTreesClassifier()
    model.fit(x, y)
    feat_importances2 = pd.Series(model.feature_importances_, index=x.columns).sort_values(ascending=False)
    
    csv = convert_df(feat_importances1)
    st.write(" Παρακάτω μπορείτε να κατεβάσετε τα δεδομένα μετά την επεξεργασία του αλγορίθμου Random Forest")
    st.download_button(
    "Download Random Forest results",
    csv,
    "random_forest.csv",
    "text/csv",
    key='download-csv'
    )
    csv = convert_df(feat_importances2)
    st.write(" Παρακάτω μπορείτε να κατεβάσετε τα δεδομένα μετά την επεξεργασία του αλγορίθμου Extra Trees")
    st.download_button(
    "Download Extra trees results",
    csv,
    "extra_trees.csv",
    "text/csv",
    key='download-csv2'
    )
else:
    st.info('Awaiting for CSV file to be uploaded.')
  
        
        
