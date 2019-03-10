import numpy as np


def chooseStartingState():
    states = ["WIN", "HIGH", "SAFE", "LOW", "BTM2", "ELIM"]
    probabilityMatrix = [0.07, 0.14, 0.58, 0.07, 0.07, 0.07]
    state = np.random.choice(states, replace=True, p=probabilityMatrix)
    return state


def runMarkov(eps):
    states = ["WIN", "HIGH", "SAFE", "LOW", "BTM2", "ELIM"]
    transitionName = [["WW", "WH", "WS", "WL", "WB", "WE"], ["HW", "HH", "HS", "HL", "HB", "HE"],
                      ["SW", "SH", "SS", "SL", "SB", "SE"], ["LW", "LH", "LS", "LL", "LB", "LE"],
                      ["BW", "BH", "BS", "BL", "BB", "BE"]]
    transitionMatrix = [[0.065, 0.25, 0.41, 0.11, 0.10, 0.065], [0.15, 0.26, 0.275, 0.11, 0.14, 0.065],
                        [0.13, 0.21, 0.315, 0.115, 0.12, 0.11], [0.1225, 0.26, 0.25, 0.09, 0.145, 0.1325],
                        [0.17, 0.12, 0.23, 0.08, 0.12, 0.28]]
    epRes = chooseStartingState()
    epResList = [epRes]
    if epRes == "ELIM":
        return epResList
    i = 1
    while i != eps:
        if epRes == "WIN":
            change = np.random.choice(transitionName[0], replace=True, p=transitionMatrix[0])
            if change == "WW":
                epResList.append("WIN")
                pass
            elif change == "WH":
                epResList.append("HIGH")
                epRes = "HIGH"
            elif change == "WS":
                epResList.append("SAFE")
                epRes = "SAFE"
            elif change == "WL":
                epResList.append("LOW")
                epRes = "LOW"
            elif change == "WB":
                epResList.append("BTM2")
                epRes = "BTM2"
            elif change == "WE":
                epResList.append("ELIM")
                break
        elif epRes == "HIGH":
            change = np.random.choice(transitionName[1], replace=True, p=transitionMatrix[1])
            if change == "HW":
                epResList.append("WIN")
                epRes = "WIN"
            elif change == "HH":
                epResList.append("HIGH")
                epRes = "HIGH"
            elif change == "HS":
                epResList.append("SAFE")
                epRes = "SAFE"
            elif change == "HL":
                epResList.append("LOW")
                epRes = "LOW"
            elif change == "HB":
                epResList.append("BTM2")
                epRes = "BTM2"
            elif change == "HE":
                epResList.append("ELIM")
                break
        elif epRes == "SAFE":
            change = np.random.choice(transitionName[2], replace=True, p=transitionMatrix[2])
            if change == "SW":
                epResList.append("WIN")
                epRes = "WIN"
            elif change == "SH":
                epResList.append("HIGH")
                epRes = "HIGH"
            elif change == "SS":
                epResList.append("SAFE")
                epRes = "SAFE"
            elif change == "SL":
                epResList.append("LOW")
                epRes = "LOW"
            elif change == "SB":
                epResList.append("BTM2")
                epRes = "BTM2"
            elif change == "SE":
                epResList.append("ELIM")
                break
        elif epRes == "LOW":
            change = np.random.choice(transitionName[3], replace=True, p=transitionMatrix[3])
            if change == "LW":
                epResList.append("WIN")
                epRes = "WIN"
            elif change == "LH":
                epResList.append("HIGH")
                epRes = "HIGH"
            elif change == "LS":
                epResList.append("SAFE")
                epRes = "SAFE"
            elif change == "LL":
                epResList.append("LOW")
                epRes = "LOW"
            elif change == "LB":
                epResList.append("BTM2")
                epRes = "BTM2"
            elif change == "LE":
                epResList.append("ELIM")
                break
        elif epRes == "BTM2":
            change = np.random.choice(transitionName[4], replace=True, p=transitionMatrix[4])
            if change == "BW":
                epResList.append("WIN")
                epRes = "WIN"
            elif change == "BH":
                epResList.append("HIGH")
                epRes = "HIGH"
            elif change == "BS":
                epResList.append("SAFE")
                epRes = "SAFE"
            elif change == "BL":
                epResList.append("LOW")
                epRes = "LOW"
            elif change == "BB":
                epResList.append("BTM2")
                epRes = "BTM2"
            elif change == "BE":
                epResList.append("ELIM")
                break
        i += 1
    return epResList


for x in range(0,15):
    res = runMarkov(11)
    print(res)

