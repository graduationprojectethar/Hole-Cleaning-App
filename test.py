import streamlit as st
import plotly.graph_objs as go
import numpy as np

# Generate some random data for the plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plotly figure
fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines', name='sin(x)'))

# Set plot title and axis labels
fig.update_layout(title='Plotly Line Plot', xaxis_title='x', yaxis_title='sin(x)')

# Render the plot using st.plotly_chart
st.plotly_chart(fig)

