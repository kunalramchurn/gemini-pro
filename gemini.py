import pathlib
import textwrap
import os

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

os.environ['GOOGLE_API_KEY']="AIzaSyC-mDQQBJjm2hGbejYsz7L6jfr3-pPVqfA"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("Can you output a python script to train a random forest model?")

to_markdown(response.text)
