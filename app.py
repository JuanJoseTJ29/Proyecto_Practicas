import streamlit as st
from multiapp import MultiApp
from apps import  dolar, euro #, model1 # import your app modules here

app = MultiApp()

st.markdown("""
#  PROYECTO PRACTICAS-PREPROFESIONALES

""")

st.title('Integrantes:')


st.write('- Tirado Julca Juan Jose')


st.title('Escoja la divisa:')

# Add all your application here
#app.add_app("Home", home.app)
#app.add_app("Dolares", dolar.app)
#app.add_app("Euros", euro.app)
#app.add_app("Euros", model1.app)
# The main app
app.run()



