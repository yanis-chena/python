from riotwatcher import LolWatcher


lol_watcher = LolWatcher('RGAPI-bf84cce7-2730-4c67-9bcc-1480e498ac4f')

my_region = 'euw1'

me = lol_watcher.summoner.by_name(my_region, 'Forrix')

my_match = lol_watcher.match.matchlist_by_account(my_region, me['accountId'], begin_index=000, end_index=100)

my_last = lol_watcher.match.by_id(my_region, my_match['matches'][0]['gameId'])

last_1 = my_last['participantIdentities']

a = 0

last_2 = last_1[a]['player']['summonerName']
playerNames = []

for x in last_1:
    last_2 = last_1[a]['player']['summonerName']
    playerNames.append(last_2)
    a += 1

print(playerNames)
print(me['name'])

print(me['name'] in playerNames)


