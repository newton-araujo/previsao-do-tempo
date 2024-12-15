import flet as ft
from modules.API import previsao_atual

def main(page:ft.Page):
    
    page.window_max_width = 600
    page.window_max_height = 800
    page.title = 'Previsão do Tempo'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 0
    
    page.update()
    
    #Variable City
    city = ft.TextField(
        label="INFORME A CIDADE",
        border= ft.InputBorder.NONE,
        width=450,
        bgcolor=ft.colors.WHITE12,
        color=ft.colors.WHITE,
        label_style=ft.TextStyle(color=ft.colors.WHITE,size=14,weight=ft.FontWeight.BOLD),
        text_style=ft.TextStyle(size=20,weight=ft.FontWeight.BOLD)
    )


    #Display main
    def display_main():
    
        search = ft.Row(
            [
                ft.Container(
                    width=510,
                    height=50,
                    bgcolor=ft.colors.BLACK38,
                    content=ft.Row(
                        [
                            city,
                            ft.IconButton(
                                icon=ft.icons.SEARCH,
                                icon_size=35,
                                icon_color=ft.colors.WHITE,
                                #on_click= lambda e: temp(e,city.value) #create function
                                )
                        ],
                        spacing=0
                        
                    ),
                    border_radius=ft.border_radius.only(top_right=30,bottom_right=30)
                )
                
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=0
        )
         
        container = ft.Container(
            width=600,
            height=800,
            content= ft.Column(
                [
                    search
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            image_src='https://cdn.pixabay.com/photo/2022/02/07/15/43/mountains-6999713_1280.jpg',
            image_opacity=0.2,
            image_fit=  ft.ImageFit.COVER
            
        )

        page.update()
        
        page.add(container)
    

    def temp(city):
        page.clean()

        date = previsao_atual(city=city)
        temperature = date['current']['temp_c']
        condition = date['current']['condition']['text']


        container_temp = ft.Container(
            width=500,
            height=500,
            bgcolor=ft.colors.WHITE10,
            alignment=ft.alignment.center, 
            content=ft.Column(
                [   
                    ft.Text(f"{city}",size=60,color=ft.colors.WHITE,weight=ft.FontWeight.BOLD),
                    ft.Text(f"Temperatura: {temperature}°C", size=24, color="white",weight=ft.FontWeight.BOLD),
                    ft.Text(f"Condição: {condition}", size=18, color="white",weight=ft.FontWeight.BOLD),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            border_radius=ft.border_radius.all(30)
        )
        #Condition 
        if 'chuva' in condition.lower():
            background_img = 'https://cdn.pixabay.com/animation/2023/06/25/21/55/21-55-38-961_512.gif'
        elif 'nublado' in condition.lower():
            background_img = 'https://cdn.pixabay.com/animation/2023/03/11/17/29/17-29-25-849_256.gif'
        elif 'limpo' in condition.lower():
            background_img = 'https://cdn.pixabay.com/animation/2023/02/20/01/27/01-27-16-323_512.gif'

        # Container main (Stack)
        container_main = ft.Container(
            width=600,
            height=800,
            content=ft.Stack(
                [
                    ft.Image(
                        src=background_img,
                        fit=ft.ImageFit.COVER,
                        width=600,
                        height=800,
                        opacity=0.7,
                    ),
                    container_temp,  # Adiciona o container de temperatura
                ],
                alignment=ft.alignment.center,  # Centraliza todos os itens no Stack
            ),
        )

        # Adiciona o container principal à página
        page.add(container_main)
    temp("São Paulo")

    
ft.app(target=main)