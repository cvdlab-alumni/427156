from pyplasm import *
from numpy import *
from mapper import *

def crown(params):
   r,R = params
   def crown0(shape=[24,36]):
      V,CV = larIntervals(shape)([0.7*PI,0.7*PI])
      V = translatePoints(V,[-PI/2,0])
      domain = V,CV
      x = lambda V : [(R + r*COS(p[0])) * COS(p[1]) for p in V]
      y = lambda V : [(R + r*COS(p[0])) * SIN(p[1]) for p in V]
      z = lambda V : [-r * SIN(p[0]) for p in V]
      mapping = [x,y,z]
      return larMap(mapping)(domain)
   return crown0

def larPneumatico(params=[4,7]):
   def larPneumatico0(shape=[15,70]):
      V,CV = checkModel(crown(params)(shape))
      return V,CV
   return larPneumatico0

cuboPilone = CUBOID([20,20,20])
cilindroPilone = CYLINDER([10,21])(36)
sottParapetto = CYLINDER([9.5,1])(36)
sottCubo = CUBOID([20,20,21])
cilindroPilone = DIFFERENCE([cilindroPilone,T(3)(20)(sottParapetto)])
cilindriPilone = DIFFERENCE([STRUCT([T(2)(-10)(cilindroPilone),T(2)(10)(cilindroPilone) ]),T([1,2])([-10,-10])(sottCubo) ])
pilone = STRUCT([cuboPilone,T([1,2])([10,10])(cilindriPilone)])
piloni = COLOR(GRAY)(STRUCT([pilone,T(1)(90)(pilone)]))
pianiPiloni = COLOR(GRAY)(STRUCT([piloni,T(3)(18)(piloni)]))

# Strutture "piloni" esterni
corda = STRUCT(MKPOLS(larPneumatico([1.5,60])()))
corda2 = STRUCT([R([3,1])(PI/2)(corda)])
corda3 = STRUCT([R([3,2])(0.24*PI)(corda2)])
corda4 = S(3)(0.8)(corda3)

corde = COLOR([0.13,0.01,0.34])(STRUCT([corda4,T(1)(-15)(corda4)]))
cuboPilExt = T([1,2])([-110,-3])(CUBOID([15,26,40]))
arcoPilExt = T([1,2,3])([-110,0,19.5])(CUBOID([15,20,14]))
arcoPilExt2 = STRUCT([T([1,2,3])([-110,10,33.5])(R([3,1])(PI/2)(CYLINDER([10,15])(36))),arcoPilExt])
cuboPilExt = DIFFERENCE([cuboPilExt,T(3)(6)(S(3)(0.65)(arcoPilExt2))])

pilExt = STRUCT([cuboPilExt,T([1,2,3])([-58,3,75])(R([2,1])(PI/2)(corde))])
pilsExt = COLOR([0.91,0.78,0.57])(STRUCT([pilExt, T([1,2])([110,20])(R([1,2])(PI)(pilExt))]))
pianoPilsExt = DIFFERENCE([cuboPilExt,T([1,2,3])([-110,-3,2])(CUBOID([15,26,16]))])
pianoPilsExt = DIFFERENCE([pianoPilsExt,T([1,2,3])([-110,-3,20])(CUBOID([15,26,18]))])
pianiPilsExt = COLOR([0.91,0.78,0.57])(STRUCT([pianoPilsExt, T([1,2])([110,20])(R([1,2])(PI)(pianoPilsExt))]))

punti_pyramidPil = [[0,0],[0,26],[15,26],[15,0],[0,0]]
poly_pyramidPil = (AA(POLYLINE)([punti_pyramidPil]))
polig_pyramidPil = STRUCT(poly_pyramidPil)

piramidePil = T([1,2,3])([-110,-3,40])(PYRAMID(10)(polig_pyramidPil))
piramidiPil = STRUCT([piramidePil,T([1])([315])(piramidePil)])



