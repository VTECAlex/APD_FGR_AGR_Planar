import nazca as nd 
from n_metal_open_v2 import n_metal_ring_process
from p_rings_metal_openings import p_metal_contact_structure
import numpy as np
from device import draw_device
from frame import draw_frame





def device_complete(radius,angle,custom_angle3,width,bondpad_length,flop, second_sbent_radius):
    with nd.Cell("Device {}".format(radius)) as complete_device:
        radius = radius
        width = width
        distance_from_mesa  = 15

        active_area_regrowth_layer = 1
        fgr_layer = active_area_regrowth_layer


        layer_metallization =2
        layer_etch =3
        layer_etch_sio = 4
        metal_layer_rings = 5
        bondpads_metal_layer = 6
        sio_opening_layer = 7

        isolation_layer = 12
        isolation_width = 30






        custom_angle1_metal = angle
        custom_angle2_metal = custom_angle1_metal
        custom_angle1_etch_semicond = custom_angle1_metal
        custom_angle2_etch_semicond = custom_angle2_metal
        custom_angle1_sio_etch = custom_angle1_metal
        custom_angle2_sio_etch = custom_angle2_metal

        width_etch_semicond = width -5
        width_etch_sio = width - 10

        bondpad_lenght = bondpad_length
        trapezoid_height = 80
        trapezoid_side1 = 80
        trapezoid_side2 = width



        active_area_radius = radius
        ring_width_metallization = 15
        distance_from_edge = 0  # fixed spelling
        angle = 80
        # length_bondpad_p_metal = 100+360.25
        width_bond_pad = 80
        metal_sio_opening = 10
        rotation_angle = 0
        active_area_radius = active_area_radius+ring_width_metallization
        p_metal_position = active_area_radius# - distance_from_edge - 1.2 * ring_width_metallization
        radius  = radius +ring_width_metallization
        double_s_bend_length = 2*((radius+distance_from_mesa+ring_width_metallization)*np.sin(np.pi*custom_angle1_metal/180))
        second_s_bend_length = 2*((second_sbent_radius+distance_from_mesa+ring_width_metallization)*np.sin(np.pi*custom_angle3/180))
        length_bondpad_p_metal = double_s_bend_length - radius + bondpad_lenght + ring_width_metallization+distance_from_edge + second_s_bend_length

        # length_bondpad_p_metal = 100+360.25

        fgr_thickness = 2
        fgr_distance = 1

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
        fgr_thickness,fgr_distance,fgr_layer,flop, custom_angle3,second_sbent_radius , isolation_layer, isolation_width).put()
    return complete_device



def tile_apd(i,j,q):
    with nd.Cell(name = "Tile {}".format(i,j)) as tile_apd:
        flop = False
        custom_angle3 = 30
        second_sbent_radius = 80
        general_bondpad_length_control = -300

        with nd.Cell("Tile right side") as tile_right_side:
            angle = 53
            width = 50
            bondpad_length = 300+general_bondpad_length_control
            radius = 250
            distance_inbetween  =700
            device_complete(250,angle,custom_angle3,width,bondpad_length,flop,second_sbent_radius).put(0,0)
            bondpad_length = 23.5615 + 64.278+300+general_bondpad_length_control
            angle = 51.46

            device_complete(200,angle,custom_angle3,width,bondpad_length,flop,second_sbent_radius).put(0,distance_inbetween)
            bondpad_length = 48.30+128.558+300+general_bondpad_length_control
            angle = 49

            device_complete(150,angle,custom_angle3,width,bondpad_length,flop,second_sbent_radius).put(0,2*distance_inbetween)
            bondpad_length = 73.32+192.8375+300+general_bondpad_length_control
            angle = 45

            device_complete(100,angle,custom_angle3,width,bondpad_length,flop,second_sbent_radius).put(0,3*distance_inbetween)
            angle = 30
            bondpad_length = 49.69+218.50193+300+35.744+general_bondpad_length_control
            angle = 42

            device_complete(80,angle,custom_angle3,width,bondpad_length,flop,second_sbent_radius).put(0,4*distance_inbetween)
            # device_complete(250,angle,width,bondpad_length).put(0,5*850)
        tile_right_side.put(0,0)


        flop = True
        with nd.Cell("Tile left side") as tile_left_side:
            angle = 40
            width = 50
            bondpad_length = 300+general_bondpad_length_control
            # radius = 50
            distance_inbetween  =700
            bondpad_length = +300+362.215+general_bondpad_length_control
            angle = 35
            device_complete(50,angle,custom_angle3,width,bondpad_length,flop,second_sbent_radius).put(0,0)
            bondpad_length = 23.5615+300+359.225+general_bondpad_length_control
            angle = 31.3
            device_complete(40,angle,custom_angle3,width,bondpad_length,flop,second_sbent_radius).put(0,distance_inbetween)
            bondpad_length =48.30+300+357.61+general_bondpad_length_control
            angle = 25.8
            device_complete(30,angle,custom_angle3,width,bondpad_length,flop,second_sbent_radius).put(0,2*distance_inbetween)
            bondpad_length = 73.32+300+362.283+general_bondpad_length_control
            angle = 15.9
            device_complete(20,angle,custom_angle3,width,bondpad_length,flop,second_sbent_radius).put(0,3*distance_inbetween)
            bondpad_length = +49.69+300+391.393-66.44+26.35+23.904+general_bondpad_length_control
            width  = 30
            custom_angle3_r10 = 35
            device_complete(10,angle,custom_angle3_r10,width,bondpad_length,flop,second_sbent_radius).put(0,4*distance_inbetween)
            # device_complete(250,angle,width,bondpad_length).put(0,5*850)
        tile_left_side.put(-600,0,flop= flop)

        frame = draw_frame(frame_layer=8, dicing_area=50, length=2082.438+100, width=3439.77+100+420).put(-250-50,1350+50-210.18)
        name = nd.text("R{}C{}Q{}".format(i,j,q),height=400,layer=6).put(-(1391.219+608.781)/2,-449.885-270.18-100)
    return tile_apd

tile_apd(1,1,0).put()
        
nd.export_gds(filename="test.gds")
