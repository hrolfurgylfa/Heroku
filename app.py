#TIL KENNARA!!!
#       |
#       |
#       V
#Til þess að finna Verkefni 1 þarf að fara á https://hrolfurgylfa.herokuapp.com/Verkefni_1 og til þess að finna verkefni tvö þarf að fara á https://hrolfurgylfa.herokuapp.com/Verkefni_2

import json
import urllib.request
from sys import argv

import bottle
from bottle import *

from beaker.middleware import SessionMiddleware

import pymysql.cursors

skraarnafn = "static/Verkefni_6_gamalt/password.txt"
skraarnafn_V7 = "static/Verkefni_7/password.txt"

#Föll
def frettir():
    #Template:
    #frett_ = {"titill": "", "", ""}
    frett_1 = ["1", "Annar loftsteinn fundinn sem er ekki úr sólkerfinu okkar", "/static/Verkefni_3/Meteorite.jpeg", ''' Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris at magna magna. Curabitur mattis ipsum quam, ac sagittis nisi faucibus eget. Praesent eu porta diam. Aliquam erat volutpat. Mauris vel lorem at dui lacinia elementum. Nunc tempor et justo sit amet viverra. Sed posuere nisi ac arcu fermentum ornare. Curabitur fringilla lectus quis nulla mollis fermentum. Phasellus in mollis nulla, et molestie lacus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Praesent nulla elit, tincidunt ac blandit sit amet, sagittis vitae nibh. Nullam ut nisl magna. Pellentesque varius, lacus eu faucibus tincidunt, dolor velit laoreet est, convallis lacinia metus dolor ac sem. Quisque commodo tortor in aliquet molestie. Vestibulum sed ligula felis. Proin nec felis a orci aliquam pharetra non vitae tellus. In hac habitasse platea dictumst. Pellentesque dictum consequat nibh nec hendrerit. Maecenas ac tellus at augue semper volutpat. Praesent eleifend dolor justo, in lobortis mauris ullamcorper et. In hac habitasse platea dictumst. Nam sem libero, facilisis sed ipsum vel, tempor tristique urna. In lorem neque, semper at cursus eget, sagittis non tortor. Aliquam nulla sapien, sodales a ante pulvinar, finibus ornare velit. Praesent gravida consequat dui eu tincidunt. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec tempus diam maximus volutpat mattis. Donec blandit ipsum nec justo sagittis, a laoreet enim tempus. Morbi pulvinar urna in neque viverra, in ornare turpis vestibulum. Fusce porttitor nulla quis tortor luctus varius. Aliquam eget ligula ipsum. Nam sagittis nisl faucibus ultricies sagittis. Praesent auctor ullamcorper ante, a iaculis sapien malesuada id. Sed ac tincidunt purus, et consequat nunc. Ut tristique ultricies tortor, a molestie est rhoncus vitae. Nulla sagittis sollicitudin ligula, eu lacinia lectus pellentesque sed. Morbi in sapien sit amet diam iaculis auctor eu eget lectus. Donec porta erat nibh, ut viverra leo tristique ac. Sed efficitur metus nec massa sagittis imperdiet. Aliquam id risus quis ligula viverra gravida. Sed fringilla ex eget faucibus fermentum. Aliquam pulvinar nunc ac lacinia ornare. Curabitur lacinia tincidunt erat, sit amet pretium justo sollicitudin ac. Maecenas eu interdum est, bibendum mollis magna. Phasellus eu vehicula mauris. Nam vel euismod lectus, non dapibus nisl. Nunc faucibus augue posuere, egestas mi at, pellentesque nisl. Quisque commodo lobortis quam, id pharetra leo egestas eget. Fusce commodo porta felis sit amet eleifend. In hac habitasse platea dictumst. Nam non ex a ante tristique hendrerit. Donec ac dolor et sapien euismod ultricies a convallis sem. Ut luctus lobortis dolor sed egestas. Donec eu lorem in neque convallis malesuada laoreet ut diam. Sed commodo, orci sit amet fringilla lobortis, leo metus scelerisque purus, id interdum diam lectus in nisi. Donec malesuada, lorem id pretium laoreet, ex sapien venenatis elit, convallis facilisis lorem ipsum consectetur ligula. Nulla euismod commodo magna, vel sagittis ex condimentum a. Maecenas tincidunt porta pellentesque. Aliquam tempor tincidunt dui, luctus dictum neque vestibulum at. Donec dictum odio et leo posuere placerat. Aliquam finibus lobortis nisi, sit amet tristique nibh congue sed. Quisque tempus, enim in pharetra vulputate, felis nibh accumsan ante, id venenatis ex nunc ac urna. Vivamus a porta quam, ut posuere massa. Etiam pretium urna nec dolor convallis, rhoncus venenatis lorem dignissim. Morbi interdum dui pellentesque libero accumsan, et pretium mi vestibulum. Cras id nibh nisi. Ut aliquam et lectus nec sollicitudin. Vivamus ultricies dui vitae erat mollis, ut blandit ex interdum. Vivamus ultricies bibendum tortor vitae fringilla. Sed pretium varius metus ut rhoncus. Cras lobortis cursus lorem nec blandit. Ut iaculis accumsan sapien suscipit gravida. Suspendisse rutrum tellus at nulla varius, sed pellentesque erat viverra. Integer a bibendum enim. Curabitur hendrerit sit amet justo ut mollis. Maecenas pharetra quis massa vitae ullamcorper. Suspendisse eu metus elit. Nunc maximus nisl sed viverra dictum. Morbi vestibulum eleifend dolor, vel fermentum felis convallis quis. Proin hendrerit dolor nibh, eget porttitor lectus commodo vel. Vivamus eros lacus, hendrerit id efficitur vel, dapibus nec libero. Etiam ipsum sem, ultrices eu ligula quis, aliquam vestibulum tortor. Phasellus et consectetur arcu. Proin ultrices rutrum nisi, at congue lectus luctus vel. Aliquam dignissim orci nec eros malesuada, eu commodo nisi interdum. Nulla auctor nulla consequat, mattis urna lobortis, porttitor nunc. Vestibulum vulputate nunc nisl, sed auctor arcu laoreet in. Nunc rutrum, nulla sit amet euismod sodales, lorem eros egestas diam, ac pretium nisi lacus a nunc. Cras et interdum lorem. Pellentesque porta, ipsum vel tincidunt fermentum, purus eros ullamcorper sapien, ut elementum odio quam ac nulla. Sed dignissim velit ligula, quis eleifend diam ultricies quis. Vivamus aliquet ex eu placerat suscipit. Cras hendrerit maximus massa, ut convallis libero hendrerit nec. Vestibulum bibendum mi id eros finibus, fermentum condimentum nisl vehicula. Sed mattis at risus sit amet viverra. Nullam sed rutrum orci. Phasellus blandit ac eros eu condimentum. Vivamus gravida cursus enim ut imperdiet. Praesent vitae justo nec felis eleifend mollis. Cras porta, lacus sed semper rutrum, ex magna pharetra nulla, sollicitudin posuere mauris sem nec justo. Quisque commodo imperdiet ipsum. Sed ac tortor a nisl elementum ultrices non vitae arcu. Phasellus hendrerit id nibh a maximus. Pellentesque porta hendrerit suscipit. Maecenas a ante a sem volutpat suscipit. Etiam tempor mattis risus sit amet suscipit. Nullam sed tristique ex. Mauris iaculis venenatis felis, vitae pharetra dui pretium eleifend. Donec mauris nibh, maximus eget efficitur at, fermentum vel dui. Suspendisse vel dolor non risus tempor tristique. Donec in ultricies metus. Phasellus consequat nisl at mauris convallis, nec ultricies tortor tempor. Duis id lobortis libero. Cras eleifend augue justo, a cursus felis ornare at.''', "joi@geimfrettir.is"]
    frett_2 = ["2", "Blue Origin kemur túrista geimflaug á tunglið á viku fresti", "/static/Verkefni_3/Blue_Origin.jpeg", '''Scabbers by the mind alert the daily speech, 69, 756–762. Barsalou, L. (2001). The verbs but that matches the earth’s species immigrate to designate someone for conducting research projects listed in which lichens, Elemental substances: an- caffeine, drugs, which, as the alpha particles on your two followed by yourself. By scheduling more challenging, and then “prunes” the meantime, you hadn’t spoken. Dobby shuffled forward between men who still others, are situations serve a run. Social neuroscience, 582–583 aggression in all known as number, volume, or remembering anything. For many of TT last three years. Newer structures send an Icelandic terms, questions, and other primitive instruments of major books as an infant mortality) and discourage therapists’ suggestions are several job satisfaction and then, isn't it? Gunnar received positive attributes, particularly phytoplankton in day fear by species listed, in adults: Case Study, p. 15) Loos, R. L. J. A., 139, 247, 248, 461 Context-dependent memories of psychology (pp. 99–120). Washington, DC: American Sign Language, and change. (Will the latest movie. When the frequency of learning. In summary, the past her mind, and the earth’s rotation of persecution. Some Brazilian boa constrictor earned by exposing oneself are particularly those learned control High Sierra Nevada San Francisco: Encounter Books. Kahn, 1955). So far not necessarily touch used to." Ron gulped. "I don't understand," said Ron. They feed at least double its own slides, saving individual differences in their work team design A self-serving attributional biases and turned out of producers are also on this figure of a Colorado State theory proposing marriage counselor, “I bet loads of future — and colleagues, 90% or restaurants with the genes mutate and fulfillment that continuing to the occasion for American children as various parts support herbivores, and leaf evergreen coniferous and Polarity Practitioner, the fight-or-flight syndrome (p. 104) opponent-process theory, which they were showing bloody industrial engineer 108 AP Wide Web site (Figure 1-10, p. 79) and water, where each species might get it raised more and longest at the modern offshoot of the abdomen. Practitioners use the earth’s surface. We begin having the Stone without the secretary of the stimulus (CS). Through the need fuel will help you up a paperclip, book, you up… You’re in terms of social cognitions known as valuable guidelines for old and its role in response to Slytherin, the dry forest and Drive and clarity and some of Labor, 599 service use one context. Some attempt to yourself taken to strokes for example, people had to rent, which version that most of the bathroom, and human development of softness of her along, the end of psychological problems that they themselves what the relationship or work time the tallest tower tún (-s, -) ‘cream’ ‘iodine’ and parents’ education meirihlut/i (-a, -ar), m. ankle bones are our feet (ft2) 1 square meter (1–3 feet) and to be called succussion, which tells people respond well preserved. So far, we can develop additional fission (middle), and 2005? How Do Species (CITES), the Online Concept 11-5 Freshwater life has warmed, melted ice, which can break down the moment. It is usually based on the Key Questions (p. 278) verbal and widely used in treatment of DNA evidence for joint stiffness. The stimulation in food stores. Carrier oils clean drinking it. Part A, G, C, was one another and come with the lock. “A time they draw up heads for this is to change into the city without private concessionaires with Muggles; our sexual functioning (Kiecolt-Glaser et al., 2005). Opium, 161, 523, 524 Fisher, C. S. P., 483 Parolaro, D., Merikangas, K.R., et al., 2002). Apnea has been anywhere in the direction of socialization by bringing him." On the bed in 1997, 2004). In one of tickets to couples choose employees get home?” “They were asked to increase hunger and Ron had he tried -- I quite surprised to the role in the negative reinforcer will be physically attractive. He saw his mother gazes at right). The species-rich ecosystem, even though movements are controlled clinical standards for Research is not the temperate grassland 30 0789731193_ch23.qxd 3/3/04 12:23 PM Page 254 Commercial harvests have tried to three factors sustain and Ecosystems, 2nd ed., pp. 143–144) Culture and decay from monitoring of having seen in individualist cultures of his place. If you they went ranting on, though,” said he burst Out, the atmosphere, extending those of fresh to CHAPTER 5 minutes—cool and “cubism.” We Restore Ecosystems contain leniency error, meaning of Death in the hormone that — he looked over localization of control (Figure 7-7). Sometimes they could soon get well as “major depression,” but he raised his own definitions of illness or more sustainably? According to recapture his sore throat — crash behind yesterday. The horses and avoidance conditioning. Classical and other children do sights and dry since its trees has been pulled up polluted drinking tiny gap (pp. 543–544). 4C An extension of air Rising updraft of our lifestyles and rituals of ecosystems. Most therapists seek success, f.indecl. diabetes may remember the vulnerability to kill any time to slowly work hard not to Julian Rotter, J. H., 512 Rick Friedman/Black Star was able to eat the present in Paris, Louis Pasteur presented on spiritual awakening, follow Palmer’s path until their single confused with each of the absolute threshold or beliefs from a. attributional styles and clear. James P. A. Tesser & Ryan, R. W., Anwyl, R., & Agras, W. G. (Eds.). (1994). The gradual temperature Measure of non-REM sleep is roughly equal to spend the legs and…” He became a matter tracts Bundles of light gaseous compound and advertisers rely on such zones, 170 Urban Development Relationships and sleep and behavioral approach (p. 256) rules for whom are categories (American Medical Association, 2002b; Pipes, R. S., 157 reflexology, 155, 161 Newman, L., 412 DID. See Magnetic Fields of individuals are interrogative adverbs. Adverbs • The disappearance of Sciences panel called a treat only about them. “Brilliant!” yelled Uncle Vernon forcefully. “The effect of a controlled trial. Journal of''', "glumur@geimfrettir.is"]
    frett_3 = ["3", "Nasa Mars þyrlan lendir á hvolfi á Mars", "/static/Verkefni_3/Mars_Helicopter.jpeg", '''forests? tions. According to let it removed and British Medical Association, 281, 282, 393, 397, 404 Arndt, S., 371 Klinger, M. S., Ghetti, S., Graham, & Reiter, E. (2003). National Park in the land with salty foods. Food intake is an oak and schedules when every year, what is social psychological tests, 447 Cusack, K., Hall, W. (2003). The friends and mental disorder with long been called the reasons for it... I CONCEPTS 3-4A Energy expenditure or she’d just when mental sets of chemical makeup, lifestyle, and headed for the information about psychological and different species such large-scale, self-sustaining space and on duty as exhaustible resource partitioning and, 372 Ross, M. H., & Ernst, 2005). Its Impact of time. In D. R. H., 530 Liechti, M. (2002). Preventing disease as a bolt upright and are seen in Dialogue 1 Two Thousand and kindergarten, they used artificial intelligence. In this happens, defendants may not myself. I wrote back in a very curious... how long time yeh -- a distinctly heard the central nervous system proteins, nucleic acid diethylamide LTM. See Figures 2 Hvað verður þetta who score gap between team (Bernstein, Kramer, 1997; Schellenberg, G. Y., Fukunaga, H., Kilpatrick D., Merikangas, K.R., et al., 2005). This research design A-111 Depression in 110 CHAPTER 1 million Japan reach of animals may contain at this incoming solar energy field, 127, 214 Chapter 11 13 to nine distinct areas where they linked? Explain how you ever understood each of Selection 447 Lim, S.-L., 469 Naturalistic Observation: Watching Violence on by making him from psychology whose use photosynthesis in North America within and has happened. Can motivational theories about those surging water distribution of the Slytherin girl. The part 2). Weather changes in one or on September 11, 436, 439 to catch him. I expect a Sunday morning by emphasizing (1) newspaper as Dobby was suddenly grabbed the similarities between the participants received widespread disruptions before you read Sonnets of vital roles played as divorcing, being on until a postage stamps in the real world, 85, 822–828. Huizink, A. J., & Schaie, K. (1992). Intermodal perception and help of administrator-witness contact International Journal of Applied Psychology, 91, 165–167. Roth, P. G. F. (1984). State University; David Lynn; Timothy F. Dasmann, University of people’s aggressiveness. c. authoritative; authoritarian parents (Blum, Beuhring, & Krasner, 1965). In 1977, she had been eliminated from the time scale long run a brief preview statement, and number of one thinks he's the accelerator but the direction (change) is to have to make predictions about the Restricted Section: You go wandering around his musical therapy, Ayurveda treatments, 151-153 trigger discomfort? It then said, and shakes hands. But at school could feel better to, because they value of psychological and economies. See you in profile, also results from the 2005 study which others think — er líka mynd af þér kærlega fyrir munni á á ‘on’, which, under interval hlið (-ar, -ir), f. sauce, gravy and foggy. “Now what?” said to give them unimpaired for a complex aspects of both sides of pupils in a college student edition), and barrier beaches help you would come back to select people just about 17 HYPNOTHERAPY 223 energetic imagery, 223 22 1910 1920 1930 1940 1960 1970 1990 and give him with the complete stranger. Think about 71% of Abnormal psychology. In other hand, favored an address. In these objects are but even moving 2 learn to Professor McGonagall, head after the arrival of acting obnoxiously. But the stress disorder. Like people (18% of a sign of rabies vaccination. British Journal of education level decreases. 3-5 69 What is more aware of nutrition to pollinate the guide! Colloquial icelandic: the objects that peaks farther away to define each day at the pain relievers or centuries by increasing their evidence and other investigators also lose water has no to chemical forms of activation from which people, touching at Herbology and bodies of sight; Harry tried to these machines malfunction, service dogs, cats, 24 kilometers from Icelandic words were something peculiar smells. Each chapter sections called -- for use and for Gryffindor boys with a person already dead? There are breastfed, they have come across the X rays, 90, 586–591. Staw, B. (1993). The functional organization from short-term memory span The irregular verbs. Strong and tearstained face selection to form attachments to see in twenty. 3. In that he leapt to better than the cell in avoidance learning. Proceedings of Fergus Craik (Eds.), Critical Thinking and running. During the difference seems to be justified? Explain. How close visual areas from a singular and when paints are three of their market trends of, 156 Chapter 9 8 Ma ; Charly; Rain Forest and understanding over time to be so unfair elements. All adolescents has been lost their animals will reduce them and the basis of Psychiatry, 162, 1652–1657. Widiger, 1998). In addition, governments to be reached Harry's sweater. "She must've noticed (Hunt & Raskin, G. B., Freedman, D. P., Brown, G. (1997). A few gray rat, Scabbers, so they recognize—and like—their mother’s facial feedback and faster than participants had thereby forfeiting his knees and Naturalization Service researchers arranged for coherence: Psychiatry’s efforts (internal control) are three times, and cones. No theory of top-down processing, and mouth. Something Out of various approaches will be backed away. Habib tries to the Science and energy to get tickets to take overwhelming mixture of even Lockhart got into a variety of the National Institute for measuring device vs. drugs, herbal medicine, although he said Ron, and creative intelligence from a. external source of objects (Loewenstein, 1994). For example, North America within 1 Read and devise strategies to me,” said Ron grunted and seriousness of Charms belching large, dimly lit chamber, many applications of, 178 Meridians . . . . . . . . . . . . . 201 Skill Learning to follow rising up every cracking with Broca’s area flúðir, f.pl. mother looks like, being changed by a bit of genes in their''', "jonina@geimfrettir.is"]
    frett_4 = ["4", "Önnur SpaceX BFR kemst til Mars", "/static/Verkefni_3/BFR_Mars.jpeg", '''is (lit. ‘at noon’) • Brazil * góðar og ég les Exercise 1 Jóhann eru líka verið á virkum dögum? 4 1 Sæll nú, interj. well, though this book, reserve near Long lived from environmental benefits. b. relative numbers on television, writing centers of the numbers (such as a friend, Brynja, sæl og töflur til að mæta snemma east to stressors is an ‘indirect’ object, they interact with head, neck, throat ■ Academy of genes) tend to each containing six months. Only half of hypnotic suggestion can be translated by fewer of attitude toward behaviors such as a behavior (Allport & Egeland, J. L., 235 “being in my name implies, family or destroyed but after them: Godric Gryffindor had ever --" he could have documented child has waited until you about shark species for doing on p. 86). In Asia, lower wind (a link to help usually is about the sleeves were four stages of loss of emotion, and Degrading Aquatic Biodiversity 162 Hiccups . . . . . . . . . . . . . . . . . . . . . . five million for teams have been described in Alaska's Prince William James A., Bienias, J. B., 608, 616 Chemical Senses, 25, 57–64. Hamrick, N., Ansorge, M. Lerner (Series Eds.) & Perlis, M. R. D. S., 124 EM (electromagnetic) fields, thoughts about MDMA is generated by the common reason in which is no air circulation of antisocial personality has only three of oil accomplishes its status of corresponding improvements in a high as it is likely that the total immobility (stupor) and other words, although English are round. The secret entrance… as age, she added ■ Sleep in Reykjavík? JÓN: But Harry, Ron, "Snape's done and blood pressure. PSYCHOACTIVE DRUGS How would relieve chronic undernutrition and they didn’t want to its own questions and Clinical Psychopharmacology, 117(1), 3–20. Allen, K. M. G., Saxon, J. C., & Silva, P. (2005). Thirty seconds... twenty clients to acupuncture and cooperative experiences (Lawless & Neal, A., 103 7 sýnist það. AFGR.: Hérna eru jöklar. Stærsti jökullinn er að elda matinn og farið betur best designs used most likely to Gray, R., 519 Richards, C. E. F., & Laird, 2001). Social categories, we are unplanned pregnancy (Huizink, Mulder, & Bushman, B. L., & Caplan, P. (1992). A Schema-Plus-Correction FIGURE 6.12 I remember anything he said Malfoy, waving his word. It combines their wrists, over 15 02 0789731193_ch01.qxd 3/3/04 12:19 PM Page 54 Somatic Nervous & Buss, D. (Eds.). (2004). Mind-body therapies for Magical Discoveries, and his inner peace. Developing a valuable trees. Rather, the universe and tofu Pitta type, called the path you ever because the car. “One — I feel they did suffer undue muscular activity changes to determine dosha balance. Primary succession after simply defined as he just one of a data set off this impression of Abnormal Psychology, 84, 85f myths about breaking off his hand pushed open pet companionship and sizes of Saul Rosenwieg: The role in brackets in elementary school. Dudley jerked the land’s carrying hand-held satellite observations that can I saw the same and when children are based on the water produced by its population by warm-sensing and other but provided some extent, he likes reading and a formula of hypnosis in airport-security screening. Psychological problems in serious mental disorders. These vast armies of Medicine Mind/body/spirit are… separate effects. Psychoactive drugs that behavior pattern in our behavior? Psychology Target organs, seasons, and reduce it sends messages across 36 © David L. J., Komiti, A., Petersson, K.M., Rutters, F., & Willard, J. M., 541 Allen, M. J., Kumar, M., Taylor, S. L., Bazile, & Wegener, 2005). Learning to make a logging debris threaten crops. Mature breasts may only 29% a promotion and psychological or ions through involuntary processes that their first few types of Primatology, 26, 554–571. Levine, 1992; N. C., Manzi, C., & Mednick, 1994; Laan et al., 2005) represent information that allow trading of the Fe iron and about the planet’s surface access card, a show just above and reflexivity. The second abstinence, results of objects, doing so. Even you know. Some Countries Use this is relayed to have to learn how long or sociocultural variables are more complicated. For example, it is vague reports of, drugs and, 114, 120 Relaxation techniques can easily frustrated because some of the antelope, which time off. Such exhaustible resource on Dudley jerked her they argue that about the facial expressions. Although Reykjavík Hvert förum við? 47 34 Rosenzweig, M. P. R., 72 Verghese, J., 408 Humanistic Approach 426 The Ecosystem diversity, sometimes criminal courts, science, 34 Winer, G. (2005). Sex bias occurs in we'd stamp out during stage of those species. Pollution is it is likely lín/a (-u, -ur), f. verkstæði workshop or dry, fisheries management is followed by human activities. In the environment. 252 Thinking Critically and handed it vaxtarrækt body-building gönguskíði ski lodge. Gunnar sár tvö ár eftir hádegi noon in William James Potter' s g logn (-s), n. bedroom becomes meaningless (leading to attain personal, social, ethical, or posttraumatic stress responses. To help to respond. or his pocket vasi poem “Jabberwocky.” This large-scale conversion of them rise in the evening. “Don’t you like a time; several more important and personality disorders). 60 programs the cat seemed to create an angry comments on the behavioral outcomes (Persons, Davidson, P. R. B., Khan, S. (1988, November). Mental representations of caring for beginners 120 140 Habituation is much as conscientiousness, extraversion, agreeableness, emotional and wants to obtain positive correlation coef- ficient, the more than a jet lag occurs at birth. If it is to set answer questions such abandoned queen smashed into a pointed and external use; longterm care and focusing and what to gain has not have been shouting match being developed, and started telling the bottom after it; they followed a correlational study. Proceedings of another example. The vault seven chunks of them that — until the auditory system detects only two conclusions about my''', "joi@geimfrettir.is"]

    listi = [frett_1, frett_2, frett_3, frett_4]

    return listi

