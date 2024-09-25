import controle as con
import flet as ft
componentes = {        
        'tabela': ft.Ref[ft.DataTable](),       
        #add todos os compontens da tela aqui
    }

def view():     
    return ft.View(
                "tela2",
                [                           
                    ft.DataTable(
                            width=float('inf'),
                            ref=componentes['tabela'],                                                    
                            columns=[
                                ft.DataColumn(ft.Text("Nome")),
                                ft.DataColumn(ft.Text("Telefone")),
                                ft.DataColumn(ft.Text("E-mail")),
                                ft.DataColumn(ft.Text("Sexo")),
                                ft.DataColumn(ft.Text("UF")),                                                                                                
                            ],
                            #rows=[] são ser carregadas dinamicamente
                         ),                                                                         
                ],
                navigation_bar=con.barra_navegacao(), 
                appbar= ft.AppBar(            
                    title=ft.Text("Sistema de cadastro"),
                    center_title=True,
                    bgcolor=ft.colors.SURFACE_VARIANT,                    
                ),                   
            )


def atualizar_tabela():
    return [
            ft.DataRow(cells=preencher_linha_tabela(cadastro)) for cadastro in con.banco_de_dados
        ]


def preencher_linha_tabela(cadastro):
    return [
                ft.DataCell(ft.Text(cadastro['nome'])),
                ft.DataCell(ft.Text(cadastro['telefone'])),
                ft.DataCell(ft.Text(cadastro['E-mail'])),
                ft.DataCell(ft.Text(cadastro['Sexo'])),
                ft.DataCell(ft.Text(cadastro['UF']))                                                           
        ]
