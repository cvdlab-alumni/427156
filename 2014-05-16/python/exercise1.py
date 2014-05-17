from pyplasm import *
from scipy import *
from lar2psm import *
from simplexn import *
from larcc import *
from largrid import *
from mapper import *
from boolean import *
from sysml import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])
MAKEMODEL = COMP([STRUCT,MKPOLS])

def aggiungiFinestra(x,y,cubo,arrayFinestre):
    return STRUCT([arrayFinestre, T([1,2,3])([x,y,8])(cubo)])

def spiralStair(thickness=0.2,R=1.,r=0.5,riser=0.1,pitch=2.,nturns=2.,steps=18):
    V,CV = larSolidHelicoid(thickness,R,r,pitch,nturns,steps)()
    W = CAT([[V[k],V[k+1],V[k+2],V[k+3]]+[SUM([V[k+1],[0,0,-riser]]),SUM([V[k+3],[0,0,-riser]])]
        for k,v in enumerate(V[:-4]) if k%4==0])
    for k,w in enumerate(W[:-12]):
        if k%6==0: W[k+1][2]=W[k+10][2]; W[k+3][2]=W[k+11][2]
    nsteps = len(W)/12
    CW =[SUM([[0,1,2,3,6,8,10,11],[6*k]*8])
            for k in range(nsteps)]
    return W,CW

#SALA DA PRANZO
diagramSalaPranzo = assemblyDiagramInit([3,3,2])([[3,50,1],[3,36,1],[1,22]])
hpcSalaPranzo = SKEL_1(STRUCT(MKPOLS(diagramSalaPranzo)))
VSalaPranzo,CVSalaPranzo = diagramSalaPranzo
hpcSalaPranzo = cellNumbering (diagramSalaPranzo,hpcSalaPranzo)(range(len(CVSalaPranzo)),CYAN,2)
#VIEW (hpcSalaPranzo);

#porta

toMergeSalaPranzo = 15     #parete dove va la porta

diagramDoorSalaPranzo2 = assemblyDiagramInit([1,3,2])([[1],[24,10,2],[16,6]]) #se asse x, 1,3,2 su y.
masterSalaPranzo = diagram2cell(diagramDoorSalaPranzo2,diagramSalaPranzo,toMergeSalaPranzo)
hpcSalaPranzo = SKEL_1(STRUCT(MKPOLS(masterSalaPranzo)))
hpcSalaPranzo = cellNumbering (masterSalaPranzo,hpcSalaPranzo)(range(len(masterSalaPranzo[1])),CYAN,15)
#VIEW(hpcSalaPranzo)

toRemoveSalaPranzo = [19,9]    # buco porta
masterSalaPranzo = masterSalaPranzo[0], [cell for k,cell in enumerate(masterSalaPranzo[1]) if not (k in toRemoveSalaPranzo)]

hpcSalaPranzo = SKEL_1(STRUCT(MKPOLS(masterSalaPranzo)))
hpcSalaPranzo = cellNumbering (masterSalaPranzo,hpcSalaPranzo)(range(len(masterSalaPranzo[1])),CYAN,2)
#VIEW(hpcSalaPranzo)
toMergeSalaPranzo2 = 10
diagramDoorSalaPranzo3 = assemblyDiagramInit([3,1,2])([[36,10,4],[1],[16,6]])
masterSalaPranzo2 = diagram2cell(diagramDoorSalaPranzo3,masterSalaPranzo,toMergeSalaPranzo2)
hpcSalaPranzo = SKEL_1(STRUCT(MKPOLS(masterSalaPranzo2)))
hpcSalaPranzo = cellNumbering (masterSalaPranzo2,hpcSalaPranzo)(range(len(masterSalaPranzo2[1])),CYAN,20)
VIEW(hpcSalaPranzo)
toRemoveSalaPranzo2 = [22]    # buco porta
masterSalaPranzo2 = masterSalaPranzo2[0], [cell for k,cell in enumerate(masterSalaPranzo2[1]) if not (k in toRemoveSalaPranzo2)]


