from django.db import models


class BranchChoices(models.TextChoices):
    ASMB_MU = 'АСМБ МУ', 'АСМБ МУ'
    ASMB_SU = 'АСМБ СУ', 'АСМБ СУ'
    ASMB_VARNA = 'АСМБ Варна', 'АСМБ Варна'
    ASMB_PLOVDIV = 'АСМБ Пловдив', 'АСМБ Пловдив'
    ASMB_BURGAS = 'АСМБ Бургас', 'АСМБ Бургас'
    ASMB_PLEVEN = 'АСМБ Плевен', 'АСМБ Плевен'
    ASMB_STARA_ZAGORA = 'АСМБ Стара Загора', 'АСМБ Стара Загора'
