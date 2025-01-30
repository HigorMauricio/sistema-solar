from tkinter import*


def Sol():
    #janela
    infoSol = Tk()
    infoSol.minsize(410, 600)
    infoSol.maxsize(410, 600)
    csol = Canvas(infoSol, height=410, width=600, bg='gray5')
    csol.pack(side=LEFT, expand=True, fill=BOTH)
    infoSol.title('Informações acerca do Sol')

    logo = PhotoImage(file=r'imagens\sol.png', master=infoSol)
    logo = logo.subsample(8, 8)
    logo_label = Label(infoSol, image=logo, bg='gray5')
    logo_label.place(x=10, y=10)
    logo_label.image = logo
    Label(infoSol, text='Sol', background='gray5', foreground='white').place(x=33, y=75)
    csol.create_rectangle(390, 39, 90, 44, fill='tan2')
    csol.create_rectangle(42, 105, 47, 580, fill='tan2')

    Label(infoSol, text='É a estrela central do sistema solar,\n'
                        'trata-se da estrela mais próxima do \nplaneta Terra e a maior de todo o \nSistema Solar.'
                        'Todos os outros corpos \ndo sistema solar giram ao seu redor.\n \n \n '
                        'Ele é formado por gases, sendo os\n principais, hidrogênio e hélio e não\n'
                        'dispõe de nenhuma superfície sólida. \n \n \n'
                        'O sol é fonte de luz natural, fornece luz,\ncalor e energia que são muito importantes\n'
                        'para a vida humana, ele produz vitamina D,\n'
                        'que é responsável pela saúde dos dentes\ne ossos.\n\n\n'
                        'Outros seres como plantas dependem do\nSol para alimentação, por meio da\n'
                        'fotossínteses, alem de defender os corpos\ncontra franquezas.\n\n\n'
                        'Seu raio é de 696.340 km;\nSua massa de 1,989 × 10^30 kg;\nGravidade de 274 m/s²;\n'
                        'Sua distância da Terra é de 149.600.000 km.',
          font='rockwell 11', background='gray5', foreground='white', justify=LEFT).place(x=85, y=60)


def Mercurio():
    #janela
    infoMercurio = Tk()
    infoMercurio.minsize(410, 600)
    infoMercurio.maxsize(410, 600)
    cmercurio = Canvas(infoMercurio, height=410, width=600, bg='gray5')
    cmercurio.pack(fill=BOTH, expand=True, side=LEFT)
    infoMercurio.title('Informações acerca de Mercurio')

    #logo
    logoMercurio = PhotoImage(file=r'imagens\mercurio.png', master=infoMercurio)
    logoMercurio = logoMercurio.subsample(8, 8)
    mercurio_label = Label(infoMercurio, image=logoMercurio, bg='gray5')
    mercurio_label.place(x=20, y=20)
    mercurio_label.image = logoMercurio
    cmercurio.create_rectangle(390, 49, 100, 54, fill='sienna4')
    cmercurio.create_rectangle(52, 115, 57, 580, fill='sienna4')
    Label(infoMercurio, text='Mercúrio', background='gray5', foreground='white').place(x=30, y=87)
    #escrita
    Label(infoMercurio, text='É o menor e mais interno planeta do\n'
                             'Sistema Solar. A sua órbita tem a maior\nexcentricidade e o seu eixo apresenta\n'
                             'a menor inclinação em relação a todos\n'
                             'os planetas do Sistema Solar.\n\n\n'
                             'A atmosfera de Mercúrio é basicamente\ncomposta por átomos de árgon, néon\n'
                             'e hélio e apresenta uma pressão muito\nbaixa, cerca de um bilhão de vezes\n'
                             'menor do que a da Terra ao nível do mar.\n\n\n'
                             'Mercúrio é o planeta com o ano mais\ncurto. São necessários 88 dias terrestres\n'
                             'para fazer uma volta completa em torno\ndo Sol\n\n\n'
                             'Seu raio é de 2.439,7 km;\nSua massa de 3,285 × 10^23 kg;\nGravidade de 3,7 m/s²;\n'
                             'Área superficial de 74.800.000 km²;\nTemperatura media de 170°C;\n'
                             'E sua distância do Sol de 58.000.000 km.',
          background='gray5', foreground='white', font='rockwell 11', justify=LEFT).place(x=100, y=80)