DRAW(masterSalaPranzo2)
plasmSalaPranzo = MAKEMODEL(masterSalaPranzo2)


#CUCINA
diagramCucina = assemblyDiagramInit([3,3,2])([[3,40,1],[1,28,1],[1,22]])
hpcCucina = SKEL_1(STRUCT(MKPOLS(diagramCucina)))
VCucina,CVCucina = diagramCucina
hpcCucina = cellNumbering (diagramCucina,hpcCucina)(range(len(CVCucina)),CYAN,2)
#VIEW(hpcCucina)

toMergeCucina = 7     #parete dove va la porta
diagramDoorCucina2 = assemblyDiagramInit([3,1,2])([[26,10,4],[1],[16,6]]) #se asse x, 1,3,2 su y.
masterCucina = diagram2cell(diagramDoorCucina2,diagramCucina,toMergeCucina)
hpcCucina = SKEL_1(STRUCT(MKPOLS(masterCucina)))
hpcCucina = cellNumbering (masterCucina,hpcCucina)(range(len(masterCucina[1])),CYAN,2)
#VIEW(hpcCucina)
toRemoveCucina = [19,8]    # buco porta
masterCucina = masterCucina[0], [cell for k,cell in enumerate(masterCucina[1]) if not (k in toRemoveCucina)]
DRAW(masterCucina)
plasmCucina = MAKEMODEL(masterCucina)

#SALONE
diagramSalone = assemblyDiagramInit([3,3,2])([[1,38,1],[3,52,1],[1,22]])
hpcSalone = SKEL_1(STRUCT(MKPOLS(diagramSalone)))
VSalone,CVSalone = diagramSalone
hpcSalone = cellNumbering (diagramSalone,hpcSalone)(range(len(CVSalone)),CYAN,2)
#VIEW(hpcSalone)

toMergeSalone = 11     #parete dove va la porta
diagramDoorSalone2 = assemblyDiagramInit([3,1,2])([[2,10,26],[1],[16,6]]) #se asse x, 1,3,2 su y.
masterSalone = diagram2cell(diagramDoorSalone2,diagramSalone,toMergeSalone)
hpcSalone = SKEL_1(STRUCT(MKPOLS(masterSalone)))
hpcSalone = cellNumbering (masterSalone,hpcSalone)(range(len(masterSalone[1])),CYAN,2)
#VIEW(hpcSalone)
toRemoveSalone = [19,9]    # buco porta
masterSalone = masterSalone[0], [cell for k,cell in enumerate(masterSalone[1]) if not (k in toRemoveSalone)]
DRAW(masterSalone)
plasmSalone = MAKEMODEL(masterSalone)

#BAGNO_3
diagramBagno_3 = assemblyDiagramInit([3,3,2])([[3,23,1],[1,10,1],[1,22]])
hpcBagno_3 = SKEL_1(STRUCT(MKPOLS(diagramBagno_3)))
VBagno_3,CVBagno_3 = diagramBagno_3
hpcBagno_3 = cellNumbering (diagramBagno_3,hpcBagno_3)(range(len(CVBagno_3)),CYAN,2)
#VIEW(hpcBagno_3)

toMergeBagno_3 = 15     #parete dove va la porta
diagramDoorBagno_32 = assemblyDiagramInit([1,3,2])([[1],[1,8,1],[16,6]]) #se asse x, 1,3,2 su y.
masterBagno_3 = diagram2cell(diagramDoorBagno_32,diagramBagno_3,toMergeBagno_3)
hpcBagno_3 = SKEL_1(STRUCT(MKPOLS(masterBagno_3)))
hpcBagno_3 = cellNumbering (masterBagno_3,hpcBagno_3)(range(len(masterBagno_3[1])),CYAN,2)
#VIEW(hpcBagno_3)
toRemoveBagno_3 = [19,9]    # buco porta
masterBagno_3 = masterBagno_3[0], [cell for k,cell in enumerate(masterBagno_3[1]) if not (k in toRemoveBagno_3)]
DRAW(masterBagno_3)
plasmBagno_3 = MAKEMODEL(masterBagno_3)

