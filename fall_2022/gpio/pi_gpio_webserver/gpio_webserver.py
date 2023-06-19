# dash documentation & stuff:   https://dash.plotly.com/dash-core-components
# frameworks & web info:    https://www.educative.io/blog/web-development-in-python#frameworks
# dash example (githubl linked):    https://dash.gallery/dash-clustergram/
# dash html.P style references/examples:    https://www.programcreek.com/python/example/100614/dash_html_components.P

# this python script will be run on a raspberry pi 4
# it should be able to run a simple webserver to control
# the states of the pins (on/off, input/output) remotely
    
from dash import Dash, html, dcc, Input, Output
from gpio_functions import *

############################################    ---     CONSTANTS
ON = 'dh'
OFF = 'dl'

INPUT = 'ip'
OUTPUT = 'op'

### webserver
PORT = 8000
if Test == True:
    HOST = '127.0.0.1'              # dash defult
else:
    HOST = 'host ip'

app = Dash(__name__)
############################################    ---     DISPLAY FORMATTING
# titles, pinout, and checkboxes display on page
#   vertical: increase --> move down, decrease --> move up
#   horizontal: increase --> move right, decrease --> move left
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

# message to display stuff
msg_vert = 570
msg_hori = center_vert
out_msg = [
    html.P("changing the lvl (on/off) of an input will change it on the site but not the actual pin"), 
    html.P("changing the input/output might change the pin level but wont display the change"),
    html.Br(), html.P("cmd line:"), html.P("raspi-gpio get <gpio number>    # show lvl and func"), 
    html.P("raspi-gpio set <gpio number> <dl/dh>    # off/on"), 
    html.P("raspi-gpio set <gpio number> <ip/op>    # input/output")
    ]
############################################    ---     VARIABLES
# list of pins to initially checkmark
l_onpins = pin_auto_set()[0]    # on / off
r_onpins = pin_auto_set()[1]

l_inpins = pin_auto_set()[2]    # input / output
r_inpins = pin_auto_set()[3]

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
    html.Div(                       # message
        out_msg,style={
            'top':msg_vert, 'left':msg_hori, 
            'position':'absolute', 'textAlign':'center', 'line-height':line_space}
    ),

    html.Div(                       # left on/off
        html.P('on/off'),style={
            'top':center_vert-45, 'left':l_hori+onoff_offset+92, 
            'position':'absolute', 'textAlign':'center',
            #'writing-mode': 'vertical-lr', 'text-orientation': 'upright',
            'letter-spacing': letter_space}
        ),
    html.Div(                       # right on/off
        html.P('on/off'),style={
            'top':center_vert-45, 'left':r_hori-onoff_offset+112, 
            'position':'absolute', 'textAlign':'center',
            #'writing-mode': 'vertical-lr', 'text-orientation': 'upright',
            'letter-spacing': letter_space}
        ),
    html.Div(                       # left input/output
        html.P('output'),style={
            'top':center_vert-35, 'left':l_hori+inout_offset+70, 
            'position':'absolute', 'textAlign':'center',
            'letter-spacing': letter_space}
    ),
    html.Div(                       # right input/output
        html.P('output'),style={
            'top':center_vert-35, 'left':r_hori-inout_offset+130, 
            'position':'absolute', 'textAlign':'center',
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
    html.Div(           # pinout right side (even numbers)
        right_disp, style={
            'top':r_vert-9, 
            'left':r_hori+175, 
            'position':'absolute', 
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
    ], style={'top':l_vert, 'left':l_hori+onoff_offset+100, 'position':'absolute', 'textAlign':'right'}),

    html.Div([          # pinout right side (even numbers)
        dcc.Checklist(
            options=right_checks, value=r_onpins, inline=False, 
            id='right_onoff_checks',
            labelStyle = dict(display='block')      # not inline
        ),
        html.Div(id='right_onoff')
    ], style={'top':r_vert, 'left':r_hori-onoff_offset+120, 'position':'absolute'}),

#------ input / output
    html.Div([          # pinout left side (odd dumbers)
        dcc.Checklist(
            options=left_checks, value=l_inpins, inline=False, 
            id='left_inout_checks', 
            labelStyle = dict(display='block')      # not inline
        ),
        html.Div(id='left_inout')
    ], style={'top':l_vert, 'left':l_hori+inout_offset+80, 'position':'absolute', 'textAlign':'right'}),

    html.Div([          # pinout right side (even numbers)
        dcc.Checklist(
            options=right_checks, value=r_inpins, inline=False, 
            id='right_inout_checks',
            labelStyle = dict(display='block')      # not inline
        ),
        html.Div(id='right_inout')
    ], style={'top':r_vert, 'left':r_hori-inout_offset+140, 'position':'absolute'})
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
def r_state_oo (inp):
    states = pin_state_inp(inp, 'right', 'onoff')
    states_out = html.Div(           # pin state right side (even numbers) - on/off
    states, style={
        'top':r_vert+stv+33, 
        'left':r_hori+sth+21, 
        'position':'absolute', 
        'line-height':line_space,
        'color': 'red',
        'font-size':font_size}
        )
    return states_out
def l_state_io (inp):
    states = pin_state_inp(inp, 'left', 'inout')
    states_out = html.Div(           # pin state left side (odd numbers) - in/out
    states, style={
        'top':l_vert+stv+7, 
        'left':l_hori+sth+180, 
        'position':'absolute', 
        'textAlign':'right', 
        'line-height':line_space,
        'color': 'red',
        'font-size':font_size}
        )
    return states_out
def r_state_io (inp):
    states = pin_state_inp(inp, 'right', 'inout')
    states_out = html.Div(           # pin state right side (even numbers) - in/out
    states, style={
        'top':r_vert+stv+32, 
        'left':r_hori+sth+20, 
        'position':'absolute', 
        'line-height':line_space,
        'color': 'red',
        'font-size':font_size}
        )
    return states_out

############################################    ---     CALLBACKS

### CALLBACKS
""" 
to optimize, can use dash.callback_context to get which input triggered
the callback (avoid all the shit in the set_func(), set_lvl() functions)
"""
# on / off
@app.callback(
    Output(component_id='left_onoff', component_property='children'),
    Input(component_id='left_onoff_checks', component_property='value')
)
def left_onoff (input_value):
    set_lvl(input_value, 'left')                # change lvl
    return l_state_oo(input_value)

@app.callback(
    Output(component_id='right_onoff', component_property='children'),
    Input(component_id='right_onoff_checks', component_property='value')
)
def right_onoff (input_value):
    set_lvl(input_value, 'right')
    return r_state_oo(input_value)



# input / output
@app.callback(
    Output(component_id='left_inout', component_property='children'),
    Input(component_id='left_inout_checks', component_property='value')
)
def left_inout (input_value):
    set_func(input_value, 'left')               # change func
    return l_state_io(input_value)

@app.callback(
    Output(component_id='right_inout', component_property='children'),
    Input(component_id='right_inout_checks', component_property='value')
)
def right_inout (input_value):
    set_func(input_value, 'right')
    return r_state_io(input_value)


############################################    ---     MAIN

if __name__ == "__main__":
    app.run(debug=True, port=PORT, host=HOST)