def Venus():
    #janela
    infoVenus = Tk()
    infoVenus.minsize(410, 600)
    infoVenus.maxsize(410, 600)
    cvenus = Canvas(infoVenus, height=410, width=600, bg='gray5')
    cvenus.pack(side=LEFT, expand=True, fill=BOTH)
    infoVenus.title('Informações acerca de Vênus')

    #logo
    logovenus = PhotoImage(file=r'imagens\venus.png', master=infoVenus)
    logovenus = logovenus.subsample(8, 8)
    logovenus_label = Label(infoVenus, image=logovenus, bg='gray5')
    logovenus_label.place(x=20, y=20)
    logovenus_label.image = logovenus
    Label(infoVenus, text='Vênus', background='gray5', foreground='white').place(x=33, y=88)
    cvenus.create_rectangle(390, 49, 100, 54, fill='tomato')
    cvenus.create_rectangle(52, 115, 57, 580, fill='tomato')

    #escrita
    Label(infoVenus, text='É o segundo planeta do Sistema Solar,\nem ordem de distância a partir do Sol.\n'
                          'Recebeu seu nome em homenagem à\ndeusa romana do amor e da beleza\n'
                          'Vénus, equivalente a Afrodite.\n\n\n'
                          'Como um planeta rochoso, sua superfície\né composta por vales e altas montanhas,\n'
                          'cheias de vulcões. Vênus é o mais\nbrilhante dos planetas, podendo ser\n'
                          'avistado durante o dia. Isso se deve pelo\nfato do planeta se encontrar coberto por\n'
                          'uma espessa e densa camada quase\nuniforme de nuvens, compostas\n'
                          'predominantemente por ácido sulfúrico\ne dióxido de carbono, que reflectem\n'
                          'a luz solar.\n\n\n'
                          'Seu raio é de 6.051,8 km;\nSua massa é de 4,867 × 10^24 kg;\nGravidade 8,87 m/s²;\n'
                          'Período Orbital de 225 dias;\nTemperatura média de 475° C;\n'
                          'E sua distância do Sol de 108.200.000 km.',
          font='rockwell 11', justify=LEFT, background='gray5', foreground='white').place(x=95, y=80)


def Terra():
    #janela
    infoTerra = Tk()
    infoTerra.minsize(410, 600)
    infoTerra.maxsize(410, 600)
    cterra = Canvas(infoTerra, height=410, width=600, bg='gray5')
    cterra.pack(side=LEFT, expand=True, fill=BOTH)
    infoTerra.title('Informações acerca da Terra')

    #logo
    logoterra = PhotoImage(file=r'imagens\terra.png', master=infoTerra)
    logoterra = logoterra.subsample(8, 8)
    logoterra_label = Label(infoTerra, image=logoterra, bg='gray5')
    logoterra_label.place(x=20, y=20)
    logoterra_label.image = logoterra
    Label(infoTerra, text='Terra', background='gray5', foreground='white').place(x=40, y=90)
    cterra.create_rectangle(390, 53, 100, 58, fill='medium aquamarine')
    cterra.create_rectangle(52, 115, 57, 580, fill='medium aquamarine')

    #escrita
    Label(infoTerra, text='A Terra é o terceiro planeta mais próximo\ndo Sol. Conhecido também como planeta\n'
                          'água por ter cerca de 70% da sua\nsuperfície coberta por água, é o maior\n'
                          'dentre os quatro planetas rochosos que\nfazem parte do Sistema Solar.\n\n\n'
                          'A Terra tem um único e maior satélite\nnatural do Sistema Solar, a Lua, que\n'
                          'influencia fortemente nas marés, em\nvirtude da força gravitacional que existe\n'
                          'entre esses astros. É o único planeta do\nSistema Solar em que existe água em\n'
                          'estado líquido, característica que junto\nao oxigênio e a temperatura média de\n'
                          '14ºC tornam possível a vida no planeta.\nSua estrutura interna é dividida em: crosta\n'
                          'terrestre, manto e núcleo.\n\n\n'
                          'Seu raio é de 6.371 km;\nSua massa é de 5,972 × 10^24 kg;\nGravidade de 9,807 m/s²;\n'
                          'Período orbital de 365 dias;\nPeriodo de rotação de 24 horas;\n'
                          'E sua distanância do Sol de 149.600.000 km.',
          font='rockwell 11', justify=LEFT, background='gray5', foreground='white').place(x=95, y=80)


