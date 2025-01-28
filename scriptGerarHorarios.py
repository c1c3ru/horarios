import datetime
import random
import calendar


def get_month_days(month, year):
    _, days_in_month = calendar.monthrange(year, month)
    days = []
    for day in range(1, days_in_month + 1):
        days.append({
            'day': day,
            'weekDay': calendar.weekday(year, month, day)  # 0 = Segunda-feira, 6 = Domingo
        })
    return days


def calculate_easter(year):
    """Calcula a data da Páscoa para um ano específico usando o algoritmo de Meeus."""
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1
    return datetime.date(year, month, day)


def calculate_movable_holidays(year):
    """Calcula os feriados móveis (Carnaval, Sexta-feira Santa, e Corpus Christi)."""
    easter = calculate_easter(year)
    carnival = easter - datetime.timedelta(days=47)  # Carnaval: 47 dias antes da Páscoa
    good_friday = easter - datetime.timedelta(days=2)  # Sexta-feira Santa: 2 dias antes da Páscoa
    corpus_christi = easter + datetime.timedelta(days=60)  # Corpus Christi: 60 dias após a Páscoa
    return {
        "Carnaval": carnival,
        "Sexta-feira Santa": good_friday,
        "Corpus Christi": corpus_christi
    }


def generate_random_time(start_hour, start_minute, init_lunch, end_minute):
    if start_hour == init_lunch and start_minute == end_minute:
        return f"{start_hour:02d}:{start_minute:02d}"

    start_total_minutes = start_hour * 60 + start_minute
    end_total_minutes = init_lunch * 60 + end_minute

    random_total_minutes = random.randint(start_total_minutes, end_total_minutes)

    random_hour = random_total_minutes // 60
    random_minute = random_total_minutes % 60

    return f"{random_hour:02d}:{random_minute:02d}"


# Perguntar ao usuário o mês e o ano
year = int(input("De qual ano você precisa gerar? (Digite o ano, ex.: 2025): "))
month = int(input("De qual mês você precisa gerar? (Digite de 1 a 12): "))

# Obter os dias do mês e ano selecionados
calendar_days = get_month_days(month, year)

# Calcular os feriados móveis para o ano selecionado
movable_holidays = calculate_movable_holidays(year)

# Lista de feriados fixos no formato "dd/mm"
fixed_holidays = ["01/01", "21/04", "01/05", "07/09", "12/10", "02/11", "15/11", "25/12"]
movable_holidays_dates = [date.strftime("%d/%m") for date in movable_holidays.values()]
all_holidays = fixed_holidays + movable_holidays_dates

# Dados básicos
servidor = "Cícero José Sousa da Silva"
matricula = "2231232"
cargo = "Tec de TI"
funcao = "N/C"
lotacao = "Campus Marcanaú"
jornada = "40 horas"
horario = "08:00 - 12:00 / 13:00 - 17:00"

html_table = f"""
<table border="1" style="margin:auto;width:700px;font-family:Arial, Helvetica, sans-serif;border:2px solid black;font-size:0.9em;line-height:1.2em;border-collapse:collapse;margin-bottom:1em;white-space:nowrap">
  <tbody style="text-align:left">
    <tr style="background-color:rgb(221, 221, 221);text-align:center">
      <td colspan="4" style="padding:0.2em"><strong>DADOS BÁSICOS</strong></td>
    </tr>
    <tr>
      <td style="border:none;width:0;padding-left:0.5em;padding-bottom:0.2em"><strong>SERVIDOR:</strong></td>
      <td style="border:none">{servidor}</td>
      <td style="border:none;width:0"><strong>MATRÍCULA:</strong></td>
      <td style="border:none">{matricula}</td>
    </tr>
    <tr>
      <td style="border:none;padding-left:0.5em;padding-bottom:0.2em"><strong>CARGO:</strong></td>
      <td style="border:none">{cargo}</td>
      <td style="border:none"><strong>FUNÇÃO:</strong></td>
      <td style="border:none">{funcao}</td>
    </tr>
    <tr>
      <td style="border:none;padding-left:0.5em;padding-bottom:0.2em"><strong>LOTAÇÃO:</strong></td>
      <td style="border:none">{lotacao}</td>
      <td style="border:none"><strong>JORNADA:</strong></td>
      <td style="border:none">{jornada}</td>
    </tr>
    <tr>
      <td style="border:none;padding-left:0.5em;padding-bottom:0.2em"><strong>SETOR:</strong></td>
      <td style="border:none">{horario}</td>
    </tr>
  </tbody>
</table>

<table border="1" style="margin:auto;width:700px;font-family:Arial, Helvetica, sans-serif;border:2px solid black;border-collapse:collapse">
  <thead>
    <tr style="background-color:rgb(221, 221, 221);text-align:center;font-weight:bold">
      <td colspan="2" style="padding:0.2em">1º TURNO</td>
      <td rowspan="2" style="padding:0.2em">DIA</td>
      <td colspan="2" style="padding:0.2em">2º TURNO</td>
    </tr>
    <tr style="background-color:rgb(231, 231, 231);text-align:center;font-weight:bold">
      <td style="padding:0.2em">ENTRADA</td>
      <td style="padding:0.2em">SAÍDA</td>
      <td style="padding:0.2em">ENTRADA</td>
      <td style="padding:0.2em">SAÍDA</td>
    </tr>
  </thead>
  <tbody style="text-align:center">
"""

for day in calendar_days:
    day_of_month = day['day']
    week_day_index = day['weekDay']
    week_day_name = calendar.day_name[week_day_index]

    week_day_ptbr = {
        "Monday": "Segunda",
        "Tuesday": "Terça",
        "Wednesday": "Quarta",
        "Thursday": "Quinta",
        "Friday": "Sexta",
        "Saturday": "Sábado",
        "Sunday": "Domingo",
    }[week_day_name]

    formatted_date = f"{day_of_month:02d}/{month:02d}"

    init_hour = ""
    init_lunch = ""
    end_lunch = ""
    end_hour = ""

    if week_day_name == "Saturday" or week_day_name == "Sunday":
        init_hour = f"<strong>{week_day_ptbr}</strong>"
        init_lunch = f"<strong>{week_day_ptbr}</strong>"
        end_lunch = f"<strong>{week_day_ptbr}</strong>"
        end_hour = f"<strong>{week_day_ptbr}</strong>"
    elif formatted_date in all_holidays:
        init_hour = "<strong>Feriado</strong>"
        init_lunch = "<strong>Feriado</strong>"
        end_lunch = "<strong>Feriado</strong>"
        end_hour = "<strong>Feriado</strong>"
    else:
        init_hour = generate_random_time(7, 55, 8, 5)  # Gerar horário aleatório para o 1º turno
        init_lunch = generate_random_time(11, 55, 12, 5)  # Gerar horário aleatório para o 1º turno
        end_lunch = generate_random_time(12, 55, 13, 5)  # Gerar horário aleatório para o 2º turno
        end_hour = generate_random_time(16, 55, 17, 5)  # Gerar horário aleatório para o 2º turno

    html_table += f"""
    <tr>
      <td>{init_hour}</td>
      <td>{init_lunch}</td>
      <td>{formatted_date}</td>
      <td>{end_lunch}</td>
      <td>{end_hour}</td>
    </tr>
    """

html_table += """
  </tbody>
</table>
"""

print(html_table)
