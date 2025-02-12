import maya.cmds as mc

def createTrainTrack():
    pass

def createLocomotiveWheel():
    pass

def createLocomotive():
    pass

def create2ndCar():
    pass

def booleanLocomotive():
    pass

def booleanCar():
    pass

def createWindows():
    pass

def addGlassDomeAndFittings():
    pass

MOVER = 1

def main():
    trainTrackSections = input("How many sections would you like? Each one has 5 ties")
    cars = input("How many cars would you like between the locomotives?")
    zTrackSetMover = 0
    zWheelMover = 0
    wheelSetLst = []
    for i in range(int(trainTrackSections)):
        trackSection_grp = createTrainTrack()
        mc.move(0, 0, zTrackSetMover, trackSection_grp)
        zTrackSetMover += 270

    for i in range(0,int(cars) + 2):
        for j in range(0, 4):
            if j == 0:
                z = -81.354
            if j == 1:
                z = -9.301
            if j == 2:
                z = 785.389
            if j == 3:
                z = 857.442
            wheel_grp = createLocomotiveWheel()
            mc.move(0, -20.214, z, wheel_grp)
            wheelSetLst.append(wheel_grp)

        wheelSet_pyGroup = mc.group(wheelSetLst[0])
        for j in range(1, len(wheelSetLst)):
            mc.parent(wheelSetLst[j], wheelSet_pyGroup)

        mc.move(0, 0, zWheelMover, wheelSet_pyGroup)
        zWheelMover += 1296.217
        wheelSetLst.clear()

    booleanLocomotive()
    booleanCar()

    MOVER = 1
    for i in range(0,(int(cars) - 1)):
        booleanCar()
        mc.move(0, 0, 1300 * MOVER)
        MOVER += 1

    booleanLocomotive()
    mc.scale(1,1,-1)
    mc.move(0, 0, 1310 * (MOVER + 1))
    createWindows()

    ear = mc.polyCylinder(r=27.497, h=47.964, sx=20, sz=4, rcp=True)
    mc.select(ear)
    mc.move(-102.394, 295.917, 28.151)
    mc.rotate(90, 0, 0)

    ear = mc.polyCylinder(r=27.497, h=47.964, sx=20, sz=4, rcp=True)
    mc.select(ear)
    mc.move(102.394, 295.917, 28.151)
    mc.rotate(90, 0, 0)

    ear = mc.polyCylinder(r=27.497, h=47.964, sx=20, sz=4, rcp=True)
    mc.select(ear)
    mc.move(-102.394, 295.917, 4628)
    mc.rotate(90, 0, 0)

    ear = mc.polyCylinder(r=27.497, h=47.964, sx=20, sz=4, rcp=True)
    mc.select(ear)
    mc.move(102.394, 295.917, 4628)
    mc.rotate(90, 0, 0)



    mc.select(all=True)

def booleanLocomotive():
    locomotiveBase = createLocomotive()

    wheelWellNegation = mc.polyCube(w=47.1, h=36.2, d=141)
    mc.move(-85.098, 50.484, -46.390)
    booleanedLocomotiveFL = mc.polyCBoolOp(locomotiveBase, wheelWellNegation, op=2)

    wheelWellNegation2 = mc.polyCube(w=47.1, h=36.2, d=141)
    mc.move(85.098, 50.484, -46.390)
    booleanedLocomotiveFR = mc.polyCBoolOp(booleanedLocomotiveFL, wheelWellNegation2, op=2)

    wheelWellNegation3 = mc.polyCube(w=47.1, h=36.2, d=141)
    mc.move(-85.098, 50.484, 822.445)
    booleanedLocomotiveBL = mc.polyCBoolOp(booleanedLocomotiveFR, wheelWellNegation3, op=2)

    wheelWellNegation4 = mc.polyCube(w=47.1, h=36.2, d=141)
    mc.move(85.098, 50.484, 822.445)
    mc.polyCBoolOp(booleanedLocomotiveBL, wheelWellNegation4, op=2)

    return locomotiveBase