def Marte():
    #janela
    infoMarte = Tk()
    infoMarte.maxsize(410, 600)
    infoMarte.minsize(410, 600)
    infoMarte.title('Informações acerca de Marte')
    cmarte = Canvas(infoMarte, height=410, width=600, bg='gray5')
    cmarte.pack(side=LEFT, expand=True, fill=BOTH)

    #logo
    logomarte = PhotoImage(file=r'imagens\marte.png', master=infoMarte)
    logomarte = logomarte.subsample(7, 7)
    logomarte_label = Label(infoMarte, image=logomarte, bg='gray5')
    logomarte_label.place(x=20, y=20)
    logomarte_label.image = logomarte
    Label(infoMarte, text='Marte', background='gray5', foreground='white').place(x=40, y=98)
    cmarte.create_rectangle(390, 57, 110, 62, fill='red4')
    cmarte.create_rectangle(55, 123, 60, 580, fill='red4')

    #escrita
    Label(infoMarte, text='Marte é o quarto planeta a partir do Sol,\no segundo menor do Sistema Solar.\n'
                          'Muitas vezes é descrito como o "Planeta\nVermelho", porque o óxido de ferro\n'
                          'predominante em sua superfície lhe dá\numa aparência avermelhada.\n\n\n'
                          'Marte é um dos planetas mais estudados\ndo sistema solar. Podendo ser visto da\n'
                          'Terra a olho nu, ou seja, sem auxílio de\num telescópio. É um planeta muito frio,\n'
                          'árido e rochoso.\n\n\n'
                          'O planeta Marte completa uma volta ao\nredor do próprio eixo em 24 horas e 37\n'
                          'minutos, ao passo que o movimento de\ntranslação demora 687 dias.\n\n\n'
                          'Seu raio é de 3.389,5 km;\nSua massa de 6,39 × 10^23 kg;\nGravidade de 3,721 m/s²;\n'
                          'Área superficial de144.800.000 km²\n'
                          'Temperatura média de −55°C;\nE sua distância do Sol de 227.900.000 km',
          font='rockwell 11', justify=LEFT, background='gray5', foreground='white').place(x=106, y=80)


def Jupter():
    #janela
    infoJupter = Tk()
    infoJupter.maxsize(410, 600)
    infoJupter.minsize(410, 600)
    infoJupter.title('Informações acerca de Júpiter')
    cjupter = Canvas(infoJupter, height=410, width=600, bg='gray5')
    cjupter.pack(fill=BOTH, expand=True, side=LEFT)

    #logo
    logoJupter = PhotoImage(file=r'imagens\jupiter.png', master=infoJupter)
    logoJupter = logoJupter.subsample(7, 7)
    logoJupter_label = Label(infoJupter, image=logoJupter, bg='gray5')
    logoJupter_label.place(x=20, y=20)
    logoJupter_label.image = logoJupter
    Label(infoJupter, text='Júpiter', background='gray5', foreground='white').place(x=40, y=98)
    cjupter.create_rectangle(390, 57, 110, 62, fill='LightPink1')
    cjupter.create_rectangle(55, 123, 60, 580, fill='LightPink1')

    #escrita
    Label(infoJupter, text='Júpiter é o maior planeta do Sistema\nSolar, tanto em diâmetro quanto em\n'
                           'massa, e é o quinto mais próximo\ndo Sol. Ele tem 2,5 vezes a massa de\n'
                           'todos os outros planetas em conjunto.\nÉ um planeta gasoso, junto com Saturno,\n'
                           'Urano e Netuno.\n\n\n'
                           'Júpiter possui o dia mais curto do\nSistema Solar: ele leva apenas cerca\n'
                           'de 10 horas para girar uma volta\ncompleta, em contraponto, Júpiter faz\n'
                           'uma órbita completa ao redor do Sol\nem cerca de 12 anos terrestres\n\n\n'
                           'Júpite tem a presença de nuvens\ncoloridas que pairam na superfície. Tal\n'
                           'coloração é resultado da composição\natmosférica de hidrogênio e hélio\n\n\n'
                           'Seu raio é de 69.911 km;\nSua massa de 1,898 × 10^27 kg;\n'
                           'Gravidade de 24,79 m/s²;\nTemperatura média de -110 °C\n'
                           'E sua Distância do Sol de 778.500.000 km.',
          font='rockwell 11', justify=LEFT, background='gray5', foreground='white').place(x=108, y=80)


