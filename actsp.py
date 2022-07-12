import streamlit as st
import pandas as pd
import hashlib
from PIL import Image

from io import BytesIO
import requests

r = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vTjhdfDYTI3HNP0wpxBAp_YePhfyBj9GlLAmFgW2zUsTQiWJwkY_iUvVuhiT9AD2X81uJQalB89rYlw/pub?gid=2112212887&single=true&output=csv')
DB = r.content
df = pd.read_csv(BytesIO(DB), index_col=0)
df.columns = ['Curso', 'Nome', 'CPF', 'Endereco', 'Telefone', 'e-mail']
curso = df['Curso']
nome = df['Nome']
#mail = df['email'][[0]
#st.write(df)
#st.write(df['email'])

image = Image.open('desenvolvimento.jpg')
st.image(image, caption='Web site em desenvolvimento')
st.markdown(":books:")	
st.header("Bootcamps - Aprendizagem intensiva!")
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
#col1, col2, col3 = st.columns((1, 1, 1))
col1, col2 = st.columns((1,1))
with col1:
    st.info(
    """
    A tradução do termo ***Bootcamp*** é “Campo de Treinamento”. Tem suas origens nos Campos de treinamentos Militares dos Estados Unidos, onde acontece a preparação de soldados para a guerra.  
    [MULAS, Victor, et al. Coding Bootcamps: Building Future-Proof Skills Through Rapid Skills Training, Washington, D.C.World Bank Group, 2017](http://documents.worldbank.org/curated/en/795011502799283894/Coding-bootcamps-building-future-proof-skills-through-rapid-skillstraining)
    """
    )
with col2:
    st.info(
    """
    Mais recentemente o termo ***Coding Bootcamp*** se tornou um fenômeno comum em cursos de tecnologia para definir uma aprendizagem intensiva e acelerada, focada em conteúdos tecnológicos. Venha conosco e você poderá escolher uma aprendizagem intensiva, acelerada e transparente para adquirir habilidades nas mais diversas áreas do conhecimento; não somente tecnológia!
    """
    )
task1 = st.selectbox("👈 Selecione o curso desejado:",
                    ["Clique na seta para exibir informações sobre o curso!", 
                     "Curso D1 - Nova lei de improbidade administrativa",                                #Curso 01 - ok
                     "Curso D2 - Compliance em escritórios de advocacia",                                #Curso 02 - ok
                     "Curso D3 - Lei Geral de Proteção de Dados (LGPD)",                                 #Curso 03 - ok
                     "Curso D4 - Introdução à elaboração de Contratos",                                  #Curso 04 - ok
                     "Curso C1 - Eng. Civil 1.....",                                                     #Curso 05
                     "Curso C2 - Eng. Civil 2.....",                                                     #Curso 06
                     "Curso F1 - Introdução à Finanças",                                                 #Curso 07 - ok             
                     "Curso F2 - Análise financeira em Modelo de Negócio",                               #Curso 08 - ok
                     "Curso G1 - Introdução à Gestão de Pessoas e Projetos",                             #Curso 09 - ok?
                     "Curso G2 - Gestão 2...",                                                           #Curso 10 
                     "Curso M1 - Manutenção e Instalação de Ar Condicionado",                            #Curso 11 - ok
                     "Curso M2 - Manutenção 2...",                                                       #Curso 12
                     "Curso P1 - Comunicação e Liderança",                                               #Curso 13 - ?
                     "Curso P2 - Cinco passos IKIGAI p/ um equilíbrio profissional e pessoal",               #Curso 14 - ?
                     "Curso T1 - Introdução à Python com RPA",                                           #Curso 15 - ok
                     "Curso T2 - Introdução à análise de dados com R e Python",                          #Curso 16 - ok
                     "Curso T3 - Introdução à análise de dados com Power BI",                            #Curso 17 - ok
                     "Curso T4 - Introdução à Alterix",                                                  #Curso 18 - ok
                     "Curso T5 - Criação de App para Smartphones",                                       #Curso 19 - ok
                     "Curso T6 - Excel - Do Básico à Programação VBA",                                   #Curso 20  
                     "Curso T7 - Eletrônica embarcada com Arduino e ESP32"                               #Curso 21 - 
                     "Curso T8 - Sensoriamento remoto com ESP32"                                         #Curso 22 - 
                     "Curso W1 - Preparação e transmissão de vídeos na WEB",                             #Curso 23
                     "Curso W2 - Verificar com Sandro"                                                   #Curso 24
                     ])                                  

