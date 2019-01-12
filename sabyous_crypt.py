                              # -*- coding: utf-8 -*-
#############################################################################################################
#writen by: Sabir Amhaida 2017  facebook: www.facebook.com/sabir.amhaida               #
#"""                                                                                                        #
#""" codage basé sur le principe de cesar mais modifié; 		                        										    #
#le mot de passe peut contenir des mots/ des caractères ...des caractères spéciaux peuvent aussi etre codés #                                                                                                      #
#############################################################################################################
from Tkinter import *
#_________________________________1______________________________________
def cryptage():
	lettres = "sabircdefghjklmnopktuvwxySABIRCDEFGHJKLMNOPKTUVWXY ÀÂÇÉÈÊËÎÔÛÙ)(_-'&°£*%§.?!:;,5697123840"
	lettres = lettres.decode("utf-8")
	msg = ""
	message=entree.get()
	mp=entree1.get()
	s=0
	if type(mp)==str:
    		for i in mp :
        	    s+=ord(i)
	else:
		s=mp
    	for i in message:
	    if i in lettres:
	    	num = lettres.find(i)
	    	num += s
	    	while num >= len(lettres):
		    	num = num - len(lettres)
	    	msg += lettres[num]
	    else:
	   	msg += i
        crypter.set(msg)
#_________________________________2_________________________________________
def decryptage():
	lettres = "sabircdefghjklmnopktuvwxySABIRCDEFGHJKLMNOPKTUVWXY ÀÂÇÉÈÊËÎÔÛÙ)(_-'&°£*%§.?!:;,5697123840"
	lettres = lettres.decode("utf-8")
	msg = ""
	mp=entre1.get()
	message=entre.get()
	s=0
	if type(mp)==str:
    		for i in mp:
        		s+=ord(i)
	else:
    		s=mp
    	for i in message:
	    if i in lettres:
		    num = lettres.find(i)
		    num -= s
		    while num < 0 :
			    num = num + len(lettres)
		    msg += lettres[num]
	    else:
		    msg += i
	decrypter.set(msg)


fen = Tk()
fen.title(" SABYOUS Cryptage ")

#pour quitter

bou2 = Button(fen,text ='Quitter',fg ='red',command =fen.quit)
bou2.grid(row=9,column=3,columnspan =3)

#Cryptage -----

Label(fen,text='** Cryptage :**',fg ='black').grid(row =0,column=1)
Label(fen,text='Texte à crypter : ',fg ='blue').grid(row =1,sticky =W)
Label(fen,text='Clé de cryptage : ',fg ='blue').grid(row =2,sticky =W)

crypter = StringVar()
crypt1 = Entry(fen,textvariable = crypter)
crypt1.grid(row =3,column =1)
crypter.set("Texte crypté")

entree = Entry(fen,fg='brown')
entree.grid(row =1,column =1)

message = entree.get()

entree1 = Entry(fen,fg ='black',show='*')
entree1.grid(row =2,column =1)

boutton1 = Button(fen,text ='Crypter',fg ='green',command =cryptage)
boutton1.grid(row = 3)


#Decryptage ----

Label(fen,text ='** decryptage **',fg ='black').grid(row =5,column=1)

Label(fen,text ='Texte a décrypter : ',fg ='blue').grid(row =6,sticky =W)
Label(fen,text ='Clé de décryptage : ',fg ='blue').grid(row =7,sticky =W)

entre = Entry(fen,fg ='brown')
entre.grid(row=6,column =1)

entre1 = Entry(fen,fg ='black', show='*')
entre1.grid(row =7,column =1)

decrypter = StringVar()
crypt2 = Entry(fen,textvariable = decrypter)
crypt2.grid(row =8,column=1)
decrypter.set("Texte décrypté")

boutton2 = Button(fen,text ='Décrypter',fg ='red',command=decryptage)
boutton2.grid(row =8,column=0)



fen.mainloop()
fen.destroy()
