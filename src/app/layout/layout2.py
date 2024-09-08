import streamlit as st

from ...data import CSVLoader


def page_2():
    st.markdown('<div class="header">#2 Feature Engineering_</div>', unsafe_allow_html=True)
    st.text("")
    st.text("Here is the feature engineering phase.")
    st.markdown('---')

    loader = CSVLoader('./data/raw')
    dataframes = loader.load_csv_files()

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("## #Raw Data_")
        st.dataframe(dataframes['Loan_Data'])
    with col2:
        st.markdown("## #Statistics_")
        st.dataframe(dataframes['Loan_Data'].describe())