def booleanCar():
    car = create2ndCar()
    zMover = + 1298.522

    wheelWellNegation = mc.polyCube(w=47.1, h=36.2, d=141)
    mc.move(-85.098, 50.484, -46.390 + zMover)
    booleanedCarFL = mc.polyCBoolOp(car, wheelWellNegation, op=2)

    wheelWellNegation2 = mc.polyCube(w=47.1, h=36.2, d=141)
    mc.move(85.098, 50.484, -46.390 + zMover)
    booleanedCarFR = mc.polyCBoolOp(booleanedCarFL, wheelWellNegation2, op=2)

    wheelWellNegation3 = mc.polyCube(w=47.1, h=36.2, d=141)
    mc.move(-85.098, 50.484, 822.445 + zMover)
    booleanedCarBL = mc.polyCBoolOp(booleanedCarFR, wheelWellNegation3, op=2)

    wheelWellNegation4 = mc.polyCube(w=47.1, h=36.2, d=141)
    mc.move(85.098, 50.484, 822.445 + zMover)
    mc.polyCBoolOp(booleanedCarBL, wheelWellNegation4, op=2)

    return car

def createTrainTrack():
    width = 0
    height = 0
    x = 79
    y = 0
    z = 0
    zMove = 0
    xMove = 0
    trackPieces = []
    spikePlateAssembly = []

    #Create ties
    for i in range(0, 5):
        trackPieces.append(mc.polyCube(w=244, h=23, d=18, name='railTie_geo'))
        mc.move(0, 0, z)
        z += -54

    #Create Rails
    z = -108
    for i in range(0, 6):
        if i == 0:
            width = 14
            height = 2
            y = 12.75

        elif i == 2:
            width = 2
            height = 8
            y = 17.5

        elif i == 4:
            width = 7
            height = 4
            y = 23.5

        trackPieces.append(mc.polyCube(w=width, h=height, d=270, name = 'railPiece_geo'))
        x *= -1
        mc.move(x, y, z)

    #Group ties and rails
    trainTrackSection_pyGrp = mc.group(trackPieces[0], name = 'trainTrackSection_grp')
    for i in range(1, len(trackPieces)):
        mc.parent(trackPieces[i], trainTrackSection_pyGrp)

    #Create Spike Plate Assembly
    for j in range(0, 4):
        z = -216
        if j == 0:
            width = 10
            height = 1
            x = 91
            y = 12

        elif j == 1:
            width = 5
            height = .5
            x = 88.5
            y = 12.75

        elif j == 2:
            width = 2
            height = .5
            x = 85
            y = 13.75

        elif j == 3:
            width = 5
            height = 1
            x = 88.5
            y = 13.5

        spikePlateAssembly.append(mc.polyCube(w=width, h=height, d=16, name = 'platePiece_geo'))
        mc.move(x, y, z)

    # Create Spike Heads
    width = 2.4
    height = 2.4
    x = 93.5
    y = 14.502

    for j in range(0, 2):
        if j == 0:
            z = -220
        elif j == 1:
            z = -212

        spikePlateAssembly.append(mc.polyCube(w=width, h=height, d=2.4, name = 'spikeHead_geo'))
        mc.move(x, y, z)

    # Create Washers
    x = 93.394
    y = 12.5

    for j in range(0, 3):
        if j == 0:
            z = -220

        elif j == 1:
            z = -212

        elif j == 2:
            x = 88
            y = 14
            z = -216

        spikePlateAssembly.append(mc.polyTorus(r=1.7, sr=.8, sx=12, sy=12, name = 'washer_geo'))
        mc.move(x, y, z)

    # Create bolt
    x = 88
    y = 15.8
    z = -216

    spikePlateAssembly.append(mc.polyPipe(r=2, h=4, t=1, sa=6, name = 'bolt_geo'))
    mc.move(x, y, z)

    # Create screw
    x = 88
    y = 16.467
    z = -216

    spikePlateAssembly.append(mc.polyCylinder(r=1, h=2, sx=12, name = 'screw_geo'))
    mc.move(x, y, z)

    # Group assembly
    spikePlateAssembly_pyGroup = mc.group(spikePlateAssembly[0])
    # Print out variables to check
    for i in range(1, len(spikePlateAssembly)):
        mc.parent(spikePlateAssembly[i], spikePlateAssembly_pyGroup)
    mc.parent(spikePlateAssembly_pyGroup, trainTrackSection_pyGrp)

    # Create remaining spike groups
    zMove = 54
    x = 0
    z = 0
    y = 0
    for i in range(0, 19):
        if i < 4:
            mc.duplicate(spikePlateAssembly_pyGroup)
            mc.move(x, y, (z + zMove), spikePlateAssembly_pyGroup)
            zMove += 54
        if 3 < i < 9:
            xMove = -24
            if i == 4:
                zMove = 0
            mc.duplicate(spikePlateAssembly_pyGroup)
            mc.scale(-1, 1, 1, spikePlateAssembly_pyGroup)
            mc.move((x + xMove), y, (z + zMove), spikePlateAssembly_pyGroup)
            zMove += 54
        if 8 < i < 14:
            xMove = -158
            if i == 9:
                zMove = 0
            mc.duplicate(spikePlateAssembly_pyGroup)
            mc.scale(1, 1, 1, spikePlateAssembly_pyGroup)
            mc.move((x + xMove), y, (z + zMove), spikePlateAssembly_pyGroup)
            zMove += 54
        if 13 < i < 19:
            xMove = -182
            if i == 14:
                zMove = 0
            mc.duplicate(spikePlateAssembly_pyGroup)
            mc.scale(-1, 1, 1, spikePlateAssembly_pyGroup)
            mc.move((x + xMove), y, (z + zMove), spikePlateAssembly_pyGroup)
            zMove += 54

    return trainTrackSection_pyGrp