def Saturno():
    #janela
    infoSaturno = Tk()
    infoSaturno.maxsize(410, 600)
    infoSaturno.minsize(410, 600)
    infoSaturno.title('Informaçõea acerca de Saturno')
    csaturno = Canvas(infoSaturno, height=410, width=600, bg='gray5')
    csaturno.pack(fill=BOTH, expand=True, side=LEFT)

    #logo
    logoSaturno = PhotoImage(file=r'imagens\saturno.png', master=infoSaturno)
    logoSaturno = logoSaturno.subsample(6, 6)
    logoSaturno_label = Label(infoSaturno, image=logoSaturno, bg='gray5')
    logoSaturno_label.place(x=20, y=20)
    logoSaturno.image = logoSaturno
    Label(infoSaturno, text='Saturno', background='gray5', foreground='white').place(x=45, y=98)
    csaturno.create_rectangle(390, 57, 110, 62, fill='burlywood3')
    csaturno.create_rectangle(65, 123, 70, 580, fill='burlywood3')

    #escrita
    Label(infoSaturno, text='Saturno é o sexto planeta a partir do Sol\ne o segundo maior do Sistema Solar\n'
                            'atrás de Júpiter. Pertencente ao grupo\ndos gigantes gasosos. Seu aspecto mais\n'
                            'característico é seu brilhante sistema\nde anéis, o único visível da Terra.\n\n\n'
                            'Dispõe de 7 conjuntos de anéis\ncircundantes e 82 luas. São formados\n'
                            'por fragmentos de gelo e de rochas\nespaciais, com tamanhos que vão de\n'
                            'um grão de areia até o de uma casa.\n\n\n'
                            'Saturno tem seus polos achatados e\né principalmente formado pelos gases\n'
                            'hidrogênio e hélio\n\n\n'
                            'Seu raio é de 58.232 km;\nSua massa é de 5,683 × 10^26 kg;\n'
                            'Gravidade de 10,44 m/s²;\nTemperatura média de -138ºC;\nTempo orbital de 29 anos;\n'
                            'E distância do Sol de 1,434 × 10^9 km.',
          font='rockwell 11', justify=LEFT, background='gray5', foreground='white').place(x=110, y=87)


