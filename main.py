import PySimpleGUI as sg

def hello_world(name):
    # Use a breakpoint in the code line below to debug your script.
    sg.Window(title=f'Hello World, {name}', layout=[[]], margins=(100, 50)).read()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hello_world('PyCharm')