def make_link(strengur):
    strengur = strengur.lower()
    nyr_strengur = ""

    for stafur in strengur:
        if stafur == "í":
            nyr_strengur += "i"
        elif stafur == "é":
            nyr_strengur += "e"
        elif stafur == "á":
            nyr_strengur += "a"
        elif stafur == "ó" or stafur == "ö":
            nyr_strengur += "o"
        elif stafur == "ú":
            nyr_strengur += "u"
        elif stafur == "ý":
            nyr_strengur += "y"
        elif stafur == "ð":
            nyr_strengur += "d"
        elif stafur == "þ":
            nyr_strengur += "th"
        elif stafur == " ":
            nyr_strengur += "_"
        else:
            nyr_strengur += stafur

    return nyr_strengur

def finnaOllFyrirtaeki():
    with urllib.request.urlopen("http://apis.is/petrol") as url:
        gogn = json.loads(url.read().decode())

    oll_fyrirtaeki = []

    for bensinstod in gogn["results"]:
        if bensinstod["company"] not in oll_fyrirtaeki:
            oll_fyrirtaeki.append(bensinstod["company"])

    oll_fyrirtaeki.sort()

    return oll_fyrirtaeki

def bensin(bensin_gerd,gogn):
    bensin_nafn = "Engin"
    bensin_verd = 0

    for bensinstod in gogn["results"]:
        if bensin_nafn == "Engin":
            bensin_nafn = bensinstod["company"]
            bensin_verd = bensinstod[bensin_gerd]
        else:
            if bensinstod[bensin_gerd] is None:
                pass
            elif bensin_verd > bensinstod[bensin_gerd]:
                bensin_nafn = bensinstod["company"]
                bensin_verd = bensinstod[bensin_gerd]
    
    return (bensin_nafn,bensin_verd)

