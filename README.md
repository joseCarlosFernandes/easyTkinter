<h1>Resumo:</h1><br>
<h3>A biblioteca easyTkinter foi criada para facilitar a criação de telas simples no python, simplificando as funções presentes na biblioteca Tkinter, nativa do python.</h3><br>

<h1>Como utilizar:</h1>
<p>Para utilizar a biblioteca, baixe o arquivo e o adicione no mesmo diretório de seu projeto python, o importando para dentro do código com:</p><br>
<b>#import easyTk</b><br>

<h1>Observações:</h1><br>
<p>A tela criada está numa váriável que sempre tera o nome de <b>window</b> que é global, logo, caso queira interagir direto nela sem utilizar as funções, basta chamar com <b>easyTk.window</b></p><br>
<p>
<b>Para passar funções com parâmetros dentro dos botões (indepente se for createButton() ou setBtnCommand()) use "lamba:" antes da função, independente se é uma função interna da biblioteca ou própria do seu código. Respeitando os formatos, por exemplo para passar uma função interna da biblioteca passe como string de texto "lamba: nome_da_funcao()", já para funções próprias passe sem as " ", como: lambda: sua_funcao() </b>
</p>
<br>
<h1>Funções:</h1>
<h2>Funções Create:</h2>
<h3>createWindow():</h3>
<p>A função <b>createWin()</b> recebe dois parâmetros: title e size, respectivamente. Sendo <b>title</b> o nome da janela e <b>size</b> o tamanho da mesma.<br>O parâmetro <b>size</b> deve ser declarado como uma string da seguinte forma: <br>
"widthxheight+x+y"<br>
  Sendo <b>x</b> e <b>y</b> as coordenadas da tela onde a janela vai abrir
</p>
<br>
<h3>createButton():</h3>
<p>A função <b>createButton()</b> recebe 8 parâmtros: name, text, command, width, height, x, y e type, respectivamente. Sendo:<br>
    ▶️<b>name:</b> o nome do botão<br>
    ▶️<b>text:</b> o texto que vai aparecer no botão, por exemplo: "Clique"<br>
    ▶️<b>command:</b> a ação que esse botão vai executar<br>
    ▶️<b>width</b> e <b>height</b>: definem o tamanho do botão<br>
    ▶️<b>x</b> e <b>y</b>: definem a posição do botão na tela<br>
    ▶️<b>type:</b> esse parâmetro pode receber os valor de <b>False</b> ou <b>True</b> dependendo do que foi passado no <b>command</b>, pois, caso você queira utilizar uma função própria do Tkinter como <b>.quit</b> ou até mesmo uma função dessa própria biblioteca tem de passa-las como uma string de texto (ex: "lamba: createLabel(parametros aqui)") e atribuir <b>False</b> a <b>type</b> na chamada da função. Agora, caso queira passar uma função que está presente dentro do seu código (ou até mesmo de outra biblioteca) define <b>type</b> como <b>True</b> e não passe como string de texto.<br>
</p>
<br>
<h3>createLabel():</h3>
<p>A função <b>createLabel()</b> recebe 4 parâmetros: name, text, x, y, respectivamente. Sendo:<br>
  ▶️<b>name:</b> o nome da label<br>
  ▶️<b>text:</b> o texto da label<br>
  ▶️<b>x</b> e <b>y:</b> definem a posição da label<br>
</p>
<br>
<h3>createEntry():</h3>
<p>
  A função <b>createEntry()</b> recebe 4 parâmetros: name, width, x e y, respectivamente. Sendo:<br>
  ▶️<b>name:</b> o nome do campo Entry<br>
  ▶️<b>width:</b> o tamanho horizontal dela, ou seja, seu comprimento<br>
  ▶️<b>x</b> e <b>y:</b> definem a posição da label<br>
</p>
<br>
<h3>createText()</h3>
<p>
  A função <b>createText</b> recebe 5 parâmetros: name, width, height, x e y, respectivamente. Sendo:<br>
  ▶️<b>name:</b> o nome do campo Text<br>
  ▶️<b>width:</b> o comprimento do campo<br>
  ▶️<b>height:</b> a altura do campo<br>
  ▶️<b>x</b> e <b>y:</b> definem a posição do campo Text<br>
</p>
<br>
<h2>Funções GET:</h2>
<p>Existem duas funções <b>get</b> na biblioteca, usadas para "capturar" os valores inseridos nas Entrys e nos Text pelos usuários.</p><br>
<h3>getText():</h3>
<p>
  A função <b>getText()</b> possuí somente 1 parâmetro, chamado de <b>nameText</b>, sendo ele o nome do campo Text que se deseja capturar o valor.