if task1 == "Clique na seta ao lado para exibir informações sobre o curso!":
    st.markdown(
    """
    **👈 Os cursos possuem temas focados em: Direito, Eng. Civil, Manutenção e Instalação, Tecnologia e Temas diversos!**        
    """
    )
elif task1 == "Curso D1 - Nova lei de improbidade administrativa":
    st.markdown(""" ### **Curso D1 - Nova lei de improbidade administrativa (Carga Horária: 12h)** """) 
    st.markdown(""" **👈 Responsável:** Dr. Edilson Vitorelli """)
    st.markdown(
    """
    Neste minicurso os participantes serão apresentados à ......
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
    Dia 1 de 3 | ?h | ? a ?
    Dia 2 de 3 | ?h | ? a ?
    Dia 3 de 3 | ?h | ? a ?  
    """
    )
elif task1 == "Curso D2 - Compliance em escritórios de advocacia":
    st.markdown(""" ### **Curso D2 - Compliance em escritórios de advocacia (Carga Horária: 9h)** """) 
    st.markdown(""" **👈 Responsável:** Angélica França """)
    st.markdown(
    """
    Neste minicurso os participantes serão apresentados à ......
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
    Dia 1 de 3 | ?h | ? a ?
    Dia 2 de 3 | ?h | ? a ?
    Dia 3 de 3 | ?h | ? a ?  
    """
    )
elif task1 == "Curso D3 - Lei Geral de Proteção de Dados (LGPD)":
    st.markdown(""" ### **Curso D3 - Lei Geral de Proteção de Dados (LGPD) (Carga Horária: 6h)** """) 
    st.markdown(""" **👈 Responsável:** Messias Freire """)
    st.markdown(
    """     
    Neste minicurso os participantes serão apresentados à ......
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
    Dia 1 de 3 | ?h | ? a ?
    Dia 2 de 3 | ?h | ? a ?
    Dia 3 de 3 | ?h | ? a ?   
    """
    )
elif task1 == "Curso D4 - Introdução à elaboração de Contratos":
    st.markdown(""" ### **Curso D4 - Introdução à elaboração de Contrato (Carga Horária: 12h)** """) 
    st.markdown(""" **👈 Responsável:** Rodolpho Vanucci """)
    st.markdown(
    """    
    Neste minicurso os participantes serão apresentados à ......
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
    Dia 1 de 3 | ?h | ? a ?
    Dia 2 de 3 | ?h | ? a ?
    Dia 3 de 3 | ?h | ? a ?   
    """
    )
elif task1 == "Curso F1 - Introdução à Finanças":
    st.markdown(""" ### **Curso F1 - Introdução à Finanças (Carga Horária: 8h)** """) 
    st.markdown(""" **👈 Responsável:** Dr. Matias """)
    st.markdown(
    """
    Neste minicurso os participantes serão apresentados à ......
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
    Dia 1 de 3 | ?h | ? a ?
    Dia 2 de 3 | ?h | ? a ?
    Dia 3 de 3 | ?h | ? a ?  
    """
    )
elif task1 == "Curso F2 - Análise financeira em Modelo de Negócio":
    st.markdown(""" ### **Curso F2 - Análise financeira em Modelo de Negócio (Carga Horária: 8h)** """) 
    st.markdown(""" **👈 Responsável:** Dr. Ricardo Fenrandes. """)
    st.markdown(
    """
    Neste minicurso os participantes serão apresentados à ......
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
    Dia 1 de 3 | ?h | ? a ?
    Dia 2 de 3 | ?h | ? a ?
    Dia 3 de 3 | ?h | ? a ? 
    """
    )
elif task1 == "Curso G1 - Introdução à Gestão de Pessoas e Projetos":
    st.markdown(""" ### **Curso G1 - Introdução à Gestão de Pessoas e Projetos (Carga Horária: ?h)** """) 
    st.markdown(""" **👈 Responsável:** Victor Marques. """)
    st.markdown(
    """
    Neste minicurso os participantes serão apresentados à ......
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
    Dia 1 de 3 | ?h | ? a ?
    Dia 2 de 3 | ?h | ? a ?
    Dia 3 de 3 | ?h | ? a ?  
    """
    )