#STUDIO
diagramStudio = assemblyDiagramInit([3,3,2])([[3,40,1],[1,24,3],[1,22]])
hpcStudio = SKEL_1(STRUCT(MKPOLS(diagramStudio)))
VStudio,CVStudio = diagramStudio
hpcStudio = cellNumbering (diagramStudio,hpcStudio)(range(len(CVStudio)),CYAN,2)
#VIEW(hpcStudio)

toMergeStudio = 7     #parete dove va la porta
diagramDoorStudio2 = assemblyDiagramInit([3,1,2])([[27,10,3],[1],[16,6]]) #se asse x, 1,3,2 su y.
masterStudio = diagram2cell(diagramDoorStudio2,diagramStudio,toMergeStudio)
hpcStudio = SKEL_1(STRUCT(MKPOLS(masterStudio)))
hpcStudio = cellNumbering (masterStudio,hpcStudio)(range(len(masterStudio[1])),CYAN,2)
#VIEW(hpcStudio)
toRemoveStudio = [19,8]    # buco porta
masterStudio = masterStudio[0], [cell for k,cell in enumerate(masterStudio[1]) if not (k in toRemoveStudio)]
DRAW(masterStudio)
plasmStudio = MAKEMODEL(masterStudio)

#BAGNO_2
diagramBagno_2 = assemblyDiagramInit([3,3,2])([[1,29,1],[1,16,3],[1,22]])
hpcBagno_2 = SKEL_1(STRUCT(MKPOLS(diagramBagno_2)))
VBagno_2,CVBagno_2 = diagramBagno_2
hpcBagno_2 = cellNumbering (diagramBagno_2,hpcBagno_2)(range(len(CVBagno_2)),CYAN,2)
#VIEW(hpcBagno_2)

toMergeBagno_2 = 7     #parete dove va la porta
diagramDoorBagno_22 = assemblyDiagramInit([3,1,2])([[1,8,20],[1],[16,6]]) #se asse x, 1,3,2 su y.
masterBagno_2 = diagram2cell(diagramDoorBagno_22,diagramBagno_2,toMergeBagno_2)
hpcBagno_2 = SKEL_1(STRUCT(MKPOLS(masterBagno_2)))
hpcBagno_2 = cellNumbering (masterBagno_2,hpcBagno_2)(range(len(masterBagno_2[1])),CYAN,2)
#VIEW(hpcBagno_2)
toRemoveBagno_2 = [19,8]    # buco porta
masterBagno_2 = masterBagno_2[0], [cell for k,cell in enumerate(masterBagno_2[1]) if not (k in toRemoveBagno_2)]
DRAW(masterBagno_2)
plasmBagno_2 = MAKEMODEL(masterBagno_2)

#BAGNO_1
diagramBagno_1 = assemblyDiagramInit([3,3,2])([[1,18,1],[1,21,1],[1,22]])
hpcBagno_1 = SKEL_1(STRUCT(MKPOLS(diagramBagno_1)))
VBagno_1,CVBagno_1 = diagramBagno_1
hpcBagno_1 = cellNumbering (diagramBagno_1,hpcBagno_1)(range(len(CVBagno_1)),CYAN,2)
#VIEW(hpcBagno_1)

