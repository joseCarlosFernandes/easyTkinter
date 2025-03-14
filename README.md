<h1>Resumo:</h1><br>
<h3>A biblioteca easyTkinter foi criada para facilitar a criação de telas simples no python, simplificando as funções presentes na biblioteca Tkinter, nativa do python.</h3><br>

<h1>Como utilizar:</h1>
<p>Para utilizar a biblioteca, baixe o arquivo e o adicione no mesmo diretório de seu projeto python, o importando para dentro do código com:</p><br>
<b>#import easyTk</b><br>

<h1>Observações:</h1><br>
<p>A tela criada está numa váriável que sempre tera o nome de <b>screen</b> que é global, logo, caso queira interagir direto nela sem utilizar as funções, basta chamar com <b>easyTk.screen</b></p><br>

<h1>Funções:</h1>
<h2>Funções Create:</h2>
<h3>createScreen():</h3>
<p>A função <b>createScreen()</b> recebe dois parâmetros: title e size, respectivamente. Sendo <b>title</b> o nome da janela e <b>size</b> o tamanho da mesma.<br>O parâmetro <b>size</b> deve ser declarado como uma string da seguinte forma: <br>
"widthxheight+x+y"<br>
  Sendo <b>x</b> e <b>y</b> as coordenadas da tela onde a janela vai abrir
</p>
<br>
<h3>createButton():</h3>
<p>A função <b>createButton()</b> recebe 7 parâmtros: name, text, command, width, height, x e y, respectivamente. Sendo:<br>
    ▶️<b>name:</b> o nome do botão<br>
    ▶️<b>text:</b> o texto que vai aparecer no botão, por exemplo: "Clique"<br>
    ▶️<b>command:</b> a ação que esse botão vai executar<br>
    ▶️<b>width</b> e <b>height</b>: definem o tamanho do botão<br>
    ▶️<b>x</b> e <b>y</b>: definem a posição do botão na tela<br>
  <h3>Sobrecarga de createButton():</h3>
  A sobrecarga da função <b>createButton()</b> foi feita para que o usuário possa passar dentro do parâmetro <b>command</b> suas próprias funções, pois na função padrão, <b>command</b> só aceitava funções da biblioteca Tkinter.<br>
  Para a implementação dessa sobrecarga, foi adicionado mais um parâmetro após <b>y</b>, o parâmetro <b>type</b>, que na chamada da função tem de ser definido como uma string contendo o texto "null", por exemplo:<br>
  <br>
  <b>easyTk.createButton("btn1", "Botão", teste, 20, 3, 30, 50, "null")</b>
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
<p> Essa função tamém recebe dois parâmetros: <b>nameBtn</b> e <b>command</b>, sendo <b>nameBtn</b> o nome do botão e <b>command</b> o novo comando que vai ser atribuído ao botão. Porém, assim como a função <b>createButton()</b> essa tamém possuí uma sobrecarga, para possibilitar o usuário inserir suas próprias funções como comandos.<br>
<h3>Sobrecarga de setBtnCommand():</h3>
  <p> Assim como <b>createButton()</b> essa função também passa a receber um parâmetro identificado como <b>type</b> que deve ser adicionado na chamada da função com uma string contendo o texto "null".</p>
</p>
<br>
<h3>setPosition()</h3>
<p> A função <b>setPosition()</b> se trata de um conjunto de 4 funções, cada uma servindo para alterar a posição de um tipo básico de objeto do Tkinter (Buttons, Texts, Entrys e Labels), cada uam dessas funções recebem 4 parâmetros: <b>name</b>, <b>x</b>, <b>y</b> e <b>type</b>, respectivamente. Sendo:<br>
▶️<b>name:</b> O nome do objeto, por exemplo, o nome do botão que se quer alterar a posição<br>
▶️<b>x</b> e <b>y:</b> definem a posição<br>
▶️<b>type:</b> O identificador das funções, nele exitem 4 opções de strings para serem passadas: "btn", "lbl", "txt" e "etr". É através desse parâmetro que se define para qual tipo básico de obejeto a função vai se referir.<br>
</p>
<br>
<h3>setSize()</h3>
<p>A função <b>setSize()</b> também se trata de um conjunto de 4 funções, cada uma servindo para alterar o tamanho de algo, seja da janela, dos botões, texts ou entrys. Essas funções porém, recebem diferentes parametros entre si.
<h3>Sobrecarga de setSize() para manipular a janela:</h3>
  <p>Essa possuí apenas 2 parâmetros: <b>size</b> e <b>type</b>, sendo <b>type</b> sempre declarado como uma string contendo <b>"win"</b>, que indica que a função usada é a qual manipula a janela.<br>
    Já <b>size</b> sempre deve ser delcarado como <b>"widthxheight+x+y"</b>, indicando primeiro o tamanho e em seguida a posição da janela, ou seja, essa função tamém serve para alterar a posição da janela.
  </p>
<h3>Sobrecarga de setSize() para manipular Buttons e Text:</h3>
  <p>As funções <b>setSize()</b> para manipular <b>Buttons</b> e <b>Text</b> possuem os mesmos parâmetros, sendo eles: <b>name</b>, <b>width</b>, <b>height</b> e <b>type</b>, respectivamente. O parâmetro que as diferencia é <b>type</b>, onde, para se manipular <b>Buttons</b> deve se passar <b>"btn"</b> em <b>type</b> e para <b>Text</b> deve se passar <b>"txt".</b></p>
</p>
<h3>Sobrecarga de setSize() para manipular Entry:</h3>
  <p>Diferente das anteriores, essa possuí somente 3 parâmetros, pois uma entry só recebe <b>width</b> em sua criação, logo os parâmetros dessa sobrecarga são: <b>name</b>, <b>width</b> e <b>type</b>, respectivamente. Sendo <b>type</b> declarado sempre como <b>"etr"</b> para indicar que é a função que se refere as entrys.</p>
<br>
<h2>Funções para limpar Text e Entry:</h2>
<h3>cleanText():</h3>
<p>Precisa somente de um parâmetro, chamado de <b>nameText</b>, servindo para identificar de qual Text é para apagar o texto.</p>
<br>
<h3>cleanEntry():</h3>
<p>Precisa somente de um parâmetro, chamado de <b>nameEntry</b>, servindo para identificar de qual Entry é para apagar o texto.</p>
<br>
<h2>Função screenMain()</h2>
<p>Essa função não recebe parâmetros, ela é responsável por chamar a <b>screen.mainloop()</b> que faz com que a janela seja aberta e continue em execução até ser fechada. Deve ser chamada ao final do código.</p>
