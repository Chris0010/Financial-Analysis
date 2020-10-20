import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from copy import copy
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go

# import stock data
stock_file = 'stock.csv'
stocks_df = pd.read_csv(stock_file)

def show_plot(df, plot_title):
    df.plot(x='Date', figsize=(15, 7), linewidth=3, title=plot_title)
    plt.grid()
    plt.show()

dates = pd.DataFrame(stocks_df.iloc[:, 0])
stocks = stocks_df.iloc[:, 1:]
stock_names = stocks_df.columns[1:]
sc = StandardScaler()
stocks = pd.DataFrame(sc.fit_transform(stocks), columns=stock_names)
