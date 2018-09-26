bensinverd95AL_nafn = "Engin"
bensinverd95AL_verd = 0

for bensinstod in gogn["results"]:
    if bensinverd95AL_nafn == "Engin":
        bensinverd95AL_nafn = bensinstod["company"]
        bensinverd95AL_verd = bensinstod["bensin95"]
    else:
        if bensinverd95AL_verd > bensinstod["bensin95"]:
            bensinverd95AL_nafn = bensinstod["company"]
            bensinverd95AL_verd = bensinstod["bensin95"]
