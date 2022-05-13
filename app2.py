import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open('model.sav','rb'))

st.title("Predicting Whiffs for 4-seam fastballs")
st.markdown("Predicting Whiffs")

with open('./list.pkl', 'rb') as pickle_in:
    columns = pickle.load(pickle_in)

df_list = columns
form_list = [[]]
list_diff = []

with st.form('prediction_form'):



    spin_axis = st.text_input('spin_axis', max_chars = 15) 
    speed = st.text_input('effective_speed', max_chars = 15) 
    spin = st.text_input('release_spin_rate', max_chars = 15) 
    az = st.text_input('az', max_chars = 15) 
    ay = st.text_input('ay', max_chars = 15) 
    ax = st.text_input('ax', max_chars = 15)
    vz = st.text_input('vz0', max_chars = 15)
    vy = st.text_input('vy0', max_chars = 15)
    vx = st.text_input('vx0', max_chars = 15)
    location = st.text_input('zone', max_chars = 15)
    balls = st.text_input('balls', max_chars = 15)
    strikes = st.text_input('strikes', max_chars = 15)
    horizontal_break = st.text_input('pfx_x', max_chars = 15)
    vertical_break = st.text_input('pfx_z', max_chars = 15)
    
    submitted = st.form_submit_button("Submit")
    if submitted:
        form_list[0].append(float(spin_axis))
        form_list[0].append(float(speed))
        form_list[0].append(float(spin))
        form_list[0].append(float(az))
        form_list[0].append(float(ay))
        form_list[0].append(float(ax))
        form_list[0].append(float(vz))
        form_list[0].append(float(vy))
        form_list[0].append(float(vx))
        form_list[0].append(float(location))
        form_list[0].append(float(balls))
        form_list[0].append(float(strikes))
        form_list[0].append(float(horizontal_break))
        form_list[0].append(float(vertical_break))
        

        df = pd.DataFrame(form_list, columns = ['spin_axis','effective_speed','release_spin_rate', 'az', 'ay', 'ax', 'vz0', 'vy0', 'vx0', 'zone', 'balls', 'strikes', 'pfx_x', 'pfx_z'])
        df = df.reindex(columns=columns).fillna(0)


        
        preds = model.predict(df)
        st.write('Is it a whiff',str(preds[0]))