def createLocomotiveWheel():
    wheelAssembly = []
    wheelGroup = []
    mirrorVal = 1
    nameExtender = ''

    for i in range (0,2):

        wheelAssembly.clear()


        if i == 1:
            mirrorVal = -1
            nameExtender = 'Mirrored'

        wheelAssembly.append(mc.polyCylinder(r=45, h=4, sx=20, sy=1, sz=1, name='wheelRim' + nameExtender))
        mc.scale((.5 * mirrorVal),1,.5)
        mc.rotate(90, 90, 0)

        wheelAssembly.append(mc.polyPipe(r=40, h=10, t=4.5, sa=20, name='wheelRimCatch' + nameExtender))
        mc.rotate(90, 90, 0)
        mc.scale((.5 * mirrorVal),1,.5)
        mc.move((4.5 * mirrorVal), 0, 0)

        wheelAssembly.append(mc.polyPipe(r=36, h=10, t=11, sa=20, name='wheelRimInner' + nameExtender))
        mc.rotate(90, 90, 0)
        mc.scale((.5 * mirrorVal),1,.5)
        mc.move((2.5 * mirrorVal), 0, 0)

        wheelAssembly.append(mc.polyPipe(r=26, h=4, t=9, sa=20, name='wheelRimInnerInner' + nameExtender))
        mc.rotate(90, 90, 0)
        mc.scale((.5 * mirrorVal),1,.5)
        mc.move((2.5 * mirrorVal), 0, 0)

        wheelAssembly.append(mc.polyCylinder(r=13, h=8, sx=20, sy=1, sz=1, name='wheelRimInnerInnerInner' + nameExtender))
        mc.rotate(90, 90, 0)
        mc.scale((.5 * mirrorVal),1,.5)
        mc.move((2.5 * mirrorVal), 0, 0)

        wheelAssembly.append(mc.polyCylinder(r=10, h=6, sx=20, sy=1, sz=1, name='wheelAxleHousing' + nameExtender))
        mc.rotate(90, 90, 0)
        mc.scale((.5 * mirrorVal),1,.5)
        mc.move((7.5 * mirrorVal), 0, 0)

        wheelAssemblyGrp = mc.group(wheelAssembly[0], name='wheel_grp' + nameExtender)

        for i in range(1, len(wheelAssembly)):
            mc.parent(wheelAssembly[i], wheelAssemblyGrp)

        mc.move((73.5 * mirrorVal), 65.560, 0, wheelAssemblyGrp)

        wheelGroup.append(wheelAssemblyGrp)

    axle = mc.polyCylinder(r=4, h=182, sx=20, sy=1, sz=1, name='wheelAxle')
    mc.rotate(90, 90, 0)
    mc.move(0, 65.579, 0)
    wheel_grp = mc.group(wheelGroup[0], wheelGroup[1], name='wheel_grp')
    mc.parent(axle, wheel_grp)

    return wheel_grp

