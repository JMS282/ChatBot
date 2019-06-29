#-*-coding:utf8;-*-
#qpy:2
#qpy:console
import time

# Classe crono responsavel pela verificacao do tempo real... 
class Time(): 
      def __init__(self): 
          pass 
      def GreetingNow(self): 
          t = time.localtime() 
          hora = t[3] 
          periodo = "good evening" 
          if(hora>0 and hora<=4): periodo = "good nigth" 
          if(hora>4 and hora<12): periodo = "good morning" 
          if(hora>=12 and hora<18): periodo = "good afternoon" 
          tempo = [periodo, t[0], t[1], t[2], t[3], t[4]] 
          return tempo[0] 
             
      def Clock(self): 
         t = time.asctime(); tm = t[11:16] 
         weekday = t[:3];    month = t[4:7]
         day = t[8:10];      houer = t[11:13] 
         minutes = t[14:16]; year = t[20:] 
         result = [houer,minutes,day,month,year,weekday,tm,t] 
         return result 



