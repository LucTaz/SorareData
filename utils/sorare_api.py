import json
import logging
from typing import Dict, List

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from .metaclasses import SingletonMeta

logger = logging.getLogger(__name__)


class SorareEndpoints:
    PLAYER_STATS = "https://www.soraredata.com/api/players/stats/{player_id}"
    TEAM_PLAYERS = "https://www.soraredata.com/api/teams/info/{team_id}"
    PLAYER_INFO = "https://www.soraredata.com/api/players/info/{player_id}"


class SorareAPI(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.driver = self._start_webdriver()

    def _start_webdriver(self):
        logging.info("SorareAPI: Starting webdriver")
        firefox_options = Options()
        firefox_options.headless = True
        return webdriver.Firefox(options=firefox_options)

    def get(self, url: str) -> dict:
        logging.info(f"SorareAPI: get url: {url}")

        self.driver.get(url)
        response = self.driver.find_element_by_tag_name("body").text
        return json.loads(response)

    def get_players_per_team(self, team_id: str) -> List[Dict]:
        logging.info(f"SorareAPI: get team: {team_id}")

        players = []
        response = self.get(SorareEndpoints.TEAM_PLAYERS.format(team_id=team_id))

        for player in response["licensed_players"]:
            player_fields = {}
            player_fields["player_name"] = player["player"]["FullName"]
            player_fields["player_id"] = player["player"]["PlayerId"]
            players.append(player_fields)

        return players

    def _get_player_match_data(self, player_id):
        logging.info(f"SorareAPI: Get player match data: {player_id}")
        return self.get(SorareEndpoints.PLAYER_STATS.format(player_id=player_id))

    def get_player_info(self, player_id):
        logging.info(f"SorareAPI: Get player info: {player_id}")
        return self.get(SorareEndpoints.PLAYER_INFO.format(player_id=player_id))

    def get_so5_stats(self, player_id) -> List[Dict]:
        logging.info(f"SorareAPI: Get player stats: {player_id}")

        matches = self._get_player_match_data(player_id)
        return [stats.get("stats") for stats in matches]

    def get_game_data(self, player_id) -> List[Dict]:
        logging.info(f"SorareAPI: Get match: {player_id}")

        matches = self._get_player_match_data(player_id)
        return [stats.get("game") for stats in matches]

    def close(self):
        logging.info(f"SorareAPI: Closing the webdriver")
        self.driver.close()
