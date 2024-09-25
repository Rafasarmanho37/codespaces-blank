import tela_cadastro as formulario
import tela_tabela as tabela
import flet as ft
def init(p):
    global page, telas, banco_de_dados
    page = p
    banco_de_dados = []
    telas = {
        '1': formulario.view(),
        '2': tabela.view()
    }


def controle_de_rota(route_event):
    page.views.clear()    
    page.views.append(telas[route_event.route])          
    page.update()


def barra_navegacao():
    return ft.NavigationBar(
                        destinations=[
                            ft.NavigationDestination(icon=ft.icons.SAVE, label="Cadastrar"),
                            ft.NavigationDestination(icon=ft.icons.SEARCH, label="Listar"),                            
                        ],
                        on_change= navegacao 
            )#NavigationBar


def navegacao(e):
    if e.control.selected_index+1 == 2:
        tabela.componentes["tabela"].current.rows = tabela.atualizar_tabela()
        
    page.go(str(e.control.selected_index+1))