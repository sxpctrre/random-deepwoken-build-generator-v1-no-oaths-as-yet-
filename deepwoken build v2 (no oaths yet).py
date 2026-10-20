
import random

attributePointsRemaining = 330
weightAttribute = [5, 5, 5, 5, 5, 5, 7, 7]

flm = "Flamecharm"
ice = "Frostdraw"
wnd = "Galebreathe"
ltn = "Thundercall"
sdw = "Shadowcast"
mtl = "Bloodrend"
blo = "Ironsing"

attunementless = "Attunementless"

fst = "Fist"
dgr = "Dagger"
gun = "Pistol"
rpr = "Rapier"
swd = "Sword"
spr = "Spear"
rif = "Rifle"
twn = "Twinblade"
grt = "Greataxe"
grs = "Greatsword"
grh = "Greathammer"
grc = "Greatcannon"

oth = "Oathless"
arc = "Arcwarder"
bld = "Bladeharper"
blg = "Blightsurger"
bln = "Blindseer"
con = "Contractor"
dwn = "Dawnwalker"
fde = "Fadetrimmer"
jts = "Jetstriker"
lnk = "Linkstrider"
snt = "Saintsworn"
slt = "Saltchemist"
sln = "Silentheart"
slb = "Soulbreaker"
sta = "Starkindred"
vsi = "Visionshaper"


# Available attunements
attunements = {
    flm: "Flamecharm",
    ice: "Frostdraw",
    wnd: "Galebreathe",
    ltn: "Thundercall",
    sdw: "Shadowcast",
    mtl: "Bloodrend",
    blo: "Ironsing"
}

# Available light weapons
weaponTypesLight = {
    fst: "Fist",
    dgr: "Dagger",
    gun: "Pistol",
    rpr: "Rapier"
}

# Available medium weapons
weaponTypesMedium = {
    swd: "Sword",
    spr: "Spear",
    rif: "Rifle",
    twn: "Twinblade"
}

# Available heavy weapons
weaponTypesHeavy = {
    grt: "Greataxe",
    grs: "Greatsword",
    grh: "Greathammer",
    grc: "Greatcannon"
}

# Available oaths
oathsDictionary = {
    oth: "Oathless",
    arc: "Arcwarder",
    bld: "Bladeharper",
    blg: "Blightsurger",
    bln: "Blindseer",
    con: "Contractor",
    dwn: "Dawnwalker",
    fde: "Fadetrimmer",
    jts: "Jetstriker",
    lnk: "Linkstrider",
    snt: "Saintsworn",
    slt: "Saltchemist",
    sln: "Silentheart",
    slb: "Soulbreaker",
    sta: "Starkindred",
    vsi: "Visionshaper"
}

# Weapon class point totals
weaponPoints = {
    "light": 0,
    "med": 0,
    "heavy": 0
}

# Weapon class selection
weaponClasses = {
    "light": 0,
    "med": 0,
    "heavy": 0
}

# Character attributes
attributesDictionary = {
    "strength": 0,
    "fortitude": 0,
    "agility": 0,
    "intelligence": 0,
    "willpower": 0,
    "charisma": 0,
    "attunement": 0,
    "weapon": 0
}

# Points for individual attunements
attunementPointsDictionary = {
    "Flamecharm": 0,
    "Frostdraw": 0,
    "Thundercall": 0,
    "Galebreathe": 0,
    "Shadowcast": 0,
    "Ironsing": 0,
    "Bloodrend": 0
}


def randomAttunement():
    return random.choice(list(attunements.values()))


def randomWeaponClass():
    return random.choice(list(weaponClasses.keys()))


def randomAllocation():
    global attributePointsRemaining

    attributeNames = list(attributesDictionary.keys())

    while attributePointsRemaining > 0:
        attributeChosen = random.choices(
            attributeNames,
            weights=weightAttribute,
            k=1
        )[0]

        attributesDictionary[attributeChosen] += 5
        attributePointsRemaining -= 5


# Generate the build
randAttune = randomAttunement()
randWeaponCls = randomWeaponClass()

randomAllocation()

# Display the build
print("----- DEEPWOKEN BUILD GENERATOR (by dunno__ on discord)-----")
print("Attunement:", randAttune)
print("Weapon class:", randWeaponCls)
print()

print("Attributes:")
for attribute, points in attributesDictionary.items():
    print(f"{attribute.capitalize()}: {points}")

print()


