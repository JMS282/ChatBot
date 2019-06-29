# PROGRAMER: jmsixpenze50@gmail.com

#-*-coding:utf8;-*-
import time, random as r
from Str.Str import Str
from Timer.Timer import Time

class Response():
      def __init__(self):
          pass
      def response(self, question):
#[1] -> What question
          if Str(question).indexOf("what") or Str(question).indexOf("show"):

             # [1.1] -> Asking for time
             if Str(question).indexOf("time"):
                return Time().Clock()[6]
                
#[2] -> Greetings1
          if Str(question).indexOf("good"):
             # [2.1] -> Morning
             if Str(question).indexOf("morning"):
                return Time().GreetingNow()
             # [2.2] -> Afternoon
             if Str(question).indexOf("afternoon"):
                return Time().GreetingNow()
             # [2.3] -> Everning
             if Str(question).indexOf("evening"):
                return Time().GreetingNow()
             # [2.4] -> Night
             if Str(question).indexOf("night"):
                return Time().GreetingNow()
#[3] -> Greetings2
          if Str(question).indexOf("hi"):
             greet_2_response= ("hello", "hi")
             return r.choice(greet_2_response)
          if Str(question).indexOf("hello"):
             greet_2_response= ("hello", "hi")
             return r.choice(greet_2_response)


          else:
              try:
                  return str(eval(question))
              except:
                  return "chatbot_db_error"
                  

#if __name__ == "__main__":
#   while True:
#       question = raw_input("\033[5;32m> ")
#       Resp = Response()
#       resp = Resp.response(question)
#       print " \033[2;33m::",resp
       
       
       
       
       
