import json

import streamlit as st

from ..components import get_mlruns_data, check_mlruns_directory, save_data_to_json


def page_5():
    st.markdown('<div class="header">#5 Mlflow Artifacts_</div>', unsafe_allow_html=True)
    st.text("")
    st.text("Here is raw view of mlflow experiments, runs & artifacts registry carried out during devlopment phase.")
    st.markdown('---')

    #--------- Mlflow registry -------------
    try:
        check_mlruns_directory('mlruns')     # Check if 'mlruns' directory exists
        data = get_mlruns_data('mlruns')     # Retrieve data
        save_data_to_json(data)

    except FileNotFoundError as e:
        print(e)

    def load_json(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    try:
        st.markdown("## MLflow Artifacts Explorer")
        st.json(load_json('models/mlruns_data.json'))
    except FileNotFoundError:
        st.error(f"The file '{'models/mlruns_data.json'}' does not exist.")
    except json.JSONDecodeError:
        st.error("Error decoding JSON from the file.")
