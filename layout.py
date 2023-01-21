from dash import dcc, dash_table, html

resin_options = ['Epoxy', 'Polyester', 'Polyurethane', 'Vinylester']
material_options = ['Glass Fiber E-type', 'Carbon Fiber', 'Aramid', 'Flux']
content_layout = html.Div(children=[
    html.Div(className='column left', children=html.Br()),
    html.Div(className='column middle',
             children=[
                 html.Div(className='h1', children=['Laminate thickness calculator']),
                 html.Div(dcc.Store(id='memory')),
                 html.Div(  # FIRST ROW OF COMPONENTS
                     className='container',
                     children=[
                         html.Div(  # RESIN TYPE DROPDOWN
                             className='container',
                             children=[
                                 html.Div(className='label', children='Resin type'),
                                 html.Div(
                                     dcc.Dropdown(className='dcc dropdown', id='resin_type', options=resin_options)),
                             ]),
                         html.Div(children=html.Br()),
                         html.Div(  # FVF INPUT FIELD
                             className='container',
                             children=[
                                 html.Div(className='label', children='FvF*'),
                                 html.Div(dcc.Input(className='dcc input', id='fvf', placeholder='%', min=0, max=100,
                                                    type='number', size='4'))
                             ])]),
                 html.Div(  # SECOND ROW OF COMPONENTS
                     className='container',
                     children=[
                         html.Div(
                             # className='container',
                             children=[
                                 html.Div(className='dcc label', children='Material'),
                                 html.Div(dcc.Dropdown(
                                     className='dcc dropdown',
                                     id='material_dropdown',
                                     options=material_options)),
                             ],
                         ),
                         html.Div(
                             # className='container',
                             children=[
                                 html.Div(className='dcc label', children='Aerial weight'),
                                 html.Div(dcc.Input(
                                     className='dcc input',
                                     id='weight_input', type='number', size='4', placeholder='gsm')),
                             ]
                         ),
                         html.Div(
                             # className='container',
                             children=[
                                 html.Div(className='dcc label', children='Multiplier'),
                                 html.Div(dcc.Input(
                                     className='dcc input',
                                     id='ply_multiple_input', type='number', size='2', placeholder='1', value=1)),
                             ]
                         )
                     ]
                 ),
                 html.Div(  # THIRD ROW OF COMPONENTS (BUTTONS)
                     className='container',
                     children=[
                         html.Div(html.Button('Submit ply', id='add_ply')),
                         html.Div(html.Button('Undo', id='undo_btn')),
                     ]
                 ),
                 html.Div(  # FOURTH ROW OF COMPONENTS (TABLE)
                     className='container',
                     children=[
                         dash_table.DataTable(
                             id='ply_table',
                             columns=[{'id': "Ply no.", 'name': "Ply no."},
                                      {'id': "Material", 'name': "Material"},
                                      {'id': 'Weight', 'name': 'Weight'},
                                      {'id': 'Thickness', 'name': 'Thickness'}],
                             style_cell={'border': '1px solid rgba(128,128,128,0.1)'},
                             row_selectable=False,
                             cell_selectable=False,
                         )]
                 ),
                 html.Div(  # FIFTH ROW OF COMPONENTS (SUMMARY DATA)
                     className='container',
                     children=[
                         html.Div(children=[
                             html.Div(className='label', children='Total thickness'),
                             dcc.Input(className='dcc input', id='total_thk', disabled=True)]),
                         html.Div(children=[
                             html.Div(className='label', children='Laminate weight per sqm'),
                             dcc.Input(className='dcc input', id='weight_sqm', disabled=True)]),
                         html.Div(children=[
                             html.Div(className='label', children='Approx. resin intake'),
                             dcc.Input(className='dcc input', id='resin_intake', disabled=True),
                         ]),

                     ]
                 ),
                 html.Div(
                     className='container',
                     children=[
                         html.Div(children=[
                             html.Button('Export table to csv', id='export_btn'),
                             dcc.Download(id='download_table')])
                     ]
                 ),
                 html.Div(
                     className='footer',
                     children=[
                         html.Div(
                             className='container',
                             children=[
                                 html.Div(children=[
                                     html.Div(children=['Check out my ']),
                                     dcc.Link(className='link', children=['website'], href='https://furmanp.com',
                                              target='_blank')])
                             ]),
                     ], ),
             ]),

    html.Div(className='column right',
             children=[html.Div(
                 className='side-note',
                 children=
                 [html.A(children='*FvF for most common manufacturing processes:'),
                  html.P(className='p', children='Vacuum infusion: 53%'),
                  html.P(className='p', children='Hand layup: 45%'),
                  html.P(className='p', children='Pre-pregs: 56%'),
                  html.P(className='p', children='Resin Transfer Moulding: 55%')])
             ]
             ),
])
