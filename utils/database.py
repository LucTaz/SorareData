import json
import logging
from typing import Union

from schemas.base import Base
from schemas.player_stats import PlayerStats
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .metaclasses import SingletonMeta

logger = logging.getLogger(__name__)


class LocalFiles:
    @staticmethod
    def store_to_file(path: str, content: dict):
        with open(path, mode="wb") as writer:
            writer.write(json.dumps(content, indent=2, ensure_ascii=False).encode("utf8"))
            logging.info(f"Stored file: {path}")

    @staticmethod
    def load_from_file(path: str):
        with open(path, mode="rb") as reader:
            content = json.load(reader)
        return content


class DataBase(metaclass=SingletonMeta):

    DB_NAME = "SorareDataRip"

    def __init__(self) -> None:
        self.engine = self._start_engine()
        self.session = sessionmaker(bind=self.engine)()

    def _start_engine(self):
        engine = create_engine(f"sqlite:///{self.DB_NAME}.db")
        Base.metadata.create_all(bind=engine)
        return engine

    def append_record(self, record: Union[PlayerStats, None]):
        existing_record = (
            self.session.query(PlayerStats)
            .filter_by(PlayerId=record.PlayerId)
            .filter_by(GameId=record.GameId)
            .first()
        )
        if not existing_record:
            self.session.add(record)
            self.session.commit()

    def close(self):
        self.session.close()
