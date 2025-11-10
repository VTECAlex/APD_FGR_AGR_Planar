
import nazca as nd 
from n_metal_open_v2 import n_metal_ring_process
from p_rings_metal_openings import p_metal_contact_structure








radius = 250
width = 80
distance_from_mesa  = 90

layer_metallization =8
custom_angle1_metal = 22
custom_angle2_metal = 22
custom_angle1_etch_semicond = custom_angle1_metal
custom_angle2_etch_semicond = custom_angle2_metal
custom_angle1_sio_etch = custom_angle1_metal
custom_angle2_sio_etch = custom_angle2_metal

bondpad_lenght = 500
trapezoide_height = 200
trapezoide_side1 = 200
trapezoide_side2 = 80

width_etch_semicond = 70
layer_etch =2


width_etch_sio = 60
layer_etch_sio = 3

n_metal_ring_process(
    radius,
    width,
    distance_from_mesa,
    layer_metallization,
    custom_angle1_metal,
    custom_angle2_metal,
    bondpad_lenght,
    trapezoide_height,
    trapezoide_side1,
    trapezoide_side2,
    width_etch_semicond,
    layer_etch,
    custom_angle1_etch_semicond,
    custom_angle2_etch_semicond,
    width_etch_sio,
    layer_etch_sio,
    custom_angle1_sio_etch,
    custom_angle2_sio_etch).put(0,0,180)



active_area_radius = 250
ring_width_metallization = 15
metal_layer_rings = 3
bondpads_metal_layer = 4
distance_from_edge = 5  # fixed spelling
angle = 80
length_bondpad = 200
width_bond_pad = 80

p_metal_contact_structure(
    active_area_radius=250,
    ring_width_metallization=15,
    metal_layer_rings=3,
    bondpads_metal_layer=4,
    distance_from_edge=5,
    length_bondpad=200+546.553,
    width_bond_pad=80,
    metal_sio_opening=10,
    sio_opening_layer=5,
    rotation_angle=0
    ).put(0,0)

nd.export_gds(filename="test.gds")
