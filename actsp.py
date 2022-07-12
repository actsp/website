import streamlit as st
import pandas as pd
import hashlib
from PIL import Image

image = Image.open('desenvolvimento.jpg')
st.image(image, caption='Web site em desenvolvimento')
st.markdown(":books:")	
st.header("Bootcamps do Prof. Massaki e Parceiros")
st.subheader("(Com emissão de CERTIFICADOS)")

mystyle = '''
    <style>
        p {
            text-align: justify;
        }
    </style>
    '''
st.markdown(mystyle, unsafe_allow_html=True)
# Generate tree equal columns
#c1, c2, c3 = st.columns((1, 1, 1))
c1, c2 = st.columns((1,1))
with c1:
    st.info(
    """
    A tradução do termo ***Bootcamp*** é “Campo de Treinamento”. Tem suas origens nos Campos de treinamentos Militares dos Estados Unidos, onde acontece a preparação de soldados para a guerra.  
    [MULAS, Victor, et al. Coding Bootcamps: Building Future-Proof Skills Through Rapid Skills Training, Washington, D.C.World Bank Group, 2017](http://documents.worldbank.org/curated/en/795011502799283894/Coding-bootcamps-building-future-proof-skills-through-rapid-skillstraining)
    """
    )
with c2:
    st.info(
    """
    O termo "Coding Bootcamp" se tornou um fenômeno comum em cursos de tecnologia para definir uma aprendizagem intensiva e acelerada, focada em conteúdos tecnológicos. Venha conosco e você poderá escolher uma aprendizagem intensiva, acelerada e transparente para adquirir habilidades nas mais diversas áreas do conhecimento; não somente tecnológia!
    """
    )
task1 = st.selectbox("👈 Selecione um Curso / Temas Diversos:",["D0 - Clique na seta para selecionar", "Curso D1 - Ar Condicionado","Curso D2","Curso_D3"])
task2 = st.selectbox("👈 Ou Selecione um Curso /Tema Tecnológico:",["T0 - Clique na seta para selecionar", "Curso T1 - Introdução à Python com RPA", "Curso_T2"])
if task1 == "D0 - Clique na seta para selecionar":
    st.markdown(
    """
    **👈 Os cursos temas diversos podem ser desde Ar condicionado, elaboração de curriculo.. etc**        
    """
    )
    
elif task1 == "Curso D1 - Ar Condicionado":			 
    st.markdown(
    """
    **Curso 01: Responsável: Especialista Técnico Edmar - BHD Ar condicionado**        
    ***Curso de instalação ar condicionado SPLIT, com prática. (Carga horária: 8h)***
    - 01.Introdução;
    - 02.Normas Técnicas Relacionadas;
    - 03.Primeiros Passos;       
    - 04.Conhecendo o Equipamento;
    - 05.Ferramentas e Equipamentos Necessários para Instalação;
    - 06.Como escolher o Local Correto para instalar  a Unidade Interna;
    - 07.Instalação do Suporte Para Fixar a Unidade Interna;
    - 08.Instalação dos Tubos da Unidade Interna;
    - 09.Como escolher o Local Correto para instalar Unidade Externa;
    - 10.Ligação dos Tubos na Unidade Externa;
    - 11.O Procedimento de Gerar Vácuo é Obrigatório na Instalação?
    - 12.Como Gerar Vácuo nas Tubulações;
    - 13.Ciclos de Refrigeração e Aquecimento do Ar Condicionado;
    - 14.Instalação Elétrica;
    - 15.Esquema Elétrico de Ligação;
    - 16.Como Deverá ser Feita a Instalação Elétrica Residencial;
    - 17.Ocorrências de Má Funcionamento do Equipamento.
    
    ### CRONOGRAMA
    DIA | CH HORÁRIA | CONTEÚDO
    :---------: | :------: | :-------:
    Dia 1 de 3 | 3h | 01 a 06
    Dia 2 de 3 | 2h | 07 a 13
    Dia 3 de 3 | 3h | 14 a 17   
    """
    )   
    
