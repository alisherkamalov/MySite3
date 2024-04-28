import flet as ft
from flet import FilePicker
import time
def main(page: ft.Page):
    
    page.bgcolor=ft.colors.WHITE
    page.scroll = "auto"
    
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
        
    }
    entry = ft.CupertinoTextField(width=400, height=65)
    
    drop = ft.Dropdown(options=[
                                        ft.dropdown.Option('центнер'),
                                        ft.dropdown.Option('тонн'),
                                        ft.dropdown.Option('килограмм'),
                                        ], width=400)
    
    entry2 = ft.CupertinoTextField(width=400, height=65)
    
    drop2 = ft.Dropdown(options=[
                                        ft.dropdown.Option('Москва'),
                                        ft.dropdown.Option('Санкт-Петербург'),
                                        ft.dropdown.Option('Мурманск'),
                                        ], width=400)
    
    company = ft.CupertinoTextField(width=400)
    
    email = ft.CupertinoTextField(width=400)
    
    error = ft.Container (
        margin=ft.margin.only(460,-150),
        animate_opacity=300, 
        opacity=1,
        content=ft.Stack([
            ft.Text('Вы не заполнили нужные поля!', size=20, color=ft.colors.RED, selectable=True, weight=ft.FontWeight.W_900)
        ])
    )
    def order(event):
        order_cont = ft.Container (
            
            bgcolor=ft.colors.GREY_200,
            border_radius=15,
            margin=ft.margin.only(410,0),
            padding=ft.padding.only(20,20),
            width=400,
            height=150,
            content=ft.Column([
                ft.Text('Ваша заявка на рассмотрении. Ожидайте', size=20, color=ft.colors.BLACK, selectable=True, weight=ft.FontWeight.W_900),
                ft.Container (
                    padding=ft.padding.only(45,25),
                    content=ft.Stack([
                        ft.Text('ВСЕ ПРАВА ЗАЩИЩЕНЫ АО VISMA', size=15, color=ft.colors.GREY_500)
                    ])
                )
                
            ])
        )
        if entry.value == "":
            page.clean()
            page.add(ft.Column([cap_cont, loading_cont,article2, error, bottombar, bottombar2]))
            page.update
        elif entry2.value == '':
            page.clean()
            page.add(ft.Column([cap_cont, loading_cont,article2, error, bottombar, bottombar2]))
            page.update
        elif drop.value == None:
            page.clean()
            page.add(ft.Column([cap_cont, loading_cont,article2, error, bottombar, bottombar2]))
            page.update
        elif drop2.value == None:
            page.clean()
            page.add(ft.Column([cap_cont, loading_cont,article2, error, bottombar, bottombar2]))
            page.update
        elif company.value == '':
            page.clean()
            page.add(ft.Column([cap_cont, loading_cont,article2, error, bottombar, bottombar2]))
            page.update
        elif email.value == '':
            page.clean()
            page.add(ft.Column([cap_cont, loading_cont,article2, error, bottombar, bottombar2]))
            page.update
            
        else:
            page.clean()
            page.add(ft.Column([cap_cont, loading_cont,order_cont, bottombar, bottombar2]))
            page.update
            
    def loading(event):
        
        page.route = '/loading-unloading'
        
        if page.route == '/loading-unloading':
            
            page.clean()
            page.add(ft.Column([cap_cont, loading_cont, article2, bottombar, bottombar2]))
            
            
        page.update
    
    def home(event):
        
        page.route = '/home'
        
        if page.route == '/home':
            
            page.clean()
            page.add(ft.Column([cap_cont, body_cont, cont_services, cont_company,cont_news, bottombar, bottombar2]))
        
        
        
        page.update
        
        
    def client(event):
        
        page.route = '/client'
        
        if page.route == '/client':
            
            page.clean()
            page.add(ft.Column([cap_cont, breadcrumbs, article, bottombar, bottombar2]))
        
        page.update
    
        
    

    page.theme = ft.Theme(font_family="Kanit")

    cont_logo = ft.Container(
        width=130,
        height=38,
        on_click=home,
        alignment=ft.alignment.Alignment(0,0.5),
        content=ft.Stack([
            ft.Image(src="https://raw.githubusercontent.com/alisherkamalov/MySite3/main/Vector.png", width=100, height=100),
        ])
    )
    
    
    
    
    
        
        
            
    
    
    cap_cont = ft.Container (
        alignment=ft.alignment.center,
        padding=ft.padding.only(150,0),
        content=ft.Column([
                    
                ft.Row([
                    
                cont_logo,
                ft.Container (
                    expand=True,
                    bgcolor=ft.colors.WHITE,
                    alignment=ft.alignment.Alignment(0,0.5),
                    padding=ft.padding.only(75,0),
                    content=ft.Row([
                        
                        ft.Column([
                            ft.Container (
                                
                                on_click=lambda _: cont_company.scroll_to(key="A", duration=1000),
                                padding=ft.padding.only(30,0),
                                content=ft.Stack([
                                    ft.Text('О компании', size=15, color=ft.colors.BLACK)
                                ])
                            )
                        
                        
                        ]),
                        ft.Column([
                            ft.Container (
                                on_click=True,
                                padding=ft.padding.only(30,0),
                                content=ft.Stack(
                                    [
                                        ft.Text("Новости", size=15, color=ft.colors.BLACK),
                                    ]
                                )
                            )
                        
                        
                        ]),
                        
                        ft.Column([
                            ft.Container (
                                on_click=True,
                                padding=ft.padding.only(30,0),
                                content=ft.Stack(
                                    [
                                        ft.Text("Новости", size=15, color=ft.colors.BLACK),
                                    ]
                                )
                            )
                        
                        
                        ]),
                        
                        ft.Column([
                            ft.Container (
                                on_click=True,
                                padding=ft.padding.only(30,0),
                                content=ft.Stack(
                                    [
                                        ft.Text("Новости", size=15, color=ft.colors.BLACK),
                                    ]
                                )
                            )
                        
                        
                        ]),
                        ft.Column([
                            ft.Container (
                                on_click=client,
                                padding=ft.padding.only(30,0),
                                content=ft.Stack(
                                    [
                                        ft.Text("Информация", size=15, color=ft.colors.BLACK),
                                    ]
                                )
                            )
                        
                        
                        ]),
                        ft.Column([
                            ft.Container (
                                on_click=True,
                                padding=ft.padding.only(30,0),
                                content=ft.Stack(
                                    [
                                        ft.Icon(name=ft.icons.SEARCH, size=20, color=ft.colors.PURPLE_700),
                                    ]
                                )
                            )
                        
                        
                        ]),
                        ft.Column([
                            ft.Container (
                                on_click=True,
                                padding=ft.padding.only(175,0),
                                content=ft.Row(
                                    [
                                        ft.Text('RU', size=20, color=ft.colors.BLACK),
                                        ft.Icon(name=ft.icons.ARROW_DROP_DOWN, color=ft.colors.BLUE_500)
                                        ]
                                )
                            )
                        
                        
                        ]),
                        
                        
                        ])
                )
                ]),
                
                
        ]))
    
    body_cont =  ft.Container (
        
                                content=ft.Stack([
                                    ft.Image(src='https://s3-alpha-sig.figma.com/img/c57d/560c/19a1563b86789d52771e3672bd069cbe?Expires=1714953600&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=i2Dnr0IEoH4s5hJULJQus9qBea2BWCoS9pMZCV9UyWf-FAYtKcgQ2f4JPBgd0hGnRhbRxyeBXXrw2h2U8YrzPQOBfyGV0DdX240LReVEjp6dNqN0H067HUiT1XKOFgonxXYLa~18lSj2v9-l9Izxx5piCJyXkb4HGaraIhGsN~QT0G5Nb8ERLx5gs-U3r82mxgny0s4yuq7QcVmDfG5Oa5XU-8CL3sLIj92XxzKNoDp3gcJZtSHOtvGlp-mIo4GNVGMT-qaG-akDkGFyZVKF999Yoh0q2s8p2a9qSeaq2-WoZG-US6MV4WKQPicMGVBBqmgNxardyJ7zL6bEAQgR1w__'),
                                    ft.Container (
                                        width=10000,
                                        height=830,
                                        bgcolor=ft.colors.INDIGO,

                                        opacity=0.5,
                                        
                                        
                                    ),
                                    ft.Container (
                                        padding=ft.padding.only(200,0),
                                        width=500,
                                        
                                        content=ft.Column([
                                            ft.Row([
                                            ft.Text('Тавимский морской\nпорт VISMA', size=35, color=ft.colors.WHITE),
                                            
                                            ft.Container (
                                                width=250,
                                                height=175,
                                                margin=70,
                                                padding=20,
                                                bgcolor=ft.colors.BLUE_300,
                                                border_radius=15,
                                                
                                                
                                                
                                                content=ft.Column([
                                                        ft.Text('Услуги', size=15, color=ft.colors.WHITE),
                                                        ft.Container(
                                                            
                                                            padding=ft.padding.only(0,65),
                                                            content=ft.Stack([
                                                                ft.Text('Погрузочно-разгрузочная деятельность', size=15, color=ft.colors.WHITE)
                                                            ]),
                                                            on_click=loading,
                                                        )
                                                    ])
                                                ),
                                            
                                            ft.Container (
                                                width=250,
                                                height=175,
                                                
                                                padding=20,
                                                bgcolor=ft.colors.BLUE_300,
                                                border_radius=15,
                                                
                                                
                                                animate_scale=ft.animation.Animation(300, ft.AnimationCurve.EASE),
                                                content=ft.Column([
                                                            ft.Text('Услуги', size=15, color=ft.colors.WHITE),
                                                            ft.Container(
                                                                padding=ft.padding.only(0,65),
                                                                content=ft.Stack([
                                                                    ft.Text('Хранение\nгрузов', size=15, color=ft.colors.WHITE)
                                                            ])
                                                        )
                                                    ])
                                                ),
                                            
                                            
                                            ]),
                                            
                                            
                                            ft.Row([
                                            ft.Text('Vel posuere nibh odio placerat massa vel tellus\ntortor. Varius eget nunc scelerisque etiam felis\nfacilisi ante viverra sem. Nunc eros elementum.', size=15, color=ft.colors.WHITE),
                                            ft.Container (
                                                width=250,
                                                height=175,
                                                margin = 60.5,
                                                padding=20,
                                                bgcolor=ft.colors.BLUE_300,
                                                border_radius=15,
                                                
                                                
                                                animate_scale=ft.animation.Animation(300, ft.AnimationCurve.EASE),
                                                content=ft.Column([
                                                            ft.Text('Услуги', size=15, color=ft.colors.WHITE),
                                                            ft.Container(
                                                                padding=ft.padding.only(0,65),
                                                                content=ft.Stack([
                                                                    ft.Text('Складские\nоперации', size=15, color=ft.colors.WHITE)
                                                            ])
                                                        )
                                                    ])
                                                ),
                                            ft.Container (
                                                width=250,
                                                height=175,
                                                
                                                padding=20,
                                                bgcolor=ft.colors.BLUE_300,
                                                border_radius=15,
                                                
                                                
                                                animate_scale=ft.animation.Animation(300, ft.AnimationCurve.EASE),
                                                content=ft.Column([
                                                            ft.Text('Услуги', size=15, color=ft.colors.WHITE),
                                                            ft.Container(
                                                                padding=ft.padding.only(0,65),
                                                                content=ft.Stack([
                                                                    ft.Text('Швартовые\nоперации', size=15, color=ft.colors.WHITE)
                                                            ])
                                                        )
                                                    ])
                                                ),
                                            
                                        ]),
                                        ft.Column([
                                            ft.Row([
                                            ft.Container (
                                                on_click=True,
                                                content=ft.Row([
                                                    ft.Text("О КОМПАНИИ", size=25, color=ft.colors.WHITE),
                                                    ft.Icon(name=ft.icons.NAVIGATE_NEXT, size=25, color=ft.colors.WHITE)
                                                ])
                                            )
                                            
                                        ])])
                                ])),
                                    
                                    
                                
                                    
                                ])
    )
    
    cont_services = ft.Container (
        padding=50,
        content=ft.Row([
            ft.Column([
                ft.Container(
                    content=ft.Column([
                        ft.Text('Услуги', size=30, color=ft.colors.BLACK),
                        ft.Row([
                        ft.Text('Тарифы на услуги по обеспечению\nконтроля доступа на территорию\nVISMA на 2022 год', size=15, color=ft.colors.PURPLE_300),
                        ft.Container(
                            width=75,
                            height=50,
                            alignment=ft.alignment.center,
                            bgcolor=ft.colors.BLUE_200,
                            border_radius=15,
                            content=ft.Stack([
                                ft.Text('PDF', color=ft.colors.WHITE)
                            ]),
                        
                        ),
                        
                            ft.Container (
                                padding=ft.padding.only(100,0),
                                content=ft.Row([
                                ft.Container (
                                    bgcolor=ft.colors.INDIGO,
                                    width=350,
                                    height=200,
                                    padding=25,
                                    border_radius=15,
                                    content=ft.Column([
                                        ft.Text('Услуги', size=20, color=ft.colors.WHITE),
                                        ft.Container (
                                            padding = ft.padding.only(0,90),
                                            content=ft.Stack([
                                                ft.Text('Хранение грузов', size=20, color=ft.colors.WHITE),
                                            ])
                                        )
                                        
                                    ])
                                        )
                                    ])
                            ),
                            ft.Container (
                                padding=ft.padding.only(10,0),
                                content=ft.Row([
                                ft.Container (
                                    bgcolor=ft.colors.INDIGO,
                                    width=350,
                                    height=200,
                                    border_radius=15,
                                    padding=25,
                                    content=ft.Column([
                                        ft.Text('Услуги', size=20, color=ft.colors.WHITE),
                                        ft.Container (
                                            padding = ft.padding.only(0,90),
                                            content=ft.Stack([
                                                ft.Text('Швартовые операции', size=20, color=ft.colors.WHITE),
                                            ])
                                        )
                                        
                                    ])
                                        ),
                                    
                                    ])
                            )
                        ]),
                        ft.Row([
                        ft.Text('Условия определения цены\nдоговора и тарифы на работы', size=15, color=ft.colors.PURPLE_300),
                        ft.Container(
                            width=75,
                            height=50,
                            margin=ft.margin.only(33.5,0),
                            alignment=ft.alignment.center,
                            bgcolor=ft.colors.BLUE_200,
                            border_radius=15,
                            content=ft.Stack([
                                ft.Text('PDF', color=ft.colors.WHITE)
                            ]),
                            
                        ),
                        ft.Container (
                                padding=ft.padding.only(100,0),
                                content=ft.Row([
                                ft.Container (
                                    bgcolor=ft.colors.INDIGO,
                                    width=350,
                                    height=200,
                                    padding=25,
                                    border_radius=15,
                                    content=ft.Column([
                                        ft.Text('Услуги', size=20, color=ft.colors.WHITE),
                                        ft.Container (
                                            padding = ft.padding.only(0,90),
                                            content=ft.Stack([
                                                ft.Text('Складские операции', size=20, color=ft.colors.WHITE),
                                            ])
                                        )
                                        
                                    ])
                                        )
                                    ])
                            ),
                            ft.Container (
                                padding=ft.padding.only(10,0),
                                content=ft.Row([
                                ft.Container (
                                    bgcolor=ft.colors.INDIGO,
                                    width=350,
                                    height=200,
                                    border_radius=15,
                                    padding=25,
                                    content=ft.Column([
                                        ft.Text('Услуги', size=20, color=ft.colors.WHITE),
                                        ft.Container (
                                            padding = ft.padding.only(0,65),
                                            content=ft.Stack([
                                                ft.Text('Агентское обслуживание\nсудов', size=20, color=ft.colors.WHITE),
                                            ])
                                        )
                                    ])
                            ),
                                        
                            
                                    
                        ])),
                        
                        
                        
                        
                        ]),
                        ft.Row([
                        ft.Text('Договор перевалки\n(типовая форма)', size=15, color=ft.colors.PURPLE_300),
                        ft.Container(
                            width=75,
                            height=50,
                            margin=ft.margin.only(107.5,5),
                            alignment=ft.alignment.center,
                            bgcolor=ft.colors.BLUE_200,
                            border_radius=15,
                            content=ft.Stack([
                                ft.Text('PDF', color=ft.colors.WHITE),
                                
                            
                            ])
                        ),
                        ft.Container (
                                padding=ft.padding.only(95,0),
                                content=ft.Row([
                                ft.Container (
                                    bgcolor=ft.colors.INDIGO,
                                    width=350,
                                    height=200,
                                    padding=25,
                                    margin=4,
                                    border_radius=15,
                                    content=ft.Column([
                                        ft.Text('Услуги', size=20, color=ft.colors.WHITE),
                                        ft.Container (
                                            padding = ft.padding.only(0,60),
                                            content=ft.Stack([
                                                ft.Text('Буксировка / сопровождение судов', size=20, color=ft.colors.WHITE),
                                            ])
                                        )
                                        
                                    ])
                                        ),
                                    ft.Container (
                                    
                                    bgcolor=ft.colors.INDIGO,
                                    width=350,
                                    height=200,
                                    padding=25,
                                    border_radius=15,
                                    content=ft.Column([
                                        ft.Text('Услуги', size=20, color=ft.colors.WHITE),
                                        ft.Container (
                                            on_click=loading,
                                            padding = ft.padding.only(0,60),
                                            content=ft.Stack([
                                                ft.Text('Погрузочно-разгрузочная деятельность', size=20, color=ft.colors.WHITE),
                                            ])
                                        )
                                        
                                    ])
                                        )
                                    ])
                            ),
                        ])
            ])),
                
            
        ])
        ]
        )
    )
    
    cont_company = ft.Container (
        
        ft.Row ([
            ft.Column([
                
                ft.Container (
                    padding=ft.padding.only(70,50),
                    content=ft.Column([
                        ft.Text('О компании', size=35, color=ft.colors.BLACK),
                        ft.Text('Tristique orci consectetur sit felis. Sed ac auctor tellus lobortis. Enim non turpis nulla nec a\nsapien sit amet molestie. Et id malesuada gravida sit volutpat. Volutpat sed lectus\nelementum diam neque facilisis in. Convallis nibh sem in viverra quis. Interdum pharetra.', color=ft.colors.BLACK, size=15),
                        ft.Text('Libero nunc porttitor id mi convallis ultricies convallis erat. At sagittis nisi at in diam sit.', color=ft.colors.BLACK, size=15),
                        ft.Container (
                            content=ft.Column([
                                ft.Text('●  Vivamus tincidunt non lectus odio magna semper odio risus.', color=ft.colors.BLACK, size=15),
                                ft.Text('●  Vivamus tincidunt non lectus odio magna semper odio risus.', color=ft.colors.BLACK, size=15),
                                ft.Text('●  Vivamus tincidunt non lectus odio magna semper odio risus. Vivamus tincidunt non\nlectus odio magna semper odio risus.Vivamus tincidunt non lectus odio magna semper\nodio risus', color=ft.colors.BLACK, size=15),
                                ft.Text('●  Vivamus tincidunt non lectus odio magna semper odio risus.', color=ft.colors.BLACK, size=15),
                                ft.Text('●  Vivamus tincidunt non lectus odio magna semper odio risus.', color=ft.colors.BLACK, size=15),
                                ft.Text('Quam accumsan mauris enim quam. A commodo ultrices urna vitae nibh rhoncus at nisl. Duis\nnibh libero ut enim. Metus aliquam cursus molestie sapien risus. Suspendisse volutpat', color=ft.colors.BLACK, size=15),
                                ft.Text('●  Vivamus tincidunt non lectus odio magna semper odio risus.', color=ft.colors.BLACK, size=15),
                                ft.Text('●  Vivamus tincidunt non lectus odio magna semper odio risus.', color=ft.colors.BLACK, size=15),
                                ft.Text('●  Vivamus tincidunt non lectus odio magna semper odio risus.', color=ft.colors.BLACK, size=15),
                                ft.Text('●  Vivamus tincidunt non lectus odio magna semper odio risus.', color=ft.colors.BLACK, size=15),
                            ])
                        )

                    ])
                )
            ]),
        ft.Column([
        ft.Container (
            offset=ft.transform.Offset(0,0.7),
            margin=ft.margin.only(20,0),
            content=ft.Stack([
                ft.Image(src='https://s3-alpha-sig.figma.com/img/7e4f/b869/8c48e87440f300040284081acad7d5c7?Expires=1714953600&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=Yxdn8rkhOEzz7SwRC-C9TRRMKjenlwk3RrK4FjkU6jNn8No5FwJVIEgmXnDXf8OOZ73e~pSLYq-I8X-diOgJ9ufv9AqA1~uX45K2r~TUqoFQSKDHUequ0vQSDGCtdmLikqi4EuNVvKN~pC78me2gooMLOMYGOPlnqzIPBXImDy~XPwwG7jlVPnXGE~bmFGvwXEBIwwRzWKlN~YJGg~~~ME4uXCMNpDqIAJvzQJg2G9APbqmSk0iuwa6LTJRZJxWSnmXw6VAUyhqoROCD8H9OY9QzE23ic8GBLSTnMBn58Wnd-4gvfKFUCRvx6KjlQIt4VlBtScUlVu8UZLr7~3WcKA__', border_radius=15, width=350),
                ft.Container (
                    width=350,
                    height=195.5,
                    bgcolor=ft.colors.INDIGO,
                    opacity=0.5,
                    border_radius=15,
                    
                    
                ),
                ft.Container(
                    padding=ft.padding.only(120,50),
                    content=ft.Stack([
                        ft.Icon(name=ft.icons.PLAY_ARROW, color=ft.colors.WHITE, size=100)
                    ])
                )
                
                
            ])
            ),
        ft.Container (
                margin=ft.margin.only(20,0),
                offset=ft.transform.Offset(0,1.3),
                padding=ft.padding.only(15,15),
                bgcolor=ft.colors.BLUE_300,
                width=350,
                height=160,
                border_radius=15,
                content=ft.Column([
                    ft.Text('Запрос ставки и условий погрузочно-разгрузочных работ\n', size=17, color=ft.colors.WHITE),
                    ft.Text('Рассчитайте моментально стоимость полных портовых услуг в порту VISMA', size=17, color=ft.colors.WHITE),
                    
                ])
                
            )
        ])
        
            
        
        ]),
        bgcolor=ft.colors.GREY_200,
        height=650,
        
    )
    
    cont_news = ft.Container (
        content=ft.Column ([
                ft.Row([

                    ft.Text('Новости', size=40, color=ft.colors.BLACK),
                    ft.Container (
                        padding=ft.padding.only(800,0),
                        content=ft.Row([
                            ft.Text('ВСЕ НОВОСТИ', size=15, color=ft.colors.INDIGO),
                            ft.Icon(name=ft.icons.NAVIGATE_NEXT, size=15, color=ft.colors.INDIGO)
                            
                            ]
                                       ),
                            
                        
                        ),
                    ]),
                    ft.Row([
                        ft.Row([
                            ft.Container (
                                padding=ft.padding.only(0,50),
                                content=ft.Column([
                                ft.Image(src='https://s3-alpha-sig.figma.com/img/bf97/c8df/45dd9927b263016bc5601481b14e7d89?Expires=1714953600&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=D~NFaqRK9zB9~jvaIShVxeoaCoDnRPzbuYiovab3XrPOMFJKLZr-i5vNrc1kDLPhLdboeetFO~7vgTb2c0rAR3jprttvPHidnsRo9zPNNm3nfpcWlt7LsF7aLnFPO5SDo4l2tqWBmZZoTJq7r6QcTf90sKzE9Ju9ozPup1vLcWXeCnssPyZhcMnaAJj2sGbPdGTN7gbIvIHkmX-dZ0prBPgzlxXXVvGV7yGilqPFl1q0jkGMGEY77AnfW2ucqy-pc7OeYfkKipv2HdlUoJSXh1i6oSkOPelqw1Zc1mq~j3FmHEZAwPbzBiFTsc8LI7yqpAdst~v5KUY6imRYvpD4-A__', width=250, border_radius=15),
                                ft.Text('20/05/22', size=20, color=ft.colors.BLACK),
                                ft.Text('Semper eu pulvinar\neget integer', size=25, color=ft.colors.BLACK),
                                ft.Text('Pretium duis phasellus netus ac.\nNunc nibh nunc integer feugiat\net aliquam cras. Amet pharetra\nmontes ipsum gravida tellus tellus.', size=15, color=ft.colors.BLACK),
                                
                    
                                    ])
                                ),
                            ft.Container (
                                padding=ft.padding.only(0,50),
                                offset=ft.transform.Offset(0,0.04),
                                content=ft.Column([
                                ft.Image(src='https://s3-alpha-sig.figma.com/img/7f21/4021/4ad2e8b8d6eec35cf756da322d6dab85?Expires=1714953600&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=QCgQqwMN0MqOlraZSSk626zZL5gGnT31tlOXix5EZweXqQoAtLKC4Zviy7ozxDjSYUKTBKSDHXi5KC4Xwsq-KhOyeV7ZaTjd5DKoU9LLCzjHWFbFBQQlyy5wkcEacX2GMmBp5tYU6Qvh9cwMb-EMGSkBP-vMv7UeubUl3dgm8aaysmaamUYBVf-6k~C2ZAm5wZcx1EBT47X44vCS0weYU~95EBkgLpdnIyzQvqfpohVo9OoOLzETqJRbHqukdnsdCK5OdGEDGh6MdnEhjKHlu-Nvpc2sxZmhw2lL5-THPH6VTXijDKTtJza5UrkXRShj1m5EayCJYrsYBZJwdSRSBg__', width=250, border_radius=15),
                                ft.Text('20/02/22', size=20, color=ft.colors.BLACK),
                                ft.Text('Vitae id nec nulla sit\nnunc cursus curabitur\ntempus vel enim.', size=25, color=ft.colors.BLACK),
                                ft.Text('Cras arcu ac commodo suspendisse\ncommodo ipsum turpis dui. Quis\npharetra malesuada eget sit egestas\net integer. Suspendisse a.', size=15, color=ft.colors.BLACK),
                                
                    
                                    ])
                                ),
                            ft.Container (
                                padding=ft.padding.only(0,50),
                                offset=ft.transform.Offset(0,0.04),
                                content=ft.Column([
                                ft.Image(src='https://s3-alpha-sig.figma.com/img/5c90/aeda/4397d4f80ab287453227ebf58027c6cb?Expires=1714953600&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=Du0qzF7KPQk5U~G70xfYbrvphtfgIguIcvVkTeOMBhAvMP27q~B1mJwQsTOfY0WzEqHE8KdA4iFy2zAzwjrlzjfAEwd-vvwGnHL5IDlCV5qZN15QNzvSDKEMo9pV~onHcWsNfGll5uJcbsxMEwGBi8uCW5zEbtnfpdmRrZwRppaSW4OoPZrg~eQ1ydvs~-CpDPlFkC5kwimayPERp1cExfoxHbv8AI15NbN71tSFoQO2UHstsg4CY~Rv7Q69oDOzU3kah-nwRdtipLtP~9sB5RC-9iYdbGYV~6Ce9ZgCfxIsVshOKBzZZo1NyORVaFRpMDgjdvEMtoXTKURDpgpQxw__', width=295, border_radius=15),
                                ft.Text('30/12/21', size=20, color=ft.colors.BLACK),
                                ft.Text('Integer nisi sagittis in\naliquet. Enim eget varius\nlacinia est a.', size=25, color=ft.colors.BLACK),
                                ft.Text('Lectus tempus felis pretium vitae. Tempor\nmassa vestibulum condimentum cursus\ndiam quam. Mattis facilisi dignissim\ndonec eget vel.', size=15, color=ft.colors.BLACK),
                                
                    
                                    ])
                                ),
                            ft.Container (
                                padding=ft.padding.only(0,50),
                                content=ft.Column([
                                ft.Image(src='https://s3-alpha-sig.figma.com/img/6fe1/6ff7/15d6b1d3d02d6a7eb1e3874cef1c77ce?Expires=1714953600&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=N-K7p~4tESzUT2P8Gl09CuwKgyPKaRlF-RbwD531U9Em2CqS~mPjSPhaU8M5FLrK65MrryM-dopNXIiDkseBR2I6dHm2fKanzlJueDp4oa~miO7bA5~r7bb1L4k6bFVx9O4-A0dPuo~ZetAUoBJ~CXp93UkzBEN7djub1CNm8TivHp~PHkRPbBJA8iDlh2yy~vNIIvBvr7e1Id12aYZWxjDs9Vl79W0xOKFG6TGRAuSeKleDE3B-6EBoUm~EU3SZmQjZrqUCrK5mkOqRGepNZxuBk~f508eeFmqaq6d03D4o6tklhIOEsPLwv-aqIAYBYUua2JF65HX7WJzkS7M~og__', width=250, border_radius=15),
                                ft.Text('29/06/21', size=20, color=ft.colors.BLACK),
                                ft.Text('Facilisis vitae proin\nquis', size=25, color=ft.colors.BLACK),
                                ft.Text('Iaculis diam quam velit sit\nnunc turpis ultricies elementum.\nVitae lacinia tristique rutrum\nfaucibus nulla quis ultricies. Risus.', size=15, color=ft.colors.BLACK),
                                
                    
                                    ])
                                )
                        ])]),
            
                    
        
        ]),
        
        
        alignment=ft.alignment.top_center,
        padding=ft.padding.only(100,100),
        height=800
        )
    
    bottombar = ft.Container (
        bgcolor='#3D348B',
        opacity=0.7,
        offset=ft.transform.Offset(0,0.1),
        width=10000,
        height=150,
        padding=ft.padding.only(100, 35),
        content=ft.Column([
            ft.Row([
                ft.Icon(name=ft.icons.LOCATION_ON, size=30, color=ft.colors.WHITE),
                ft.Text('123456, г. Тавима, ул. Морская, д. 21', size=15, color=ft.colors.WHITE),
                ft.Container (
                    padding=ft.padding.only(135,0),
                    content=ft.Stack([
                        ft.Image(src='https://raw.githubusercontent.com/alisherkamalov/MySite3/main/Vector%20(1).png')
                    ])
                ),
                ft.Container (
                    padding=ft.padding.only(130,0),
                    content=ft.Row([
                        ft.Icon(name=ft.icons.PHONE, size=30, color=ft.colors.WHITE),
                        ft.Text('+7 (123) 456-67-89', size=15, color=ft.colors.WHITE),
                        
                    ])
                ),
                ft.Container (
                    padding=ft.padding.only(35,0),
                    content=ft.Row([
                        ft.Icon(name=ft.icons.EMAIL, size=30, color=ft.colors.WHITE),
                        ft.Text('order@visma.ru', size=15, color=ft.colors.WHITE),
                        
                    ])
                )
            ])
        ])
        
    )
    
    bottombar2 = ft.Container (
                width=10000,
                height=500,
                bgcolor='#3D348B',
                
                content=ft.Column([
                    ft.Row([
                        ft.Container (
                            padding=ft.padding.only(100,50),
                            content=ft.Column([
                                ft.Text('ИНФОРМАЦИЯ О ЮР. ЛИЦЕ', size=15, color=ft.colors.WHITE),
                                ft.Text('ОГРН 11111111111111111\n\nИНН 2222222222222\n\nКПП 3333333333333\n\nОКПО 44444444444 ОКВЭД 52.24\n\nОКТМО 5555555555555', size=12.5, color=ft.colors.WHITE),
                            ])
                        ),
                        ft.Container (
                            padding=ft.padding.only(100,-22.0),
                            content=ft.Column([
                                ft.Text('ЗАКУПКИ', size=15, color=ft.colors.WHITE),
                                ft.Text('Нормативные документы\n\nЗакупки на VISMA Order\n\nЗакупки на VISMA Tender', size=12.5, color=ft.colors.WHITE),
                            ])
                        ),
                        ft.Container (
                            padding=ft.padding.only(100,50),
                            content=ft.Column([
                                ft.Text('АКЦИОНЕРАМ', size=15, color=ft.colors.WHITE),
                                ft.Text('Устав VISMA\n\nСвидетельства госрегистрации\n\nСписок аффилированных лиц\n\nИнформация\n\nОтчеты', size=12.5, color=ft.colors.WHITE),
                            ])
                        ),
                        ft.Container (
                            padding=ft.padding.only(100,122.5),
                            content=ft.Column([
                                ft.Text('О КОМПАНИИ', size=15, color=ft.colors.WHITE),
                                ft.Text('Порт сегодня\n\nХарактеристики порта\n\nИстория\n\nДипломы и награды\n\nТранспортная безопасность\n\nЭкология\n\nПравовая информация', size=12.5, color=ft.colors.WHITE),
                            ])
                        )
                    ]),
                    ft.Container (
                        alignment=ft.alignment.bottom_center,
                        offset=ft.transform.Offset(-0.02,1.5),
                        content=ft.Stack([
                            ft.Text('ВСЕ ПРАВА ЗАЩИЩЕНЫ АО VISMA', size=15, color=ft.colors.GREY_300, opacity=0.5)
                        ])
                    )
                ])
                
            )
                        
                        
    breadcrumbs = ft.Container (
        bgcolor=ft.colors.GREY_100,
        width=cap_cont.width,
        height=75,
        content=ft.Row([
            ft.Container (
                padding=ft.padding.only(30,0),
                content=ft.Row([
                    ft.Text('ГЛАВНАЯ', size=15, color=ft.colors.BLACK),
                    ft.Icon(name=ft.icons.NAVIGATE_NEXT, size=15, color=ft.colors.BLACK),
                    ft.Text('КЛИЕНТАМ', size=15, color=ft.colors.BLACK),
                    ft.Icon(name=ft.icons.NAVIGATE_NEXT, size=15, color=ft.colors.BLACK),
                    ft.Text('ЗАЯВКА И ПЕРЕЧЕНЬ ДОКУМЕНТОВ ДЛЯ ЗАКЛЮЧЕНИЯ ДОГОВОРОВ', size=15, color=ft.colors.BLACK),
                ])
            )
        ])
        
        
        
    )
    
    article = ft.Container (
        width=cap_cont.width,
        content=ft.Column(
            [
                ft.Container (
                    padding=ft.padding.only(185,150),
                    content=ft.Column([
                        ft.Text('Заявка и перечень документов для заключения', size=35, color=ft.colors.BLACK, selectable=True, weight=ft.FontWeight.W_900),
                        ft.Container (
                            padding=ft.padding.only(310,0),
                            content=ft.Stack([
                                ft.Text('договоров\n\n', size=35, color=ft.colors.BLACK, selectable=True, weight=ft.FontWeight.W_900)
                            ])
                        ),
                        ft.Text('''Для рассмотрения возможности заключения договора контрагент должен предоставить следующие документы:
• заявку (оферту) на имя генерального директора VISMA Technology, которая подается на фирменном бланке\nорганизации и должна содержать сведения о виде работ и услуг, на которые контрагент предлагает заключить\nдоговор, номенклатуре груза и общем объеме на год с разбивкой по месяцам.
\n
Для резидентов РФ (документы должны быть заверены подписью руководителя и печатью организации):
\n
• копию выписки из ЕГРЮЛ (выданной не позднее одного месяца до даты заключения договора);
\n
• копии учредительных документов (устава, положения);
\n
• копию протокола или выписки из протокола о назначении исполнительного органа;
\n
• копию свидетельства о государственной регистрации;
\n
• копию приказа о назначении лица, действующего на основании положения;
\n
• копию доверенности представителя;
\n
• копию свидетельства о постановке на учет в качестве налогоплательщика;
\n
• заполненную карточку контрагента, заверенную подписью и печатью руководителя организации и\nглавного бухгалтера и содержащую следующую информацию:
\n
1. Юридический адрес контрагента;
\n
2. Фактический адрес контрагента;
\n
3. Банковские реквизиты контрагента;
\n
4. Контактная информация: номер факса, адрес электронной почты и контактные лица с указанием номеров телефонов.
\n
Для нерезидентов РФ (документы должны быть предоставлены с нотариально заверенным переводом на русский язык):
\n
• выписка из Торгового реестра страны происхождения компании-контрагента (о благонадежности компании);
\n
• учредительные документы и документы регистрации фирмы (копии);
\n
• подтверждение полномочий лица на право подписания договора, нотариально заверенная доверенность с апостилем,\nлибо выписка из протокола о назначении (избрании) на должность;
\n
• заполненную карточку контрагента, заверенную подписью и печатью руководителя организации и содержащую\nследующую информацию:
\n
1. Юридический адрес контрагента;
\n
2. Фактический адрес контрагента;
\n
3. Банковские реквизиты контрагента;
\n
4. Контактная информация: номер факса, адрес электронной почты и контактные лица с указанием номеров телефонов.\n\n\n\n\n\n''', size=15, color=ft.colors.BLACK)
                        
                    ])
                )
            ]
        )
    )
    
    
    loading_cont = ft.Container (
        bgcolor=ft.colors.GREY_100,
        width=cap_cont.width,
        height=75,
        content=ft.Row([
            ft.Container (
                padding=ft.padding.only(30,0),
                content=ft.Row([
                    ft.Text('ГЛАВНАЯ', size=15, color=ft.colors.BLACK),
                    ft.Icon(name=ft.icons.NAVIGATE_NEXT, size=15, color=ft.colors.BLACK),
                    ft.Text('КЛИЕНТАМ', size=15, color=ft.colors.BLACK),
                    ft.Icon(name=ft.icons.NAVIGATE_NEXT, size=15, color=ft.colors.BLACK),
                    ft.Text('ЗАПРОС СТАВКИ И УСЛОВИЙ ПОГРУЗОЧНО-РАЗГРУЗОЧНЫХ РАБОТ', size=15, color=ft.colors.BLACK),
                ])
            )
        ])
        
        
    )
    name_file = ft.Text(value='ФАЙЛ НЕ ВЫБРАН', size=15, color=ft.colors.BLACK)
    
    
    
    def file(event: ft.FilePickerResultEvent):
        
        file_picker = ft.FilePicker(on_result=file)
        page.overlay.append(file_picker)
        page.update()
        
        
        
        file_picker.pick_files(allow_multiple=True)
        
        
        
        
        for f in event.files:
            name_file.value = f'{f.name}'
        page.update()
        page.overlay.clear()
        page.update()
        
    
    
    article2 = ft.Container (
        width=cap_cont.width,
        height=1900,
        content=ft.Column(
            [
                ft.Container (
                    padding=ft.padding.only(230,150),
                    content=ft.Column([
                        ft.Text('Запрос ставки и условий погрузочно-\nразгрузочных работ', size=35, color=ft.colors.BLACK, selectable=True, weight=ft.FontWeight.W_900),
                        ft.Container (
                            margin=ft.margin.only(-10,50),
                            content=ft.Row([
                                ft.Column([
                                    ft.Text('НАИМЕНОВАНИЕ ГРУЗА *',size=15, selectable=True, weight=ft.FontWeight.W_900),
                                    entry,
                                    ft.Text('ЕД. ИЗМЕРЕНИЯ *',size=15, selectable=True, weight=ft.FontWeight.W_900),
                                    drop,
                                    ft.Text('ПУНКТ НАЗНАЧЕНИЯ ПЕРЕВОЗКИ ',size=15, selectable=True, weight=ft.FontWeight.W_900),
                                    ft.CupertinoTextField(width=400, height=65),
                                    ft.Text('ГРУЗ ПОСТУПАЕТ В ПОРТ ',size=15, selectable=True, weight=ft.FontWeight.W_900),
                                    ft.Dropdown(options=[
                                        ft.dropdown.Option('Азово-Черноморский'),
                                        ft.dropdown.Option('Усть-Луга'),
                                        ft.dropdown.Option('Мурманск'),
                                        ], width=400),
                                    ft.Text('РАЗМЕР СУДОВОЙ ПАРТИИ ',size=15, selectable=True, weight=ft.FontWeight.W_900),
                                    ft.CupertinoTextField(width=400, height=65),
                                    ft.Text('ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ О ГРУЗЕ',size=15, selectable=True, weight=ft.FontWeight.W_900),
                                    ft.CupertinoTextField(width=400, height=150, multiline=True,),
                                ]),
                                ft.Column([
                                    ft.Text('РАЗМЕР ПАРТИИ *',size=15, selectable=True, weight=ft.FontWeight.W_900),
                                    entry2,
                                    ft.Text('НАПРАВЛЕНИЕ ПЕРЕВОЗКИ *',size=15, selectable=True, weight=ft.FontWeight.W_900),
                                    drop2,
                                    ft.Text('ПЕРИОД ПОСТУПЛЕНИЯ ГРУЗА К ПЕРЕВАЛКЕ ',size=15, selectable=True, weight=ft.FontWeight.W_900),
                                    ft.Dropdown(options=[
                                        ft.dropdown.Option('15-30 дней'),
                                        ft.dropdown.Option('2-3 месяца'),
                                        ft.dropdown.Option('4 и больше'),
                                        ], width=400),
                                    ft.Text('ГРУЗ ОТПРАВЛЯЕТСЯ ИЗ ПОРТА ',size=15, selectable=True, weight=ft.FontWeight.W_900),
                                    ft.Dropdown(options=[
                                        ft.dropdown.Option('Азово-Черноморский'),
                                        ft.dropdown.Option('Усть-Луга'),
                                        ft.dropdown.Option('Мурманск'),
                                        ], width=400),
                                    ft.Text('ОПАСТНОСТЬ ГРУЗА (КЛАСС)',size=15, selectable=True, weight=ft.FontWeight.W_900),
                                    ft.CupertinoTextField(width=400, height=65),
                                    ft.Text('ПРИКРЕПИТЬ ФАЙЛ',size=15, selectable=True, weight=ft.FontWeight.W_900),
                                    ft.Row([
                                        ft.Container (
                                            bgcolor=ft.colors.BLUE_300,
                                            alignment=ft.alignment.center,
                                            width = 150,
                                            height = 35,
                                            border_radius=15,
                                            on_click=file,
                                            content=ft.Stack([
                                                ft.Text('ВЫБЕРИТЕ ФАЙЛ', size=12, color=ft.colors.WHITE, selectable=True)
                                            ])
                                        ),
                                        name_file
                                        
                                    ]),
                                    ft.Text('', size=17.9,),
                                    ft.Text(''),
                                    ft.Text('\n'),
                                    
                                    
                                ]),
                                
                                
                            ])
                        ),
                        ft.Container (
                            padding=ft.padding.only(0,50),
                            content=ft.Column(
                                [
                                    ft.Text('Просим сообщить:', size=25, color=ft.colors.BLACK, selectable=True, weight=ft.FontWeight.W_900),
                                    ft.Row([
                                        ft.CupertinoCheckbox(),
                                        ft.Text('СТАВКУ ПРР', size=15, color=ft.colors.BLACK, selectable=True, weight=ft.FontWeight.W_900)
                                    ]),
                                    ft.Row([
                                        ft.CupertinoCheckbox(),
                                        ft.Text('СРОК ТЕХНОЛОГИЧЕСКОГО НАКОПЛЕНИЯ ГРУЗА', size=15, color=ft.colors.BLACK, selectable=True, weight=ft.FontWeight.W_900)
                                    ]),
                                    ft.Row([
                                        ft.CupertinoCheckbox(),
                                        ft.Text('СТАВКУ ХРАНЕНИЯ ГРУЗА СВЕРХ СРОКА ТЕХНОЛОГИЧЕСКОГО НАКОПЛЕНИЯ', size=15, color=ft.colors.BLACK, selectable=True, weight=ft.FontWeight.W_900)
                                    ]),
                                    ft.Row([
                                        ft.CupertinoCheckbox(),
                                        ft.Text('ВОЗМОЖНОСТЬ ПРИЁМА И ПЕРЕВАЛКИ ГРУЗА В УКАЗАННЫЕ СРОКИ', size=15, color=ft.colors.BLACK, selectable=True, weight=ft.FontWeight.W_900)
                                    ]),
                                    
                                ]
                            )
                        ),
                        ft.Container (
                            padding=ft.padding.only(0,50),
                            content=ft.Column([
                                ft.Text('Информация для обратной связи:', size=25, color=ft.colors.BLACK, selectable=True, weight=ft.FontWeight.W_900),
                                ft.Row([
                                    ft.Column([
                                        ft.Text('ИМЯ, ФАМИЛИЯ', size=15, color=ft.colors.BLACK, selectable=True, weight=ft.FontWeight.W_900),
                                        ft.CupertinoTextField(width=400)
                                    ]),
                                    ft.Column([
                                        ft.Text('НАЗВАНИЕ КОМПАНИИ *', size=15, color=ft.colors.BLACK, selectable=True, weight=ft.FontWeight.W_900),
                                        company
                                    ]),
                                ]),
                                ft.Row([
                                    ft.Column([
                                        ft.Text('НОМЕР ТЕЛЕФОНА/ФАКСА', size=15, color=ft.colors.BLACK, selectable=True, weight=ft.FontWeight.W_900),
                                        ft.CupertinoTextField(width=400)
                                    ]),
                                    ft.Column([
                                        ft.Text('АДРЕС ЭЛ. ПОЧТЫ *', size=15, color=ft.colors.BLACK, selectable=True, weight=ft.FontWeight.W_900),
                                        email
                                    ]),
                                ]),
                            ])
                        ),
                        ft.Container (
                            on_click=order,
                            margin=ft.margin.only(320,100),
                            content = ft.Row([
                                ft.Text('ОТПРАВИТЬ', size=20, color=ft.colors.PURPLE_500, selectable=True, weight=ft.FontWeight.W_900),
                                ft.Icon(name=ft.icons.NAVIGATE_NEXT, size=20, color=ft.colors.PURPLE_500)
                            ])
                        )
                    ])
                ),
                
                        
                
                
                
                        
                            
                                
                            
                        
                    
                
            ])
    )
                    
                    
    
    
    
    
    page.route = '/home'

    def route_change(e: ft.RouteChangeEvent):
        if page.route == '/client':
            
            page.clean()
            page.add(ft.Column([cap_cont, breadcrumbs, article, bottombar, bottombar2]))
            
        elif page.route == '/home':
            
            page.clean()
            page.add(ft.Column([cap_cont, body_cont, cont_services, cont_company,cont_news, bottombar, bottombar2]))
            
        elif page.route == '/loading-unloading':
            
            page.clean()
            page.add(ft.Column([cap_cont, loading_cont, article2,  bottombar, bottombar2]))

    page.on_route_change = route_change
    page.update()
    
    
    
    
    
    
    
    
    
    
    page.update
    
    
    #
    
ft.app(target=main, port=5200, view=ft.WEB_BROWSER)
