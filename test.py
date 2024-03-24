import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import psycopg2

dbname = 'siwzqkyp'
user = 'siwzqkyp'
password = 'U_jmIQv_D0ogqpmfign1RPTAoKnnWsbT'
host = 'castor.db.elephantsql.com'
port = '5432'

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
cursor = conn.cursor()
cursor.execute("SELECT * FROM flow_rate")
data = cursor.fetchall()

MD_m = np.array([])
cuttings_size_in = np.array([])
cuttings_density = np.array([])
Estimated_TR = np.array([])
Optimal_Q_gpm = np.array([])
Enhanced_TR = np.array([])

# call the columns
for j in data:
    first_column = j[1]
    MD_m = np.append(MD_m, first_column)
    second_column = j[2]
    cuttings_size_in = np.append(cuttings_size_in , second_column)
    third_column = j[3]
    cuttings_density = np.append(cuttings_density , third_column)
    fourth_column = j[4]
    Estimated_TR = np.append(Estimated_TR , fourth_column)
    fifth_column = j[5]
    Optimal_Q_gpm = np.append(Optimal_Q_gpm , fifth_column)
    sixth_column = j[6]
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
