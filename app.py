{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "76b21b79-2e1b-4770-894f-5e96eabd70b0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pickle\n",
    "\n",
    "model = pickle.load(open('modeltest.sav','rb'))\n",
    "\n",
    "st.title(\"Predicting Whiffs for 4-seam fastballs\")\n",
    "st.markdown(\"Predicting Whiffs\")\n",
    "\n",
    "with open('./list2.pkl', 'rb') as pickle_in:\n",
    "    columns = pickle.load(pickle_in)\n",
    "\n",
    "df_list = columns\n",
    "form_list = [[]]\n",
    "list_diff = []\n",
    "\n",
    "with st.form('prediction_form'):\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "    speed = st.text_input('effective_speed', max_chars = 15) # first importance ranking\n",
    "    spin = st.text_input('release_spin_rate', max_chars = 15) # second importance ranking\n",
    "    \n",
    "    submitted = st.form_submit_button(\"Submit\")\n",
    "    if submitted:\n",
    "        form_list[0].append(float(speed))\n",
    "\n",
    "        form_list[0].append(float(spin))\n",
    "       \n",
    "        \n",
    "\n",
    "        df = pd.DataFrame(form_list, columns = ['effective_speed','release_spin_rate'])\n",
    "        df = df.reindex(columns=columns).fillna(0)\n",
    "\n",
    "\n",
    "        \n",
    "        preds = model.predict(df)\n",
    "        st.write('Is it a whiff',str(preds[0]))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8442525e-5104-43fd-af96-4c72486db192",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:GA]",
   "language": "python",
   "name": "conda-env-GA-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