def createLocomotive():

        locomotiveBase = mc.polyCube(w=281, h=270, d=1253)
        mc.scale(1, 1, 1, locomotiveBase)
        mc.move(0, 175.383, 395.942)
        mc.polySelect(locomotiveBase, erp=[2, 2])
        mc.move(0, 0, 197.968374, r=True)
        mc.polySelect(locomotiveBase, edgeRing=9)
        mc.polySplitRing(sma=30, stp=1, wt=.82)
        mc.polySelect(locomotiveBase, edgeRing=13)
        mc.polySplitRing(sma=30, stp=1, wt=.40)
        mc.polySelect(locomotiveBase, edgeRing=23)
        mc.polySplitRing(sma=30, stp=1, wt=.343)
        mc.polySelect(locomotiveBase, erp=[16, 16])
        mc.move(0, 0, -104.122088, r=True)
        mc.polySelect(locomotiveBase, erp=[24, 24])
        mc.move(0, 0, -118.969557, r=True)
        mc.polySelect(locomotiveBase, erp=[32, 32])
        mc.move(0, 0, -45.326612, r=True)
        mc.polySelect(locomotiveBase, edgeRing=1)
        mc.polySplitRing(sma=30, stp=1, wt=.5)
        mc.polySelect(locomotiveBase, d=True, el=38)
        mc.polySelect(locomotiveBase, sep=[4, 6])
        mc.polySelect(locomotiveBase, sep=[5, 7])
        mc.move(0, 0, 35.583886, r=True)
        mc.polySelect(locomotiveBase, erp=[10, 10])
        mc.move(61.037369, 0, 0, r=True)
        mc.polySelect(locomotiveBase, erp=[11, 11])
        mc.move(-61.037369, 0, 0, r=True)
        mc.polySelect(locomotiveBase, erp=[30, 30])
        mc.move(32.055471, 0, 0, r=True)
        mc.polySelect(locomotiveBase, erp=[34, 34])
        mc.move(-32.055471, 0, 0, r=True)
        mc.polySelect(locomotiveBase, erp=[14, 14])
        mc.move(11.179254, 0, 0, r=True)
        mc.polySelect(locomotiveBase, erp=[18, 18])
        mc.move(-11.179254, 0, 0, r=True)
        mc.polySelect(locomotiveBase, edgeRing=1)
        mc.polySplitRing(sma=30, stp=1, wt=.5)
        mc.polySelect(locomotiveBase, edgeRing=35)
        mc.polySplitRing(sma=30, stp=1, wt=.5)
        mc.polySelect(locomotiveBase, d=True, el=92)
        mc.polySelect(locomotiveBase, erp=[6, 6])
        mc.move(37.374182, -11.654315, 0, r=True)
        mc.polySelect(locomotiveBase, erp=[7, 7])
        mc.move(-37.374182, -11.654315, 0, r=True)
        mc.polySelect(locomotiveBase, erp=[66, 66])
        mc.move(15.115551, -0.783189, 0, r=True)
        mc.polySelect(locomotiveBase, erp=[94, 94])
        mc.move(-15.115551, -0.783189, 0, r=True)

        mc.polySelect(locomotiveBase, elp=[9, 31])
        mc.move(0, 0, 37.407045, r=True)
        mc.polySelect(locomotiveBase, elp=[8, 29])
        mc.move(0, 0, 37.407045, r=True)

        mc.polySelect(locomotiveBase, el=69)
        mc.polyBevel(o=3)

        mc.polySelect(locomotiveBase, edgeRing=10)
        mc.polySplitRing(sma=30, stp=1, wt=.97)
        mc.polySelect(locomotiveBase, edgeRing=7)
        mc.polySplitRing(sma=30, stp=1, wt=.9)
        mc.polySelect(locomotiveBase, edgeRing=6)
        mc.polySplitRing(sma=30, stp=1, wt=.03)
        mc.polySelect(locomotiveBase, edgeRing=157)
        mc.polySplitRing(sma=30, stp=1, wt=.07)

        return locomotiveBase

