import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import make_s_curve
from sklearn.manifold import TSNE
import umap.umap_ as umap
from mpl_toolkits.mplot3d import Axes3D
import random


def random_n(min_value=0, max_value=1000):
    return random.randint(min_value, max_value)

uploaded_file = st.file_uploader("Φορτώστε ένα αρχείο CSV ή Excel", type=["csv", "xlsx"])
if uploaded_file is not None:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file, engine='openpyxl')
        st.write(df)
        
        # Display a loading warning
        with st.spinner('Please wait while the plots are being generated...'):
            trows= len(df)
            
            X, color = make_s_curve(n_samples=trows)

            # Apply PCA
            pca = PCA(n_components=2)
            pca_3d = pca.fit_transform(df.iloc[:,:-1])

            # Apply t-SNE
            tsne = TSNE(n_components=2, random_state=42)
            tsne_3d = tsne.fit_transform(df.iloc[:,:-1])

            # Apply UMAP
            reducer = umap.UMAP(random_state=42)
            umap_3d = reducer.fit_transform(df.iloc[:,:-1])

            # Points for the GREEN line
            green_pointC = trows-1
            green_pointD = trows-1

            # Calculate the absolute difference between all color values
            color_diffs = np.abs(color[:, None] - color)

            # Set the diagonal to a large value to ignore self-differences
            np.fill_diagonal(color_diffs, np.inf)

            # Find the indices of the two points with the smallest color difference
            red_pointA, red_pointB = np.unravel_index(np.argmin(color_diffs), color_diffs.shape)

            # Plot the results
            fig, axs = plt.subplots(3, 1, figsize=(10, 50))

    

            # PCA
            axs[0] = fig.add_subplot(311)
            axs[0].scatter(pca_3d[:, 0], pca_3d[:, 1], c=color)
            axs[0].plot(*zip(pca_3d[green_pointC], pca_3d[green_pointD]), color='green')  
            axs[0].plot(*zip(pca_3d[red_pointA], pca_3d[red_pointB]), color='red')  
            axs[0].set_title('PCA')

            # t-SNE
            axs[1] = fig.add_subplot(312)
            axs[1].scatter(tsne_3d[:, 0], tsne_3d[:, 1], c=color)
            axs[1].plot(*zip(tsne_3d[green_pointC], tsne_3d[green_pointD]), color='green')  
            axs[1].plot(*zip(tsne_3d[red_pointA], tsne_3d[red_pointB]), color='red')  
            axs[1].set_title('t-SNE')


            # UMAP
            axs[2] = fig.add_subplot(313)
            axs[2].scatter(umap_3d[:, 0], umap_3d[:, 1], c=color)
            axs[2].plot(*zip(umap_3d[green_pointC], umap_3d[green_pointD]), color='green')  
            axs[2].plot(*zip(umap_3d[red_pointA], umap_3d[red_pointB]), color='red')  
            axs[2].set_title('UMAP')

            plt.tight_layout()
            st.pyplot(fig)
            
      