elif task1 == "Curso M1 - Manutenção e Instalação de Ar Condicionado":			 
    st.markdown(""" ### **Curso M1 - Manutenção e Instalação de Ar Condicionado (Carga horária: 8h)** """) 
    st.markdown(""" **Responsável:** Especialista Técnico Edmar - BHD Ar condicionado / e Eng. Eletricista Massaki de O. Igarashi """)
    st.markdown(
    """    
    Curso rápido de instalação e manutenção de ar condicionado SPLIT, com prática!
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
elif task1 == "Curso P1 - Comunicação e Liderança":
    st.markdown(""" ### **Curso P1 - Comunicação e Liderança (Carga Horária: ?h)** """) 
    st.markdown(""" **👈 Responsável:** ???? """)
    st.markdown(
    """
    Neste minicurso os participantes serão apresentados à ......
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
    Dia 1 de 3 | ?h | ? a ?
    Dia 2 de 3 | ?h | ? a ?
    Dia 3 de 3 | ?h | ? a ?  
    """
    )
elif task1 == "Curso P2 - Cinco passos IKIGAI p/ um equilíbrio profissional e pessoal":
    st.markdown(""" ### **Curso P2 - Os 5 passos IKIGAI p/ equilíbrio profissional e pessoal (Carga Horária: ?h)** """) 
    st.markdown(""" **👈 Responsável:** ???? """)
    st.markdown(
    """
    Neste minicurso os participantes serão apresentados à ......
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
    Dia 1 de 3 | ?h | ? a ?
    Dia 2 de 3 | ?h | ? a ?
    Dia 3 de 3 | ?h | ? a ?   
    """
    )
elif task1 == "Curso T1 - Introdução à Python com RPA":
    st.markdown(""" ### **Introdução à linguagem de programação Python com Automação Robótica de Processos (Carga Horária: 6h)** """) 
    st.markdown(""" **👈 Responsável:** Prof. Ms. Massaki de O. Igarashi. """)
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
 
elif task1 == "Curso T2 - Introdução à análise de dados com R e Python":
    st.markdown(""" ### **Curso T2 - Introdução à análise de dados com R e Python (Carga Horária: 8h)** """) 
    st.markdown(""" **👈 Responsável:** Prof. Ms. Massaki de O. Igarashi e/ou Gabriel. """)
    st.markdown(
    """
    Neste minicurso os participantes serão apresentados à ......
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
    Dia 1 de 3 | ?h | ? a ?
    Dia 2 de 3 | ?h | ? a ?
    Dia 3 de 3 | ?h | ? a ?  
    """
    )

elif task1 == "Curso T3 - Introdução à análise de dados com Power BI":
    st.markdown(""" ### **Curso T4 - Introdução à análise de dados com Power BI (Carga Horária: 9h)** """) 
    st.markdown(""" **👈 Responsável:** Prof. Ms. Massaki de O. Igarashi. """)
    st.markdown(
    """
    Neste minicurso os participantes serão apresentados à ......
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
    Dia 1 de 3 | ?h | ? a ?
    Dia 2 de 3 | ?h | ? a ?
    Dia 3 de 3 | ?h | ? a ?  
    """
    )
elif task1 == "Curso T4 - Introdução à Alterix":
    st.markdown(""" ### **Curso T5 - Introdução à Alterix (Carga Horária: 6h)** """) 
    st.markdown(""" **👈 Responsável:** Felipe S. """)
    st.markdown(
    """
    Neste minicurso os participantes serão apresentados à ......
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
    Dia 1 de 3 | ?h | ? a ?
    Dia 2 de 3 | ?h | ? a ?
    Dia 3 de 3 | ?h | ? a ?  
    """
    )
elif task1 == "Curso T5 - Criação de App para Smartphones":
    st.markdown(""" ### **Curso T6 - Criação de App para Smartphones (Carga Horária: 6h) **""") 
    st.markdown(""" **👈 Responsável:** Prof. Ms. Massaki de O. Igarashi. """)
    st.markdown(
    """
    Neste minicurso os participantes serão apresentados à ......
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
    Dia 1 de 3 | ?h | ? a ?
    Dia 2 de 3 | ?h | ? a ?
    Dia 3 de 3 | ?h | ? a ?  
    """
    )
    
elif task1 == "Curso T6 - Excel - Do Básico à Programação VBA":
    st.markdown(""" ### **TÍTULO CURSO (Carga Horária: 9h)** """) 
    st.markdown(""" **👈 Responsável:** Prof. Ms. Massaki de O. Igarashi. """)
    st.markdown(
    """
    Neste minicurso os participantes serão apresentados à ......
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
    Dia 1 de 3 | ?h | ? a ?
    Dia 2 de 3 | ?h | ? a ?
    Dia 3 de 3 | ?h | ? a ?  
    """
    )
                        
elif task1 == "Curso T7 - Eletrônica embarcada com Arduino e ESP32":
    st.markdown(""" ### **Curso T7 - Eletrônica embarcada com Arduino e ESP32 (Carga Horária: 8h)** """) 
    st.markdown(""" **👈 Responsável:** Prof. Ms. Sandro Valerius dos Santos? """)
    st.markdown(
    """
    Neste minicurso os participantes serão apresentados à ......
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
    Dia 1 de 4 | 2h | ? a ?
    Dia 2 de 4 | 2h | ? a ?
    Dia 3 de 4 | 2h | ? a ? 
    Dia 4 de 4 | 2h | ? a ?     
    """
    )
elif task1 == "Curso T8 - Sensoriamento remoto com ESP32":
    st.markdown(""" ### **Curso T8 - Sensoriamento remoto com ESP32 (Carga Horária: 6h)** """) 
    st.markdown(""" **👈 Responsável:** ???? """)
    st.markdown(
    """
    Neste minicurso os participantes serão apresentados à ......
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
    Dia 1 de 3 | ?h | ? a ?
    Dia 2 de 3 | ?h | ? a ?
    Dia 3 de 3 | ?h | ? a ?  
    """
    ) 

elif task1 == "Curso W1 - Preparação e transmissão de vídeos na WEB":
    st.markdown(""" ### **Curso W1 - Preparação e transmissão de vídeos na WEB (Carga Horária: ?h)** """) 
    st.markdown(""" **👈 Responsável:** Prof. Ms. Sandro Valerius dos Santos? """)
    st.markdown(
    """
    Neste minicurso os participantes serão apresentados à ......
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
    Dia 1 de 3 | ?h | ? a ?
    Dia 2 de 3 | ?h | ? a ?
    Dia 3 de 3 | ?h | ? a ?  
    """
    ) 

elif task1 == "TÍTULO":
    st.markdown(""" ### **TÍTULO CURSO (Carga Horária: ?h)** """) 
    st.markdown(""" **👈 Responsável:** ???? """)
    st.markdown(
    """
    Neste minicurso os participantes serão apresentados à ......
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
    Dia 1 de 3 | ?h | ? a ?
    Dia 2 de 3 | ?h | ? a ?
    Dia 3 de 3 | ?h | ? a ?  
    """
    )     

st.subheader("TEMA: DIREITO")
a1, a2 = st.columns((1,1))
with a1:
    st.info(
    """
    ***D1 - Nova lei de improbidade administrativa*** (Carga Horária: ?h).
    :male-technologist: ***Resp.:*** Dr. Edilson Vitorelli
    Neste minicurso os participantes serão apresentados à ......
    *** Objetivos:...***
    [Inscreva-se neste curso clicando aqui!](https://docs.google.com/forms/d/e/1FAIpQLSd52Ie1P7XzGKhtSsOcDyWgF6hFdf0DilAIgrqpaeE3DBZDGQ/viewform?usp=pp_url&entry.1084815957=D1+-+Nova+lei+de+improbidade+administrativa)
    """
    )
with a2:
    st.info(
    """
    ***D2 - Compliance em escritórios de advocacia*** (Carga Horária: ?h).
    :male-technologist: ***Resp.:*** Angélica França
    Neste minicurso os participantes serão apresentados à ......
    *** Objetivos:...***
    [Inscreva-se neste curso clicando aqui!](https://docs.google.com/forms/d/e/1FAIpQLSd52Ie1P7XzGKhtSsOcDyWgF6hFdf0DilAIgrqpaeE3DBZDGQ/viewform?usp=pp_url&entry.1084815957=D2+-+Compliance+em+escrit%C3%B3rios+de+advocacia)
    """
    )

b1, b2 = st.columns((1,1))
with b1:
    st.info(
    """
    ***D3 - Lei Geral de Proteção de Dados (LGPD)*** (Carga Horária: ?h).
    :male-technologist: ***Resp.:*** Messias Freire
    Neste minicurso os participantes serão apresentados à ......
    *** Objetivos:...***
    [Inscreva-se neste curso clicando aqui!](https://docs.google.com/forms/d/e/1FAIpQLSd52Ie1P7XzGKhtSsOcDyWgF6hFdf0DilAIgrqpaeE3DBZDGQ/viewform?usp=pp_url&entry.1084815957=D3+-+Lei+Geral+de+Prote%C3%A7%C3%A3o+de+Dados+(LGPD))
    """
    )
with b2:
    st.info(
    """
    ***D4 - Introdução à elaboração de Contratos*** (Carga Horária: ?h).
    :male-technologist: ***Resp.:*** Rodolpho Vanucci
    Neste minicurso os participantes serão apresentados à ......
    *** Objetivos:...***
    [Inscreva-se neste curso clicando aqui!](https://docs.google.com/forms/d/e/1FAIpQLSd52Ie1P7XzGKhtSsOcDyWgF6hFdf0DilAIgrqpaeE3DBZDGQ/viewform?usp=pp_url&entry.1084815957=D4+-+Introdu%C3%A7%C3%A3o+%C3%A0+elabora%C3%A7%C3%A3o+de+Contrato)
    """
    )

st.subheader("TEMA: ENG. CIVIL")
c1, c2, c3 = st.columns((1,1,1))
with c1:
    st.info(
    """
    ***ENG. CIVIL 1...*** (Carga Horária: ?h).
    :male-technologist: ***Resp.:*** ????
    Neste minicurso os participantes serão apresentados à ......
    *** Objetivos:...***
    [Inscreva-se neste curso clicando aqui!](https://forms.gle/GPCnsywpCSvUuZkv5)
    """
    )
with c2:
    st.info(
    """
    ***ENG. CIVIL 2...*** (Carga Horária: ?h).
    :male-technologist: ***Resp.:*** ???
    Neste minicurso os participantes serão apresentados à ......
    *** Objetivos:...***
    [Inscreva-se neste curso clicando aqui!](https://forms.gle/GPCnsywpCSvUuZkv5)
    """
    )
with c3:
    st.info(
    """
    ***ENG. CIVIL 3...*** (Carga Horária: ?h).
    :male-technologist: ***Resp.:*** ????
    Neste minicurso os participantes serão apresentados à ......
    *** Objetivos:...***
    [Inscreva-se neste curso clicando aqui!](https://forms.gle/GPCnsywpCSvUuZkv5)
    """
    )
st.subheader("TEMA: FINANÇAS")

d1, d2 = st.columns((1,1))
with d1:
    st.info(
    """
    ***F1 - Introdução à Finanças*** (Carga Horária: ?h).
    :male-technologist: ***Resp.:*** Matias
    Neste minicurso os participantes serão apresentados à ......
    *** Objetivos:...***
    [Inscreva-se neste curso clicando aqui!](https://docs.google.com/forms/d/e/1FAIpQLSd52Ie1P7XzGKhtSsOcDyWgF6hFdf0DilAIgrqpaeE3DBZDGQ/viewform?usp=pp_url&entry.1084815957=F1+-+Introdu%C3%A7%C3%A3o+%C3%A0+Finan%C3%A7as)
    """
    )
with d2:
    st.info(
    """
    ***F2 - Análise financeira em Modelo de Negócio*** (Carga Horária: ?h).
    :male-technologist: ***Resp.:*** Ricardo Fernandes
    Neste minicurso os participantes serão apresentados à ......
    *** Objetivos:...***
    [Inscreva-se neste curso clicando aqui!](https://docs.google.com/forms/d/e/1FAIpQLSd52Ie1P7XzGKhtSsOcDyWgF6hFdf0DilAIgrqpaeE3DBZDGQ/viewform?usp=pp_url&entry.1084815957=F2+-+An%C3%A1lise+financeira+em+Modelo+de+Neg%C3%B3cio)
    """
    )

st.subheader("TEMA: GESTÃO")
E1, E2 = st.columns((1,1))
with E1:
    st.info(
    """
    ***G1 - Introdução à Gestão de Pessoas e Projetos*** (Carga Horária: ?h)
    :male-technologist: ***Resp.:*** Victor Marques
    Neste minicurso os participantes serão apresentados à ...
    *** Objetivos:...***
    [Inscreva-se neste curso clicando aqui!](https://docs.google.com/forms/d/e/1FAIpQLSd52Ie1P7XzGKhtSsOcDyWgF6hFdf0DilAIgrqpaeE3DBZDGQ/viewform?usp=pp_url&entry.1084815957=G1+-+Introdu%C3%A7%C3%A3o+%C3%A0+Gest%C3%A3o+de+Pessoas+e+Projetos)
    """
    )  
with E2:
    st.info(
    """
    ***Curso G2 - Gestão 2...o*** (Carga Horária: ?h).
    :male-technologist: ***Resp.:*** ???
    Neste minicurso os participantes serão apresentados à ......
    *** Objetivos:...***
    [Inscreva-se neste curso clicando aqui!](https://forms.gle/GPCnsywpCSvUuZkv5)
    """
    )

st.subheader("TEMA: MANUTENÇÃO E INSTALAÇÃO")
F1, F2 = st.columns((1,1))
with F1:
    st.info(
    """
    ***M1 - Manutenção e Instalação de Ar Condicionado*** (Carga horária: 8h).
    :male-technologist: ***Resp.:*** Espec. Téc. Edmar - BHD Ar condicionado / Eng. Eletricista Massaki de O. Igarashi
    *** Objetivos: Conceitos básicos para instalação e manutenção de ar condicionado SPLIT, com prática.***  
    [Inscreva-se neste curso clicando aqui!](https://docs.google.com/forms/d/e/1FAIpQLSd52Ie1P7XzGKhtSsOcDyWgF6hFdf0DilAIgrqpaeE3DBZDGQ/viewform?usp=pp_url&entry.1084815957=M1+-+Manuten%C3%A7%C3%A3o+e+Instala%C3%A7%C3%A3o+de+Ar+Condicionado)
    """
    )
with F2:
    st.info(
    """
    ***M2 - Manutenção 2...*** (Carga horária: ?h).
    :male-technologist: ***Resp.:*** ????
    Neste minicurso os participantes serão apresentados à ......
    *** Objetivos:...***
    [Inscreva-se neste curso clicando aqui!](https://forms.gle/GPCnsywpCSvUuZkv5)
    """
    )  
st.subheader("TEMA: PESSOAS")
G1, G2 = st.columns((1,1))
with G1:
    st.info(
    """
    ***P1 - Comunicação e Liderança*** (Carga Horária: ?h).
    :male-technologist: ***Resp.:*** ????
    Neste minicurso os participantes serão apresentados à ......
    *** Objetivos:...***
    [Inscreva-se neste curso clicando aqui!](https://docs.google.com/forms/d/e/1FAIpQLSd52Ie1P7XzGKhtSsOcDyWgF6hFdf0DilAIgrqpaeE3DBZDGQ/viewform?usp=pp_url&entry.1084815957=P1+-+Comunica%C3%A7%C3%A3o+e+Lideran%C3%A7a)
    """
    )  
with G2:
    st.info(
    """
    ***P2 - Cinco passos IKIGAI p/ um equilíbrio profissional e pessoal*** (Carga Horária: ?h).
    :male-technologist: ***Resp.:*** ???
    Neste minicurso os participantes serão apresentados à ......
    *** Objetivos:...***
    [Inscreva-se neste curso clicando aqui!](https://docs.google.com/forms/d/e/1FAIpQLSd52Ie1P7XzGKhtSsOcDyWgF6hFdf0DilAIgrqpaeE3DBZDGQ/viewform?usp=pp_url&entry.1084815957=P2+-+Cinco+passos+IKIGAI+p/+um+equil%C3%ADbrio+profissional+e+pessoal)
    """
    )

st.subheader("TEMA: TECNOLOGIA")
H1, H2, H3 = st.columns((1,1,1))  
with H1:
    st.info(
    """
    ***T1 - Introdução à Python com RPA*** (Carga Horária: 6h).
    :male-technologist: ***Resp.:*** Prof. Ms. Massaki de O. Igarashi.
    *** Objetivos:*** programar: envio automático de E-MAILs, envio automático de MENSAGENS pelo WHATSAPP e PREENCHIMENTO automático de FORMULÁRIO.
    [Inscreva-se neste curso clicando aqui!](https://docs.google.com/forms/d/e/1FAIpQLSd52Ie1P7XzGKhtSsOcDyWgF6hFdf0DilAIgrqpaeE3DBZDGQ/viewform?usp=pp_url&entry.1084815957=T1+-+Introdu%C3%A7%C3%A3o+%C3%A0+Python+com+RPA)
    """
    )
with H2:
    st.info(
    """
    ***T2 - Introdução à análise de dados com R e Python*** (Carga Horária: ?h).
    :male-technologist: ***Resp.:*** ????
    Neste minicurso os participantes serão apresentados à ......
    *** Objetivos:...***
    [Inscreva-se neste curso clicando aqui!](https://docs.google.com/forms/d/e/1FAIpQLSd52Ie1P7XzGKhtSsOcDyWgF6hFdf0DilAIgrqpaeE3DBZDGQ/viewform?usp=pp_url&entry.1084815957=T2+-+Introdu%C3%A7%C3%A3o+%C3%A0+an%C3%A1lise+de+dados+com+R+e+Python)
    """
    ) 
with H3:
    st.info(
    """
    ***T3 - Introdução à análise de dados com Power BI*** (Carga Horária: 9h).
    :male-technologist: ***Resp.:*** ????
    Neste minicurso os participantes serão apresentados à ......
    *** Objetivos:...***
    [Inscreva-se neste curso clicando aqui!](https://docs.google.com/forms/d/e/1FAIpQLSd52Ie1P7XzGKhtSsOcDyWgF6hFdf0DilAIgrqpaeE3DBZDGQ/viewform?usp=pp_url&entry.1084815957=T3+-+Introdu%C3%A7%C3%A3o+%C3%A0+an%C3%A1lise+de+dados+com+Power+BI)
    """
    ) 
i1, i2, i3 = st.columns((1,1,1))  
with i1:
    st.info(
    """
    ***T4 - Introdução à Alterix*** (Carga Horária: 6h).
    :male-technologist: ***Resp.:*** Felipe S..
    *** Objetivos:*** aprender .....
    [Inscreva-se neste curso clicando aqui!](https://docs.google.com/forms/d/e/1FAIpQLSd52Ie1P7XzGKhtSsOcDyWgF6hFdf0DilAIgrqpaeE3DBZDGQ/viewform?usp=pp_url&entry.1084815957=T4+-+Introdu%C3%A7%C3%A3o+%C3%A0+Alterix)
    """
    )
with i2:
    st.info(
    """
    ***T5 - Criação de App para Smartphones*** (Carga Horária: 6h).
    male-technologist: ***Resp.:*** Prof. Ms. Massaki de O. Igarashi.
    Neste minicurso os participantes serão apresentados à ......
    *** Objetivos:...***
    [Inscreva-se neste curso clicando aqui!](https://docs.google.com/forms/d/e/1FAIpQLSd52Ie1P7XzGKhtSsOcDyWgF6hFdf0DilAIgrqpaeE3DBZDGQ/viewform?usp=pp_url&entry.1084815957=T5+-+Cria%C3%A7%C3%A3o+de+App+para+Smartphones)
    """
    ) 
with i3:
    st.info(
    """
    ***T6 - Excel - Do Básico à Programação VBA*** (Carga Horária: 9h).
    male-technologist: ***Resp.:*** Prof. Ms. Massaki de O. Igarashi.
    Neste minicurso os participantes serão apresentados à ......
    *** Objetivos:...***
    [Inscreva-se neste curso clicando aqui!](https://docs.google.com/forms/d/e/1FAIpQLSd52Ie1P7XzGKhtSsOcDyWgF6hFdf0DilAIgrqpaeE3DBZDGQ/viewform?usp=pp_url&entry.1084815957=T6+-+Excel+-+Do+B%C3%A1sico+%C3%A0+Programa%C3%A7%C3%A3o+VBA)
    """
    )
 
j1, j2 = st.columns((1,1))  
with j1:
    st.info(
    """
    ***T7 - Eletrônica embarcada com Arduino e ESP32*** (Carga Horária: ?h).
    :male-technologist: ***Resp.:*** Felipe S..
    *** Objetivos:*** aprender .....
    [Inscreva-se neste curso clicando aqui!](https://docs.google.com/forms/d/e/1FAIpQLSd52Ie1P7XzGKhtSsOcDyWgF6hFdf0DilAIgrqpaeE3DBZDGQ/viewform?usp=pp_url&entry.1084815957=T7+-+Eletr%C3%B4nica+embarcada+com+Arduino+e+ESP32)
    """
    )
with j2:
    st.info(
    """
    ***T8 - Sensoriamento remoto com ESP32*** (Carga Horária: ?h).
    male-technologist: **Responsável:** Prof. Ms. Sandro Valerius dos Santos?
    Neste minicurso os participantes serão apresentados à ......
    *** Objetivos:...***
    [Inscreva-se neste curso clicando aqui!](https://docs.google.com/forms/d/e/1FAIpQLSd52Ie1P7XzGKhtSsOcDyWgF6hFdf0DilAIgrqpaeE3DBZDGQ/viewform?usp=pp_url&entry.1084815957=T8+-+Sensoriamento+remoto+com+ESP32)
    """
    ) 

st.subheader("TEMA: WEB")
K1, K2 = st.columns((1,1))  
with K1:
    st.info(
    """
    ***W1 - Preparação e transmissão de vídeos na WEB*** (Carga Horária: ?h).
    :male-technologist: **Responsável:** Prof. Ms. Sandro Valerius dos Santos?
    *** Objetivos:*** programar: envio automático de E-MAILs, envio automático de MENSAGENS pelo WHATSAPP e PREENCHIMENTO automático de FORMULÁRIO.
    [Inscreva-se neste curso clicando aqui!](https://docs.google.com/forms/d/e/1FAIpQLSd52Ie1P7XzGKhtSsOcDyWgF6hFdf0DilAIgrqpaeE3DBZDGQ/viewform?usp=pp_url&entry.1084815957=W1+-+Prepara%C3%A7%C3%A3o+e+transmiss%C3%A3o+de+v%C3%ADdeos+na+WEB)
    """
    )
with K2:
    st.info(
    """
    ***W2 - Verificar com Sandro*** (Carga Horária: ?h).
    :male-technologist: **Responsável:** Prof. Ms. Sandro Valerius dos Santos?
    Neste minicurso os participantes serão apresentados à ......
    *** Objetivos:...***
    [Inscreva-se neste curso clicando aqui!](https://forms.gle/GPCnsywpCSvUuZkv5)
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

	st.subheader("------ **Desenvolvido por: Massaki de O. Igarashi** -----")

	menu = ["Cursos",
            "Admin",
            "Contato",
            "SignUp"
            ]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Cursos":       
		st.subheader("ACESSO RESTRITO (em desenvolvimento): \n Preencha os dados abaixo:")
	elif choice == "Admin":
		st.subheader("Login Section")
		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')        
		if st.sidebar.checkbox("Logar!"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)
			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:
				st.success("Logged In as {}".format(username))
				task = st.selectbox("Task",["Add Post","PERFIL","Panorama_INSCRITOS"])
				if task == "Add Post":
					st.subheader("Add Your Post")
				elif task == "PERFIL":
					st.subheader("PERFIL DE USUÁRIO \n Linha 01 - Texto do perfil.")
				elif task == "Panorama_INSCRITOS":
					st.subheader(str(curso))                    
					user_result = view_all_users()
					clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
					#st.dataframe(clean_db)                    
			else:
				st.warning("Incorrect Username/Password") 
	elif choice == "Contato":
		st.subheader("Massaki de O. Igarashi - Cel: (11)98810-9797 / e-mail: prof.massaki@gmail.com")
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
