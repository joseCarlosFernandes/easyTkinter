import easyTk

def teste():
	print("teste")

def teste2(n):
	print(n)

#uso das creates

#criando a janela
easyTk.createWindow("win1","500x500+500+200")

#criando os botões (funções sem parâmetros)
easyTk.createButton("btn1", "Button 1", "window.quit", 20, 3, 30, 50, False) #com função do tkinter ou interna da biblioteca
easyTk.createButton("btn2", "Button 2", teste, 20, 3, 30, 100, True) #com função local
#criando os botões (funções com parâmetros)
easyTk.createButton("btn3", "Button 1", "lambda: getText('txt1')", 20, 3, 30, 150, False) #com função do tkinter ou interna da biblioteca
easyTk.createButton("btn4", "Button 2", lambda: teste2("teste2"), 20, 3, 30, 200, True) #com função local

#criando Label
easyTk.createLabel("lbl1", "show of balls", 30, 5)

#criando uma Entry
easyTk.createEntry("etr1", 50, 30, 250)

#criando um Text
easyTk.createText("txt1", 40, 10, 30, 270)

#usando as funções set 

easyTk.setText("txt1", "texto set")
easyTk.setEntry("etr1", "entry set")
easyTk.setBtnText("btn1", "texto set btn")
#funções sem parâmetros nos botões
easyTk.setBtnCommand("btn1", "window.withdraw", False) #com função do tkinter ou interna da biblioteca
easyTk.setBtnCommand("btn2", teste, True) #com função local
#funções com parâmetros nos botões
easyTk.setBtnCommand("btn3", "lambda: getEntry('etr1')", False) #com função do tkinter ou interna da biblioteca
easyTk.setBtnCommand("btn3", lambda: teste2("teste2 set"), True) #com função local

#diferentes setPositions
easyTk.setPosition("btn1", 100, 50, "btn") #posição de buttons
easyTk.setPosition("lbl1", 100, 50, "lbl") #posição de labels
easyTk.setPosition("txt1", 100, 50, "txt") #posição de texts
easyTk.setPosition("etr1", 100, 50, "etr") #posição de entrys

#trocando o tamanho da janela
easyTk.setWindowSize("700x700+500+200")

#trocando o tamanho dos objetos
easyTk.setSize("btn1", 30, 6, "btn") #alterar tamanho de botões
easyTk.setSize("txt1", 50, 20, "txt") #alterar tamanho de texts
easyTk.setSize("etr1", 70, None ,"etr") #altera tamanho de entrys

easyTk.winMain()