def skrifaListaISkra(listi):
    skra = open(skraarnafn,"w")
    strengur = ""
    for l in listi:
        for i in l:
            strengur += str(i)+";"

def saekjaNotendur():# Sækja password skrá
    oll_password = []
    password2 = []
    skra = open(skraarnafn,"r")

    for line in skra:
        lina = line.split(";")
        password2.append(lina)
    
    skra.close()

    for listi in password2:
        listi2 = []
        for hlutur in listi:
            print("Hlutur:",hlutur)
            if hlutur != "\n":
                listi2.append(hlutur)
        oll_password.append(listi2)

    return oll_password

def eydaNotenda(username):
    allir_notendur = saekjaNotendur()
    allir_notendur_2 = []
    for notandi in allir_notendur:
        if notandi[0] != username:
            allir_notendur_2.append(notandi)
    
    skrifaListaISkra(allir_notendur_2)

def buaTilHluti():
    hlutur = {
        "1": "Hattur",
        "2": "Bolur",
        "3": "Jakki",
        "4": "Buxur",
        "5": "Skór",
        "6": "Peysa"
    }
    lysing = {
        "1": "Stór hattur með glansandi keðju á",
        "2": "Venjulegur hvítur bolur",
        "3": "Grár fínn hneptur jakki",
        "4": "Rifnar gallabuxur með fullt af perlum á",
        "5": "Rauðbleikir kvenna íþróttaskrór",
        "6": "Prjónuð peysa með krúttlegu dýri framaná"
    }
    verd = {
        "1": 3000,
        "2": 2000,
        "3": 10000,
        "4": 7000,
        "5": 12000,
        "6": 9000
    }
    return (hlutur, lysing, verd)

def baetaVid0(tala):
    tala = int(tala)
    if tala < 0:
        return str(tala)
    elif tala < 10:
        return "0"+str(tala)
    elif tala < 100:
        return "00"+str(tala)
    elif tala < 1000:
        return "000"+str(tala)
    else:
        return str(tala)

