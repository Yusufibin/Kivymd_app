from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import openai
from kivymd.uix.textfield import MDTextField
from kivymd.app import MDApp

from kivy.properties import ObjectProperty,StringProperty

# Configuration de l'API OpenAI
openai.api_key = "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"

# Chargement du fichier KV pour la mise en page de l'interface utilisateur
Builder.load_file('interface.kv')

class MyApp(MDApp):

    def build(self):
        return MyBoxLayout()

class MyBoxLayout(BoxLayout):
    # Les propriétés de l'interface utilisateur
    question_input = ObjectProperty()
    answer_output = ObjectProperty()
    
    def ask_question(self):
        # Obtention de la question de l'input utilisateur
        qtext = self.ids.question_input.text
        self.ids.response_label.text = ' Patientez..'

        question = qtext 
   
       
    
        if not question:
            # Si la question est vide, ne rien faire
            return
    
        # Connexion à l'API OpenAI pour obtenir la réponse
        response = openai.Completion.create(
            model="text-davinci-003", prompt=question, temperature=0.9, max_tokens=1000
        )
    
        # Obtenir la réponse du modèle d'IA OpenAI
       
        #r = self.answer_output
        #r= str(r)
        answer = response.choices[0].text.strip()
        r = answer
     
    
        # Affiche la réponse dans le label
        #self.ids['response_label'].text = r
        self.ids.response_label.text = r
    

if __name__ == '__main__':
    MyApp().run()
