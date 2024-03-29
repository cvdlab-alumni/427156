from pyplasm import *

#Definisco le strutture di base per i piloni del ponte (floor0)
quadratoPilone = CUBOID([20,20])
cerchioPilone = CIRCLE(10)([36,36])
cerchiPilone = DIFFERENCE([STRUCT([T(2)(-10)(cerchioPilone),T(2)(10)(cerchioPilone) ]),T([1,2])([-10,-10])(quadratoPilone) ])
pilone = STRUCT([quadratoPilone,T([1,2])([10,10])(cerchiPilone)])

#Il floor0 � composto dalle basi dei piloni
floor0 = STRUCT([pilone,T(1)(90)(pilone)])

#VIEW(piloni)    # FLOOR0

#Definisco le forme necessarie per il profilato delle torri
cerchioTorre = CIRCLE(1)([36,36])
cerchiTorre = STRUCT([cerchioTorre, T(1)(18)(cerchioTorre), T(2)(18)(cerchioTorre), T([1,2])([18,18])(cerchioTorre) ])
quadratoTorre = CUBOID([19,19])
torre = STRUCT([quadratoTorre,T([1,2])([0.5,0.5])(cerchiTorre)])
torri = STRUCT([torre,T(1)(90)(torre)])
strada = CUBOID([270,20])

#Il floor1 � formato dalla base delle torri e dal manto stradale

floor1 = (STRUCT([T([1,2])([0.5,0.5])(torri),floor0, COLOR(BLACK)(T(1)(-80)(strada)) ] ))

#VIEW(COLOR(RED)(floor1))


#Il floor2 contiente le travi orizzontali che vanno da una torre all'altra
trave = CUBOID([70,4])
floor2 = COLOR([0.13,0.01,0.34])(STRUCT([trave, T([2])([12])(trave)]))
#VIEW(floor2)

#Il floor3 rappresenta la proiezione del tetto delle torri
tetto1 = CUBOID([6,19])
tetto2 = CUBOID([19,6])
tetto3 = CUBOID([15,15])
tettoJoin = STRUCT([T(1)(6.5)(tetto1),T(2)(6.5)(tetto2), T([1,2])([2,2])(tetto3)])
tetto = T([1,2])([0.5,0.5])(tettoJoin)
floor3 = COLOR([0.25,0.25,0.25])(STRUCT([tetto,T([1])([90])(tetto)]))

#Creo ls struct building 2.5D
building = STRUCT([COLOR(CYAN)(floor0), COLOR(GREEN)(T(3)(20)(floor1)), T(3)(75)(floor3), T([1,2,3])([20,2,62])(floor2)])
mainfloors = STRUCT([COLOR(CYAN)(floor0), COLOR(GREEN)(floor1), floor3, (T([1,2])([20,2])(floor2))])

VIEW(building)