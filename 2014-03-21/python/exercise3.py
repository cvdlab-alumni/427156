from pyplasm import *
from numpy import *

cuboPilone = CUBOID([20,20,20])
cilindroPilone = CYLINDER([10,21])(36)
sottParapetto = CYLINDER([9.5,1])(36)
sottCubo = CUBOID([20,20,21])
cilindroPilone = DIFFERENCE([cilindroPilone,T(3)(20)(sottParapetto)])
cilindriPilone = DIFFERENCE([STRUCT([T(2)(-10)(cilindroPilone),T(2)(10)(cilindroPilone) ]),T([1,2])([-10,-10])(sottCubo) ])
pilone = STRUCT([cuboPilone,T([1,2])([10,10])(cilindriPilone)])
piloni = COLOR(GRAY)(STRUCT([pilone,T(1)(90)(pilone)]))


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
torr = STRUCT([cuboTorre,T([1,2])([0.5,0.5])(cilindriTorre),T([1,2,3])([0.5,0.5,55])(coniTorre),])

arco = CUBOID([19,9,12])
torre = DIFFERENCE([torr,T([2])([5])(arco)])
torri = COLOR([0.91,0.78,0.57])(STRUCT([torre,T([1])([90])(torre)]))
strada = CUBOID([270,20,2])
pilons = COLOR(GRAY)(DIFFERENCE([piloni,T(3)(18)(strada)]))

trave = CUBOID([70,4,4])
travi = COLOR([0.13,0.01,0.34])(STRUCT([trave, T([2])([12])(trave)]))
cavo = T([1,2,3])([-40,2,20]) (R([3,1])(PI/4)((CUBOID([1.2,1.2,60]))))
cavi = COLOR([0.13,0.01,0.34])(STRUCT([cavo, T(2)(14.8)(cavo)]))
cavo2 =  T([1,2,3])([148,2,20])(R([1,3])(PI/4)(CUBOID([1.2,1.2,60])))
cavi2 = COLOR([0.13,0.01,0.34])( STRUCT([cavo2, T(2)(14.8)(cavo2)]))


parapetto = T([1,3])([-80,20])(CUBOID([270,0.5,1]))
parapetti = COLOR([0.13,0.01,0.34])(STRUCT([parapetto,T(2)(19.5)(parapetto)]))

finestra = T(3)(40)(CUBOID([20,6,4]))
finestra2 = T(3)(60)(CUBOID([6,20,4]))
finestre = COLOR([0.80,0.67,0.46])((STRUCT([T([1,2])([0,6.5])(finestra),T([1,2])([6.5,0])(finestra2),T([1,2,3])([0,6.5,20])(finestra) ])))
finestre2 = COLOR([0.80,0.67,0.46])((STRUCT([finestre, T(1)(90)(finestre)])))

solid_model_3D = STRUCT([finestre2,parapetti,cavi,cavi2,T([1,2,3])([0.5,0.5,20])(torri),pilons, COLOR([0.1,0.1,0.1])(T([1,3])([-80,18])(strada) ),T([1,2,3])([20,2,62])(travi),tetti])

VIEW(solid_model_3D) 