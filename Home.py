import streamlit as web_ui
import plotly.express as px
import pandas as pd

web_ui.title(":violet[In Search for Happiness]😁")

df = pd.read_csv("happy.csv")

opt = [i.replace("_", " ").upper() for i in df.columns]

x_axis = web_ui.selectbox(label=":green[Select the data for the X-axis]", options=opt, key="xa")
y_axis = web_ui.selectbox(label=":green[Select the data for the Y-axis]", options=opt, key="ya")

web_ui.subheader(f':violet[{x_axis.title()} and {y_axis.title()}]')


def get_data(X_axis, Y_axis):
    x_lower = X_axis.lower()
    y_lower = Y_axis.lower()

    df.columns = [i.replace("_", " ") for i in df.columns]

    for i in df.columns:
        if x_lower == i:
            X_axis = df[i]

        if y_lower == i:
            Y_axis = df[i]

    return X_axis, Y_axis


getx, gety = get_data(x_axis, y_axis)

printCountry = df['country']

dff = pd.read_csv("happy.csv")
df_c = dff['country']
figures = px.scatter(df, x=getx, y=gety, labels={"x": x_axis, "y": y_axis},color="country")

web_ui.plotly_chart(figures)
