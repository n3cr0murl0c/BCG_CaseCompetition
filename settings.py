#SKLEARN LIBS
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
#SKLEARN MODELS
from sklearn.multioutput import MultiOutputClassifier
from sklearn.linear_model import (
    LogisticRegression,
    LinearRegression
)
from sklearn.tree import (
    DecisionTreeRegressor
)
# from sklearn.
#SKLEARN TOOLS
from sklearn.model_selection import train_test_split
from sklearn.metrics import(
    mean_squared_error
)
#To save a python object into a binary file---> PICKLE RICK!
import pickle

#CrossValidation Libraries
from sklearn.model_selection import cross_val_score, KFold

from dash import (
    Dash,
    dcc,
    html,
    Input,Output,

)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go