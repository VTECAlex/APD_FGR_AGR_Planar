import nazca as nd 
from n_metal_open_v2 import n_metal_ring_process
from p_rings_metal_openings import p_metal_contact_structure
import numpy as np
from device_for_array import draw_device
from frame import draw_frame


def n_contact_custom_trapezoids(layer,px1,px2, py1,py2,px3,py3,bondpad_box_size):
        with nd.Cell(name = "Custom contact") as custom_contact:
                nd.Polygon(layer=layer, points=[(px1,py1), (px2,py2), (px3,py3), (px3, py3+bondpad_box_size)]).put(0,0)
        return custom_contact



def device_complete(radius,angle,custom_angle3,width,bondpad_length,flop, second_sbent_radius):
    with nd.Cell("Device {}".format(radius)) as complete_device:


        frame_length = 158+20
        frame_width  = -300+263-40 +36.5-47-9.696+10-6.811+20+2*7.003+2*165
        dicing_area = 5
        frame_layer = 9
        draw_frame(frame_length, frame_width, dicing_area,frame_layer).put(+36.5/2+13.5/2-31+17.44+5-4.848-1.6+11.313,0)

        n_metal_layer = 2
        px1 = 26.163
        py1 = 50.83700
        px2 = 14.14
        py2 = 62.858
        px3 = 1000
        py3 = 1000
        bondpad_box_size = 0
        n_contact_custom_trapezoids(n_metal_layer,px1,px2, py1,py2,px3,py3,bondpad_box_size)

        px1 = 13.523
        py1 = 40.948
        px2 = 9.699
        py2 = 57.513
        px3 = 50.305
        py3 = 225-150
        px4 = 50.305+50
        py4 = 225-150

        top_n_contact_bent = nd.Polygon(layer=n_metal_layer, points=[(px1,py1), (px2,py2), (px3,py3), (px4, py4)])
        top_n_contact_bent.put(0,0)
        top_n_contact_bent.put(0,0, flop = True)

        n_metal_box_bondpad_1 = nd.strt(layer = n_metal_layer,length = 50,width  = 50).put(100.305-50,100)
        n_metal_box_bondpad_1 = nd.strt(layer = n_metal_layer,length = 50,width  = 50).put(100.305-50,-100)

        #n_metal_box_bondpad_2 = nd.strt(layer = n_metal_layer,length = 50,width  = 50).put(-100.3,-250)



        radius = radius
        width = width
        distance_from_mesa  = 15-11.5

        active_area_regrowth_layer = 1
        fgr_layer = active_area_regrowth_layer


        layer_metallization =2
        layer_etch =3
        layer_etch_sio = 4
        metal_layer_rings = 5
        bondpads_metal_layer = 6
        sio_opening_layer = 7

        isolation_layer = 12
        isolation_width = 5






        custom_angle1_metal = angle
        custom_angle2_metal = custom_angle1_metal
        custom_angle1_etch_semicond = custom_angle1_metal
        custom_angle2_etch_semicond = custom_angle2_metal
        custom_angle1_sio_etch = custom_angle1_metal
        custom_angle2_sio_etch = custom_angle2_metal

        width_etch_semicond = width -5
        width_etch_sio = width - 10

        bondpad_lenght = bondpad_length
        trapezoid_height = 10
        trapezoid_side1 = 50
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
        length_bondpad_p_metal = double_s_bend_length - radius + bondpad_lenght + ring_width_metallization+distance_from_edge + second_s_bend_length +22.277

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
        fgr_thickness,fgr_distance,fgr_layer,flop, custom_angle3,second_sbent_radius , isolation_layer, isolation_width).put(0,0)
    return complete_device



def tile_apd(i,j,q):
    with nd.Cell(name = "Tile {}".format(i,j)) as tile_apd:
        flop = False
        custom_angle3 = 13
        second_sbent_radius = 10
        general_bondpad_length_control = -300+5.2

        with nd.Cell("Tile right side") as tile_right_side:
            angle = 0
            width = 17
            bondpad_length = 300+general_bondpad_length_control
            radius = 250
            distance_inbetween  =700
            device_complete(15,angle,custom_angle3,width,bondpad_length,flop,second_sbent_radius).put(0,0)

        tile_right_side.put(0,0)
    return tile_apd


array_size = 10
for i in range(0,array_size):
    for j in range(0,array_size):
        frame_length = 158+20
        frame_width  = -300+263-40 +36.5-47-9.696+10-6.811+20+2*7.003+2*165
        dicing_area = 5
        tile_apd(1,1,0).put(i*(frame_length+dicing_area),j*(frame_width+dicing_area))
        real_radius = 15
        fill_factor_layer = 1111
        nd.text("Fill Factor: {:.2f}%, for the radius of {}".format((np.pi*np.pow(real_radius,2))/(frame_length*frame_width)*100,real_radius), height=500,layer = fill_factor_layer).put(+200+787+100,frame_length)
        
nd.export_gds(filename="test_PD_Array_V3.gds")
