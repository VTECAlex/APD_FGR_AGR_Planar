from frame import draw_frame
import nazca as nd
from device_v2_for_matrix import draw_device
import numpy as np

array_size = 10
for i in range(0,array_size):
    for j in range(0,array_size):
        with nd.Cell(name = "Block For matrix") as block_matrix:


            frame_length = 263-40
            frame_width  = frame_length
            dicing_area = 5
            frame_layer = 19
            draw_frame(frame_length, frame_width, dicing_area,frame_layer).put(0,0)
            with nd.Cell("device with n contacts") as device_with_n_contacts:
                radius = 70
                width = 80
                distance_from_mesa  = 55

                layer_metallization =8
                custom_angle1_metal = 40
                custom_angle2_metal = custom_angle1_metal
                custom_angle1_etch_semicond = custom_angle1_metal
                custom_angle2_etch_semicond = custom_angle2_metal
                custom_angle1_sio_etch = custom_angle1_metal
                custom_angle2_sio_etch = custom_angle2_metal

                width_etch_semicond = 75
                layer_etch =2
                width_etch_sio = 70
                layer_etch_sio = 33
                active_regrowth_area_layer = 11
                isolation_regions_layer = 12 
                isolation_width = 30

                bondpad_lenght = 70 #this one changes the lenfth of the bodpad
                trapezoid_height = 0
                trapezoid_side1 = 80
                trapezoid_side2 = 20

                

                # width_etch_semicond = 70
                # layer_etch =2
                active_area_radius = 250
                ring_width_metallization = 15
                metal_layer_rings = 3
                bondpads_metal_layer = 4
                distance_from_edge = 7  # fixed spelling
                angle = 80
                # length_bondpad_p_metal = 100+360.25
                width_bond_pad = 20
                metal_sio_opening = 10
                sio_opening_layer = 5
                rotation_angle = 0

                p_metal_position = radius - distance_from_edge - 1.2 * ring_width_metallization

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
                p_metal_position, active_regrowth_area_layer, isolation_regions_layer, isolation_width).put(-20-1.6-5,-20-1.6-5,45)


                width = 80
                width_etch_semicond = 75
                width_etch_sio = 70
                

                x_n_metal = 90
                y_n_metal = 75
                with nd.Cell("N metal process") as N_metal_process:
                    with nd.Cell("Top box contaxt") as Bot_box_contact:
                        south_contact_metal = nd.strt(length =width, 
                                                width=width,
                                                layer = layer_metallization).put(-width/2,0)
                        
                        south_contact_etc_semi = nd.strt(length =width_etch_semicond, 
                                        width=width_etch_semicond,
                                        layer = layer_etch).put(-width_etch_semicond/2,0)
                        
                        south_contact_etc_sio = nd.strt(length =width_etch_sio, 
                                width=width_etch_sio,
                                layer = layer_etch_sio).put(-width_etch_sio/2,0)
                    Bot_box_contact.put(x_n_metal-3.4,-y_n_metal+60.2,0)
                    with nd.Cell("Top box contaxt") as Top_box_contact:
                        south_contact_metal = nd.strt(length =width, 
                                                width=width,
                                                layer = layer_metallization).put(-width/2,0)
                        
                        south_contact_etc_semi = nd.strt(length =width_etch_semicond, 
                                        width=width_etch_semicond,
                                        layer = layer_etch).put(-width_etch_semicond/2,0)
                        
                        south_contact_etc_sio = nd.strt(length =width_etch_sio, 
                                width=width_etch_sio,
                                layer = layer_etch_sio).put(-width_etch_sio/2,0)
                    Bot_box_contact.put(-x_n_metal+75,y_n_metal+11.5,0)
                N_metal_process.put(0,0)
            device_with_n_contacts.put(-20,-20)

        block_matrix.put(i*(frame_length+dicing_area),j*(frame_length+dicing_area))
nd.export_gds(filename="test_array_changes.gds")





