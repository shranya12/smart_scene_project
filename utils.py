import time

def calculate_fps(prev_time):
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    return fps, current_time
