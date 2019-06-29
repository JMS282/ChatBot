# PRPGRAMADOR: jmsixpenze50@gmail.com

#-*-coding:utf8;-*-
from Response.Response import Response
from Str.Str import Str

# Classe ChaTBot
class ChatBot():
      def __init__(self, bot_name="chatbot"):
          # Dados para treinamento - 10
          data_1 = {}; data_2 = {}; data_3 = {}; data_4 = {}; data_5 = {}
          data_6 = {}; data_7 = {}; data_8 = {}; data_9 = {}; data_10 = {}               
          # Nome do chatbot
          self.bot_name = bot_name
          # Trainando na inicializacao - 10
          self.set_trainer_1(data_1)
          self.set_trainer_2(data_2)
          self.set_trainer_3(data_3)
          self.set_trainer_4(data_4)
          self.set_trainer_5(data_5)
          self.set_trainer_6(data_6)
          self.set_trainer_7(data_7)
          self.set_trainer_8(data_8)
          self.set_trainer_9(data_9)
          self.set_trainer_10(data_10)
         
      # 10 definicoes de treinamento
      def set_trainer_1(self, dictionary_1):
          self.dictionary_1 = dictionary_1
      def set_trainer_2(self, dictionary_2):
          self.dictionary_2 = dictionary_2
      def set_trainer_3(self, dictionary_3):
          self.dictionary_3 = dictionary_3
      def set_trainer_4(self, dictionary_4):
          self.dictionary_4 = dictionary_4
      def set_trainer_5(self, dictionary_5):
          self.dictionary_5 = dictionary_5
      def set_trainer_6(self, dictionary_6):
          self.dictionary_6 = dictionary_6
      def set_trainer_7(self, dictionary_7):
          self.dictionary_7 = dictionary_7
      def set_trainer_8(self, dictionary_8):
          self.dictionary_8 = dictionary_8
      def set_trainer_9(self, dictionary_9):
          self.dictionary_9 = dictionary_9
      def set_trainer_10(self, dictionary_10):
          self.dictionary_10 = dictionary_10

      # Aqui o chatbot devolve o seu nome Ex: bot.get_chatbot_name()
      def get_chatbot_name(self):
      	  return self.bot_name
      # Aqui o chatbot devolve a resposta apois a verificacao da questao: Ex: bot.get_response("hello")
      def get_response(self, question):
          try:
              # Accessa o primeiro dicionario de trainamento
              return self.dictionary_1[question]
          except:
              try:
                  # Accessa o segundo dicionario de trainamento
                  return self.dictionary_2[question]
              except:
                  try:
                     # Accessa o terceiro dicionario de trainamento
                     return self.dictionary_3[question]
                  except:
                     try:
                         # Accessa o quarto dicionario de trainamento
                         return self.dictionary_4[question]
                     except:
                          try:
                             # Accessa o quinto dicionario de trainamento
                             return self.dictionary_5[question]
                          except:
                                try:
                                   # Accessa o segundo dicionario de trainamento
                                   return self.dictionary_6[question]
                                except:
                                       try:
                                          # Accessa o setimo dicionario de trainamento
                                          return self.dictionary_7[question]
                                       except:
                                              try:
                                                 # Accessa o oitavo dicionario de trainamento
                                                 return self.dictionary_8[question]
                                              except:
                                                     try:
                                                        # Accessa o nono dicionario de trainamento
                                                        return self.dictionary_9[question]
                                                     except:
                                                            try:
                                                               # Accessa o decimo dicionario de trainamento
                                                               return self.dictionary_10[question]
                                                            except:
                                                               # Quando todos os 10 dicionarios resultarem em KeyError, o chatbot accessa a Class de Resposta
                                                               if Str(question).indexOf("what"): 
                                                                  if Str(question).indexOf("your"):
                                                                     if Str(question).indexOf("name"):
                                                                        return self.bot_name
                                                               return Response().response(question)
   

                

