import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression

def main():
    st.title("Ai Postmoterm Interval Prediction ")
    st.sidebar.title("Ai Postmoterm Interval Prediction ")
    st.markdown("Using Blood🩸 Biomarkers")
    st.sidebar.markdown("Using Blood🩸 Biomarkers")

    def load_data():
        data = pd.read_csv('pmi_new.csv')
        st.write(data)
        return data

    def split(df):
        y = df.Pmi
        x = df.drop(columns=['Pmi'])
        return x,y
    def add(LDH,AST,trig,ph_level,pmi_v):
        data = {
            'ldh': [LDH],
            'ast': [AST],
            'triglycerides': [trig],
            'ph_level': [ph_level],
            'pmi': [pmi_v]
        }
        df = pd.DataFrame(data)
        df.to_csv('pmi_new.csv', mode='a', index=False, header=False)
        print("Data appended successfully.")
    df=load_data()
    x,y=split(df)
    C = st.sidebar.number_input("C (Regularization parameter)", 0.01, 10.0, step=0.01, key="C_LR")
    max_iter = st.sidebar.slider("Maximum number of iterations", 100, 500, key="max_iter")
    LDH=st.sidebar.number_input("LDH is",step=10)
    AST=st.sidebar.number_input("AST is",step=10)
    trig=st.sidebar.number_input("Triglycerides is",step=5)
    ph_level=st.sidebar.number_input("Ph Level is",step=1)
    if "btn_clk" not in st.session_state:
        st.session_state.btn_clk=False
    def callback():
        st.session_state.btn_clk=True
    if st.sidebar.button("Predict",on_click=callback , key="classify") or st.session_state.btn_clk:
        st.subheader("Prediction Results")
        model = LogisticRegression(C=C, max_iter=max_iter)
        model.fit(x, y)
        xc=[(LDH,AST,trig,ph_level)]
        x_test = pd.DataFrame(xc, columns=['ldh', 'ast', 'triglycerides','ph_level'])
        y_pred=model.predict(x_test)
        st.write("The PMI estimated is",(int(y_pred[0])))
        st.write("Wanna add the results to prediction data?")
        if st.button("ADD",key="add"):
            st.subheader("Adding the data")
            add(LDH,AST,trig,ph_level,int(y_pred[0]))
            f=load_data()


if __name__ == '__main__':
    main()