doc_control = """

=========================================================================
R.C Wall calculator in accordance with AS3600:2018, Section 11

Calculator is limited to compression and in-plane shear capacity only
=========================================================================
R.C Pad footing calculator in accordance with AS3600:2018

Calculator is limited to concentric loading only.
=========================================================================
R.C Slab calculator (simplified method) in accordance with AS3600:2018

Calculator is limited to section 6 of AS3600:2018, 1-way & 2-way slabs
=========================================================================

Created: 11/07/2020 - David Hill
Version: V1.0 (beta)

Additional Comments: 

"""


navigation_helper = """
Screen:
    NavigationLayout:
        ScreenManager: 
            id: screen_manager
            
            Screen:
                name: "screen1"
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        id: home
                        title: 'Structural Design Calculators'
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                        specific_text_color: 0.9, 0.9, 0.9, 0.8
                    
                    MDLabel: 
                        text:"Structural Design Calculators\\nin Accordance with Australian Standards"
                        text_size: self.width, None
                        color: 0.2, 0.255, 0.292, 0.9
                        font_style: "H5"
                        pos_hint: {'x':0, 'y':0.3}
                        halign:"center"
                        
                    MDLabel: 
                        text:"Software Notes & Updates:"
                        text_size: self.width, None
                        color: 0.2, 0.255, 0.292, 0.9
                        font_style: "H6"
                        pos_hint: {'x':0.02, 'y':0.5}
                        halign:"left"
                    
                    MDLabel: 
                        text:"R.C Wall calculator in accordance with AS3600:2018, Section 11\\nCalculator is limited to compression and in-plane shear capacity only\\nR.C Pad footing calculator in accordance with AS3600:2018\\n\\nCalculator is limited to concentric loading only.\\nR.C Slab calculator (simplified method) in accordance with AS3600:2018\\nCalculator is limited to section 6 of AS3600:2018, 1-way & 2-way slabs\\n\\nCreated: 11/07/2020 - David Hill\\nVersion: V1.0 (beta)\\n \\nAdditional Comments by Desginer:"
                        text_size: self.width, None
                        color: 0.2, 0.255, 0.292, 0.9
                        font_style: "Body2"
                        pos_hint: {'x':0.02, 'y':0.5}
                        
            
            Screen:
                name: "screen2"
                BoxLayout:
                    orientation: 'vertical'
                    
                    MDToolbar:
                        id: home
                        title: 'R.C Wall Design - In Accordance with AS3600:2018'
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                        specific_text_color: 0.9, 0.9, 0.9, 0.8
                        
                    BoxLayout:
                        id: wall_tabs
                        orientation: 'vertical'
                        MDTabs:
                            id: walltabs
                            tab_display_mode: 'text'            
            
                            MDTabsBase:
                                id: wall_inputs
                                name: 'Wall Set-Out Properties'
                                text: "Wall Set-Out Properties"                                        
            
                            MDTabsBase:
                                id: reo_inputs
                                name: 'Reinforcement Properties'
                                text: 'Reinforcement Properties'
                                
                            MDTabsBase:
                                id: design_loads
                                name: 'Design Loads'
                                text: 'Design Loads'
                                
                            MDTabsBase:
                                id: design_loads
                                name: 'Calculations & Design Summary'
                                text: 'Calculations & Design Summary'
                FloatLayout:
                    BoxLayout:
                        orientation: "vertical"
                        spacing: "18dp"
                        padding: "8dp"
                        MDLabel: 
                            text: "R.C Wall Properties"
                            pos_hint: {'center_x': 0.5, 'center_y': 0.8}
                            color: 0.2, 0.255, 0.292, 0.9
                        MDLabel: 
                            text: "Wall Height"
                            pos_hint: {'center_x': .5, 'center_y': .8}
                            color: 0.2, 0.255, 0.292, 0.9
                        MDLabel: 
                            text: "Wall Length"
                            pos_hint: {'center_x': .5, 'center_y': .8}
                            color: 0.2, 0.255, 0.292, 0.9
                        MDLabel: 
                            text: "Wall Thickness"
                            pos_hint: {'center_x': .5, 'center_y': .8}
                            color: 0.2, 0.255, 0.292, 0.9
                        MDLabel: 
                            text: "Effective Height Factor"
                            pos_hint: {'center_x': .5, 'center_y': .8}
                            color: 0.2, 0.255, 0.292, 0.9
                        MDLabel: 
                            text: "Concrete Strength"
                            pos_hint: {'center_x': .5, 'center_y': .8}
                            color: 0.2, 0.255, 0.292, 0.9
                        MDLabel: 
                            text: "Concrete Density"
                            pos_hint: {'center_x': .5, 'center_y': .8}
                            color: 0.2, 0.255, 0.292, 0.9
                        MDLabel: 
                            text: "Is wall braced or unbraced?"
                            pos_hint: {'center_x': .5, 'center_y': .8}
                            color: 0.2, 0.255, 0.292, 0.9
                        MDLabel: 
                            text: "Wall Structure Over:"
                            pos_hint: {'center_x': .5, 'center_y': .8}
                            color: 0.2, 0.255, 0.292, 0.9
                    
                    BoxLayout:
                        
                        orientation: "vertical"
                        MDTextField:
                            hint_text: "(mm)"
                            halign: 'center'
                            size_hint_x:None
                            width: 300
                            pos_hint: {'center_x': 0.5, 'center_y': 0.8}
                            line_color_normal: 0.2, 0.255, 0.292, 0.9
                            
                        MDTextField:
                            hint_text: "(mm)"
                            halign: 'center'
                            size_hint_x:None
                            width: 300
                            pos_hint: {'center_x': .5, 'center_y': .8}
                            line_color_normal: 0.2, 0.255, 0.292, 0.9
                            
                        MDTextField:
                            hint_text: "(mm)"
                            size_hint_x:None
                            halign: 'center'
                            width: 300
                            pos_hint: {'center_x': .5, 'center_y': .8}
                            line_color_normal: 0.2, 0.255, 0.292, 0.9
                        
                        
            Screen:           
                name: "screen3"
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        id: home
                        title: 'R.C Pad Footing Design - Concentrically Loaded Footing'
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                        specific_text_color: 0.9, 0.9, 0.9, 0.8
                    MDLabel: 
                        text: "Screen 3"
                        halign: 'center'
                        halign: 'center'
                        color: 0.2, 0.255, 0.292, 0.9
            
            Screen:           
                name: "screen4"
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        id: home
                        title: 'R.C Slab Design - Simplified Method in Accordance with AS3600:2018'
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                        specific_text_color: 0.9, 0.9, 0.9, 0.9
                    MDLabel: 
                        text: "Screen 4"
                        halign: 'center'
                        halign: 'center'
                        color: 0.2, 0.255, 0.292, 0.9

        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '12dp'
                padding: '20dp'
                
                MDFloatingActionButton:
                    icon: "home"
                    md_bg_color: 0.9, 0.9, .9, 0.9
                    theme_text_color: "Custom"
                    text_color: 0.9, 0.9, .9, 0.9
                    spacing:'20dp'
                    padding:'20dp'
                    font_size: "10sp"
                    text_color: 0.2, 0.255, 0.292, 0.9
                    on_release: screen_manager.current = "screen1"
                    on_release: nav_drawer.toggle_nav_drawer() 
                    elevation_normal: 12
                    pos_hint: {"center_x": .15, "center_y": .5}

                ScrollView:
                    MDList: 
                        MDLabel:
                            text: 'Design Packages:'
                            font_style: 'Subtitle2'
                            size_hint_y: None
                            height: self.texture_size[1]
                            color: 0.2, 0.255, 0.292, 0.9
                            
                        MDFlatButton:
                            text: 'R.C Wall Design                                 '
                            text_color: 0.2, 0.255, 0.292, 0.9
                            spacing:'12dp'
                            padding:'12dp'
                            on_release: screen_manager.current = "screen2"
                            on_release: nav_drawer.toggle_nav_drawer()
                            
                           
                            
                        MDFlatButton:
                            text: 'R.C Pad Footing Design                         '
                            spacing:'12dp'
                            padding:'12dp'
                            text_color: 0.2, 0.255, 0.292, 0.9
                            on_release: screen_manager.current = "screen3"
                            on_release: nav_drawer.toggle_nav_drawer()
                           
                            
                        MDFlatButton:
                            text: 'R.C Slab Design                                '
                            spacing:'12dp'
                            padding:'12dp'
                            text_color: 0.2, 0.255, 0.292, 0.9
                            on_release: screen_manager.current = "screen4"
                            on_release: nav_drawer.toggle_nav_drawer()
 



"""

