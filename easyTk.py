import tkinter as tk


#tudo se baseia nessa variável, é o "núcleo"
window = tk.Tk()

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
def createWin(title,size):
	window.title(title)
	window.geometry(size)

def createButton(name, text, command, width, height, x, y, type):
	if type == True:
		name_btn = f"{base_name_btn}_{name}"
		btns[name_btn]= tk.Button(window, text= text, command= command, width= width, height= height)
		btns[name_btn].place(x=x,y=y)
	elif type == False:
		cmd = eval(command) 
		name_btn = f"{base_name_btn}_{name}"
		btns[name_btn]= tk.Button(window, text= text, command= cmd, width= width, height= height)
		btns[name_btn].place(x=x,y=y)
	else:
		print("Erro, parametro type não existente")

def createLabel(name, text, x, y):
	name_lbs = f"{base_name_lbs}_{name}"
	lbs[name_lbs] = tk.Label(window, text=text)
	lbs[name_lbs].place(x=x,y=y)

def createEntry(name, width, x, y):
	name_etr = f"{base_name_etr}_{name}"
	etr[name_etr] = tk.Entry(window, width=width)
	etr[name_etr].place(x=x,y=y)

def createText(name, width, height, x, y):
	name_txt = f"{base_name_txt}_{name}"
	txt[name_txt] = tk.Text(window, width=width, height=height)
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

def setBtnCommand(nameBtn, command, type):
	if type == True:
		name_btn = f"{base_name_btn}_{nameBtn}"
		btns[name_btn].config(command=command)
	elif type == False:
		cmd = eval(command) 
		name_btn = f"{base_name_btn}_{nameBtn}"
		btns[name_btn].config(command=cmd)
	else:
		print("Erro, parametro type inexistente")


#função para mudar a posição dos itens

def setPosition(name, x, y, type):
    if type == "btn":
        name_btn = f"{base_name_btn}_{name}"
        btns[name_btn].place(x=x, y=y)
    elif type == "lbl":
        name_lbs = f"{base_name_lbs}_{name}"
        lbs[name_lbs].place(x=x, y=y)
    elif type == "txt":
        name_txt = f"{base_name_txt}_{name}"
        txt[name_txt].place(x=x, y=y)
    elif type == "etr":
        name_etr = f"{base_name_etr}_{name}"
        etr[name_etr].place(x=x, y=y)
    else:
    	print("Erro, tipo desconhecido")

#funções para manipulação de tamanho
def setWindowSize(size): #altera tamanho da janela
	window.geometry(size)

def setSize(name, width, height, type):
	if (height == 0 or height is None) and type == "etr":
		name_etr = f"{base_name_etr}_{name}"
		etr[name_etr].config(width=width)
	else:
		if type=="btn":
			name_btn = f"{base_name_btn}_{name}"
			btns[name_btn].config(width=width, height=height)
		elif type=="txt":
			name_txt = f"{base_name_txt}_{name}"
			txt[name_txt].config(width=width, height=height)
		else:
			return print("Erro, insira um tipo válido")

#funções de limpar as caixas de texto
def cleanText(nameText):
	name_txt = f"{base_name_txt}_{nameText}"
	txt[name_txt].delete("1.0", tk.END)

def cleanEntry(nameEntry):
	name_etr = f"{base_name_etr}_{nameEntry}"
	etr[name_etr].delete(0, tk.END)


#função para chamar mainloop (mantém a tela aberta), tem de ser sempre declarada
def winMain():
	window.mainloop()

def winQuit():
	window.quit()