def Urano():
    #janela
    infoUrano = Tk()
    infoUrano.maxsize(410, 600)
    infoUrano.minsize(410, 600)
    infoUrano.title('Informações acerca de Urano')
    csaturno = Canvas(infoUrano, height=410, width=600, bg='gray5')
    csaturno.pack(fill=BOTH, expand=True, side=LEFT)

    #logo
    logoUrano = PhotoImage(file=r'imagens\urano.png', master=infoUrano)
    logoUrano = logoUrano.subsample(7, 7)
    logoUrano_label = Label(infoUrano, image=logoUrano, bg='gray5')
    logoUrano_label.place(x=20, y=20)
    logoUrano_label.image = logoUrano
    Label(infoUrano, text='Urano', background='gray5', foreground='white').place(x=43, y=98)
    csaturno.create_rectangle(390, 57, 110, 62, fill='cadet blue')
    csaturno.create_rectangle(60, 123, 65, 580, fill='cadet blue')

    #escrita
    Label(infoUrano, text='Urano é o sétimo planeta a partir do Sol\ne o terceiro maior. É um planeta gasoso\n'
                          'formado principalemnte por hidrogênio\ne hélio.\n\n\n'
                          'É conhecido como gigante de gelo,\njunto a Netuno, por conta da temperatura\n'
                          'média de -197°C e de sua composição.\n\n\n'
                          'Urano dispõe de um conjunto de anéis\nformado por 13 sistemas. Sua coloração\n'
                          'varia de cinza a avermelhada, do sistema\nmais interno ao mais externo.\n\n\n'
                          'O eixo magnético desse planeta tem uma\ngrande inclinação de cerca de 60º com\n'
                          'relação ao seu eixo de rotação.\n\n\n'
                          'Seu raio é de 25.362 km;\nSua massa de 8,681 × 10^25 kg;\n'
                          'Gravidade de 8,87 m/s²;\nPeríodo Orbital de 84 anos;\n'
                          'E sua distância do Sol de 2,871 × 10^9 km.',
          font='rockwell 11', justify=LEFT, background='gray5', foreground='white').place(x=105, y=87)


def Netuno():
    infoNetuno = Tk()
    infoNetuno.maxsize(410, 600)
    infoNetuno.minsize(410, 600)
    infoNetuno.title('Informações acerca de Netuno')
    cnetuno = Canvas(infoNetuno, height=410, width=600, bg='gray5')
    cnetuno.pack(fill=BOTH, expand=True, side=LEFT)

    logonetuno = PhotoImage(file=r'imagens\netuno.png', master=infoNetuno)
    logonetuno = logonetuno.subsample(7, 7)
    logonetuno_label = Label(infoNetuno, image=logonetuno, bg='gray5')
    logonetuno_label.place(x=20, y=20)
    logonetuno_label.image = logonetuno
    Label(infoNetuno, text='Netuno', background='gray5', foreground='white').place(x=43, y=98)
    cnetuno.create_rectangle(390, 57, 110, 62, fill='medium blue')
    cnetuno.create_rectangle(60, 123, 65, 580, fill='medium blue')

    Label(infoNetuno, text='Netuno é o oitavo e ultimo planeta do\nSistema Solar a partir do Sol, possui um\n'
                           'tamanho ligeiramente menor que o de\nUrano, mas maior massa. Sua atmosfera\n'
                           'é feita de hidrogênio, hélio e também\n'
                           'metano.\n\n\n'
                           'A principal lua de Netuno é Titã que\ntem como peculiar sua orbita que é no\n'
                           'sentido contrário  do planeta. Ao todo\nNetuno tem 13 luas, sendo noemadas a\n'
                           'partir de nomes da mitologia grega.\n\n\n'
                           'Por conta das peculiaridades do núcleo\ne atmosfera, Netuno também é chamado\n'
                           'de gigante de gelo.\n\n\n'
                           'Seu raio é de 24.622 km;\nSua massa de 1,024 × 10^26 kg;\n'
                           'Gravidade de 11,15 m/s²;\nTemperatura média de -223 ºC;\n'
                           'Tempo orbital de 165 anos;\nE distância do Sol de 4,495 × 10^9 km.',
          font='rockwell 11', justify=LEFT, background='gray5', foreground='white').place(x=107, y=87)


janela = Tk()
janela.title('Sistema Solar')
canva = Canvas(janela, height=1080, width=1920)
canva.pack(side=LEFT, expand=True, fill=BOTH)
canva.config(bg='black')

#sol
canva.create_oval(10, 455, 200, 265, fill='yellow', outline='')
sol = Label(text='Sol', background='black', foreground='white')
sol.place(x=98, y=460)
soli = PhotoImage(file=r'imagens\sol.png')
soli = soli.subsample(30, 30)
botaos = Button(janela, image=soli, command=Sol, bd=0, highlightthickness=0, bg='black')
botaos.place(x=79, y=461)