elif task1 == "urso D2":
    st.markdown(""" ### **TÍTULO CURSO D2**. """) 
    st.markdown(
    """
    **👈 Responsável: Prof. MSc. Massaki de O. Igarashi (Carga Horária: 8h)**        
    """
    )
    st.markdown(
    """
    Neste minicurso de “TPITULO D2” os participantes serão apresentados à ......
    ## Objetivos:
    - 01. ... 
    - 02. ... 
    - 03. ... 
    - 04. ...
    - 05. ...
    - 06. Prática e dúvidas
   
    ### CRONOGRAMA
    DIA | CH HORÁRIA | CONTEÚDO
    :---------: | :------: | :-------:
    Dia 1 de 3 | 3h | 0
    Dia 2 de 3 | 3h | 0  a 
    Dia 3 de 3 | 3h | 1   a 1  
    """
    )
elif task1 == "Curso_03":
    st.markdown(
        """
         Streamlit Markdown.
        **👈 NEGRITO** Veja ao lado!
        ### TÍTULO
        - Link 1: [Título Link aqui](https://streamlit.io)
        - Link 2: [Título Link aqui](https://streamlit.io)
        ### TABELA
        Alinhado a esquerda | Centralizado | Alinhado a direita
         :--------- | :------: | -------:
        Valor | Valor | Valor
        """
    )
    
if task2 == "T0 - Clique na seta para selecionar":
    st.markdown(
    """
    **👈 Responsável: Prof. MSc. Massaki de O. Igarashi (Carga Horária: 8h)**        
    """
    )
elif task2 == "Curso T1 - Introdução à Python com RPA":
    st.markdown(""" ### **Introdução à linguagem de programação Python com Automação Robótica de Processos**. """) 
    st.markdown(
    """
    **👈 Responsável: Prof. MSc. Massaki de O. Igarashi (Carga Horária: 6h)**        
    """
    )
    st.markdown(
    """
    Neste minicurso de “Introdução à linguagem Python com Automação Robótica de Processos” os participantes serão apresentados à conceitos básicos da linguagem de programação Python pelo uso de bibliotecas para Automação Robótica de Processos (do inglês ***Robotic Process Automation – RPA***). 
    Os participantes também terão uma experiência prática de programação.
    Afinal, automatizar tarefas básicas do dia a dia é muito importante para aumentar a produtividade e valorizar o seu tempo; por isso, os participantes se beneficiarão positivamente com esta atualização de ferramentas que estão sendo criadas e utilizadas no ambiente profissional.
    ## Objetivos:
    - 01. Aprender conceitos básicos de programação orientada à objetos (classes, atributos e métodos), 
    - 02. Instalação do pacote Anaconda (funcionalidades e praticidade na instalação e uso de bibliotecas desenvolvidas por terceiros) 
    - 03. Envio automático de E-MAILs, 
    - 04. Envio automático de MENSAGENS usando WHATSAPP 
    - 05. PREENCHIMENTO automático de FORMULÁRIO.
    - 06. Prática e dúvidas
    ### CRONOGRAMA
    DIA | CH HORÁRIA | CONTEÚDO
    :---------: | :------: | :-------:
    Dia 1 de 2 | 3h | 01 a 03
    Dia 2 de 2 | 3h | 04 a 06
    """
    )
# Security
#passlib,hashlib,bcrypt,scrypt

def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data

def main():
	"""Simple Login App"""

	st.title("*************************************")

	menu = ["Cursos","Login","SignUp"]
	choice = st.sidebar.selectbox("Menu",menu)
    
	if choice == "Cursos":       
		st.subheader("ACESSO RESTRITO \n Siga as instruções abaixo \n Nova linha \n Nova linha 2.")
	elif choice == "Login":
		st.subheader("Login Section")

		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:

				st.success("Logged In as {}".format(username))

				task = st.selectbox("Task",["Add Post","PERFIL","Profiles"])
				if task == "Add Post":
					st.subheader("Add Your Post")
				elif task == "PERFIL":
					st.subheader("PERFIL DE USUÁRIO \n Linha 01 - Texto do perfil.")
				elif task == "Profiles":
					st.subheader("User Profiles")
					user_result = view_all_users()
					clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
					st.dataframe(clean_db)
			else:
				st.warning("Incorrect Username/Password")

	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")



if __name__ == '__main__':
	main()
