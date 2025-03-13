import tkinter as tk


#tudo se baseia nessa variável, é o "núcleo"
screen = tk.Tk()

#vetor de botões
btns = {}
base_name_btn = "btn"

#vetor de labels
lbs = {}
base_name_lbs = "lbs"

#vetor de Entrys
etr = {}
base_name_etr = "etr"

#vetor de Texts
txt = {}
base_name_txt = "txt"


#métodos para criar os itens
def createScreen(title,size):
	screen.title(title)
	screen.geometry(size)

def createButton(name, text, command, width, height, x, y):
	cmd = eval(command) #captura o comando em string passado pelo usuário no chamado da função e passa como comando no botão
						#obrigatório passa a string no formato "lambda: nome_funcao(parametro1, parametro2)" para funções com parametros
						#só funciona com funções daqui ou com funções do próprio Tkinter
	name_btn = f"{base_name_btn}_{name}"
	btns[name_btn]= tk.Button(screen, text= text, command= cmd, width= width, height= height)
	btns[name_btn].place(x=x,y=y)

#sobrecarga da função, utilizando essa o usuário consegue passar as proprias funções no command, type tem de ser "null"
#para usar funções com parametros tem de usar "lambda: nome_funcao(parametros)"
def createButton(name, text, command, width, height, x, y,	null="null"):
	name_btn = f"{base_name_btn}_{name}"
	btns[name_btn]= tk.Button(screen, text= text, command= command, width= width, height= height)
	btns[name_btn].place(x=x,y=y)

def createLabel(name, text, x, y):
	name_lbs = f"{base_name_lbs}_{name}"
	lbs[name_lbs] = tk.Label(screen, text=text)
	lbs[name_lbs].place(x=x,y=y)

def createEntry(name, width, x, y):
	name_etr = f"{base_name_etr}_{name}"
	etr[name_etr] = tk.Entry(screen, width=width)
	etr[name_etr].place(x=x,y=y)

def createText(name, width, height, x, y):
	name_txt = f"{base_name_txt}_{name}"
	txt[name_txt] = tk.Text(screen, width=width, height=height)
	txt[name_txt].place(x=x,y=y)

#metodos get
def getText(nameText):
	name_txt = f"{base_name_txt}_{nameText}"
	return txt[name_txt].get("1.0", tk.END)

def getEntry(nameEntry):
	name_etr = f"{base_name_etr}_{nameEntry}"
	return etr[name_etr].get()

#metodos set
def setText(nameText, text):
	name_txt = f"{base_name_txt}_{nameText}"
	txt[name_txt].insert("1.0", text)

def setEntry(nameEntry, text):
	name_etr = f"{base_name_etr}_{nameEntry}"
	etr[name_etr].delete(0, tk.END)
	etr[name_etr].insert(0, text)

def setBtnText(nameBtn, text):
	name_btn = f"{base_name_btn}_{nameBtn}"
	btns[name_btn].config(text=text)

def setLabelText(nameLbl, text):
	name_lbs = f"{base_name_lbs}_{nameLbl}"
	lbs[name_lbs].config(text=text)

def setBtnCommand(nameBtn, command):
	cmd = eval(command) #captura o comando em string passado pelo usuário no chamado da função e passa como comando no botão
						#obrigatório passa a string no formato "lambda: nome_funcao(parametro1, parametro2)" para funções com parametros
						#só funciona com funções daqui ou com funções do próprio Tkinter
	name_btn = f"{base_name_btn}_{nameBtn}"
	btns[name_btn].config(command=cmd)

#sobrecarga da função, utilizando essa o usuário consegue passar as proprias funções no command, type tem de ser "null"
#para usar funções com parametros tem de usar "lambda: nome_funcao(parametros)"
def setBtnCommand(nameBtn, command, type="null"):
	name_btn = f"{base_name_btn}_{nameBtn}"
	btns[name_btn].config(command=command)

#funções para mudar a posição dos itens (sobrecargas da função position)
def setPosition(type="btn", nameBtn, x,y):
	name_btn = f"{base_name_btn}_{nameBtn}"
	btns[name_btn].place(x=x,y=y)

def setPosition(type="lbl", nameLbl, x, y):
	name_lbs = f"{base_name_lbs}_{nameLbl}"
	lbs[name_lbs].place(x=x, y=y)

def setPosition(type="txt", nameText, x, y):
	name_txt = f"{base_name_txt}_{nameText}"
	txt[name_txt].place(x=x,y=y)

def setPosition(type="etr", nameEntry, x, y):
	name_etr = f"{base_name_etr}_{nameEntry}"
	etr[name_etr].place(x=x,y=y)


#funções de limpar as caixas de texto
def cleanText(nameText):
	name_txt = f"{base_name_txt}_{nameText}"
	txt[name_txt].delete("1.0", tk.END)

def cleanEntry(nameEntry):
	name_etr = f"{base_name_etr}_{nameEntry}"
	etr[name_etr].delete(0, tk.END)


#função para chamar mainloop (mantém a tela aberta), tem de ser sempre declarada
def screenMain():
	screen.mainloop()
