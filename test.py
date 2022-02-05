from src import catnevercodes


@catnevercodes.timer
def run():
    return {"name": "猫叔", "Love": ["Cat", "Coffe", "Code"]}

catnevercodes.send_dingtalk(run(), atAll=True)