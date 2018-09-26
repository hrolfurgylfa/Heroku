def bensin(bensin_gerd,gogn):
    bensin_nafn = "Engin"
    bensin_verd = 0

    for bensinstod in gogn["results"]:
        if bensin_nafn == "Engin":
            bensin_nafn = bensinstod["company"]
            bensin_verd = bensinstod[bensin_gerd]
        else:
            if bensin_verd > bensinstod[bensin_gerd]:
                bensin_nafn = bensinstod["company"]
                bensin_verd = bensinstod[bensin_gerd]
    
    return (bensin_nafn,bensin_verd)