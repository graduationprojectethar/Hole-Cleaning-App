import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def main():
    st.title('Matplotlib Example in Streamlit')

    # Generate some sample data
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Create a plot
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Sine Wave Plot')

    # Display the plot using Streamlit
    st.pyplot(fig)

if __name__ == "__main__":
    main()