#mercurio
canva.create_oval(210, 200, 250, 240, fill='saddle brown', outline='')
mercurio = Label(text='Mercurio', background='black', foreground='white')
mercurio.place(x=203, y=248)
canva.create_oval(-180, 180, 330, 540, fill='', outline='white')
mer = PhotoImage(file=r'imagens\mercurio.png')
mer = mer.subsample(35, 35)
botaom = Button(janela, image=mer, command=Mercurio, bd=0, highlightthickness=0, bg='black')
botaom.place(x=185, y=252)

#vênus
canva.create_oval(470, 320, 390, 400, fill='chocolate3')
venus = Label(text='Vênus', background='black', foreground='white')
venus.place(x=370, y=400)
canva.create_oval(-270, 90, 435, 634, fill='', outline='white')
ven = PhotoImage(file=r'imagens\venus.png')
ven = ven.subsample(35, 35)
botaov = Button(janela, image=ven, command=Venus, bd=0, highlightthickness=0, bg='black')
botaov.place(x=353, y=403)

#terra
canva.create_oval(440, 120, 525, 205, fill='steel blue3')
terra = Label(text='Terra', background='black', foreground='white')
terra.place(x=470, y=215)
canva.create_oval(-430, 20, 570, 724, fill='', outline='white')
ter = PhotoImage(file=r'imagens\terra.png')
ter = ter.subsample(35, 35)
botaot = Button(janela, image=ter, command=Terra, bd=0, highlightthickness=0, bg='black')
botaot.place(x=450, y=217)
#lua
canva.create_oval(510, 110, 520, 120, fill='dim gray')
lua = Label(text='Lua', background='black', foreground='white')
lua.place(x=510, y=90)

#marte
canva.create_oval(610, 500, 680, 570, fill='red4')
canva.create_oval(-1000, -130, 700, 858, fill='', outline='white')
marte = Label(text='Marte', background='black', foreground='white')
marte.place(x=574, y=555)
mar = PhotoImage(file=r'imagens\marte.png')
mar = mar.subsample(35, 35)
botaoma = Button(janela, image=mar, command=Marte, bd=0, highlightthickness=0, bg='black')
botaoma.place(x=557, y=558)

#jupiter
canva.create_oval(760, 215, 880, 335, fill='sandy brown')
canva.create_oval(-1000, -170, 840, 900, fill='', outline='white')
jupter = Label(text='Júpiter', background='black', foreground='white')
jupter.place(x=789, y=345)
jup = PhotoImage(file=r'imagens\jupiter.png')
jup = jup.subsample(35, 35)
botaoj = Button(janela, image=jup, command=Jupter, bd=0, highlightthickness=0, bg='black')
botaoj.place(x=771, y=347)

#saturno
canva.create_oval(910, 470, 1010, 570, fill='burlywood4')
canva.create_oval(-1000, -210, 990, 990, fill='', outline='white')
saturno = Label(text='Saturno', background='black', foreground='white')
saturno.place(x=880, y=560)
sat = PhotoImage(file=r'imagens\saturno.png')
sat = sat.subsample(27, 27)
botaos = Button(janela, image=sat, command=Saturno, bd=0, highlightthickness=0, bg='black')
botaos.place(x=860, y=563)

#urano
canva.create_oval(960, 50, 1050, 140, fill='cornflower blue')
canva.create_oval(-1000, -260, 1120, 1050, fill='', outline='white')
uranu = Label(text='Urano', background='black', foreground='white')
uranu.place(x=990, y=145)
ura = PhotoImage(file=r'imagens\urano.png')
ura = ura.subsample(35, 35)
botaou = Button(janela, image=ura, command=Urano, bd=0, highlightthickness=0, bg='black')
botaou.place(x=973, y=147)

#netuno
canva.create_oval(1220, 320, 1302, 402, fill='midnight blue')
canva.create_oval(-1000, -270, 1270, 1060, fill='', outline='white')
netuno = Label(text='Netuno', background='black', foreground='white')
netuno.place(x=1210, y=407)
net = PhotoImage(file=r'imagens\netuno.png')
net = net.subsample(35, 35)
botaon = Button(janela, image=net, command=Netuno, bd=0, highlightthickness=0, bg='black')
botaon.place(x=1193, y=410)

janela.mainloop()