</p>
<br>
<h3>getEntry():</h3>
<p>
  A função <b>getEntry()</b> também possuí somente 1 parâmetro, chamado de <b>nameEntry</b>, sendo ele o nome do campo Entry que se deseja capturar o valor.
</p>
<br>
<h2>Funções SET:</h2>
<p>Existem 10 funções <b>set</b> na biblioteca, usadas para alterar valores de texto, posição, comandos (no caso dos botões) e tamanho. 4 dessas funções são sobrecargas.</p>
<br>
<h3>setText():</h3>
<p>A função possuí 2 parâmetros: nameText e text, respectivamente. Sendo <b>nameText</b> o nome do campo Text do qual se deseja alterar o valor, e <b>text</b> o valor pelo qual se deseja substituir. Ambos os valores são strings.</p>
<br>
<h3>setEntry():</h3>
<p> A função possuí 2 parâmetro, similares aos da função anterior, sendo: nameEntry e text, respectivamente. <b>nameEntry</b> se refere ao nome da Entry da qual se deseja alterar o valor, e <b>text</b> o valor pelo qual se deseja substituir.</p>
<br>
<h3>setBtnText():</h3>
<p> Como as anteriores, essa função também recebe dois parâmetros: <b>nameBtn</b> e <b>text</b> que possuem o mesmo propósito das anteriores.</p>
<br>
<h3>setLabelText():</h3>
<p> Assim tamém, essa função também recebe dois parâmetros: <b>nameLbl</b> e <b>text</b> que possuem o mesmo propósito das anteriores.</p>
<br>
<h3>setBtnCommand():</h3>
<p> Essa função recebe três parâmetros: <b>nameBtn</b>, <b>command</b> e <b>type</b>, respectivamente, sendo <b>nameBtn</b> o nome do botão e <b>command</b> o novo comando que vai ser atribuído ao botão. Aqui <b>type</b> possuí a mesma função que em <b>createButton()</b> e também aceita somente os valores de <b>False</b> e <b>True</b>.<br>
</p>
<br>
<h3>setPosition()</h3>
<p> A função <b>setPosition()</b> se trata de um conjunto de 4 condicionais, cada uma servindo para alterar a posição de um tipo básico de objeto do Tkinter (Buttons, Texts, Entrys e Labels), essa função recebe 4 parâmetros: <b>name</b>, <b>x</b>, <b>y</b> e <b>type</b>, respectivamente. Sendo:<br>
▶️<b> name:</b> O nome do objeto, por exemplo, o nome do botão que se quer alterar a posição<br>
▶️<b> x</b> e <b>y:</b> definem a posição<br>
▶️<b> type:</b> O identificador das funções, nele exitem 4 opções de strings para serem passadas: "btn", "lbl", "txt" e "etr". É através desse parâmetro que se define para qual tipo básico de obejeto a função vai se referir.<br>
</p>
<br>
<h3>setSize()</h3>
<p>A função <b>setSize()</b> se trata de um conjunto de 3 condicionais, cada uma servindo para alterar o tamanho de algo, seja dos botões, texts ou entrys. Essa função porém, recebe 4 parâmetros: <b>name</b>, <b>width</b>, <b>height</b> e <b>type</b>. Sendo:
  ▶️<b> name</b>: o nome do botão, text ou entry <br>
  ▶️<b> width:</b>: o comprimento <br>
  ▶️<b> height</b>: a altura (no caso de entrys, pode-se não declarar na chamada da função) <br>
  ▶️<b> type</b>: define qual o tipo do objeto que vai ser manipulado, deve ser passado como string no final da chamada da função e suporta: "btn", "txt", "etr", cada uma relacionada a um tipo. <br>
</p>
<h3>setWindowSize():</h3>
  <p>Se trata da função para manipular o tamanho da janela, recebe 1 parâmetro chamado de <b>size</b>, que deve ser declarado no formato "width x height+x+y", sendo <b>x</b> e <b>y</b> relacionados a posição da janela, ou seja essa função também manipula a posição da janela na tela.<br>
  </p>
<br>
<h2>Funções para limpar Text e Entry:</h2>
<h3>cleanText():</h3>
<p>Precisa somente de um parâmetro, chamado de <b>nameText</b>, servindo para identificar de qual Text é para apagar o texto.</p>
<br>
<h3>cleanEntry():</h3>
<p>Precisa somente de um parâmetro, chamado de <b>nameEntry</b>, servindo para identificar de qual Entry é para apagar o texto.</p>
<br>
<h2>Função winMain()</h2>
<p>Essa função não recebe parâmetros, ela é responsável por chamar a <b>screen.mainloop()</b> que faz com que a janela seja aberta e continue em execução até ser fechada. Deve ser chamada ao final do código.</p>
<br>
<h2>Função winQuit()</h2>
<p>Essa função não recebe parâmetros e serve para fechar a janela</p>
