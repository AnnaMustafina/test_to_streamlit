import streamlit as st
import pandas as pd
import numpy as np
from id_list import id_now

if id_now =='IU13488':
    st.write('Привет, пользователь', id_now)
else:
    st.write('Привет, таинственный незнакомец')

chart_data = pd.DataFrame(
    {
        "col1": list(range(20)) * 3,
        "col2": np.random.randn(60),
        "col3": ["A"] * 20 + ["B"] * 20 + ["C"] * 20,
    }
)

st.bar_chart(chart_data, x="col1", y="col2", color="col3")
