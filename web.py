import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import mysql.connector
import sqlite3

# mydb = mysql.connector.connect(host='localhost', user='root', password='Mn12312344$', port='3306', database='Mydb')
mydb = sqlite3.connect('information.db')
mycursor = mydb.cursor()
mycursor.execute('select * from flow_rate')
data = mycursor.fetchall()

MD_m = np.array([])
cuttings_size_in = np.array([])
cuttings_density = np.array([])
Estimated_TR = np.array([])
Optimal_Q_gpm = np.array([])
Enhanced_TR = np.array([])

# call the columns
for j in data:
    first_column = j[0]
    MD_m = np.append(MD_m, first_column)
    second_column = j[1]
    cuttings_size_in = np.append(cuttings_size_in , second_column)
    third_column = j[2]
    cuttings_density = np.append(cuttings_density , third_column)
    fourth_column = j[3]
    Estimated_TR = np.append(Estimated_TR , fourth_column)
    fifth_column = j[4]
    Optimal_Q_gpm = np.append(Optimal_Q_gpm , fifth_column)
    sixth_column = j[5]
    Enhanced_TR = np.append(Enhanced_TR , sixth_column)

# Create a figure and a subplot with 1 row and 2 columns
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 10))

# Plot depth & Q on the first subplot
ax1.plot(Optimal_Q_gpm, MD_m, c='#00f', alpha=0.35)
ax1.invert_yaxis()
ax1.set_xticks([634, 1300])
ax1.set_yticks([430, 1870])
ax1.set_ylabel('MD (m)')
ax1.set_xlabel('Q (gpm)')
ax1.xaxis.set_ticks_position('top')
ax1.xaxis.set_label_position('top')
ax1.grid(True, which='both', alpha=0.7, linestyle=':', lw=0.5)
ax1.minorticks_on()
ax1.grid(True, which='minor', alpha=0.7, linestyle=':', lw=0.5)

# Plot depth & TR on the second subplot
ax2.plot(Enhanced_TR, MD_m, c='r', alpha=0.35)
ax2.invert_yaxis()
ax2.set_xticks([0,  100])
ax2.set_yticks([430, 1870])
ax2.set_ylabel('MD (m)')
ax2.set_xlabel('TR')
ax2.xaxis.set_ticks_position('top')
ax2.xaxis.set_label_position('top')
ax2.grid(True, which='both', alpha=0.7, linestyle=':', lw=0.5)
ax2.minorticks_on()
ax2.grid(True, which='minor', alpha=0.7, linestyle=':', lw=0.5)
# Adjust layout to prevent clipping of labels
plt.tight_layout()
st.pyplot(fig)

# present the table
table=pd.DataFrame({"MD_m":MD_m,"cuttings_size_in":cuttings_size_in,
                    "cuttings_density":cuttings_density,"Estimated_TR":Estimated_TR,
                    "Optimal_Q_gpm":Optimal_Q_gpm,"Enhanced_TR":Enhanced_TR} )

# remove trailing zeros
columns_to_format = ["MD_m", "cuttings_size_in", "cuttings_density", "Estimated_TR", "Optimal_Q_gpm", "Enhanced_TR"]
for x in columns_to_format:
    table[x] = table[x].apply(lambda x: f"{x:,g}" if type(x) is float else x)

st.table(table)

# align the content in the center
st.markdown("""<style>table {width: 100%;}th,td{text-align: center !important;}</style>""",unsafe_allow_html=True)




