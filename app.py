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
        x = df.drop(columns=['Pmi',"name"])
        return x,y
    def add(LDH,AST,trig,ph_level,pmi_v,name=None):
        data = {
            'name': [name],
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
    name=st.sidebar.text_input("Name of the patient is")
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
        #t="name"+","+"ldh"+","+"ast"+","+"trig"+","+str(ph_level)+","+str(int(y_pred[0]))
        s="name= "+str(name)+","+"ldh= "+str(LDH)+","+"ast= "+str(AST)+","+"triglycerides= "+str(trig)+","+"ph_level= "+str(ph_level)+","+"pmi_predicted= "+str(int(y_pred[0]))
        st.write(s)
        if st.button("ADD",key="add"):
            st.subheader("Adding the data")
            if name:
                add(LDH,AST,trig,ph_level,int(y_pred[0]),name=name)
            else:
                add(LDH, AST, trig, ph_level, int(y_pred[0]),name=name)
            f=load_data()


if __name__ == '__main__':
    main()