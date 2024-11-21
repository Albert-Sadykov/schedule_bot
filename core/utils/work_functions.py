from datetime import datetime, timedelta

def is_even_week():
    year = datetime.now().year
    start_date = datetime(year, 9, 1)
    
    current_date = datetime.now()
    
    delta_days = (current_date - start_date).days
    
    week_number = (delta_days // 7) + 1
    
    return week_number % 2 == 0

def show_schedule(day, desk):
    text = f"{day} \n"

    for i in range(len(desk)):
        desk_item = desk[i]
        text += f''' \n{desk_item[0]}) Время: {desk_item[1]}
        Предмет: {desk_item[2]}
        Преподаватель: {desk_item[3]}
        Аудитория: {desk_item[4]}
                    '''
    
    return text
