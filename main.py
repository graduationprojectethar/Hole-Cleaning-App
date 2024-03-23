import streamlit as st
import pandas as pd
table=pd.DataFrame({"column 1":[1,2,3,4],"column 2":[1,2,3,4]})
hide_all = """
<style> 
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_all, unsafe_allow_html=True)

st.title("Streamlit Web Title")
st.header("This is the header")
st.subheader("and subheader")
st.text("I hope the lesson is helpful for you")
st.markdown("### Mahmood Shaker Abdulhadi")
st.markdown("**Mahmood Shaker Abdulhadi**")
st.markdown("> Mahmood Shaker Abdulhadi")
st.markdown("`Code Markdown`")
st.markdown("[Facebook Login](https://www.facebook.com/)")
st.image("fav.JPG",width=300)
st.image('https://www.opensourceforu.com/wp-content/uploads/2021/04/Mobile-ui-design_OSFY-April-2021.jpg', caption='Your Image Caption', width=444)
st.markdown("---")
code="""print("Hello World")"""
st.code(code)
st.caption("Markdown Guide and Math Guide, https://www.markdownguide.org/cheat-sheet/ , https://katex.org/docs/supported.html")
st.markdown("---")
# Define your metric values
metric_name = "Revenue"
current_value = 100000
previous_value = 90000
# Calculate delta
delta = current_value - previous_value
delta_percent = (delta / previous_value) * 100
# Display the metric
st.subheader(metric_name)
st.metric(label="Current Value", value=current_value, delta=f"{delta} (+{delta_percent:.2f}%)")
st.markdown("---")
st.table(table)
st.dataframe(table)
# --------------------------------------------------------------------------------------------------------------
state=st.checkbox("checkbox",value=True)
if state:
    st.write("Done")
else:
    pass
def x():
    print("changed")
st.checkbox("test",on_change=x)

radio_btn=st.radio("in which country do you live?",options=("US","UK","Iraq"))
print(radio_btn)

button=st.button("click here to print",on_click=x)

st.selectbox("what is your favourite car?",options=("BMW","KIA"))

multiselect=st.multiselect("your letters?",options=("A","B","C","D"))
st.write(multiselect)
# --------------------------------------------------------------------------------------------------------------
import numpy as np
x=np.interp