cilindroTorre = CYLINDER([1,55])(36)

conoTorre = CONE([1,8])(8)
coniTorre = STRUCT([conoTorre, T(1)(18)(conoTorre), T(2)(18)(conoTorre), T([1,2])([18,18])(conoTorre) ])

punti_pyramid = [[0,0],[0,15],[15,15],[15,0],[0,0]]
poly_pyramid = (AA(POLYLINE)([punti_pyramid]))
polig_pyramid = STRUCT(poly_pyramid)

piramide = PYRAMID(18)(polig_pyramid)

tetto1 = CUBOID([6,19,10])
tetto2 = CUBOID([19,6,10])
tettoJoin = STRUCT([T(1)(6.5)(tetto1),T(2)(6.5)(tetto2), T([1,2])([2,2])(piramide)])
tetto = T([1,2,3])([0.5,0.5,70])(tettoJoin)
tetti = COLOR([0.25,0.25,0.25])(STRUCT([tetto,T([1])([90])(tetto), piramidiPil]))

cilindriTorre = STRUCT([cilindroTorre, T(1)(18)(cilindroTorre), T(2)(18)(cilindroTorre), T([1,2])([18,18])(cilindroTorre) ])
cuboTorre = CUBOID([19,19,50])
torre2 = DIFFERENCE([cuboTorre, T([3])([2])(CUBOID([20,20,46]))])

torr = STRUCT([cuboTorre,T([1,2])([0.5,0.5])(cilindriTorre),T([1,2,3])([0.5,0.5,55])(coniTorre),])

baseArco = CUBOID([19,9,10])
arco1 = STRUCT([T([2,3])([4.5,10])(R([3,1])(PI/2)(CYLINDER([4.5,19])(36))),baseArco])
baseArcoPedonale = CUBOID([2,19,2])
#VIEW(arco1)

torre = DIFFERENCE([torr,T([2])([5])(arco1)])
torri = COLOR([0.91,0.78,0.57])(STRUCT([torre,T([1])([90])(torre)]))
strada = (CUBOID([405,20,2]))
pilons = COLOR(GRAY)(DIFFERENCE([piloni,T(3)(18)(strada)]))

trave = CUBOID([70,4,4])
travi = COLOR([0.13,0.01,0.34])(STRUCT([trave, T([2])([12])(trave)]))
cavo = T([1,2,3])([-40,2,20]) (R([3,1])(PI/4)((CUBOID([1.2,1.2,60]))))
cavi = COLOR([0.13,0.01,0.34])(STRUCT([cavo, T(2)(14.8)(cavo)]))
cavo2 =  T([1,2,3])([148,2,20])(R([1,3])(PI/4)(CUBOID([1.2,1.2,60])))
cavi2 = COLOR([0.13,0.01,0.34])( STRUCT([cavo2, T(2)(14.8)(cavo2)]))


parapetto = T([1,3])([-140,20])(CUBOID([405,0.5,1]))
parapetti = COLOR([0.13,0.01,0.34])(STRUCT([parapetto,T(2)(19.5)(parapetto)]))

finestra = T(3)(40)(CUBOID([20,6,4]))
finestra2 = T(3)(60)(CUBOID([6,20,4]))
finestre = COLOR([0.80,0.67,0.46])((STRUCT([T([1,2])([0,6.5])(finestra),T([1,2])([6.5,0])(finestra2),T([1,2,3])([0,6.5,20])(finestra) ])))
finestre2 = COLOR([0.80,0.67,0.46])((STRUCT([finestre, T(1)(90)(finestre)])))
solid_model_3D = STRUCT([finestre2,parapetti,T([1,2,3])([0.5,0.5,20])(torri),pilons, COLOR([0.1,0.1,0.1])(T([1,3])([-140,18])(strada) ),T([1,2,3])([20,2,62])(travi),pilsExt,tetti])


