from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from lib.libbol import *
from widgets.tree_view import BolHeader

class MoreButtons(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.vbox = QVBoxLayout(self)
        self.vbox.setContentsMargins(0, 0, 0, 0)

    def add_button(self, obj, text, optionstring):
        new_button = QPushButton(self)
        new_button.setText(text)
        new_button.clicked.connect(
            lambda: self.parent().parent.button_side_button_action(optionstring, obj))
        self.vbox.addWidget(new_button)

    def add_buttons(self, option = None):
        self.clear_buttons()

        if option is None or isinstance(option, BolHeader):
            return

        obj = option.bound_to
        if isinstance(obj, EnemyPointGroups):
            self.add_button(obj, "Add Enemy Path", "add_enemypath")
        elif isinstance(obj, (EnemyPointGroup, EnemyPoint)):
            self.add_button(obj, "Add Enemy Points", "add_enemypoints")
        elif isinstance(obj, (CheckpointGroups)):
            self.add_button(obj, "Add Checkpoint Group", "add_checkpointgroup")
        elif isinstance(obj, (CheckpointGroup, Checkpoint)):
            self.add_button(obj, "Add Checkpoints", "add_checkpoints")
        elif isinstance(obj, ObjectContainer):
            if obj.object_type is Route:
                self.add_button(obj, "Add Route", "add_route")
        elif isinstance(obj, (Route, RoutePoint)):
            self.add_button(obj, "Add Route Points", "add_routepoints")

    def clear_buttons(self):
        for i in reversed(range(self.vbox.count())):
            self.vbox.itemAt(i).widget().setParent(None)
