import streamlit as st
import math

st.title("Phương trình bậc hai")

a = st.number_input("Nhập hệ số a:", value=0, step=1)
b = st.number_input("Nhập hệ số b:", value=0, step=1)
c = st.number_input("Nhập hệ số c:", value=0, step=1)

if st.button("Giải"):
    delta = b**2 - 4*a*c
    if delta < 0:
        st.write("Phương trình vô nghiệm")
    elif delta == 0:
        x = -b / (2*a)
        st.write("Phương trình có nghiệm kép x =", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        st.write("Phương trình có hai nghiệm phân biệt:")
        st.write("x1 =", x1)
        st.write("x2 =", x2)
