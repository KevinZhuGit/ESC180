def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it'''

    global cur_hedons, cur_health

    global cur_time
    global last_activity, last_activity_duration

    global last_finished
    global bored_with_stars

    global cur_star, cur_star_activity, star_times

    global is_tired

    cur_hedons = 0
    cur_health = 0

    cur_star = None
    cur_star_activity = None
    star_times = []
    bored_with_stars = False

    last_activity = None
    last_activity_duration = 0

    is_tired = False

    cur_time = 0

    last_finished = -1000


def perform_activity(activity, duration):
    global cur_health, cur_hedons, cur_star, is_tired, last_activity, last_activity_duration

    check_tired()
    update(activity, duration)

    cur_health += estimate_health_delta(activity, duration)
    cur_hedons += estimate_hedons_delta(activity, duration)

    cur_star = None

    if activity != last_activity:
        last_activity = activity
        last_activity_duration = duration


def star_can_be_taken(activity):
    global cur_star, cur_star_activity

    if (activity == cur_star_activity) and not bored_with_stars and cur_star:
        return True
    else:
        return False


def offer_star(activity):
    global cur_star, cur_star_activity

    cur_star = True
    cur_star_activity = activity

    check_star_time()


def get_cur_hedons():
    return cur_hedons


def get_cur_health():
    return cur_health


def check_star_time():
    global bored_with_stars

    if len(star_times) == 3:
        star_times.pop(0)
        star_times.append(cur_time)
        if (star_times[2] - star_times[0]) < 120:
            bored_with_stars = True
    elif len(star_times) == 2:
        star_times.append(cur_time)
        if (star_times[2] - star_times[0]) < 120:
            bored_with_stars = True
    else:
        star_times.append(cur_time)


def update(activity, duration):
    global last_activity, last_activity_duration, cur_time

    if activity == last_activity:
        last_activity_duration += duration

    cur_time += duration


def check_tired():
    global is_tired, last_activity, last_activity_duration

    if last_activity == "resting" and last_activity_duration >= 120:
        is_tired = False
    elif last_activity == None:
        is_tired = False  # can also just pass
    else:
        is_tired = True


def most_fun_activity_minute():
    global is_tired, cur_star, cur_star_activity, bored_with_stars

    check_tired()

    if cur_star and not bored_with_stars:
        return cur_star_activity
    else:
        if is_tired:
            return "resting"
        else:
            return "running"

################################################################################
# These functions are not required, but we recommend that you use them anyway
# as helper functions


def estimate_hedons_delta(activity, duration):
    '''Return the amount of hedons the user would get for performing activity
    activity for duration minutes'''
    global is_tired

    if star_can_be_taken(activity) and is_tired:
        if duration <= 10:
            return duration
        else:
            return 30 - 2 * duration
    elif star_can_be_taken(activity):
        if activity == "running":
            if duration <= 10:
                return 5 * duration
            else:
                return 70 - 2 * duration
        elif activity == "textbooks":
            if duration <= 10:
                return 4 * duration
            elif duration <= 20:
                return 30 + duration
            else:
                return 70 - duration
    elif not is_tired:
        if activity == "running":
            if duration <= 10:
                return 2 * duration
            else:
                return 40 - 2 * duration
        elif activity == "textbooks":
            if duration <= 20:
                return duration  # *4
            else:
                return 40 - duration  # 20 - (duration - 20)
        else:
            return 0
    else:
        if activity != "resting":
            return - 2 * duration
        else:
            return 0


def estimate_health_delta(activity, duration):
    global last_activity, last_activity_duration

    if activity == "running":
        if activity == last_activity:
            remaining_time = 180 - last_activity_duration + duration
            if remaining_time < 0:
                return duration
            elif duration > remaining_time:
                return 2 * remaining_time + duration
            else:  # when duration < remaining time
                return 3 * duration
        elif duration <= 180:
            return 3 * duration
        else:
            return 360 + duration
    elif activity == "textbooks":
        return 2 * duration
    else:
        return 0

################################################################################


if __name__ == '__main__':
    initialize()

    perform_activity("textbooks", 130)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    perform_activity("textbooks", 70)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 140)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("running")
    perform_activity("textbooks", 20)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    perform_activity("resting", 20)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    perform_activity("resting", 130)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 140)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 80)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 80)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 80)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("running")
    perform_activity("running", 10)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    print(most_fun_activity_minute())
    perform_activity("resting", 30)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 20)
    print(get_cur_health())
    print(get_cur_hedons())

    '''
    perform_activity("running", 30)
    # -20 = 10 * 2 + 20 * (-2)             # Test 1
    print(get_cur_hedons())
    # 90 = 30 * 3                          # Test 2
    print(get_cur_health())
    # resting                              # Test 3
    print(most_fun_activity_minute())
    perform_activity("resting", 30)
    offer_star("running")
    # running                              # Test 4
    print(most_fun_activity_minute())
    perform_activity("textbooks", 30)
    # 150 = 90 + 30*2                      # Test 5
    print(get_cur_health())
    # -80 = -20 + 30 * (-2)                # Test 6
    print(get_cur_hedons())
    offer_star("running")
    perform_activity("running", 20)
    # 210 = 150 + 20 * 3                   # Test 7
    print(get_cur_health())
    # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
    print(get_cur_hedons())
    perform_activity("running", 170)
    # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    print(get_cur_health())
    # -430 = -90 + 170 * (-2)              # Test 10
    print(get_cur_hedons())
    '''
