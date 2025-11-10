
import nazca as nd 
from n_metal_open_v2 import *
from p_rings_metal_openings import p_metal_contact_structure_matrix
import numpy as np








# radius = 250
# width = 80
# distance_from_mesa  = 90

# layer_metallization =8
# custom_angle1_metal = 22
# custom_angle2_metal = 22
# custom_angle1_etch_semicond = custom_angle1_metal
# custom_angle2_etch_semicond = custom_angle2_metal
# custom_angle1_sio_etch = custom_angle1_metal
# custom_angle2_sio_etch = custom_angle2_metal

# bondpad_lenght = 500
# trapezoide_height = 200
# trapezoide_side1 = 200
# trapezoide_side2 = 80

# width_etch_semicond = 70
# layer_etch =2


# width_etch_sio = 60
# layer_etch_sio = 3

# n_metal_ring_process(
#     radius,
#     width,
#     distance_from_mesa,
#     layer_metallization,
#     custom_angle1_metal,
#     custom_angle2_metal,
#     bondpad_lenght,
#     trapezoide_height,
#     trapezoide_side1,
#     trapezoide_side2,
#     width_etch_semicond,
#     layer_etch,
#     custom_angle1_etch_semicond,
#     custom_angle2_etch_semicond,
#     width_etch_sio,
#     layer_etch_sio,
#     custom_angle1_sio_etch,
#     custom_angle2_sio_etch).put(0,0,180)



# active_area_radius = 250
# ring_width_metallization = 15
# metal_layer_rings = 3
# bondpads_metal_layer = 4
# distance_from_edge = 5  # fixed spelling
# angle = 80
# length_bondpad_p_metal = 600 #200+546.553
# width_bond_pad = 80
# metal_sio_opening = 10
# sio_opening_layer = 5
# rotation_angle = 0

# p_metal_contact_structure(
#     active_area_radius,
#     ring_width_metallization,
#     metal_layer_rings,
#     bondpads_metal_layer,
#     distance_from_edge,
#     length_bondpad_p_metal,
#     width_bond_pad,
#     metal_sio_opening,
#     sio_opening_layer,
#     rotation_angle,
#     trapezoide_height,
#     trapezoide_side1,
#     trapezoide_side2,
#     ).put(0,0)






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
    p_metal_position, active_regrowth_area_layer, isolation_regions_layer, isolation_width, p_box_angle
):
    with nd.Cell(name = "Device") as device:
    #     n_metal_boxes_process(
    # radius,
    # width,
    # distance_from_mesa,
    # layer_metallization,
    # custom_angle1_metal,
    # custom_angle2_metal,
    # bondpad_lenght,
    # trapezoid_height,
    # trapezoid_side1,
    # trapezoid_side2,
    # width_etch_semicond,
    # layer_etch,
    # custom_angle1_etch_semicond,
    # custom_angle2_etch_semicond,
    # width_etch_sio,
    # layer_etch_sio,
    # custom_angle1_sio_etch,
    # custom_angle2_sio_etch).put(0,0,180)

        p_metal_contact_structure_matrix(
        active_area_radius=radius,
        ring_width_metallization=ring_width_metallization,
        metal_layer_rings=metal_layer_rings,
        bondpads_metal_layer=bondpads_metal_layer,
        distance_from_edge=distance_from_edge,
        length_bondpad_p_metal=length_bondpad_p_metal,
        width_bond_pad=width_bond_pad,
        metal_sio_opening=metal_sio_opening,
        sio_opening_layer=sio_opening_layer,
        rotation_angle=rotation_angle,
        trapezoid_height=trapezoid_height,
        trapezoid_side1=trapezoid_side1,
        trapezoid_side2=trapezoid_side2,
        p_metal_position = p_metal_position,     
        active_regrowth_area_layer = active_regrowth_area_layer,
          isolation_regions_layer = isolation_regions_layer,
          isolation_width = isolation_width,
          p_box_angle = p_box_angle
    ).put(0,0)
        # Calculate the position of the right pin
        double_s_bend_length = 2*((radius)*np.sin(np.pi*custom_angle1_metal/180))
        trapezoid_bond_pad_size = trapezoid_height+trapezoid_side1
        x_position_of_device_right_pin = double_s_bend_length+trapezoid_bond_pad_size+bondpad_lenght
        nd.Pin("Device_Right_Side_Pin").put(x_position_of_device_right_pin,0)
        x_position_of_device_left_pin = radius+distance_from_mesa+width/2
        nd.Pin("Device_Left_Side_Pin").put(-x_position_of_device_left_pin,0)
        # device_name = nd.text("R{}".format(radius),height= 200, layer= metal_layer_rings).put(radius,x_position_of_device_left_pin)
        # nd.Pin("Device_Bottom_Pin").put((x_position_of_device_right_pin+x_position_of_device_left_pin)/2-x_position_of_device_left_pin,-x_position_of_device_left_pin)
        height_of_text = 160
        # nd.Pin("Device_Bottom_Pin").put((x_position_of_device_right_pin+x_position_of_device_left_pin)/2-x_position_of_device_left_pin,+x_position_of_device_left_pin+height_of_text)

        nd.put_stub()

    
    return device


if __name__ == "__main__":
    radius = 250
    width = 80
    distance_from_mesa  = 90

    layer_metallization =8
    active_regrowth_area_layer = 11
    isolation_regions_layer = 12
    isolation_width  = 30
    p_box_anlge = 0


    custom_angle1_metal = 40
    custom_angle2_metal = custom_angle1_metal
    custom_angle1_etch_semicond = custom_angle1_metal
    custom_angle2_etch_semicond = custom_angle2_metal
    custom_angle1_sio_etch = custom_angle1_metal
    custom_angle2_sio_etch = custom_angle2_metal

    width_etch_semicond = 70
    layer_etch =2
    width_etch_sio = 60
    layer_etch_sio = 3

    bondpad_lenght = 500
    trapezoid_height = 200
    trapezoid_side1 = 200
    trapezoid_side2 = 80

    

    width_etch_semicond = 70
    layer_etch =2
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

    p_metal_position = active_area_radius - distance_from_edge - 1.2 * ring_width_metallization

    double_s_bend_length = 2*((radius)*np.sin(np.pi*custom_angle1_metal/180))
    length_bondpad_p_metal = double_s_bend_length + bondpad_lenght-p_metal_position

    # length_bondpad_p_metal = 100+360.25



    
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
        active_regrowth_area_layer, isolation_regions_layer, isolation_width, p_box_anlge
).put()
    nd.export_gds(filename="test.gds")