def create2ndCar():
        # Create second car
        locomotiveBase = createLocomotive()
        mc.select(locomotiveBase)
        mc.move(0, 0, 1580, r=True)

        mc.polySelect(locomotiveBase, el=242)
        mc.polyDelEdge(cv=True)
        mc.polyOptions(ao=True, dv=True)

        mc.polySelect(locomotiveBase, el=142)
        mc.polyDelEdge(cv=True)
        mc.polyOptions(ao=True, dv=True)

        mc.polySelect(locomotiveBase, erp=[99, 99])
        mc.polySelect(locomotiveBase, add=True, erp=[9, 9])
        mc.polySelect(locomotiveBase, add=True, erp=[61, 61])
        mc.polySelect(locomotiveBase, add=True, erp=[30, 30])
        mc.polySelect(locomotiveBase, add=True, erp=[44, 44])
        mc.polySelect(locomotiveBase, add=True, erp=[2, 2])
        mc.polySelect(locomotiveBase, add=True, erp=[8, 8])
        mc.polySelect(locomotiveBase, add=True, erp=[97, 97])
        mc.polySelect(locomotiveBase, add=True, erp=[71, 71])
        mc.polySelect(locomotiveBase, add=True, erp=[103, 103])
        mc.polySelect(locomotiveBase, add=True, erp=[18, 18])
        mc.polySelect(locomotiveBase, add=True, erp=[3, 3])
        mc.polySelect(locomotiveBase, add=True, erp=[49, 49])
        mc.polySelect(locomotiveBase, add=True, erp=[35, 35])
        mc.polySelect(locomotiveBase, add=True, erp=[56, 56])
        mc.polySelect(locomotiveBase, add=True, erp=[20, 20])
        mc.polySelect(locomotiveBase, add=True, erp=[105, 105])
        mc.polySelect(locomotiveBase, add=True, erp=[79, 79])
        mc.polySelect(locomotiveBase, add=True, erp=[62, 62])
        mc.polySelect(locomotiveBase, add=True, erp=[33, 33])
        mc.polySelect(locomotiveBase, add=True, erp=[47, 47])
        mc.polySelect(locomotiveBase, add=True, erp=[14, 14])
        mc.polySelect(locomotiveBase, add=True, erp=[46, 46])
        mc.polySelect(locomotiveBase, add=True, erp=[32, 32])
        mc.polySelect(locomotiveBase, add=True, erp=[60, 60])
        mc.polySelect(locomotiveBase, add=True, erp=[110, 110])
        mc.polySelect(locomotiveBase, add=True, erp=[114, 114])
        mc.polySelect(locomotiveBase, add=True, erp=[98, 98])
        mc.polySelect(locomotiveBase, add=True, erp=[82, 82])
        mc.polySelect(locomotiveBase, add=True, erp=[94, 94])
        mc.polySelect(locomotiveBase, add=True, erp=[76, 76])
        mc.polySelect(locomotiveBase, add=True, erp=[73, 73])
        mc.polySelect(locomotiveBase, add=True, erp=[74, 74])
        mc.polySelect(locomotiveBase, add=True, erp=[78, 78])
        mc.polySelect(locomotiveBase, add=True, erp=[80, 80])
        mc.polySelect(locomotiveBase, add=True, erp=[95, 95])
        mc.polySelect(locomotiveBase, add=True, erp=[81, 81])
        mc.polySelect(locomotiveBase, add=True, erp=[77, 77])
        mc.polySelect(locomotiveBase, add=True, erp=[115, 115])
        mc.polySelect(locomotiveBase, add=True, erp=[111, 111])
        mc.polySelect(locomotiveBase, add=True, erp=[58, 58])
        mc.polySelect(locomotiveBase, add=True, erp=[34, 34])
        mc.polySelect(locomotiveBase, add=True, erp=[59, 59])
        mc.polySelect(locomotiveBase, add=True, erp=[36, 36])
        mc.polySelect(locomotiveBase, add=True, erp=[48, 48])
        mc.polySelect(locomotiveBase, add=True, erp=[50, 50])
        mc.polySelect(locomotiveBase, add=True, erp=[104, 104])
        mc.polySelect(locomotiveBase, add=True, erp=[75, 75])
        mc.polySelect(locomotiveBase, add=True, erp=[21, 21])
        mc.scale(1, 1, 1e-05, p=(0, 175.383, 1458.653823), r=True)

        mc.polySelect(locomotiveBase, el=135)
        mc.scale(1, 1, 1e-05, p=(0, 175.383, 1626.846739), r=True)
        mc.move(0, 0, -140.361965, r=True)

        mc.select(locomotiveBase)
        mc.move(0, 0, -414.222491, r=True)

        mc.polySelect(locomotiveBase, el=170)
        mc.scale(1, 1, 1e-05, p=(0, 175.383, 2158.951687), r=True)
        mc.polySelect(locomotiveBase, el=170)

        mc.select(locomotiveBase)
        mc.scale(1, 1, 1.111111, r=True)
        mc.move(0, 0, 72.883127, r=True)

        return locomotiveBase


