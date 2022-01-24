import uuid

from sqlalchemy import Boolean, Column, Integer, String
from .base import Base


class PlayerStats(Base):
    __tablename__ = "player_stats"

    PlayerId = Column("PlayerId", String, primary_key=True)
    PlayerName = Column("PlayerName", String, primary_key=False)
    GameId = Column("GameId", String, primary_key=True)
    SO5Score = Column("SO5Score", Integer, primary_key=False)
    StartingScore = Column("StartingScore", Integer, primary_key=False)
    Goals = Column("Goals", Integer, primary_key=False)
    mins_played = Column("mins_played", Integer, primary_key=False)
    Fouls = Column("Fouls", Integer, primary_key=False)
    WasFouled = Column("WasFouled", Integer, primary_key=False)
    YellowCard = Column("YellowCard", Integer, primary_key=False)
    RedCard = Column("RedCard", Integer, primary_key=False)
    ErrorLeadToGoal = Column("ErrorLeadToGoal", Integer, primary_key=False)
    ErrorLeadToShot = Column("ErrorLeadToShot", Integer, primary_key=False)
    Saves = Column("Saves", Integer, primary_key=False)
    PenaltySave = Column("PenaltySave", Integer, primary_key=False)
    GoalsConceded = Column("GoalsConceded", Integer, primary_key=False)
    CleanSheet = Column("CleanSheet", Integer, primary_key=False)
    OutfielderBlock = Column("OutfielderBlock", Integer, primary_key=False)
    BlockedCross = Column("BlockedCross", Integer, primary_key=False)
    LastManTackle = Column("LastManTackle", Integer, primary_key=False)
    InterceptionWon = Column("InterceptionWon", Integer, primary_key=False)
    ClearanceOffLine = Column("ClearanceOffLine", Integer, primary_key=False)
    EffectiveClearance = Column("EffectiveClearance", Integer, primary_key=False)
    WonTackle = Column("WonTackle", Integer, primary_key=False)
    LostTackle = Column("LostTackle", Integer, primary_key=False)
    Touches = Column("Touches", Integer, primary_key=False)
    PossWon = Column("PossWon", Integer, primary_key=False)
    PossLostCtrl = Column("PossLostCtrl", Integer, primary_key=False)
    DuelWon = Column("DuelWon", Integer, primary_key=False)
    DuelLost = Column("DuelLost", Integer, primary_key=False)
    AdjustedGoalAssist = Column("AdjustedGoalAssist", Integer, primary_key=False)
    AdjustedTotalAttAssist = Column("AdjustedTotalAttAssist", Integer, primary_key=False)
    AccuratePass = Column("AccuratePass", Integer, primary_key=False)
    AdjustedAccurateFwdZone = Column("AdjustedAccurateFwdZone", Integer, primary_key=False)
    SuccessfulFinalThirdPasses = Column("SuccessfulFinalThirdPasses", Integer, primary_key=False)
    AccurateThroughBall = Column("AccurateThroughBall", Integer, primary_key=False)
    MissedPass = Column("MissedPass", Integer, primary_key=False)
    AccurateLongBalls = Column("AccurateLongBalls", Integer, primary_key=False)
    AccurateCross = Column("AccurateCross", Integer, primary_key=False)
    AssistPenaltyWon = Column("AssistPenaltyWon", Integer, primary_key=False)
    AdjustedGoals = Column("AdjustedGoals", Integer, primary_key=False)
    AdjustedOnTargetScoringAtt = Column("AdjustedOnTargetScoringAtt", Integer, primary_key=False)
    PostScoringAtt = Column("PostScoringAtt", Integer, primary_key=False)
    BlockedScoringAtt = Column("BlockedScoringAtt", Integer, primary_key=False)
    WonContest = Column("WonContest", Integer, primary_key=False)
    LostContest = Column("LostContest", Integer, primary_key=False)
    BigChanceCreated = Column("BigChanceCreated", Integer, primary_key=False)
    BigChanceMissed = Column("BigChanceMissed", Integer, primary_key=False)
    PenaltyKickMissed = Column("PenaltyKickMissed", Integer, primary_key=False)
    DoubleDouble = Column("DoubleDouble", Integer, primary_key=False)
    TripleDouble = Column("TripleDouble", Integer, primary_key=False)
    TripleTriple = Column("TripleTriple", Integer, primary_key=False)
    PossessionBonus = Column("PossessionBonus", Integer, primary_key=False)
    PenaltyConceded = Column("PenaltyConceded", Integer, primary_key=False)
    OwnGoals = Column("OwnGoals", Integer, primary_key=False)
    PenAreaEntries = Column("PenAreaEntries", Integer, primary_key=False)
    PenaltySaves = Column("PenaltySaves", Integer, primary_key=False)
    LongPassToOpposite = Column("LongPassToOpposite", Integer, primary_key=False)
    SavedIbox = Column("SavedIbox", Integer, primary_key=False)
    SavedObox = Column("SavedObox", Integer, primary_key=False)
    GoodHighClaim = Column("GoodHighClaim", Integer, primary_key=False)
    Punches = Column("Punches", Integer, primary_key=False)
    DiveSave = Column("DiveSave", Integer, primary_key=False)
    DiveCatch = Column("DiveCatch", Integer, primary_key=False)
    CrossNotClaimed = Column("CrossNotClaimed", Integer, primary_key=False)
    GkSmother = Column("GkSmother", Integer, primary_key=False)
    AccurateKeeperSweeper = Column("AccurateKeeperSweeper", Integer, primary_key=False)
    AccurateGoalKicks = Column("AccurateGoalKicks", Integer, primary_key=False)
    TeamId = Column("TeamId", Integer, primary_key=False)
    SO5ScoreGK = Column("SO5ScoreGK", String, primary_key=False)
    SO5ScoreMD = Column("SO5ScoreMD", String, primary_key=False)
    SO5ScoreDF = Column("SO5ScoreDF", String, primary_key=False)
    SO5ScoreFW = Column("SO5ScoreFW", String, primary_key=False)
    FormationPlace = Column("FormationPlace", Integer, primary_key=False)
    Level = Column("Level", Integer, primary_key=False)
    Reviewed = Column("Reviewed", Integer, primary_key=False)
    AllAroundScore = Column("AllAroundScore", Integer, primary_key=False)
    OnGameSheet = Column("OnGameSheet", Boolean, primary_key=False)
    Started = Column("Started", Boolean, primary_key=False)
    SubbedOn = Column("SubbedOn", Boolean, primary_key=False)
    SubbedOff = Column("SubbedOff", Boolean, primary_key=False)
    SubReason = Column("SubReason", String, primary_key=False)
    ShirtNumber = Column("ShirtNumber", Integer, primary_key=False)
    FieldPosition = Column("FieldPosition", Integer, primary_key=False)
    LinePosition = Column("LinePosition", Integer, primary_key=False)
    AaGK = Column("AaGK", Integer, primary_key=False)
    AaDF = Column("AaDF", Integer, primary_key=False)
    AaMD = Column("AaMD", Integer, primary_key=False)
    AaFW = Column("AaFW", Integer, primary_key=False)
    LevelGK = Column("LevelGK", Integer, primary_key=False)
    LevelFD = Column("LevelFD", Integer, primary_key=False)