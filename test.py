import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.prompts import PromptTemplate
from langchain.schema import Document
from langchain_ollama import OllamaLLM

# Description du poste
job_description = """
Titre : Expert Python Data Science et NLP
Description : Nous recherchons un expert Python avec 5 ans d'expérience en Data Science, 
maîtrise de Pandas, Flask, API REST et Docker pour un projet de 3 ans à distance.
"""

cv_folder = "./cvs"

def load_cv(file_path) -> Document:
    loader = PyPDFLoader(file_path)
    pages = loader.load()
    full_text = "\n".join(page.page_content for page in pages)
    return Document(page_content=full_text)

prompt_template = """
Tu es un assistant RH qui analyse la pertinence d'un CV par rapport à une description de poste.

Description du poste :
{job_desc}

CV :
{cv_text}

La réponse doit être uniquement "Pertinent" ou "Non pertinent", suivie d'une courte explication de 1 phrase maximum.

Réponse :
"""

prompt = PromptTemplate(
    input_variables=["job_desc", "cv_text"],
    template=prompt_template
)

llm = OllamaLLM(model="tinyllama")

# Chaîne : prompt | llm (pipeline)
chain = prompt | llm

for filename in os.listdir(cv_folder):
    if filename.endswith(".pdf"):
        cv_path = os.path.join(cv_folder, filename)
        cv_doc = load_cv(cv_path)
        input_dict = {
            "job_desc": job_description,
            "cv_text": cv_doc.page_content
        }
        result = chain.invoke(input_dict)
        print(f"🧾 Résultat pour {filename} :\n{result}\n")
