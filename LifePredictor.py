import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout,
    QMessageBox, QProgressBar, QComboBox, QFormLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
import matplotlib.pyplot as plt


class LifeDashboard(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Life Expectancy Dashboard")
        self.setGeometry(200, 200, 500, 600)

        # Set up the main window's look
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f4f7;
                font-family: Arial, sans-serif;
            }
            QLabel {
                font-size: 14px;
                color: #333;
            }
            QLineEdit, QComboBox, QTextEdit {
                font-size: 14px;
                padding: 10px;
                border-radius: 5px;
                background-color: #fff;
                border: 1px solid #ccc;
            }
            QPushButton {
                font-size: 14px;
                background-color: #5cb85c;
                color: white;
                padding: 10px;
                border-radius: 5px;
                border: none;
            }
            QPushButton:hover {
                background-color: #4cae4c;
            }
            QTextEdit {
                font-size: 14px;
                background-color: #f9f9f9;
                border: 1px solid #ddd;
            }
            QProgressBar {
                height: 20px;
                border-radius: 10px;
                background-color: #eee;
            }
            QProgressBar::chunk {
                background-color: #5cb85c;
                border-radius: 10px;
            }
        """)

        # Input fields
        self.label_name = QLabel("👤 Name:")
        self.input_name = QLineEdit()

        self.label_age = QLabel("🎂 Current Age:")
        self.input_age = QLineEdit()

        self.label_lifespan = QLabel("📅 Expected Lifespan (years):")
        self.input_lifespan = QLineEdit()

        self.label_health = QLabel("💪 Health Status (e.g., smoker, non-smoker):")
        self.input_health = QLineEdit()

        self.label_gender = QLabel("👩‍🦳 Gender:")
        self.input_gender = QComboBox()
        self.input_gender.addItems(["Male", "Female", "Other"])

        self.label_location = QLabel("🌍 Location (e.g., Country):")
        self.input_location = QLineEdit()

        # Buttons
        self.button_calc = QPushButton("Calculate")
        self.button_calc.clicked.connect(self.calculate_life)

        self.button_clear = QPushButton("Clear")
        self.button_clear.clicked.connect(self.clear_fields)

        # Output
        self.text_output = QTextEdit()
        self.text_output.setReadOnly(True)

        # Progress bar
        self.progress = QProgressBar()
        self.progress.setMinimum(0)
        self.progress.setMaximum(100)

        # Motivational tips
        self.motivational_tips = [
           "💡 Tip: Focus on meaningful experiences, not just time.",
           "💡 Tip: Embrace challenges, they fuel growth.",
           "💡 Tip: Celebrate small victories, they build momentum.",
           "💡 Tip: Learn from mistakes, don't dwell on them.",
           "💡 Tip: Prioritize self-care, it's essential for resilience.",
           "💡 Tip: Cultivate gratitude, it shifts perspective.",
           "💡 Tip: Seek inspiration, it ignites creativity.",
           "💡 Tip: Take consistent action, it leads to progress.",
           "💡 Tip: Trust your intuition, it guides decisions.",
           "💡 Tip: Practice mindfulness, it grounds your present.",
           "💡 Tip: Set clear intentions, they define purpose.",
           "💡 Tip: Maintain a positive outlook, it attracts good.",
           "💡 Tip: Connect with others, it fosters belonging.",
           "💡 Tip: Step out of your comfort zone, it expands horizons.",
           "💡 Tip: Be persistent, success often comes after struggle.",
           "💡 Tip: Simplify your life, it reduces stress.",
           "💡 Tip: Forgive yourself and others, it frees your spirit.",
           "💡 Tip: Dream big, then work even bigger.",
           "💡 Tip: Stay curious, it opens new doors.",
           "💡 Tip: Give back, it enriches your soul.",
           "💡 Tip: Own your journey, it's uniquely yours.",
           "💡 Tip: Release what no longer serves you.",
           "💡 Tip: Find joy in the ordinary.",
           "💡 Tip: Believe in your potential, it's limitless.",
           "💡 Tip: Adapt to change, it's constant.",
           "💡 Tip: Listen actively, it strengthens understanding.",
           "💡 Tip: Be authentic, it builds trust.",
           "💡 Tip: Take breaks, they refresh your mind.",
           "💡 Tip: Challenge your assumptions, they might be wrong.",
           "💡 Tip: Inspire others through your actions.",
           "💡 Tip: Practice patience, good things take time.",
           "💡 Tip: Protect your energy, it's valuable.",
           "💡 Tip: Seek knowledge, it empowers you.",
           "💡 Tip: Be kind to yourself, always.",
           "💡 Tip: Confront fears, they hold you back.",
           "💡 Tip: Express creativity, it's a part of you.",
           "💡 Tip: Finish what you start, it builds discipline.",
           "💡 Tip: Let go of perfectionism, it's an illusion.",
           "💡 Tip: Find your purpose, it guides your path.",
           "💡 Tip: Embrace imperfection, it's human.",
           "💡 Tip: Act with integrity, it builds character.",
           "💡 Tip: Keep learning, life is a classroom.",
           "💡 Tip: Help others rise, it elevates everyone.",
           "💡 Tip: Stay humble, there's always more to learn.",
           "💡 Tip: Be decisive, inaction is also a choice.",
           "💡 Tip: Practice gratitude daily, it transforms your perspective.",
           "💡 Tip: Trust the process, even when it's tough.",
           "💡 Tip: Guard your peace, it's precious.",
           "💡 Tip: Create your own opportunities.",
           "💡 Tip: Live in the present moment, it's all you have.",
        ]

        # Layout
        layout = QFormLayout()
        layout.addRow(self.label_name, self.input_name)
        layout.addRow(self.label_age, self.input_age)
        layout.addRow(self.label_lifespan, self.input_lifespan)
        layout.addRow(self.label_health, self.input_health)
        layout.addRow(self.label_gender, self.input_gender)
        layout.addRow(self.label_location, self.input_location)
        layout.addRow(self.button_calc)
        layout.addRow(self.button_clear)
        layout.addRow(self.text_output)
        layout.addRow(self.progress)

        self.setLayout(layout)

        # Setup validators
        self.setup_validators()

    def setup_validators(self):
        self.input_age.setValidator(QIntValidator(0, 120))   # Age range
        self.input_lifespan.setValidator(QIntValidator(1, 150))  # Lifespan range

    def calculate_life(self):
        try:
            name = self.input_name.text()
            age = int(self.input_age.text())
            expected_lifespan = int(self.input_lifespan.text())  # keep original
            health_status = self.input_health.text().strip().lower()
            gender = self.input_gender.currentText()
            location = self.input_location.text().strip().lower()

            if age < 0 or age >= expected_lifespan:
                QMessageBox.warning(self, "Invalid Input", "⚠️ Age must be between 0 and expected lifespan.")
                return

            # Adjusted lifespan calculation
            adjusted_lifespan = expected_lifespan

            # Correct health checks
            if health_status in ["smoker"]:
                adjusted_lifespan -= 5
            elif health_status in ["non-smoker", "non smoker", "nonsmoker"]:
                pass  # no penalty

            # Gender adjustments
            if gender.lower() == "female":
                adjusted_lifespan += 5

            # Location adjustments
            if "usa" in location:
                adjusted_lifespan -= 3

            # Remaining time (based on adjusted lifespan)
            years_left = adjusted_lifespan - age
            months_left = years_left * 12
            weeks_left = years_left * 52
            days_left = years_left * 365
            percent_lived = (age / adjusted_lifespan) * 100

            # Update Progress Bar
            self.progress.setValue(int(percent_lived))

            # Select a random motivational tip
            random_tip = random.choice(self.motivational_tips)

            result = (
                f"📊 LIFE EXPECTANCY DASHBOARD\n"
                f"---------------------------------\n"
                f"👤 Name: {name}\n"
                f"🎂 Age: {age}\n"
                f"📅 Entered Lifespan : {expected_lifespan} years\n"
                f"📅 Adjusted Lifespan: {adjusted_lifespan} years\n\n"
                f"⏳ Years Remaining : {years_left}\n"
                f"🗓️ Months Remaining: {months_left}\n"
                f"📆 Weeks Remaining : {weeks_left}\n"
                f"📅 Days Remaining  : {days_left}\n\n"
                f"📈 Life Completed  : {percent_lived:.2f}%\n"
                f"---------------------------------\n"
                f"{random_tip}" # Display only one random tip
            )

            self.text_output.setText(result)

            # Show pie chart
            self.plot_lifetime(years_left, age, adjusted_lifespan)

        except ValueError:
            QMessageBox.critical(self, "Error", "❌ Please enter valid numbers for age and lifespan.")

    def plot_lifetime(self, years_left, age, adjusted_lifespan):
        labels = ['Lifetime Spent', 'Lifetime Remaining']
        sizes = [age, years_left]
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')
        plt.show()

    def clear_fields(self):
        self.input_name.clear()
        self.input_age.clear()
        self.input_lifespan.clear()
        self.input_health.clear()
        self.input_location.clear()
        self.text_output.clear()
        self.progress.setValue(0)


# Run the app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LifeDashboard()
    window.show()
    sys.exit(app.exec_())