def createWindows():
        createLocomotiveWindows()
        rearWindows = createLocomotiveWindows()
        mc.scale(1, 1, -1, rearWindows)
        mc.move(0, 0, 4914.476, rearWindows)
        createCarWindows()
        mc.move(0, 0, 1485.214, createCarWindows())
        addGlassDomeAndFittings()

def addGlassDomeAndFittings():
        dome = mc.polyCylinder(r=88.203, h=539.333, sx=20, sz=4, rcp=True)
        mc.select(dome)
        mc.scale(1, 1, 1.213, r=True)
        mc.move(-0, 311.386, 1706.511, r=True)
        mc.rotate(90, 0, 0)

        fitting = mc.polyCylinder(r=110.211, h=13.274, sx=20)
        mc.select(fitting)
        mc.scale(.825, 1, 1, r=True)
        mc.move(0, 311.386, 1436.844)
        mc.rotate(90, 0, 0)

        fitting = mc.polyCylinder(r=110.211, h=13.274, sx=20)
        mc.select(fitting)
        mc.scale(.825, 1, 1, r=True)
        mc.move(0, 311.386, 1571.678)
        mc.rotate(90, 0, 0)

        fitting = mc.polyCylinder(r=110.211, h=13.274, sx=20)
        mc.select(fitting)
        mc.scale(.825, 1, 1, r=True)
        mc.move(0, 311.386, 1706.511)
        mc.rotate(90, 0, 0)

        fitting = mc.polyCylinder(r=110.211, h=13.274, sx=20)
        mc.select(fitting)
        mc.scale(.825, 1, 1, r=True)
        mc.move(0, 311.386, 1841.344)
        mc.rotate(90, 0, 0)

        fitting = mc.polyCylinder(r=110.211, h=13.274, sx=20)
        mc.select(fitting)
        mc.scale(.825, 1, 1, r=True)
        mc.move(0, 311.386, 1976.177)
        mc.rotate(90, 0, 0)

        fitting = mc.polyCylinder(r=88.203, h=539.333, sx=20, sz=4, rcp=True)
        mc.select(fitting)
        mc.scale(.872, .975, .169, r=True)
        mc.move(0, 370.385, 1706.511)
        mc.rotate(90, 0, 0)


