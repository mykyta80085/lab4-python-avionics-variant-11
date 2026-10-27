"""
Лабораторна робота: Варіант 11
Студент: [Возний Микита]
Група: [2]
"""

# Задача 1: Витрата палива для зведення з орбіти (if/elif/else)
def deorbit_maneuver(fuel_mass: float) -> str:
    """
    - fuel_mass >= 15 -> "Повний гальмівний імпульс"
    - 5 <= fuel_mass < 15 -> "Частковий імпульс"
    - fuel_mass < 5 -> "Пасивний аеродинамічний парус"
    """
    ...

# Задача 2: Статус крокових двигунів (match-case з вартою)
def check_stepper_motor(motor_data: tuple) -> str:
    """
    Приймає (motor_id, position_deg, error_flag).
    - error_flag == True (через guard if) -> "Помилка двигуна {id}"
    - error_flag == False -> "Двигун {id} у нормі (позиція {pos}°)"
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
