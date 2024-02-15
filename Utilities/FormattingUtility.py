def format_scheduling_message(duty_staff):

    week_commencing = duty_staff["Week commencing"]
    duty_staff_1 = duty_staff["1st"]
    duty_staff_2 = duty_staff["2nd"]
    
    message = f":grafana2: *Grafana Monitoring for W/C {week_commencing}*\n\n"
    message += f"*1st monitor:* {duty_staff_1}\n\n"
    message += f"*2nd monitor*: {duty_staff_2}\n\n\n"

    message += "Grafana Monitoring schedule can be found here... https://confluence.sage.com/display/SBA/Grafana+monitoring+schedule"
    message += "\n\n"
    message += "Grafana Monitoring template can be found here... https://confluence.sage.com/display/SBA/Grafana+monitoring+Template"
    message += "\n\n"
    message += "on-going issues can be found here... https://confluence.sage.com/display/SBA/Ongoing+issues"
    message += "\n\n"
    
    return message