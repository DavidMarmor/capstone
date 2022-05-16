import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open('model8.sav','rb'))

st.title("Predicting Whiffs for split fingered fastballs")
st.markdown("Predicting Whiffs")

with open('./list.pkl', 'rb') as pickle_in:
    columns = pickle.load(pickle_in)

df_list = columns
form_list = [[]]
list_diff = []

with st.form('prediction_form'):



    speed = st.text_input('speed', max_chars = 15) 
    spin = st.text_input('spinrate', max_chars = 15) 
    location = st.text_input('zone', max_chars =15)
    horizontal_break = st.text_input('horizontal movement', max_chars = 15)
    vertical_break = st.text_input('vertical movement', max_chars = 15)
    
    submitted = st.form_submit_button("Submit")
    if submitted:
        form_list[0].append(float(speed))
        form_list[0].append(float(spin))
        form_list[0].append(float(location))
        form_list[0].append(float(horizontal_break))
        form_list[0].append(float(vertical_break))
        

        df = pd.DataFrame(form_list, columns = ['release_speed','release_spin_rate', 'zone', 'pfx_x', 'pfx_z'])
        df = df.reindex(columns=columns).fillna(0)


        
        preds = model.predict(df)
        st.write('Is it a whiff',str(preds[0]))