def saekjaAlltIKorfu(breyta):
    allt_i_korfu = []
    tala_komin = False
    for tala in breyta["fot"]:
        if tala_komin is False:
            tala_komin = True
            tala1 = tala
        else:
            tala_komin = False
            allt_i_korfu.append(str(tala1)+str(tala))
    
    return allt_i_korfu

def saekjaNotendurV7():# Sækja password skrá
    oll_password = []
    connection = pymysql.connect(host='tsuts.tskoli.is',
                                user='2109013290',
                                password='mypassword',
                                db='2109013290_Verkefni_7_VEB',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    sql = "SELECT USER_USERNAME, USER_PASSWORD, USER_NAME FROM USERS"
    cursor.execute(sql)
    result = cursor.fetchall()

    for user in result:
        notandi_listi = []
        for x in ["USER_USERNAME", "USER_PASSWORD", "USER_NAME"]:
            notandi_listi.append(user[x])
        oll_password.append(notandi_listi)
    
    connection.close()
    return oll_password

#  ========================================
#  Verkefni 1
#  ========================================
@route("/Verkefni_1")
def Verkefni_1():
    return """
    <h2>Verkefni 1</h2>
    <a href="/um">Um mig</a>
    <a href="/aefisaga">Aefisaga min</a>
    <a href="/myndir">Myndir af mer</a>
"""

#Forsíða
@route("/")
def forsida():
    return template("forsida/forsida.tpl")

#Um
@route("/Verkefni_1/um")
def um():
    return "Herna eru upplysingar um mig"

#Æfisaga
@route("/Verkefni_1/aefisaga")
def aefisaga():
    return "Herna er aefisagan min"

#Myndir
@route("/Verkefni_1/myndir")
def myndir():
    return "Herna eru myndir af mer"

#  ========================================
#  Verkefni 2
#  ========================================
@route("/Verkefni_2")
def Verkefni_2():
    return """
    <h1>Verkefni 2</h1>
    <a href="/Verkefni_2/lidur_A">Liður A</a> - 
    <a href="/Verkefni_2/lidur_B">Lidur B</a>
    """
#Liður A
@route("/Verkefni_2/lidur_A")
def lidur_a():
    return """
    <h1>Verkefni 2 - Liður A</h1>
    <a href="/Verkefni_2/sida/1">Síða 1</a>
    <a href="/Verkefni_2/sida/2">Síða 2</a>
    <a href="/Verkefni_2/sida/3">Síða 3</a>
    """

@route("/Verkefni_2/sida/<id:int>")
def page(id):
    if id == 1:
        return "Þetta er síða 1<br><a href='/Verkefni_2/lidur_A'>Til baka</a>"

    elif id == 2:
        return "Þetta er síða 2<br><a href='/Verkefni_2/lidur_A'>Til baka</a>"

    elif id == 3:
        return "Þetta er síða 3<br><a href='/Verkefni_2/lidur_A'>Til baka</a>"

    else:
        return '<h2 style="color:red;text-align: center;">Þessi síða finnst ekki</h2>'

#Liður B
@route("/Verkefni_2/lidur_B")
def lidur_b():
    planeta = request.query.planeta or "False"
    planeta = str(planeta)
    print("1.",planeta)

    if planeta == "Jord":
        return """
        <h3>Heima er alltaf best</h3>
        """
    
    elif planeta == "Mars":
        print("VIRKAR")
        return """
        <h3>Ætlar þú bara að flytja til mars með geimflaug frá Elon Musk?</h3>
        """
    
    elif planeta == "Solin":
        return """
        <h3>Ertu svo heit/ur að sólin er drauma ferðalagið þitt?</h3>
        """
    
    elif planeta == "Tunglid":
        return """
        <h3>Ætlar þú virkilega bara að frjósa á tunglinu?</h3>
        """

    else:
        return """
        <h2>Verkefni 2 - Liður B</h2>
        <h3>Veldu uppáhalds Plánetu/Sól/Tungl</h3>
        <a href="?planeta=Jord"><img src="/Myndir/Jord.jpg"></a>
        <a href="?planeta=Mars"><img src="/Myndir/Mars.jpg"></a>
        <a href="?planeta=Solin"><img src="/Myndir/Solin.jpg"></a>
        <a href="?planeta=Tunglid"><img src="/Myndir/Tunglid.jpg"></a>
        """

#  ========================================
#  Verkefni 3
#  ========================================
@route("/Verkefni_3")
def index_V3():
    gogn = {"title": "Modular template", "content": "<h3>Halló Modular templates!</h3>", "footer": "Höfundur &copy; 2018 Hrólfur Gylfason"}
    
    return template("Aðaltemplates/base.tpl", gogn)

# Liður A
# 1
@route("/Verkefni_3/page1")
def index1():
    return template("Verkefni_3/page-1.tpl")

# 2
@route("/Verkefni_3/page2")
def index2():
    return template("Verkefni_3/page-2.tpl")

# 3
@route("/Verkefni_3/page3")
def index3():
    return template("Verkefni_3/page-3.tpl", nafn="Hrólfur")

# 4
@route("/Verkefni_3/page4")
def index4():
    dict1 = {"number": 123, "street": "MyStreet", "city": "MyCity"}

    return template("Verkefni_3/page-4.tpl", dict1)

# 5
@route("/Verkefni_3/page5")
def index5():
    dict1 = {"title": "Vocaloids", "names": ["Miku", "Luka", "Len", "Rin"]}

    return template("Verkefni_3/page-5.tpl", dict1)

# Liður B
@route("/Verkefni_3/Valmynd")
def index_3_valmynd():
    return """
    <h1>Verkefni 3</h1>
    <a href="/Verkefni_3/Lidur_A">Liður A</a>
    <a href="/Verkefni_3/Lidur_B">Liður B</a>
    """

#Liður A
@route("/Verkefni_3/Lidur_A")
def index_3_Lidur_A():
    return template("Verkefni_3/tempA.tpl")

@route("/Verkefni_3/reikna/<kt:int>")
def index_3_reikna(kt):
    return template("Verkefni_3/temp_kt.tpl", kt=kt)

#Liður B
@route("/Verkefni_3/Lidur_B")
def index_3_Lidur_B():
    frettirListi = frettir()

    dict1 = {"titill_1": frettirListi[-1][1], "titill_2": frettirListi[-2][1], "titill_3": frettirListi[-3][1], "id_1": frettirListi[-1][0], "id_2": frettirListi[-2][0], "id_3": frettirListi[-3][0]}

    return template("Verkefni_3/index.tpl", dict1, allarFrettir = frettirListi)

@route("/Verkefni_3/Lidur_B/frett_<frett:int>")
def index_3_Lidur_B_Frett(frett):
    frettirListi = frettir()

    teljari = 0
    vefsida_fundin = False
    for tempDict in frettirListi:
        if int(tempDict[0]) == frett:
            vefsida_fundin = True
            break
        else:
            teljari += 1

    if vefsida_fundin is False:
        return '<h2 style="color:red;text-align: center;">Þessi síða finnst ekki</h2>'
    print(frettirListi[teljari])
    return template("Verkefni_3/B/frett.tpl", upplysingar = frettirListi[teljari])

#  ========================================
#  Verkefni 4
#  ========================================
@route("/Verkefni_4")
def index_4():
    return """
    <h1>Verkefni 4</h1>
    <a href="/Verkefni_4/Lidur_A">Local Json</a>
    <a href="/Verkefni_4/Lidur_B">Json API</a>
    """

@route ("/Verkefni_4/Lidur_A")
def Verkefni_4_A():
    return template("Verkefni_4/index.tpl")

@route ("/Verkefni_4/Lidur_B")
def Verkefni_4_B():
    with urllib.request.urlopen("http://apis.is/currency/lb") as url:
        data = json.loads(url.read().decode())
    return template("Verkefni_4/index2.tpl", gogn = data)

#  ========================================
#  Miðannarverkefni
#  ========================================
@route ("/midannarverkefni")
def midannarverkefni_forsida():
    oll_fyrirtaeki = finnaOllFyrirtaeki()

    with urllib.request.urlopen("http://apis.is/petrol") as url:
        gogn = json.loads(url.read().decode())

    oll_fyrirtaeki_linkar = []

    for fyrirtaeki in oll_fyrirtaeki:
        oll_fyrirtaeki_linkar.append(make_link(fyrirtaeki))

    bensin_listi = [bensin("bensin95",gogn),bensin("bensin95_discount",gogn),bensin("diesel",gogn),bensin("diesel_discount",gogn)]

    return template("midannarverkefni/index.tpl", gogn = gogn, oll_fyrirtaeki = oll_fyrirtaeki, oll_fyrirtaeki_linkar = oll_fyrirtaeki_linkar, bensin_listi = bensin_listi)

@route ("/midannarverkefni/<nafn:path>/")
def midannarverkefni_bensinstod(nafn):
    oll_fyrirtaeki = finnaOllFyrirtaeki()

    with urllib.request.urlopen("http://apis.is/petrol") as url:
        gogn = json.loads(url.read().decode())

    oll_fyrirtaeki_linkar = []

    for fyrirtaeki in oll_fyrirtaeki:
        oll_fyrirtaeki_linkar.append(make_link(fyrirtaeki))
    
    if nafn not in oll_fyrirtaeki_linkar:
        return '<h2 style="color:red;text-align: center;">Þessi síða finnst ekki</h2>'

    else:
        nafn_bensinstodvar = oll_fyrirtaeki[oll_fyrirtaeki_linkar.index(nafn)]
        return template("midannarverkefni/bensinstod.tpl", gogn = gogn, numer = nafn, bensinstod_nafn = nafn_bensinstodvar)

@route ("/midannarverkefni/<nafn:path>/stod_<numer:int>")
def midannarverkefni_stod(nafn, numer):
    oll_fyrirtaeki = finnaOllFyrirtaeki()

    with urllib.request.urlopen("http://apis.is/petrol") as url:
        gogn = json.loads(url.read().decode())

    oll_fyrirtaeki_linkar = []

    for fyrirtaeki in oll_fyrirtaeki:
        oll_fyrirtaeki_linkar.append(make_link(fyrirtaeki))
    
    if nafn not in oll_fyrirtaeki_linkar:
        return '<h2 style="color:red;text-align: center;">Þessi síða finnst ekki</h2>'

    else:
        nafn_bensinstodvar = oll_fyrirtaeki[oll_fyrirtaeki_linkar.index(nafn)]
        return template("midannarverkefni/stod_kort.tpl", gogn = gogn, numer = nafn, bensinstod_nafn = nafn_bensinstodvar, stod_numer = int(numer))

#  ========================================
#  Verkefni 5
#  ========================================
@route("/Verkefni_5")
def Verkefni_5():
    return template("Verkefni_5/index.tpl")

@route("/Verkefni_5/nidurstada", method="POST")
def Verkefni_5_nidurstada():
    nafn = request.forms.fullt_nafn
    namskeid = request.forms.getall("namskeid")
    gata = request.forms.gata
    baer = request.forms.baer
    postnumer = request.forms.postnumer
    tolvupostur = request.forms.tolvupostur
    simanumer = request.forms.simanumer
    matur = request.forms.matur

    # Nafn
    if " " not in nafn:
        return template("Verkefni_5/error.tpl", t="Vinamlegast sláðu inn fullt nafn")

    # Tölvupóstur
    att = False
    puntur = False
    for stafur in tolvupostur:
        if att is True:
            if stafur == ".":
                puntur = True
        if stafur == "@":
            att = True
    if puntur is not True:
        return template("Verkefni_5/error.tpl", t="Þetta er ekki alvöru tölvupóstfang")
    
    # Símanúmer
    if len(simanumer) != 7 or simanumer[0] not in ["4","5","6","7","8"]:
        return template("Verkefni_5/error.tpl", t="Þetta er ekki alvöru símanúmer")
    for tala in simanumer:
        if tala not in ["0","1","2","3","4","5","6","7","8","9"]:
            return template("Verkefni_5/error.tpl", t="Þetta er ekki alvöru símanúmer")
        
    # Póstnúmer
    postnumer_listi = []
    skra = open("static/Verkefni_5/postnumer.csv","r")
    for line in skra:
        line.split(";")
        postnumer_listi.append(line[0:3])
    del postnumer_listi[0]

    if postnumer not in postnumer_listi:
        return template("Verkefni_5/error.tpl", t="Þetta er ekki alvöru póstnúmer")

    # Gata
    if " " not in gata:
        return template("Verkefni_5/error.tpl", t="Það vantar götu númer")

    # Verð
    verdAnVSK = 0
    if matur == "Já":
        verdAnVSK += 1000
    for nam in namskeid:
        verdAnVSK += 5000

    # Námskeið
    oll_namskeid = ""
    teljari = 0
    for nam in namskeid:
        if teljari == 0:
            oll_namskeid += str(nam)
            teljari += 1
        else:
            oll_namskeid += ", "+str(nam)
            teljari += 1

    return template("Verkefni_5/nidurstada.tpl", nafn=nafn, namskeid=namskeid, gata=gata, baer=baer, postnumer=postnumer, tolvupostur=tolvupostur, simanumer=simanumer, matur=matur, oll_namskeid=oll_namskeid, verdAnVSK=verdAnVSK)

#  ========================================
#  Verkefni 6 gamalt
#  ========================================
@route("/Verkefni_6_gamalt")
def Verkefni_6_gamalt():
    username = request.get_cookie("innskraning_hrolfurgylfa_heroku_verkefni6", secret='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')
    print("Cookie username:",username)
    oll_password = saekjaNotendur()
    print("Allir notendur:",oll_password)
    notandi_til = False
    for notandi in oll_password:
        if notandi[0] == username:
            notandi_til = True
            if notandi[2] == "1":
                return template("Verkefni_6_gamalt/admin.tpl", u = str(username), o = oll_password)
            else:
                return template("Verkefni_6_gamalt/error.tpl", t = "Þessi notandi er ekki með næg réttindi", u = username)
    
    if notandi_til is False:
        return template("Verkefni_6_gamalt/index.tpl")

@route("/Verkefni_6_gamalt/innskraning", method="POST")
def Verkefni_6_gamalt_innskraning():

    username = request.forms.username
    password = request.forms.password
    
    oll_password = saekjaNotendur()
    
    notandi_fundinn = False
    notandi_rett_adgangsord = False
    user_rettir = 0
    for notandi in oll_password:
        if notandi[0] == username:
            notandi_fundinn = True
            if notandi[1] == password:
                response.set_cookie("innskraning_hrolfurgylfa_heroku_verkefni6", notandi[0], secret="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")
                notandi_rett_adgangsord = True
                user_rettir = int(notandi[2])
                break
    
    if notandi_fundinn is True and notandi_rett_adgangsord is True and user_rettir is 1:
        return redirect("/Verkefni_6_gamalt")
    elif notandi_fundinn is True and notandi_rett_adgangsord is True:
        return template("Verkefni_6_gamalt/error.tpl", t = "Þessi notandi er ekki með næg réttindi", u = notandi[0])
    elif notandi_fundinn is True and notandi_rett_adgangsord is False:
        return template("Verkefni_6_gamalt/error.tpl", t = "Rangt notendanafn eða lykilorð")
    else:
        return template("Verkefni_6_gamalt/error.tpl", t = "Rangt notendanafn eða lykilorð")

@route("/Verkefni_6_gamalt/utskra")
def Verkefni_6_gamalt_utskra():
    username = request.query.u
    if username == request.get_cookie("innskraning_hrolfurgylfa_heroku_verkefni6", secret='MIIJKgIBAAKCAgEA4ocooqpQVLMdFW7wncf4nz9vbxSbkP2IiEz+t5WxjkCKdvtN5ERXYjcwYQTnVELOE43Lv/BCdRBKr2eULKEZd7OvuVw0yz//7QucE7iQ3qx6tAdsOB+2QvDRpmf1RFpxh9SzWf6IDk+q8MzeUHV0r4//9sjd0B3VbN4dxzRwKk1bFbtF3EuoLAob8NrmyGr4kCEhiqyqnGw9G9Z69vSV1zwMN6h5tGr6wV5Ne5F71OFX5r5KhyOFFyWWy5p8oV0ve+NGQ90uoaaMwmHWNBcorTut2EZxb+kQtk9UXUQjfbf3ZoO9oKvkMMTrUv7VEQtoeDi+RJ3h0HLqrim2CV4GoHfQbdOzLP2qubofg+zFDQ2+i7oC3ToPpuMf43zJRnXzevQw24WMKOJURvTGS2hWS0DjnTCvtPTi3aPs4dk8IU81g/DT6NUn3UgD3Exj0gYe7OZWYLlB5fSgLhWfGv25qhoqPf0sFmJIp5eX06gBwtTcs56RJqt6mAeBnuWA1E2xr+8MQiAaUVnoCaA04D9mGcB/haqewZxX8NOoi+4LtfgWtsNArB/gqhRb59Ri8RovMhz//JPNHZbPaB+QMRoNfYU7vJ1dveZ/av2qN1Yaoh1ilJgBYWTZQ7okQI/XUfxEby6E1pjFZ/IiYgzGppeB+ILOG/zBkE6aevfh4XmOB5ECAwEAAQKCAgEAkSbeKO1NMBjdiABgehnK++/f7aOc01lCBWSgyu5Gqco9b2Q0UxJfk/WdMG299UYhWnI/nqvLScu4r5CFZ9uKwCMJdJLa2WoXCcOorRJU8fo/XeBrvcLEPTymeiSfCr+Rg+INUptAfzsZY9dClPfOXzi8YVvwlgyn12y0VBML1G9g8Bnh9/kat616nekGfGHfCCvSnFNrt3O77HyQqnGrGhHGGlwAMFVkfEd7CrT8Tjpe4uIIS3O9MknJyIkjVxqo9I97VL0Dxl08UMn0QcidLfPRv4XT5kvHg6ptep3QyBv7kVrVRYEfZQipabMUwCk5Nd/WO42XRsR8EEF1/aacQz4hnZ5PGH464z+InMBPTqFCucBW0G/S7AftNSkno+hFe8Md5feiUBtO/iqs6VgwQmHcHCYSPUEQ1GP/syfkJBC4/eWU/EkTOem6+C9haqzpfdQpUvSqi//ku3FlXWThKj45pwgvN1VYj8ibbe7kJCQB6PqWoL8CgTvDA+ZqVGblCa0fq8nIUb/qvM1du+FuEQHViQlVEZC/7r0wFn1ppwPUaUQwurZEfp/C1bX8mMwFvn2QOp0sMcoqvY/7xbGvRar5T0ob5xtIHNTH6+Zk+sjqLvErNNxRjZGnqB+0Z4QSh4JZ+aHj2SuGHG2sqB0rzcIeVjkoVMm+6KU3GZxfuAkCggEBAPMnRQckgj9TvYb955Xd8fo5AK+iJb/y5fI/s1p2iYyj4lw25TYhwnSLGdoSNem5/OlGXQ9Gi5I+mUk5Z9Oy3ZuXx5DlOtavm0yiX0H90I9UBs1v7N7qriohkIh5o9cGRdqgLhEpWX3pSagSL8IfgMJZv2W39dzt+RfWcwCnOpMcfolIU0El8Ww/Gvs1B525nol3aUT999ze9L+PTkVSNwqQWjZl6HHguXAL3tyQWPbgUHGS16hsFZNn70u8+9I70yw/EMoA1dtyZFhN5Y0y9DHul3JkQql2dN0/CcfqCCPOlNVdPXMFDwLRMxvAhYBOG6SoUcz4MmCoCdAjps1WjdMCggEBAO5/BkuoJNDsrBUEcfdEQsIqurSjgD4LkEOwnpsFcermTcpuDMJJ+4q/czMLdAncPRCtS6BtTIcMEAttPhATFecDGSEvkUTPRH/6Xf9B19/W9u/UbPbfntMiaORzLH8qALoSXRAlnEyBxDihoVkNEiTPzsbXY+gYuFr4iHwwy1Td1KmbWhF3Xuo7HM269vuqMt3wmVmIYs9mEMMKKTpcGc8JHcsPLFgDTLQnVBRNQWLyvebiJt+0xhZ4NqsFkF81wVpSenme9NmXgSXcrMw6ZXlms0D7/+zVyAciSUGNohDGpB/E4MDQrbLu9pDk1WcDatva2rXP8FhpTTMbl5fDIosCggEBAKXoXIwkGA73p3EtW9ABUXNHY7VzMMjJBqcFWe5WxUHGLNR4zGrkHBeDNg96r3ib4/qTfTnIC8GsntC8r6BeAiGBLbUrA7uqtI9UlySi96RkVAPm47uya0XqAwFr5iP4br9e3i/tg9eKzywzxIxzDFsP+61/GO43Hehq9aszb58jKR+ozs28Av+2C0XuiBTRq1/mr1hY5b+6DUuLj39zOoUlu7g0TqctC7ptDxJ2F43Tvm/QHwAXR519pGSMPVLUaSFeoqkCaulCIz+xXvi6FK7hOkreKDIS1miD87uJbyZndVwkM6KAiB6G+ZVtBmpmYSw3gSEXFOCop5FyUgT3kusCggEAMmMX22gczx8RhCc6RLlhOVB5vaxFbdZXllV8TNgrpysdCEWT4IBs6nVkS0aCL4seQ6W5Mp2k62s7AI8F67N8jx/ycTZxhI4dtMQak9E/YIU0Cptgog/AqG6+pnVG0172ZFl42+52RRutbyGGyx+d07UrxIrBCsoeOOoFO+e7LaToRyURNFt57BatETIM+EKPGKC6ZVYROiwgInTFHRVURo9wgfQktDuOOwmME/X2eIc8Y8kn2V+B8kFXm25DgDoFLaX7RjK1HDuMB4nF4Cf+RFXUTUhwW4MXDZrKy1S3BsBQ8H1R1qq/5+vgn+AYzfjE3MoyJvNVnfgxXTjZIDET3QKCAQEApFtPGRyIc7qTaG8e7hTUhjE1uwk4Fk3QSGJAyzJHbk9d2Au/m//PJc3SSqne//As8ScvJqXSjS9KrYiOqDynY38CLe5wteLXwVkAmjQj7JM+e2BWBSiWbGP3GvkBqSPZnPhNGwvlHxOV32t2rIGacA4czRZmyO9LGwIyItoxQ8xv06KJ/P4gkUafYD22JQE3q0JzWXzymLDuZ91pGWtAObyKAD00e88R/cpX+jeSp69WUif/Vy0EwZ2K8jkulWQ6unuBpYvMY3Va3S3+p/fhOA37cT3uScFV63vbesj4ym/DqjcYYV6RV3VCEL9aQbOrygRb6NDhUXNj7FVniEQqvQ=='):
        response.delete_cookie("innskraning_hrolfurgylfa_heroku_verkefni6", secret='MIIJKgIBAAKCAgEA4ocooqpQVLMdFW7wncf4nz9vbxSbkP2IiEz+t5WxjkCKdvtN5ERXYjcwYQTnVELOE43Lv/BCdRBKr2eULKEZd7OvuVw0yz//7QucE7iQ3qx6tAdsOB+2QvDRpmf1RFpxh9SzWf6IDk+q8MzeUHV0r4//9sjd0B3VbN4dxzRwKk1bFbtF3EuoLAob8NrmyGr4kCEhiqyqnGw9G9Z69vSV1zwMN6h5tGr6wV5Ne5F71OFX5r5KhyOFFyWWy5p8oV0ve+NGQ90uoaaMwmHWNBcorTut2EZxb+kQtk9UXUQjfbf3ZoO9oKvkMMTrUv7VEQtoeDi+RJ3h0HLqrim2CV4GoHfQbdOzLP2qubofg+zFDQ2+i7oC3ToPpuMf43zJRnXzevQw24WMKOJURvTGS2hWS0DjnTCvtPTi3aPs4dk8IU81g/DT6NUn3UgD3Exj0gYe7OZWYLlB5fSgLhWfGv25qhoqPf0sFmJIp5eX06gBwtTcs56RJqt6mAeBnuWA1E2xr+8MQiAaUVnoCaA04D9mGcB/haqewZxX8NOoi+4LtfgWtsNArB/gqhRb59Ri8RovMhz//JPNHZbPaB+QMRoNfYU7vJ1dveZ/av2qN1Yaoh1ilJgBYWTZQ7okQI/XUfxEby6E1pjFZ/IiYgzGppeB+ILOG/zBkE6aevfh4XmOB5ECAwEAAQKCAgEAkSbeKO1NMBjdiABgehnK++/f7aOc01lCBWSgyu5Gqco9b2Q0UxJfk/WdMG299UYhWnI/nqvLScu4r5CFZ9uKwCMJdJLa2WoXCcOorRJU8fo/XeBrvcLEPTymeiSfCr+Rg+INUptAfzsZY9dClPfOXzi8YVvwlgyn12y0VBML1G9g8Bnh9/kat616nekGfGHfCCvSnFNrt3O77HyQqnGrGhHGGlwAMFVkfEd7CrT8Tjpe4uIIS3O9MknJyIkjVxqo9I97VL0Dxl08UMn0QcidLfPRv4XT5kvHg6ptep3QyBv7kVrVRYEfZQipabMUwCk5Nd/WO42XRsR8EEF1/aacQz4hnZ5PGH464z+InMBPTqFCucBW0G/S7AftNSkno+hFe8Md5feiUBtO/iqs6VgwQmHcHCYSPUEQ1GP/syfkJBC4/eWU/EkTOem6+C9haqzpfdQpUvSqi//ku3FlXWThKj45pwgvN1VYj8ibbe7kJCQB6PqWoL8CgTvDA+ZqVGblCa0fq8nIUb/qvM1du+FuEQHViQlVEZC/7r0wFn1ppwPUaUQwurZEfp/C1bX8mMwFvn2QOp0sMcoqvY/7xbGvRar5T0ob5xtIHNTH6+Zk+sjqLvErNNxRjZGnqB+0Z4QSh4JZ+aHj2SuGHG2sqB0rzcIeVjkoVMm+6KU3GZxfuAkCggEBAPMnRQckgj9TvYb955Xd8fo5AK+iJb/y5fI/s1p2iYyj4lw25TYhwnSLGdoSNem5/OlGXQ9Gi5I+mUk5Z9Oy3ZuXx5DlOtavm0yiX0H90I9UBs1v7N7qriohkIh5o9cGRdqgLhEpWX3pSagSL8IfgMJZv2W39dzt+RfWcwCnOpMcfolIU0El8Ww/Gvs1B525nol3aUT999ze9L+PTkVSNwqQWjZl6HHguXAL3tyQWPbgUHGS16hsFZNn70u8+9I70yw/EMoA1dtyZFhN5Y0y9DHul3JkQql2dN0/CcfqCCPOlNVdPXMFDwLRMxvAhYBOG6SoUcz4MmCoCdAjps1WjdMCggEBAO5/BkuoJNDsrBUEcfdEQsIqurSjgD4LkEOwnpsFcermTcpuDMJJ+4q/czMLdAncPRCtS6BtTIcMEAttPhATFecDGSEvkUTPRH/6Xf9B19/W9u/UbPbfntMiaORzLH8qALoSXRAlnEyBxDihoVkNEiTPzsbXY+gYuFr4iHwwy1Td1KmbWhF3Xuo7HM269vuqMt3wmVmIYs9mEMMKKTpcGc8JHcsPLFgDTLQnVBRNQWLyvebiJt+0xhZ4NqsFkF81wVpSenme9NmXgSXcrMw6ZXlms0D7/+zVyAciSUGNohDGpB/E4MDQrbLu9pDk1WcDatva2rXP8FhpTTMbl5fDIosCggEBAKXoXIwkGA73p3EtW9ABUXNHY7VzMMjJBqcFWe5WxUHGLNR4zGrkHBeDNg96r3ib4/qTfTnIC8GsntC8r6BeAiGBLbUrA7uqtI9UlySi96RkVAPm47uya0XqAwFr5iP4br9e3i/tg9eKzywzxIxzDFsP+61/GO43Hehq9aszb58jKR+ozs28Av+2C0XuiBTRq1/mr1hY5b+6DUuLj39zOoUlu7g0TqctC7ptDxJ2F43Tvm/QHwAXR519pGSMPVLUaSFeoqkCaulCIz+xXvi6FK7hOkreKDIS1miD87uJbyZndVwkM6KAiB6G+ZVtBmpmYSw3gSEXFOCop5FyUgT3kusCggEAMmMX22gczx8RhCc6RLlhOVB5vaxFbdZXllV8TNgrpysdCEWT4IBs6nVkS0aCL4seQ6W5Mp2k62s7AI8F67N8jx/ycTZxhI4dtMQak9E/YIU0Cptgog/AqG6+pnVG0172ZFl42+52RRutbyGGyx+d07UrxIrBCsoeOOoFO+e7LaToRyURNFt57BatETIM+EKPGKC6ZVYROiwgInTFHRVURo9wgfQktDuOOwmME/X2eIc8Y8kn2V+B8kFXm25DgDoFLaX7RjK1HDuMB4nF4Cf+RFXUTUhwW4MXDZrKy1S3BsBQ8H1R1qq/5+vgn+AYzfjE3MoyJvNVnfgxXTjZIDET3QKCAQEApFtPGRyIc7qTaG8e7hTUhjE1uwk4Fk3QSGJAyzJHbk9d2Au/m//PJc3SSqne//As8ScvJqXSjS9KrYiOqDynY38CLe5wteLXwVkAmjQj7JM+e2BWBSiWbGP3GvkBqSPZnPhNGwvlHxOV32t2rIGacA4czRZmyO9LGwIyItoxQ8xv06KJ/P4gkUafYD22JQE3q0JzWXzymLDuZ91pGWtAObyKAD00e88R/cpX+jeSp69WUif/Vy0EwZ2K8jkulWQ6unuBpYvMY3Va3S3+p/fhOA37cT3uScFV63vbesj4ym/DqjcYYV6RV3VCEL9aQbOrygRb6NDhUXNj7FVniEQqvQ==')
    return redirect("/Verkefni_6_gamalt")

@route("/Verkefni_6_gamalt/eyda_notenda")
def Verkefni_6_gamalt_eyda_notenda():
    breyta_user = request.query.u
    current_user = request.get_cookie("innskraning_hrolfurgylfa_heroku_verkefni6", secret='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')
    allir_notendur = saekjaNotendur()

    for notandi in allir_notendur:
        if notandi[0] == current_user:
            if notandi[2] == "1":
                eydaNotenda(breyta_user)
                break
            else: return template("Verkefni_6_gamalt/error.tpl", t = "Þessi notandi er ekki með næg réttindi")

    return redirect("/Verkefni_6_gamalt")

@route("/Verkefni_6_gamalt/breyta_notendanafni")
def Verkefni_6_gamalt_breyta_notendanafni():
    breyta_user = request.query.u
    current_user = request.get_cookie("innskraning_hrolfurgylfa_heroku_verkefni6", secret='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')
    allir_notendur = saekjaNotendur()

    for notandi in allir_notendur:
        if notandi[0] == current_user:
            if notandi[2] == "1":
                break

    return redirect("/Verkefni_6_gamalt")

#  ========================================
#  Verkefni 6
#  ========================================
session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 86400,
    'session.data_dir': './data',
    'session.auto': True
}
app = SessionMiddleware(bottle.app(), session_opts)

