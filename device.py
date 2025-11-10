
import nazca as nd 
from n_metal_open_v2 import n_metal_ring_process
from p_rings_metal_openings import p_metal_contact_structure
import numpy as np






def draw_device(radius,
            width,
            distance_from_mesa,
            layer_metallization,
            custom_angle1_metal,
            custom_angle2_metal,
            bondpad_lenght,
            trapezoid_height,
            trapezoid_side1,
            trapezoid_side2,
            width_etch_semicond,
            layer_etch,
            custom_angle1_etch_semicond,
            custom_angle2_etch_semicond,
            width_etch_sio,
            layer_etch_sio,
            custom_angle1_sio_etch,
            custom_angle2_sio_etch,
            active_area_radius,
    ring_width_metallization,
    metal_layer_rings,
    bondpads_metal_layer,
    distance_from_edge,
    length_bondpad_p_metal,
    width_bond_pad,
    metal_sio_opening,
    sio_opening_layer,
    rotation_angle,
    p_metal_position,
    active_area_regrowth_layer,fgr_thickness,fgr_distance,fgr_layer,flop,custom_angle3,second_sbent_radius, isolation_layer, isolation_width):
    with nd.Cell(name = "Device") as device:
        n_metal_ring_process(
    radius,
    width,
    distance_from_mesa,
    layer_metallization,
    custom_angle1_metal,
    custom_angle2_metal,
    bondpad_lenght,
    trapezoid_height,
    trapezoid_side1,
    trapezoid_side2,
    width_etch_semicond,
    layer_etch,
    custom_angle1_etch_semicond,
    custom_angle2_etch_semicond,
    width_etch_sio,
    layer_etch_sio,
    custom_angle1_sio_etch,
    custom_angle2_sio_etch,custom_angle3,second_sbent_radius).put(0,0,180)

        p_metal_contact_structure(
        active_area_radius=radius,
        ring_width_metallization=ring_width_metallization,
        metal_layer_rings=metal_layer_rings,
        bondpads_metal_layer=bondpads_metal_layer,
        distance_from_edge=distance_from_edge,
        length_bondpad_p_metal=length_bondpad_p_metal,
        width_bond_pad=width,
        metal_sio_opening=metal_sio_opening,
        sio_opening_layer=sio_opening_layer,
        rotation_angle=rotation_angle,
        trapezoid_height=trapezoid_height,
        trapezoid_side1=trapezoid_side1,
        trapezoid_side2=trapezoid_side2,
        p_metal_position = p_metal_position,
        active_area_regrowth_layer=active_area_regrowth_layer,
        fgr_thickness = fgr_thickness,
        fgr_distance=fgr_distance,
        fgr_layer=fgr_layer , 
        isolation_layer= isolation_layer, 
        isolation_width = isolation_width
    ).put(0,0)
        # Calculate the position of the right pin
        double_s_bend_length = 2*((radius)*np.sin(np.pi*custom_angle1_metal/180))
        trapezoid_bond_pad_size = trapezoid_height+trapezoid_side1
        x_position_of_device_right_pin = double_s_bend_length+trapezoid_bond_pad_size+bondpad_lenght
        nd.Pin("Device_Right_Side_Pin").put(x_position_of_device_right_pin,0)
        x_position_of_device_left_pin = radius+distance_from_mesa+width/2
        nd.Pin("Device_Left_Side_Pin").put(-x_position_of_device_left_pin,0)
        if flop:
            x_correction = -380
            y_correction = 100
        else:
            x_correction = 0
            y_correction = 0
        device_name = nd.text("R{}".format(radius-ring_width_metallization),height= 200, layer= metal_layer_rings).put(radius - x_correction,y_correction+x_position_of_device_left_pin-50, flop=flop)
        nd.Pin("Device_Bottom_Pin").put((x_position_of_device_right_pin+x_position_of_device_left_pin)/2-x_position_of_device_left_pin,-x_position_of_device_left_pin)
        height_of_text = 160
        nd.Pin("Device_Top_Pin").put((x_position_of_device_right_pin+x_position_of_device_left_pin)/2-x_position_of_device_left_pin,+x_position_of_device_left_pin+height_of_text)

        nd.put_stub()

    
    return device


if __name__ == "__main__":
    radius = 250
    width = 50
    distance_from_mesa  = 15

    layer_metallization =8
    custom_angle1_metal = 40
    custom_angle2_metal = custom_angle1_metal
    custom_angle1_etch_semicond = custom_angle1_metal
    custom_angle2_etch_semicond = custom_angle2_metal
    custom_angle1_sio_etch = custom_angle1_metal
    custom_angle2_sio_etch = custom_angle2_metal

    width_etch_semicond = width -5
    layer_etch =2
    width_etch_sio = width - 10
    layer_etch_sio = 3

    isolation_layer = 12
    isolation_width = 30

    bondpad_lenght = 300
    trapezoid_height = 80
    trapezoid_side1 = 80
    trapezoid_side2 = width
    flop = False
    
    custom_angle3 = custom_angle1_metal
    active_area_radius = 250
    ring_width_metallization = 15
    metal_layer_rings = 3
    bondpads_metal_layer = 4
    distance_from_edge = 0  # fixed spelling
    angle = 80
    # length_bondpad_p_metal = 100+360.25
    width_bond_pad = 80
    metal_sio_opening = 10
    sio_opening_layer = 5
    rotation_angle = 0
    active_area_radius = active_area_radius+ring_width_metallization
    p_metal_position = active_area_radius# - distance_from_edge - 1.2 * ring_width_metallization
    radius  = radius +ring_width_metallization
    double_s_bend_length = 2*((radius+distance_from_mesa+ring_width_metallization)*np.sin(np.pi*custom_angle1_metal/180))
    second_s_bend_length = 2*((radius+distance_from_mesa+ring_width_metallization)*np.sin(np.pi*custom_angle3/180))
    length_bondpad_p_metal = double_s_bend_length - radius + bondpad_lenght + ring_width_metallization+distance_from_edge + second_s_bend_length
    # length_bondpad_p_metal = 100+360.25

    active_area_regrowth_layer = 123
    fgr_thickness = 2
    fgr_distance = 1
    fgr_layer = active_area_regrowth_layer

    distance_from_mesa = distance_from_mesa+ring_width_metallization
    draw_device(
            radius,
            width,
            distance_from_mesa,
            layer_metallization,
            custom_angle1_metal,
            custom_angle2_metal,
            bondpad_lenght,
            trapezoid_height,
            trapezoid_side1,
            trapezoid_side2,
            width_etch_semicond,
            layer_etch,
            custom_angle1_etch_semicond,
            custom_angle2_etch_semicond,
            width_etch_sio,
            layer_etch_sio,
            custom_angle1_sio_etch,
            custom_angle2_sio_etch,
            radius,
    ring_width_metallization,
    metal_layer_rings,
    bondpads_metal_layer,
    distance_from_edge,
    length_bondpad_p_metal,
    width_bond_pad,
    metal_sio_opening,
    sio_opening_layer,
    rotation_angle,
    p_metal_position,
    active_area_regrowth_layer,
    fgr_thickness,fgr_distance,fgr_layer,flop, custom_angle3, isolation_layer, isolation_width).put()
    nd.export_gds(filename="test.gds")

