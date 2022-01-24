import logging
from schemas.player_stats import PlayerStats

from utils.database import LocalFiles, DataBase
from utils.sorare_api import SorareAPI

logging.basicConfig(level=logging.INFO)


sorare = SorareAPI()
database = DataBase()


def ingest_player_per_team(team_ids):
    player_ids = []
    for team_id in team_ids:
        players = sorare.get_players_per_team(team_id)
        LocalFiles.store_to_file(f"output/teams/{team_id}.json", players)
        player_ids.extend([player.get("player_id") for player in players])
    return player_ids


def ingest_player_so5(player_ids: list):
    for player_id in player_ids:
        so5_scores = sorare.get_so5_stats(player_id)
        LocalFiles.store_to_file(f"output/players/{player_id}.json", so5_scores)


def ingest_game_data(player_ids: list):
    for player_id in player_ids:
        games = sorare.get_game_data(player_id)
        for game_data in games:
            LocalFiles.store_to_file(f"output/games/{game_data.get('GameId')}.json", game_data)


def enrich_player_records(player_ids):
    for player_id in player_ids:
        player_data = LocalFiles.load_from_file(f"output/players/{player_id}.json")
        enrich_data = sorare.get_player_info(player_id)
        for game_data in player_data:
            game_data["PlayerId"] = player_id
            game_data["PlayerName"] = enrich_data["player"]["FullName"]
        LocalFiles.store_to_file(f"output/players/{player_id}.json", player_data)


def store_player_to_db(player_ids: list):
    for player_id in player_ids:
        player = LocalFiles.load_from_file(f"output/players/{player_id}.json")
        for game in player:
            record = PlayerStats(**game)

            database.append_record(record)

    database.close()


def main_pipeline():

    # Get the player ids for every player in the following teams:
    ingest_teams = [
        "ajax-amsterdam",
        # "psv-eindhoven",
        # "utrecht-utrecht",
        # "feyenoord-rotterdam",
    ]
    player_ids = ingest_player_per_team(team_ids=ingest_teams)

    # player_ids = [
    #     "1393702092513437634654051348788105120071610476609320825657547900734069660691",
    #     "5053033846425754710853529377175118222182619115495884455122979774285092416065",
    #     "30288193883708656346837143579160224159713157308051116555817023611258158976190",
    #     "42665606170451751907492166239104645343304759030847736902770124274370024224554",
    #     "49700662560965501908600575173526655266237263625597339098624828191588475890402",
    #     "63932502680308222021483194430082178715319229083121661262530938517137874783927",
    #     "7439425016622120453108657068880382615896773274908952909081248411204509711509",
    #     "8406702665659676941336026424294882944810699562964186157207184447209301320720",
    #     "35114666823478871532922455645480227286935538164169097042562456194821882176932",
    #     "35823112983222491910831651711419931052701465064258329993131418468715015174323",
    #     "60850600279367459684796524195860987342413298298360417043851075131682740730102",
    #     "61137427421663572909426839926199182992661241677215160050574840237868066111404",
    #     "77915471994328879089183271752607401608123504372016828496967050054604835792989",
    #     "88672583896666198187460342828094444866353141255859195721984559374900762930578",
    #     "90352943630593776906774069127076374090618732001314547691560702095916437588936",
    #     "27745635617478463482143302304836375724147082400873814986970917902358844042750",
    #     "30547252015533972224181816491551825644928885224939313269680993310518799340570",
    #     "43098120847926672581121255406156222392475674227308596934570789367485731807691",
    #     "44137301699431911533520412001512548801932059718009445384037114452994980758032",
    #     "84575125596552140882064386892775939807653490375952857823936087769821788361595",
    #     "92863568368844658826764847416449381024221259627221878984752733481440316436628",
    #     "38415177838424193236705125566268679987839506395316965454236752400450123606258",
    #     "40946707797470167229296162201833851459362015827520427894532398807314963353941",
    #     "46180569504148164020103450581740849711233880339130983792032024777756967786986",
    #     "50166400733305245987445259038581862248098165934427002536851741874241679137447",
    #     "63180997867900447937908776170516012292175309388838371430366143712408711600235",
    #     "74547534080614137073842863223221167456535987874174898984759129698660283143039",
    #     "90603701234377116758599328813660298903391110912731667966117385697082231645342",
    #     "94093600118610829028292293586075402144036541188890769950927360004282655165221",
    #     "115196482106994982124798435455164458056829837456482750399953226217155996159810",
    # ]

    # Get player stats
    ingest_player_so5(player_ids)

    # # Enrich player stats:
    enrich_player_records(player_ids)

    # Store player games to DB
    store_player_to_db(player_ids)


# def test():

#     existing_record = (
#         database.session.query(Players)
#         .filter_by(
#             PlayerId="1393702092513437634654051348788105120071610476609320825657547900734069660691"
#         )
#         .filter_by(GameId="AJXGRO1615115701")
#         .first()
#     )
#     if not existing_record:
#         print("nope")
#     else:
#         print(existing_record)


if __name__ == "__main__":

    main_pipeline()

    sorare.close()
    database.close()
