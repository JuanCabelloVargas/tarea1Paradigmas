from menus import Menu, UserInput

class AttackMenu(Menu):
    @classmethod
    def get_menu(cls, name, available:list[str], not_available:list[str]=None, battle=True) -> str:

        text = f"\n- {name} -\nAvailable attacks:\n"
        for i, o in enumerate(available):
            text += f"{i+1}- {o}\n"
        
        #print(not_available)
        if len(not_available) != 0:
            text += "\nNot available\n"
            for o in not_available:
                text += f"- {o}\n"
        
        if not battle:
            text += f"\n{len(available)+1}- Atras\n"
        
        print(text)
        selection = UserInput.get_input()
        
        
        return available[int(selection)] if selection.isnumeric() and int(selection) > 0 and int(selection) <= len(available) else 'back' if not battle and selection == str(len(available)+1) else None
    ...

class AbilitiesMenu(Menu):
    @classmethod
    def get_menu(cls) -> str:
        return super().get_menu()
    ...

"""
    while True:
        filters = ""
        for i, c in enumerate(self.filter_names):
            filters += f"{i+1}- {c}\n"
        filters += f"\n{len(self.filter_names)+1}- Limpiar filtros"
        filters += f"\n\n{len(self.filter_names)+2}- Salir"  
        opt = input(f'''
Available filters:

{filters}            

>''')
"""
# For testing purposes
#AttackMenu.get_menu(["hola", "hi", "hello"], ["bonk"])