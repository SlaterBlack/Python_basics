#converts given time in hours, minutes and seconds into seconds
def time_to_seconds (hour, minute,seconds): 
    out=((hour*3600)+(minute*60)+(seconds))
    return out

