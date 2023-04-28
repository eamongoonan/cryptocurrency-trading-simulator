from .models import Position


def get_user_all_time_pnl(user):
    user_closed_positions = Position.objects.filter(user=user, closed_at__isnull=False)
    all_time_pnl = 0
    for position in user_closed_positions:
        all_time_pnl += position.PNL

    return all_time_pnl


def get_user_all_time_roi(user):
    user_closed_positions = Position.objects.filter(user=user, closed_at__isnull=False)
    # COI = Cost of Investment
    all_time_coi = 0
    for position in user_closed_positions:
        all_time_coi += position.USD_value_of_purchase
    all_time_roi = user.PNL / all_time_coi * 100

    return all_time_roi
