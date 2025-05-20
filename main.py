import sys
from PyQt6.QtWidgets import (
    QApplication, QLabel, QWidget, QVBoxLayout, QPushButton
)

class ClickerGame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("KDE Clicker Game")
        self.setFixedSize(400, 300)

        # Game state
        self.click_count = 0
        self.click_power = 1
        self.upgrade_level = 1
        self.upgrade_cost = 10

        # Layout
        self.layout = QVBoxLayout()

        # Labels
        self.click_label = QLabel(f"Click Count: {self.click_count}")
        self.power_label = QLabel(f"Click Power: {self.click_power}")
        self.upgrade_label = QLabel(f"Upgrade Level: {self.upgrade_level}")
        self.cost_label = QLabel(f"Upgrade Cost: {self.upgrade_cost}")

        # Buttons
        self.click_button = QPushButton("Click Me!")
        self.click_button.clicked.connect(self.handle_click)

        self.upgrade_button = QPushButton("Upgrade Click Power")
        self.upgrade_button.clicked.connect(self.buy_upgrade)

        # Add widgets to layout
        self.layout.addWidget(self.click_label)
        self.layout.addWidget(self.power_label)
        self.layout.addWidget(self.upgrade_label)
        self.layout.addWidget(self.cost_label)
        self.layout.addWidget(self.click_button)
        self.layout.addWidget(self.upgrade_button)

        self.setLayout(self.layout)

    def handle_click(self):
        self.click_count += self.click_power
        self.update_ui()

    def buy_upgrade(self):
        if self.click_count >= self.upgrade_cost:
            self.click_count -= self.upgrade_cost
            self.upgrade_level += 1
            self.click_power += 1
            # Increase cost exponentially
            self.upgrade_cost = int(self.upgrade_cost * 1.5)
            self.update_ui()

    def update_ui(self):
        self.click_label.setText(f"Click Count: {self.click_count}")
        self.power_label.setText(f"Click Power: {self.click_power}")
        self.upgrade_label.setText(f"Upgrade Level: {self.upgrade_level}")
        self.cost_label.setText(f"Upgrade Cost: {self.upgrade_cost}")

app = QApplication(sys.argv)
window = ClickerGame()
window.show()
sys.exit(app.exec())
