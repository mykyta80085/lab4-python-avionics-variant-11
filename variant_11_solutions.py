"""
Лабораторна робота: Варіант 11
Студент: [Возний Микита]
Група: [2]
"""

# Задача 1: Витрата палива для зведення з орбіти (if/elif/else)
def deorbit_maneuver(fuel_mass: float) -> str:
    if fuel_mass >= 15:
        return("Повний гальмівний імпульс")
    elif 5 <= fuel_mass < 15:
        return("Частковий імпульс")
    else:
        return("Пасивний аеродинамічний парус")
    """
    - fuel_mass >= 15 -> "Повний гальмівний імпульс"
    - 5 <= fuel_mass < 15 -> "Частковий імпульс"
    - fuel_mass < 5 -> "Пасивний аеродинамічний парус"
    """
    ...

# Задача 2: Статус крокових двигунів (match-case з вартою)
def check_stepper_motor(motor_data: tuple) -> str:
    match motor_data:
        case id, pos, flag if flag == True:
            return(f"Помилка двигуна {id}")
        case id, pos, flag if flag == False:
            return(f"Двигун {id} y нормі (позиція {pos}°)")
        case other:
            return("невідомий error flag")
    """
    Приймає (motor_id, position_deg, error_flag).
    - error_flag == True (через guard if) -> "Помилка двигуна {id}"
    - error_flag == False -> "Двигун {id} y нормі (позиція {pos}°)"
    """
    ...

# Задача 3: Очищення черги пакетів (while / continue)
def clean_packet_queue(queue: list) -> list:
    """
    У циклі while вилучає пакети з queue. Якщо пакет None або len < 4 -> пропустіть через continue.
    Поверніть список збережених валідних пакетів.
    """
    ...

# Задача 4: Ітерація рядків логу (enumerate)
def parse_log_lines(lines: list) -> list:
    """
    За допомогою enumerate формує список рядків вигляду "{індекс}: {текст_без_переносу}".
    """
    ...
