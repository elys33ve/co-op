
from dash import Dash, html, dcc, Input, Output
from gpio_functions import *



############################################    ---     CONSTANTS
ON = 'dh'
OFF = 'dl'

INPUT = 'ip'
OUTPUT = 'op'

### webserver
PORT = 8000
HOST = '127.0.0.1'              # dash defult

app = Dash(__name__)
############################################    ---     DISPLAY FORMATTING
l_vert = 150    # left up/down
r_vert = 150    # right up/down
center_vert = (l_vert + r_vert)/2   # center up/down
l_hori = 180    # left right/left
r_hori = 400    # right right/left
center_hori = (l_hori + r_hori)/2   # center right/left
inout_offset = 30                   # keep checkboxes symmetrical
onoff_offset = inout_offset*2

# pin state display formatting
font_size = 13
line_space = 6.95
letter_space = '-0.5px'
stv = -150
sth = -400

############################################    ---     VARIABLES
# list of pins to initially checkmark
l_onpins = pin_auto_set()[0]    # on / off
l_oo = filter_gpio(l_onpins)
############################################    ---     WEBSERVER

### WEBSERVER
app.layout = html.Div([                     # show stuff on webserver
    html.H2("RPI 4 GPIO stuff"),        # header
    html.Br(), html.Br(), html.Br(),

#------ headers
    html.Div(       
        html.H3('pinout'),style={
            'top':center_vert-100, 'left':center_hori+90, 
            'position':'absolute', 'textAlign':'center'}
        ),

    html.Div(                       # left on/off
        html.P('on/off'),style={
            'top':center_vert-45, 'left':l_hori+onoff_offset+92, 
            'position':'absolute', 'textAlign':'center',
            #'writing-mode': 'vertical-lr', 'text-orientation': 'upright',
            'letter-spacing': letter_space}
        ),

#------ pinout / pin state display
    html.Div(           # pinout left side (odd numbers)
        left_disp, style={
            'top':l_vert-9, 
            'left':l_hori-20, 
            'position':'absolute', 
            'textAlign':'right', 
            'line-height':4}
            ),

#------ on / off
    html.Div([          # pinout left side (odd dumbers)
        dcc.Checklist(
            options=left_checks, value=l_onpins, inline=False, 
            id='left_onoff_checks', 
            labelStyle = dict(display='block')      # not inline
        ),
        html.Div(id='left_onoff')
    ], style={'top':l_vert, 'left':l_hori+onoff_offset+100, 'position':'absolute', 'textAlign':'right'})
])


### PIN STATE OUTPUTS
def l_state_oo (inp):
    states = pin_state_inp(inp, 'left', 'onoff')
    states_out = html.Div(           # pin state left side (odd numbers) - on/off
    states, style={
        'top':l_vert+stv+7, 
        'left':l_hori+sth+197, 
        'position':'absolute', 
        'textAlign':'right', 
        'line-height':line_space,
        'color': 'red',
        'font-size':font_size}
        )
    return states_out


############################################    ---     CALLBACKS

### CALLBACKS
# on / off
@app.callback(
    Output(component_id='left_onoff', component_property='children'),
    Input(component_id='left_onoff_checks', component_property='value')
)
def left_onoff (input_value):
    for i in range(len(left_gpio)):
        if left_gpio[i] not in NOT_GPIO_PINS:
            g = int(left_gpio[i])
            p = int(l_oo[i])         # previous list
            u = int(filter_gpio(input_value[i]))  # updated list
            if left_gpio[i] in p ^ left_gpio[i] in u:
                print(f"pin {left_gpio[i]} changed")
    #set_lvl(input_value, 'left')                # change lvl
    return l_state_oo(input_value)


############################################    ---     MAIN

if __name__ == "__main__":
    app.run(debug=True, port=PORT, host=HOST)