toMergeBagno_1 = 3     #parete dove va la porta
diagramDoorBagno_12 = assemblyDiagramInit([1,3,2])([[1],[3,10,8],[16,6]]) #se asse x, 1,3,2 su y.
masterBagno_1 = diagram2cell(diagramDoorBagno_12,diagramBagno_1,toMergeBagno_1)
hpcBagno_1 = SKEL_1(STRUCT(MKPOLS(masterBagno_1)))
hpcBagno_1 = cellNumbering (masterBagno_1,hpcBagno_1)(range(len(masterBagno_1[1])),CYAN,2)
#VIEW(hpcBagno_1)
toRemoveBagno_1 = [19,8]    # buco porta
masterBagno_1 = masterBagno_1[0], [cell for k,cell in enumerate(masterBagno_1[1]) if not (k in toRemoveBagno_1)]
DRAW(masterBagno_1)
plasmBagno_1 = MAKEMODEL(masterBagno_1)

#CAMERA_1
diagramCamera_1 = assemblyDiagramInit([3,3,2])([[1,28,3],[1,39,3],[1,22]])
hpcCamera_1 = SKEL_1(STRUCT(MKPOLS(diagramCamera_1)))
VCamera_1,CVCamera_1 = diagramCamera_1
hpcCamera_1 = cellNumbering (diagramCamera_1,hpcCamera_1)(range(len(CVCamera_1)),CYAN,2)
#VIEW(hpcCamera_1)

toMergeCamera_1 = 7     #parete dove va la porta
diagramDoorCamera_12 = assemblyDiagramInit([3,1,2])([[1,8,19],[1],[16,6]]) #se asse x, 1,3,2 su y.
masterCamera_1 = diagram2cell(diagramDoorCamera_12,diagramCamera_1,toMergeCamera_1)
hpcCamera_1 = SKEL_1(STRUCT(MKPOLS(masterCamera_1)))
hpcCamera_1 = cellNumbering (masterCamera_1,hpcCamera_1)(range(len(masterCamera_1[1])),CYAN,2)
#VIEW(hpcCamera_1)
toRemoveCamera_1 = [19,8]    # buco porta
masterCamera_1 = masterCamera_1[0], [cell for k,cell in enumerate(masterCamera_1[1]) if not (k in toRemoveCamera_1)]
DRAW(masterCamera_1)
plasmCamera_1 = MAKEMODEL(masterCamera_1)

#CAMERA_2
diagramCamera_2 = assemblyDiagramInit([3,3,2])([[1,30,3],[1,36,1],[1,22]])
hpcCamera_2 = SKEL_1(STRUCT(MKPOLS(diagramCamera_2)))
VCamera_2,CVCamera_2 = diagramCamera_2
hpcCamera_2 = cellNumbering (diagramCamera_2,hpcCamera_2)(range(len(CVCamera_2)),CYAN,2)
#VIEW(hpcCamera_2)


toMergeCamera_2 = 3     #parete dove va la porta
diagramDoorCamera_22 = assemblyDiagramInit([1,3,2])([[1],[27,8,1],[16,6]]) #se asse x, 1,3,2 su y.
masterCamera_2 = diagram2cell(diagramDoorCamera_22,diagramCamera_2,toMergeCamera_2)
hpcCamera_2 = SKEL_1(STRUCT(MKPOLS(masterCamera_2)))
hpcCamera_2 = cellNumbering (masterCamera_2,hpcCamera_2)(range(len(masterCamera_2[1])),CYAN,2)
#VIEW(hpcCamera_2)
toRemoveCamera_2 = [19,8]    # buco porta
masterCamera_2 = masterCamera_2[0], [cell for k,cell in enumerate(masterCamera_2[1]) if not (k in toRemoveCamera_2)]
DRAW(masterCamera_2)
plasmCamera_2 = MAKEMODEL(masterCamera_2)

#CAMERA_3
diagramCamera_3 = assemblyDiagramInit([3,3,2])([[1,35,3],[3,40,1],[1,22]])
hpcCamera_3 = SKEL_1(STRUCT(MKPOLS(diagramCamera_3)))
VCamera_3,CVCamera_3 = diagramCamera_3
hpcCamera_3 = cellNumbering (diagramCamera_3,hpcCamera_3)(range(len(CVCamera_3)),CYAN,2)
#VIEW(hpcCamera_3)