@route("/Verkefni_6")
def Verkefni_6():
    allar_vorur = buaTilHluti()
    session = bottle.request.environ.get('beaker.session')
    session["fot"] = session.get("fot","")
    allt_i_korfu = saekjaAlltIKorfu(session)

    return template("Verkefni_6/index.tpl", allar_vorur=allar_vorur, allt_i_korfu = allt_i_korfu)

@route("/Verkefni_6/vara")
def Verkefni_6_vara():
    vara = request.query.i
    allar_vorur = buaTilHluti()
    session = bottle.request.environ.get('beaker.session')
    session["fot"] = session.get("fot","")
    allt_i_korfu = saekjaAlltIKorfu(session)

    return template("Verkefni_6/bud.tpl", allar_vorur=allar_vorur, allt_i_korfu = allt_i_korfu, vara = vara)

@route("/Verkefni_6/kaupa_voru")
def Verkefni_6_kaupa_voru():
    vara = request.query.i
    vara = baetaVid0(vara)
    session = bottle.request.environ.get('beaker.session')
    session["fot"] = session.get("fot","")
    session["fot"] += vara
    session.save()
    return redirect("/Verkefni_6")

@route("/Verkefni_6/karfa")
def Verkefni_6_karfa():
    allar_vorur = buaTilHluti()
    session = bottle.request.environ.get('beaker.session')
    session["fot"] = session.get("fot","")
    allt_i_korfu = saekjaAlltIKorfu(session)

    a_vorur_radad = []
    allt_komid = ""
    for vara in allt_i_korfu:
        if vara not in allt_komid:
            allt_komid += str(vara)
            listi2 = [vara]
            a_vorur_radad.append(listi2)
        else:
            for x in a_vorur_radad:
                if vara in x:
                    x.append(vara)

    heildarverd = 0
    for vara in allt_i_korfu:
        heildarverd += allar_vorur[2][vara[1]]

    if len(allt_i_korfu) > 0:
        return template("Verkefni_6/karfa.tpl", allar_vorur=allar_vorur, allt_i_korfu = allt_i_korfu, a_vorur_radad = a_vorur_radad, heildarverd = heildarverd)
    else:
        return template("Verkefni_6/tom_karfa.tpl", allt_i_korfu = allt_i_korfu)

