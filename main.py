from sudoku import Sudoku
import sys
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QApplication, QHeaderView, QTableWidget
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QColor, QBrush
from mainpage import Ui_Sudoku as MP
import random

'''
puzzle.show()
solution = puzzle.solve()
solution.show()
matrix = solution.board
for puzzle in matrix:
    print(puzzle)'''

# Создает Судоку, создание списка, замена None на пустое значение
def generation_numbers():
    global solution_board, game_finished

    game_finished = False
    redact_cells = []

    # Создание таблицы с None
    sudoku_table = Sudoku(3, seed=random.randint(1, 100000)).difficulty(0.5)
    raw_data = sudoku_table.board

    # исходный пазл
    print(" Пазл ")
    sudoku_table.show()

    # решение
    solved = sudoku_table.solve()
    print("\n Решение")
    solved.show()

    solution_board = [row[:] for row in solved.board]

    # None заменяется на пустое значение
    for row in range(len(raw_data)):
        for column in range(len(raw_data[row])):
            if raw_data[row][column] is None:
                redact_cells.append((row, column))
                raw_data[row][column] = ""
    fill_table(raw_data)

def fill_table(raw_data):
    # Установка строк и колонок в таблице
    mui.table_number.setColumnCount(len(raw_data))
    mui.table_number.setRowCount(len(raw_data))

    # Прячет боковые загаловки
    mui.table_number.horizontalHeader().hide()
    mui.table_number.verticalHeader().hide()

    # Установка ячеек длины таблицы
    mui.table_number.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    mui.table_number.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    # запрещает редактировать таблицу
    mui.table_number.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

    # Заполнение ячеек
    for row, row_data in enumerate(raw_data):
        for column, value in enumerate(row_data):
            str_value = QTableWidgetItem(str(value))
            str_value.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            mui.table_number.setItem(row, column, str_value)

# заполнение ячеек с помощью кнопок
def insert_numbers(digit):
    if game_finished:
        return

    row = mui.table_number.currentRow()
    col = mui.table_number.currentColumn()

    if row == -1 or col == -1:
        return

    if (row, col) not in redact_cells:
        return

    selected = mui.table_number.item(row, col)

    if selected is None:
        selected = QTableWidgetItem(digit)
        selected.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        mui.table_number.setItem(row, col, selected)
    else:
         selected.setText(digit)

    ans_check(row, col, digit)

    # снимает выделение с ячейки
    mui.table_number.clearSelection()
    mui.table_number.setCurrentCell(row, col)
    mui.table_number.setCurrentItem(None)

    win_game()

def clear_cell():
    if game_finished:
        return

    row = mui.table_number.currentRow()
    col = mui.table_number.currentColumn()

    if row == -1 or col == -1:
        return

    if (row, col) not in redact_cells:
        return

    selected = mui.table_number.item(row, col)

    if selected is not None:
        selected.setText("")

    reset_cell_color(row, col)

# проверка правильности ответа
def ans_check(row, col, selected):

    item = mui.table_number.item(row, col)
    if item is None:
        return

    user_value = int(item.text())
    correct_value = solution_board[row][col]

    # красит фон в зеленый и красный на время
    if user_value == correct_value:
        item.setBackground(QBrush(QColor("#c8e6c9")))
        item.setForeground(QBrush(QColor("#1b5e20")))
    else:
        item.setBackground(QBrush(QColor("#ffcdd2")))
        item.setForeground(QBrush(QColor("#b71c1c")))

    key = (row, col)

    timer = QTimer()
    timer.setSingleShot(True)
    timer.timeout.connect(lambda r=row, c=col: reset_cell_color(r, c))
    flash_timers[key] = timer
    timer.start(2000)

def reset_cell_color(row, col):
    item = mui.table_number.item(row, col)
    if item is not None:
        item.setBackground(QBrush(QColor("white")))
        item.setForeground(QBrush(QColor("black")))

    flash_timers.pop((row, col), None)

def win_game():
    global game_finished

    rows = mui.table_number.rowCount()
    cols = mui.table_number.columnCount()

    for row in range(rows):
            for col in range(cols):
                item = mui.table_number.item(row, col)

                if item is None or item.text() == "":
                    return False

                user_value = int(item.text())
                if user_value != solution_board[row] [col]:
                    return False
    game_finished = True

    for row in range(rows):
        for col in range(cols):
            item = mui.table_number.item(row, col)
            item.setBackground(QBrush(QColor("#c8e6c9")))
            item.setForeground(QBrush(QColor("#1b5e20")))

    for t in flash_timers.values():
        t.stop()
    flash_timers.clear()

    return True

# Запуск приложения по __main__, выдача окна Судоку
if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = QMainWindow()
    mui = MP()
    mui.setupUi(main_window)

    game_finished = False

    solution_board = []
    flash_timers = {}

    redact_cells = []

    number_buttons = [
        (mui.btn1, "1"),
        (mui.btn2, "2"),
        (mui.btn3, "3"),
        (mui.btn4, "4"),
        (mui.btn5, "5"),
        (mui.btn6, "6"),
        (mui.btn7, "7"),
        (mui.btn8, "8"),
        (mui.btn9, "9"),
    ]

    for button, digit in number_buttons:
        button.clicked.connect(lambda checked=False, d=digit: insert_numbers(d))

    mui.btn_delete.clicked.connect(clear_cell)

    main_window.setStyleSheet("""
            QMainWindow {
                background-color: #f0f4f8;
            }
            QLabel {
                color: white;
            }
            QPushButton {
                background-color: white;
                color: black;
                border-radius: 6px;
                padding: 8px 16px;
                font-weight: bold;
            }
            QTableWidget {
                background-color: white;
                color: black;
                font-size: 18px;
                font-weight: bold;
                gridline-color: #cbd5e0;
                border: 1px solid #cbd5e0;
            }
        """)

    generation_numbers()

    mui.btn_new.clicked.connect(generation_numbers)

    main_window.show()
    sys.exit(app.exec())
