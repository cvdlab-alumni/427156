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


cuboPilone = CUBOID([20,20,1])
cilindroPilone = CYLINDER([10,1])(36)
sottParapetto = CYLINDER([9.5,1])(36)
sottCubo = CUBOID([20,20,1])
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
corde = T([1,2,3])([-58,3,75])(R([2,1])(PI/2)(corde))
corde = STRUCT([corde, T([1,2])([110,20])(R([1,2])(PI)(corde))])
cuboPilExt = T([1,2])([-110,-3])(CUBOID([15,26,40]))
arcoPilExt = T([1,2,3])([-110,0,19.5])(CUBOID([15,20,14]))
arcoPilExt2 = STRUCT([T([1,2,3])([-110,10,33.5])(R([3,1])(PI/2)(CYLINDER([10,15])(36))),arcoPilExt])
cuboPilExt = DIFFERENCE([cuboPilExt,T(3)(6)(S(3)(0.65)(arcoPilExt2))])

pilExt = STRUCT([cuboPilExt,T([1,2,3])([-58,3,75])(R([2,1])(PI/2)(corde))])
pilsExt = COLOR([0.91,0.78,0.57])(STRUCT([pilExt, T([1,2])([110,20])(R([1,2])(PI)(pilExt))]))
pianoPilsExt = DIFFERENCE([cuboPilExt,T([1,2,3])([-110,-3,2])(CUBOID([15,26,16]))])
pianoPilsExt = DIFFERENCE([pianoPilsExt,T([1,2,3])([-110,-3,20])(CUBOID([15,26,18]))])
pianiPilsExt = COLOR([0.91,0.78,0.57])(STRUCT([pianoPilsExt, T([1,2])([110,20])(R([1,2])(PI)(pianoPilsExt))]))
#pilsExt = STRUCT([cuboPilExt2,T(1)(260)(cuboPilExt2),corde])
#VIEW(pilsExt)




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
tetti = COLOR([0.25,0.25,0.25])(STRUCT([tetto,T([1])([90])(tetto)]))

cilindriTorre = STRUCT([cilindroTorre, T(1)(18)(cilindroTorre), T(2)(18)(cilindroTorre), T([1,2])([18,18])(cilindroTorre) ])
cuboTorre = CUBOID([19,19,50])
torre2 = DIFFERENCE([cuboTorre, T([3])([2])(CUBOID([20,20,46]))])

torr = STRUCT([torre2,T([1,2])([0.5,0.5])(cilindriTorre),T([1,2,3])([0.5,0.5,55])(coniTorre),])

baseArco = CUBOID([19,9,10])
arco1 = STRUCT([T([2,3])([4.5,10])(R([3,1])(PI/2)(CYLINDER([4.5,19])(36))),baseArco])
#baseArcoPedonale = CUBOID([2,19,2])
#VIEW(arco1)

torre = DIFFERENCE([torr,T([2])([5])(arco1)])
torri = COLOR([0.91,0.78,0.57])(STRUCT([torre,T([1])([90])(torre)]))
strada = (CUBOID([405,20,2]))
pilons = COLOR(GRAY)(DIFFERENCE([piloni,T(3)(18)(strada)]))

trave = CUBOID([70,4,4])
travi = COLOR([0.13,0.01,0.34])(STRUCT([trave, T([2])([12])(trave)]))
travi = T([1,2,3])([20,2,62])(travi)
cavo = T([1,2,3])([-40,2,20]) (R([3,1])(PI/4)((CUBOID([1.2,1.2,60]))))
cavi = COLOR([0.13,0.01,0.34])(STRUCT([cavo, T(2)(14.8)(cavo)]))
cavo2 =  T([1,2,3])([148,2,20])(R([1,3])(PI/4)(CUBOID([1.2,1.2,60])))
cavi2 = COLOR([0.13,0.01,0.34])( STRUCT([cavo2, T(2)(14.8)(cavo2)]))


parapetto = T([1,3])([-140,20])(CUBOID([405,0.5,1]))
parapetti = COLOR([0.13,0.01,0.34])(STRUCT([parapetto,T(2)(19.5)(parapetto)]))

finestra = T(3)(40)(CUBOID([19,19,2]))
finestra2 = T(3)(60)(CUBOID([19,19,2]))
finestre = COLOR([0.80,0.67,0.46])((STRUCT([T([1,2])([0.5,0.5])(finestra),T([1,2])([0.5,0.5])(finestra2),T([1,2,3])([0.5,0.5,20])(finestra) ])))
finestre2 = COLOR([0.80,0.67,0.46])((STRUCT([finestre, T(1)(90)(finestre)])))


pareteY = T([1,2,3])([1,1,0])(CUBOID([1,18.5,70]))

paretiY = STRUCT([pareteY, T(1)(17.5)(pareteY), T(1)(90)(pareteY), T(1)(107.5)(pareteY)])

pareteY2 = DIFFERENCE([T([1,2])([-110,-3])(CUBOID([1,26,40])),T(3)(6)(S(3)(0.65)(arcoPilExt2))])

paretiY2 = STRUCT([pareteY2, T(1)(15)(pareteY2), T(1)(315)(pareteY2),  T(1)(330)(pareteY2)])

pareteX = T([1,2])([1,0.5])(CUBOID([18.5,1,70]))
paretiX = STRUCT([pareteX, T([1])([90])(pareteX)])
paretiX = STRUCT([paretiX, T(2)(18)(paretiX)])

pareteX2 = T([1,2])([-110,-3])(CUBOID([15,1,40]))
paretiX2 = STRUCT([pareteX2,T(1)(315)(pareteX2)])
paretiX2 = STRUCT([paretiX2,T(2)(25)(paretiX2)])
paretiY = DIFFERENCE([paretiY, T([2,3])([6,19])(S(1)(20)(arco1))])

pareti = COLOR([0.91,0.78,0.57])(STRUCT([paretiX,paretiX2,paretiY,paretiY2]))

solid_model_3D = STRUCT([finestre2,parapetti,T([1,2,3])([0.5,0.5,20])(torri),pianiPiloni, COLOR([0.1,0.1,0.1])(T([1,3])([-140,18])(strada) ),T([1,2,3])([20,2,62])(travi),pianiPilsExt])

# VERTICAL ENCLOSURES
vertical_ecnlosures = STRUCT([pareti, corde,parapetti,travi])

VIEW(vertical_ecnlosures)