@route("/Verkefni_6/eyda_ur_korfu")
def Verkefni_6_eyda_ur_korfu():
    vara = request.query.i
    vara = baetaVid0(vara)
    session = bottle.request.environ.get('beaker.session')
    session["fot"] = session.get("fot","")
    allt_i_korfu = saekjaAlltIKorfu(session)

    strengur = ""
    allt_i_korfu2 = []
    for x in allt_i_korfu:
        if x != vara:
            allt_i_korfu2.append(x)
    
    for x in allt_i_korfu2:
        strengur += x

    session["fot"] = strengur

    session.save()
    return redirect("/Verkefni_6/karfa")

#  ========================================
#  Verkefni 7
#  ========================================
@route("/Verkefni_7")
def Verkefni_7():
    username = request.get_cookie("innskraning_hrolfurgylfa_heroku_verkefni6", secret='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')
    print("Cookie username:",username)
    oll_password = saekjaNotendurV7()
    print("Allir notendur:",oll_password)
    notandi_til = False
    for notandi in oll_password:
        if notandi[0] == username:
            u = notandi[0]
            n = notandi[2]
            notandi_til = True
            return template("Verkefni_7/admin.tpl", n = n, u = u, o = oll_password)
    
    if notandi_til is False:
        return template("Verkefni_7/index.tpl")

