fo_fo = open("follow_me.txt","r")
fo_me = open("me_follow.txt","r")

follow_me = []
me_follow = []

for i in fo_fo:
    follow_me.append(i.rstrip('\n'))
for x in fo_me:
    me_follow.append(x.rstrip('\n'))

imposter_save = open("imposter.txt","w")

follow_me = set(follow_me)
me_follow = set(me_follow)
result = list(me_follow-follow_me)

for x in result:
    imposter_save.write(x+'\n')
