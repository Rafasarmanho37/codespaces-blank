import controle as con
import flet as ft
componentes = {
        'tf_nome': ft.Ref[ft.TextField](),
        'tf_telefone': ft.Ref[ft.TextField](), 
        'tf_E-mail': ft.Ref[ft.TextField](),
        'tf_Sexo': ft.Ref[ft.RadioGroup](),
        'tf_UF': ft.Ref[ft.Dropdown](), 
        'tabela': ft.Ref[ft.DataTable](),               
        #add todos os compontens da tela aqui
    }

def view():     
    return ft.View(
                "tela1",
                [      
                    ft.Container(content=ft.Text("Cadastro", size=20)),
                    ft.TextField(label='Nome', ref=componentes['tf_nome'], autofocus=True),
                    ft.TextField(label='Telefone', ref=componentes['tf_telefone']),
                    ft.TextField(label='E-mail' , ref=componentes['tf_E-mail'],on_submit=cadastrar),
                    ft.Container(content=ft.Text('Sexo:', size=20), width=150),

                    ft.RadioGroup(content=ft.Row([
                    ft.Radio(value="0", label="M"),
                            
                            
                    ft.Radio(value="1", label="F"),
                      
                 ] 
                 )
                
                             ,ref=componentes['tf_Sexo']
                ),
            
                    ft.Container(content=ft.Text('UF', size=20), width=150),
                        ft.Dropdown(
                               width=100,
                                options=[
                                    ft.dropdown.Option("Pa"),
                                    ft.dropdown.Option("Ro"),
                                    ft.dropdown.Option("Ma"), 
                                    ft.dropdown.Option("Am"),
                                    ft.dropdown.Option("Ap"),
                                    ft.dropdown.Option("Mg"),
                                    ft.dropdown.Option("Sp"),
                                    ft.dropdown.Option("Rj"),
                                    ft.dropdown.Option("Pe"),
                                    ft.dropdown.Option("Re"),
                                ]
                                , ref=componentes['tf_UF'], 

                                
                        ),

                    ft.Row(
                        [
                            ft.ElevatedButton('Cadastrar', icon='save', on_click=cadastrar),
                        ],
                        alignment=ft.MainAxisAlignment.END                   
                    ),                                                                                 
                ],
                
                navigation_bar=con.barra_navegacao(), 
                appbar= ft.AppBar(            
                    title=ft.Text("Sistema de cadastro"),
                    center_title=True,
                    bgcolor=ft.colors.SURFACE_VARIANT,                    
                ),                   
            )

def cadastrar(e):    
    usuario = {
        'nome' : componentes['tf_nome'].current.value,
        'telefone' : componentes['tf_telefone'].current.value,
        'E-mail' : componentes['tf_E-mail'].current.value,
        'Sexo' : componentes['tf_Sexo'].current.value,
        'UF' : componentes['tf_UF'].current.value
    }    
    
    con.banco_de_dados.append(usuario)
    componentes['tf_nome'].current.value = ""
    componentes['tf_telefone'].current.value = ""
    componentes['tf_E-mail'].current.value = ""
    componentes['tf_Sexo'].current.value = ""
    componentes['tf_UF'].current.value = ""     
    con.page.update()