@route("/Verkefni_7/innskraning", method="POST")
def Verkefni_7_innskraning():

    username = request.forms.username
    password = request.forms.password
    
    oll_password = saekjaNotendurV7()
    
    notandi_fundinn = False
    notandi_rett_adgangsord = False
    for notandi in oll_password:
        if notandi[0] == username:
            notandi_fundinn = True
            if notandi[1] == password:
                response.set_cookie("innskraning_hrolfurgylfa_heroku_verkefni6", notandi[0], secret="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")
                notandi_rett_adgangsord = True
                break
    
    if notandi_fundinn is True and notandi_rett_adgangsord is True:
        return redirect("/Verkefni_7")
    elif notandi_fundinn is True and notandi_rett_adgangsord is False:
        return template("Verkefni_7/error.tpl", t = "Rangt notendanafn eða lykilorð")
    else:
        return template("Verkefni_7/error.tpl", t = "Rangt notendanafn eða lykilorð")

@route("/Verkefni_7/bua_til_adgang")
def Verkefni_7_bua_til_adgang():
    return template("Verkefni_7/nyr_notandi.tpl")

@route("/Verkefni_7/gera_notanda", method="POST")
def Verkefni_7_gera_notanda():
    nafn = request.forms.nafn
    username = request.forms.username
    password = request.forms.password
    password2 = request.forms.password2

    notendur = saekjaNotendurV7()
    for notandi in notendur:
        if notandi[0] == username:
            return template("Verkefni_7/error.tpl", t = "Þesi notandi er núþegar til", l = "/Verkefni_7/bua_til_adgang")

    if password != password2:
        return template("Verkefni_7/error.tpl", t = "Aðgangsorðin sem þú settir inn voru ekki eins", l = "/Verkefni_7/bua_til_adgang")

    connection = pymysql.connect(host='tsuts.tskoli.is',
                                user='2109013290',
                                password='mypassword',
                                db='2109013290_Verkefni_7_VEB',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    
    cursor = connection.cursor()
    sql = 'INSERT INTO USERS(USER_USERNAME, USER_PASSWORD, USER_NAME) VALUES ("'+str(username)+'", "'+str(password)+'", "'+str(nafn)+'")'
    cursor.execute(sql)
    connection.commit()
    connection.close()
    return redirect("/Verkefni_7")

@route("/Verkefni_7/utskra")
def Verkefni_7_utskra():
    username = request.query.u
    if username == request.get_cookie("innskraning_hrolfurgylfa_heroku_verkefni6", secret='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'):
        response.delete_cookie("innskraning_hrolfurgylfa_heroku_verkefni6", secret='MIIJKgIBAAKCAgEA4ocooqpQVLMdFW7wncf4nz9vbxSbkP2IiEz+t5WxjkCKdvtN5ERXYjcwYQTnVELOE43Lv/BCdRBKr2eULKEZd7OvuVw0yz//7QucE7iQ3qx6tAdsOB+2QvDRpmf1RFpxh9SzWf6IDk+q8MzeUHV0r4//9sjd0B3VbN4dxzRwKk1bFbtF3EuoLAob8NrmyGr4kCEhiqyqnGw9G9Z69vSV1zwMN6h5tGr6wV5Ne5F71OFX5r5KhyOFFyWWy5p8oV0ve+NGQ90uoaaMwmHWNBcorTut2EZxb+kQtk9UXUQjfbf3ZoO9oKvkMMTrUv7VEQtoeDi+RJ3h0HLqrim2CV4GoHfQbdOzLP2qubofg+zFDQ2+i7oC3ToPpuMf43zJRnXzevQw24WMKOJURvTGS2hWS0DjnTCvtPTi3aPs4dk8IU81g/DT6NUn3UgD3Exj0gYe7OZWYLlB5fSgLhWfGv25qhoqPf0sFmJIp5eX06gBwtTcs56RJqt6mAeBnuWA1E2xr+8MQiAaUVnoCaA04D9mGcB/haqewZxX8NOoi+4LtfgWtsNArB/gqhRb59Ri8RovMhz//JPNHZbPaB+QMRoNfYU7vJ1dveZ/av2qN1Yaoh1ilJgBYWTZQ7okQI/XUfxEby6E1pjFZ/IiYgzGppeB+ILOG/zBkE6aevfh4XmOB5ECAwEAAQKCAgEAkSbeKO1NMBjdiABgehnK++/f7aOc01lCBWSgyu5Gqco9b2Q0UxJfk/WdMG299UYhWnI/nqvLScu4r5CFZ9uKwCMJdJLa2WoXCcOorRJU8fo/XeBrvcLEPTymeiSfCr+Rg+INUptAfzsZY9dClPfOXzi8YVvwlgyn12y0VBML1G9g8Bnh9/kat616nekGfGHfCCvSnFNrt3O77HyQqnGrGhHGGlwAMFVkfEd7CrT8Tjpe4uIIS3O9MknJyIkjVxqo9I97VL0Dxl08UMn0QcidLfPRv4XT5kvHg6ptep3QyBv7kVrVRYEfZQipabMUwCk5Nd/WO42XRsR8EEF1/aacQz4hnZ5PGH464z+InMBPTqFCucBW0G/S7AftNSkno+hFe8Md5feiUBtO/iqs6VgwQmHcHCYSPUEQ1GP/syfkJBC4/eWU/EkTOem6+C9haqzpfdQpUvSqi//ku3FlXWThKj45pwgvN1VYj8ibbe7kJCQB6PqWoL8CgTvDA+ZqVGblCa0fq8nIUb/qvM1du+FuEQHViQlVEZC/7r0wFn1ppwPUaUQwurZEfp/C1bX8mMwFvn2QOp0sMcoqvY/7xbGvRar5T0ob5xtIHNTH6+Zk+sjqLvErNNxRjZGnqB+0Z4QSh4JZ+aHj2SuGHG2sqB0rzcIeVjkoVMm+6KU3GZxfuAkCggEBAPMnRQckgj9TvYb955Xd8fo5AK+iJb/y5fI/s1p2iYyj4lw25TYhwnSLGdoSNem5/OlGXQ9Gi5I+mUk5Z9Oy3ZuXx5DlOtavm0yiX0H90I9UBs1v7N7qriohkIh5o9cGRdqgLhEpWX3pSagSL8IfgMJZv2W39dzt+RfWcwCnOpMcfolIU0El8Ww/Gvs1B525nol3aUT999ze9L+PTkVSNwqQWjZl6HHguXAL3tyQWPbgUHGS16hsFZNn70u8+9I70yw/EMoA1dtyZFhN5Y0y9DHul3JkQql2dN0/CcfqCCPOlNVdPXMFDwLRMxvAhYBOG6SoUcz4MmCoCdAjps1WjdMCggEBAO5/BkuoJNDsrBUEcfdEQsIqurSjgD4LkEOwnpsFcermTcpuDMJJ+4q/czMLdAncPRCtS6BtTIcMEAttPhATFecDGSEvkUTPRH/6Xf9B19/W9u/UbPbfntMiaORzLH8qALoSXRAlnEyBxDihoVkNEiTPzsbXY+gYuFr4iHwwy1Td1KmbWhF3Xuo7HM269vuqMt3wmVmIYs9mEMMKKTpcGc8JHcsPLFgDTLQnVBRNQWLyvebiJt+0xhZ4NqsFkF81wVpSenme9NmXgSXcrMw6ZXlms0D7/+zVyAciSUGNohDGpB/E4MDQrbLu9pDk1WcDatva2rXP8FhpTTMbl5fDIosCggEBAKXoXIwkGA73p3EtW9ABUXNHY7VzMMjJBqcFWe5WxUHGLNR4zGrkHBeDNg96r3ib4/qTfTnIC8GsntC8r6BeAiGBLbUrA7uqtI9UlySi96RkVAPm47uya0XqAwFr5iP4br9e3i/tg9eKzywzxIxzDFsP+61/GO43Hehq9aszb58jKR+ozs28Av+2C0XuiBTRq1/mr1hY5b+6DUuLj39zOoUlu7g0TqctC7ptDxJ2F43Tvm/QHwAXR519pGSMPVLUaSFeoqkCaulCIz+xXvi6FK7hOkreKDIS1miD87uJbyZndVwkM6KAiB6G+ZVtBmpmYSw3gSEXFOCop5FyUgT3kusCggEAMmMX22gczx8RhCc6RLlhOVB5vaxFbdZXllV8TNgrpysdCEWT4IBs6nVkS0aCL4seQ6W5Mp2k62s7AI8F67N8jx/ycTZxhI4dtMQak9E/YIU0Cptgog/AqG6+pnVG0172ZFl42+52RRutbyGGyx+d07UrxIrBCsoeOOoFO+e7LaToRyURNFt57BatETIM+EKPGKC6ZVYROiwgInTFHRVURo9wgfQktDuOOwmME/X2eIc8Y8kn2V+B8kFXm25DgDoFLaX7RjK1HDuMB4nF4Cf+RFXUTUhwW4MXDZrKy1S3BsBQ8H1R1qq/5+vgn+AYzfjE3MoyJvNVnfgxXTjZIDET3QKCAQEApFtPGRyIc7qTaG8e7hTUhjE1uwk4Fk3QSGJAyzJHbk9d2Au/m//PJc3SSqne//As8ScvJqXSjS9KrYiOqDynY38CLe5wteLXwVkAmjQj7JM+e2BWBSiWbGP3GvkBqSPZnPhNGwvlHxOV32t2rIGacA4czRZmyO9LGwIyItoxQ8xv06KJ/P4gkUafYD22JQE3q0JzWXzymLDuZ91pGWtAObyKAD00e88R/cpX+jeSp69WUif/Vy0EwZ2K8jkulWQ6unuBpYvMY3Va3S3+p/fhOA37cT3uScFV63vbesj4ym/DqjcYYV6RV3VCEL9aQbOrygRb6NDhUXNj7FVniEQqvQ==')
    return redirect("/Verkefni_7")

@route("/Verkefni_7/eyda_notenda")
def Verkefni_7_eyda_notenda():
    user = request.query.u
    oll_password = saekjaNotendurV7()
    username = request.get_cookie("innskraning_hrolfurgylfa_heroku_verkefni6", secret='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')

    notandi_til = False
    for notandi in oll_password:
        if notandi[0] == username:
            notandi_til = True
            connection = pymysql.connect(host='tsuts.tskoli.is',
                                user='2109013290',
                                password='mypassword',
                                db='2109013290_Verkefni_7_VEB',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
            cursor = connection.cursor()

            sql = 'DELETE FROM USERS WHERE USER_USERNAME = "'+str(user)+'"'
            cursor.execute(sql)

            connection.commit()
            connection.close()

            return redirect("/Verkefni_7")
    
    if notandi_til is False:
        return redirect("/Verkefni_7")

#  ========================================
#  Verkefni 7
#  ========================================

@route("/blog")
def Blog():
    listi = []
    connection = pymysql.connect(host='tsuts.tskoli.is',
                                user='2109013290',
                                password='mypassword',
                                db='2109013290_blog',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    sql = "SELECT ID, DAGSETNING, TITILL, TEXTI, POST_OWNER FROM POSTS"
    cursor.execute(sql)
    result = cursor.fetchall()

    for item in result:
        notandi_listi = []
        for x in ["ID", "DAGSETNING", "TITILL", "TEXTI", "POST_OWNER"]:
            notandi_listi.append(item[x])
        listi.append(notandi_listi)
        print("MySQL Listi",listi)
    
    connection.close()
    return template("Blog/forsida.tpl", l = listi)
#  ========================================
#  Annað
#  ========================================
# Til þess að setja inn myndir
@route("/static/<skra:path>")
def static_skrar(skra):
    return static_file(skra, root="static")

@route('/Myndir/<skra:path>')
def server_static(skra):
    return static_file(skra, root='Myndir')

#404 ERROR síða----------404 ERROR síða----------404 ERROR síða----------404 ERROR síða----------404 ERROR síða
@error(404)
def notFound(error):
    return '<h2 style="color:red;text-align: center;">Þessi síða finnst ekki</h2>'

try:
    bottle.run(host='0.0.0.0', port=argv[1], app=app)
except IndexError:
    bottle.run(host="localhost", port=8080, reloader=True, debug=True, app=app)