# WORLD
tronco = (CYLINDER([0.3,7])(12))
chioma = T(3)(8)(S(3)(0.7)(SPHERE(2.4)([24,24])))
albero = STRUCT([COLOR([0.59,0.29,0])(tronco), COLOR(GREEN)(chioma)])

parco = STRUCT([COLOR([0.14,0.61,0.01])(CUBOID([24,24,0.2])),T([1,2])([4,7])(albero),T([1,2])([12,9])(albero),T([1,2])([6,18])(albero),T([1,2])([17,15])(albero)])


fiume = COLOR([0.28,0.4,0.93])(T([1,2])([-100,-620])(CUBOID([310,1240,0.1])))

argine = T([1,2])([210,-620])(CUBOID([150,1240,18]))
argini = STRUCT([argine,T(1)(-460)(argine)])

strisce = STRUCT([CUBOID([.7,5,0.1]),T(2)(20)]*62)
stradaFuori = (STRUCT([COLOR([0.1,0.1,0.1])(T([1,2,3])([265,-620,18])(CUBOID([20,1240,2]))),COLOR(WHITE)(T([1,2,3])([275,-620,20])(strisce)) ]))
stradaFuori2 = STRUCT([COLOR([0.1,0.1,0.1])(T([1,2,3])([-160,-620,18])(CUBOID([20,1240,2]))),COLOR(WHITE)(T([1,2,3])([-150,-620,20])(strisce))])
stradaFuori3 = COLOR([0.1,0.1,0.1])(T([1,2,3])([285,0,18])(CUBOID([75,20,2])))
striscePonte = COLOR(WHITE)(STRUCT([CUBOID([5,.7,0.1]),T(1)(20)]*25))
striscePonte = T([1,2,3])([-140,10,20])(striscePonte)



strade = STRUCT([stradaFuori,stradaFuori2,stradaFuori3,T(2)(-245)(stradaFuori3)])

edif1 = T([1,2,3])([220,-340,18])(CUBOID([25,20,35]))
edif2 = T([1,2,3])([295,180,18])(CUBOID([18,12,30]))
edif3 = T([1,2,3])([295,280,18])(CUBOID([14,10,20]))
edif4 = T([1,2,3])([295,-50,18])(CUBOID([14,20,25]))
edif5 = T([1,2,3])([295,50,18])(CUBOID([14,40,35]))
edif6 = T([1,2,3])([295,150,18])(CUBOID([20,20,35]))
edif7 = T([1,2,3])([295,-150,18])(CUBOID([24,30,28]))
edif8 = STRUCT([T([1,2,3])([295,-200,18])(CUBOID([22,40,15])),T([1,2,3])([295,-200,33])(CUBOID([12,12,12]))])
edif9 = T([1,2,3])([295,-270,18])(CUBOID([24,20,26]))
edif10 = T([1,2,3])([295,-320,18])(CUBOID([16,24,22]))
parco1 = T([1,2,3])([295,-370,18])(parco)

edifici = COLOR([0.4,0.4,0.4])(STRUCT([edif1,edif2,edif3,edif4,edif5,edif6,edif7,edif8,edif9,edif10,parco1 ]))
edifici2 = T(1)(115)(R([1,2])(PI)(edifici))

palo = CYLINDER([.2,10])(12)
luce = COLOR(YELLOW)(SPHERE(.7)([12,12]))
lampione = STRUCT([palo,T(3)(10.5)(luce)])
lampStrada = T([1,2,3])([286,-620,18])(lampione)
lampioni1 = STRUCT([lampStrada,T(2)(20)]*63)
lampioni2 = T(1)(-449)(lampioni1)
lampioni = STRUCT([lampioni1,lampioni2])

modelWorld = STRUCT([fiume,argini, strade, edifici,edifici2,lampioni, striscePonte ])

final_model = STRUCT([solid_model_3D,modelWorld])
VIEW(final_model)

