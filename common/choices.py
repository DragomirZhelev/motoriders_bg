from django.db import models

class MotorcycleTypeChoices(models.TextChoices):
    ADVENTURE = 'Adventure', 'Adventure'
    NAKED = 'Naked', 'Naked'
    TOURING = 'Touring', 'Touring'
    SPORT = 'Sport', 'Sport'
    ENDURO = 'Enduro', 'Enduro'
    CRUISER = 'Cruiser', 'Cruiser'
    CHOPPER = 'Chopper', 'Chopper'
    SCOOTER = 'Scooter', 'Scooter'
    OTHER = 'Other', 'Other'

class RoadDifficultyChoices(models.TextChoices):
    BEGINNER = 'Beginner', 'Beginner'
    INTERMEDIATE = 'Intermediate', 'Intermediate'
    ADVANCED = 'Advanced', 'Advanced'


class TripStatusChoices(models.TextChoices):
    PLANNED = 'Planned', 'Planned'
    COMPLETED = 'Completed', 'Completed'
    CANCELED = 'Canceled', 'Canceled'

class UrgencyChoices(models.TextChoices):
    LOW = 'Low', 'Low'
    MEDIUM = 'Medium', 'Medium'
    HIGH = 'High', 'High'
    CRITICAL = 'Critical', 'Critical'


class HelpRequestStatusChoices(models.TextChoices):
    OPEN = 'Open', 'Open'
    CLOSED = 'Closed', 'Closed'


class BulgarianCityChoices(models.TextChoices):
    SOFIA = 'Sofia', 'Sofia'
    PLOVDIV = 'Plovdiv', 'Plovdiv'
    VARNA = 'Varna', 'Varna'
    BURGAS = 'Burgas', 'Burgas'
    RUSE = 'Ruse', 'Ruse'
    STARA_ZAGORA = 'Stara Zagora', 'Stara Zagora'
    PLEVEN = 'Pleven', 'Pleven'
    SLIVEN = 'Sliven', 'Sliven'
    DOBRICH = 'Dobrich', 'Dobrich'
    SHUMEN = 'Shumen', 'Shumen'
    BLAGOEVGRAD = 'Blagoevgrad', 'Blagoevgrad'
    VELIKO_TARNOVO = 'Veliko Tarnovo', 'Veliko Tarnovo'
    HASKOVO = 'Haskovo', 'Haskovo'
    KARDZHALI = 'Kardzhali', 'Kardzhali'
    SMOLYAN = 'Smolyan', 'Smolyan'
    VRATSA = 'Vratsa', 'Vratsa'
    MONTANA = 'Montana', 'Montana'
    VIDIN = 'Vidin', 'Vidin'
    OTHER = 'Other', 'Other'