toMergeCamera_3 = 11     #parete dove va la porta
diagramDoorCamera_32 = assemblyDiagramInit([3,1,2])([[4,8,23],[1],[16,6]]) #se asse x, 1,3,2 su y.
masterCamera_3 = diagram2cell(diagramDoorCamera_32,diagramCamera_3,toMergeCamera_3)
hpcCamera_3 = SKEL_1(STRUCT(MKPOLS(masterCamera_3)))
hpcCamera_3 = cellNumbering (masterCamera_3,hpcCamera_3)(range(len(masterCamera_3[1])),CYAN,2)
#VIEW(hpcCamera_3)
toRemoveCamera_3 = [19,9]    # buco porta
masterCamera_3 = masterCamera_3[0], [cell for k,cell in enumerate(masterCamera_3[1]) if not (k in toRemoveCamera_3)]
DRAW(masterCamera_3)
plasmCamera_3 = MAKEMODEL(masterCamera_3)

#DETTAGLI E MIGLIORAMENTI
modelSalaPranzo = plasmSalaPranzo
modelSalone = T([1,2])([54,14])(plasmSalone)
modelCucina = T([1,2])([10,40])(plasmCucina)
modelBagno_3 = T([1,2])([10,70])(plasmBagno_3)
modelStudio = T([1,2])([10,82])(plasmStudio)
modelBagno_2 = T([1,2])([70,105])(plasmBagno_2)
modelBagno_1 = T([1,2])([81,82])(plasmBagno_1)
modelCamera_1 = T([1,2])([101,82])(plasmCamera_1)
modelCamera_2 = T([1,2])([111,44])(plasmCamera_2)
modelCamera_3 = T([1,2])([94,0])(plasmCamera_3)
modelCorridoio1 = T([1,2])([37,44])(CUBOID([74,38,1]))
modelCorridoio2 = T([1,2])([54,82])(CUBOID([27,43,1]))
parete1 = T([1,2])([70,82])(CUBOID([1,25,23]))
parete2 = CUBOID([3,18,23])
parete2 = T([1,2])([51,107])(DIFFERENCE([parete2,T([2,3])([4,1])(CUBOID([3,10,16]))]))
parete3 = T([1,2])([54,122])(CUBOID([16,3,23]))

finestraX = CUBOID([6,3,10])
finestraY = CUBOID([3,6,10])

finestre = STRUCT([CUBOID([0,0,0])])
finestre = aggiungiFinestra(10,0,finestraX,finestre)
finestre = aggiungiFinestra(0,10,finestraY,finestre)
finestre = aggiungiFinestra(10,52,finestraY,finestre)
finestre = aggiungiFinestra(10,90,finestraY,finestre)
finestre = aggiungiFinestra(84,125,finestraX,finestre)
finestre = aggiungiFinestra(130,109,finestraY,finestre)
finestre = aggiungiFinestra(130,92,finestraY,finestre)
finestre = aggiungiFinestra(142,60,finestraY,finestre)
finestre = aggiungiFinestra(130,28,finestraY,finestre)
finestre = aggiungiFinestra(130,10,finestraY,finestre)
finestre = aggiungiFinestra(72,14,finestraX,finestre)
finestre = aggiungiFinestra(38,0,finestraX,finestre)



modelPiano = STRUCT([modelSalaPranzo,modelCucina,modelBagno_1,modelBagno_2,modelBagno_3,modelSalone,modelStudio,modelCamera_1,modelCamera_2,modelCamera_3,modelCorridoio1,modelCorridoio2,parete1,parete2,parete3,])

modelPiano = DIFFERENCE([modelPiano,T([1,2,3])([53,17,1])(CUBOID([2,22,22]))  ])
modelPiano = DIFFERENCE([modelPiano,finestre])

VIEW(modelPiano)