def createCarWindows():
    windows = []
    window = mc.polyCube(w=1, h=1, d=1)
    mc.select(window)
    mc.scale(101.538, 77.783, 113.12, r=True)
    mc.move(-88.727, 186.815, 1237.518, r=True)
    mc.rotate(0, 0, -4)
    windows.append(window)

    window = mc.polyCube(w=1, h=1, d=1)
    mc.select(window)
    mc.scale(101.538, 77.783, 113.12, r=True)
    mc.move(-88.727, 186.815, 1386.189, r=True)
    mc.rotate(0, 0, -4)
    windows.append(window)

    window = mc.polyCube(w=1, h=1, d=1)
    mc.select(window)
    mc.scale(101.538, 77.783, 113.12, r=True)
    mc.move(-88.727, 186.815, 1526.601, r=True)
    mc.rotate(0, 0, -4)
    windows.append(window)

    window = mc.polyCube(w=1, h=1, d=1)
    mc.select(window)
    mc.scale(101.538, 77.783, 113.12, r=True)
    mc.move(-88.727, 186.815, 1673.895, r=True)
    mc.rotate(0, 0, -4)
    windows.append(window)

    window = mc.polyCube(w=1, h=1, d=1)
    mc.select(window)
    mc.scale(101.538, 77.783, 113.12, r=True)
    mc.move(-88.727, 186.815, 1814.307, r=True)
    mc.rotate(0, 0, -4)
    windows.append(window)

    window = mc.polyCube(w=1, h=1, d=1)
    mc.select(window)
    mc.scale(101.538, 77.783, 113.12, r=True)
    mc.move(-88.727, 186.815, 1960.225, r=True)
    mc.rotate(0, 0, -4)
    windows.append(window)

    windows_pyGroup = mc.group(windows[0])
    for i in range(1, len(windows)):
        mc.parent(windows[i], windows_pyGroup)

    return windows_pyGroup

def createLocomotiveWindows():
    windows = []
    windowFront = mc.polyCube(w=1, h=1, d=1)
    mc.select(windowFront)
    mc.scale(64.6, 64.6, 64.6, r=True)
    mc.polySelect(windowFront, el=2)
    mc.polyBevel(o=.8)
    mc.select(windowFront)
    mc.move(-107.900116, 186.684436, -124.239468, r=True)
    mc.rotate(0, 0, -4)
    windows.append(windowFront)

    window = mc.polyCube(w=1, h=1, d=1)
    mc.select(window)
    mc.scale(101.538, 77.783, 113.12, r=True)
    mc.move(-88.727, 186.815, 50.902, r=True)
    mc.rotate(0, 0, -4)
    windows.append(window)

    window = mc.polyCube(w=1, h=1, d=1)
    mc.select(window)
    mc.scale(101.538, 77.783, 113.12, r=True)
    mc.move(-88.727, 186.815, 194.067, r=True)
    mc.rotate(0, 0, -4)
    windows.append(window)

    window = mc.polyCube(w=1, h=1, d=1)
    mc.select(window)
    mc.scale(101.538, 77.783, 113.12, r=True)
    mc.move(-88.727, 186.815, 549.226, r=True)
    mc.rotate(0, 0, -4)
    windows.append(window)

    window = mc.polyCube(w=1, h=1, d=1)
    mc.select(window)
    mc.scale(101.538, 77.783, 113.12, r=True)
    mc.move(-88.727, 186.815, 691.014, r=True)
    mc.rotate(0, 0, -4)
    windows.append(window)

    window = mc.polyCube(w=1, h=1, d=1)
    mc.select(window)
    mc.scale(101.538, 77.783, 113.12, r=True)
    mc.move(-88.727, 186.815, 845.191, r=True)
    mc.rotate(0, 0, -4)
    windows.append(window)

    windows_pyGroup = mc.group(windows[0])
    for i in range(1, len(windows)):
        mc.parent(windows[i], windows_pyGroup)

    return windows_pyGroup


main()
