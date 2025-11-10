from frame import draw_frame
import nazca as nd
from device_v2_for_matrix import draw_device
import numpy as np






def n_contacts_and_bondpads(length_n_contact = 300,
        width_n_contact = 200,
        distance_semi_and_metal = 5,
        ditance_sio_and_semi  =5,
        n_meta_layer = 1,
        sem_etc_layer = 2,
        sio_open_layer = 3,
                n_bondpad_length = 300,
        n_bondpad_width = 80,

        n_bondpad_box_length = 80,
        n_bondpad_box_width = 80):
    with nd.Cell(name = "n_contact_and_bondpads") as n_contact_and_bondpads_cell:


        n_metal = nd.strt(length=length_n_contact,
                        width=width_n_contact,
                        layer =n_meta_layer).put(0,0)
        
        semi_etch = nd.strt(length=length_n_contact-distance_semi_and_metal*2,
                            width=width_n_contact-distance_semi_and_metal*2,
                            layer =sem_etc_layer).put((distance_semi_and_metal),0)
        
        sio_opening = nd.strt(length=length_n_contact-distance_semi_and_metal*2-ditance_sio_and_semi*2,
                            width=width_n_contact-distance_semi_and_metal*2-ditance_sio_and_semi*2,
                            layer =sio_open_layer).put(distance_semi_and_metal+ditance_sio_and_semi,0)
        
        
        n_bondpad_connection = nd.strt(length =n_bondpad_length, width = n_bondpad_width,layer=n_meta_layer).put("a0", n_metal.pin["b0"])
        n_bondpad_box = nd.strt(length =n_bondpad_box_length, 
                                width = n_bondpad_box_width,
                                layer=n_meta_layer).put("a0", n_bondpad_connection.pin["b0"])
        
        
    return n_contact_and_bondpads_cell


array_size = 1
for i in range(0,array_size):
    for j in range(0,array_size):
        with nd.Cell(name = "Block For matrix") as block_matrix:
            
            # === LAYERS ===
            layer_etch =222 # not in use
            layer_metallization =333 #not in use

            active_regrowth_area_layer = 1 # in sue but obsolete
            isolation_regions_layer = 2 
            metal_layer_rings = 3 # p metal ring layer
            bondpads_metal_layer = 4 # p metal layer bondpads
            sio_opening_layer = 5 # opeing for the rings
            n_meta_layer = 6
            n_sem_etc_layer = 7
            sio_open_layer = 8
            frame_layer = 9
            fill_factor_layer = 10



            # ==== No Layer control below ====



            frame_length = 263-40 +36.5-47-9.696+10-6.811-51.133-42.004+20
            frame_width  = 263-40 +36.5-47-9.696+10-6.811+20+2*7.003-50
            dicing_area = 5
            draw_frame(frame_length, frame_width, dicing_area,frame_layer).put(-4.56+36.5/2+13.5/2-31+17.44+5-4.848-1.6,-15.25-9.5/2)
            with nd.Cell("device with n contacts") as device_with_n_contacts:

                radius = 38
                width = 80
                distance_from_mesa  = 55

                custom_angle1_metal = 40
                custom_angle2_metal = custom_angle1_metal
                custom_angle1_etch_semicond = custom_angle1_metal
                custom_angle2_etch_semicond = custom_angle2_metal
                custom_angle1_sio_etch = custom_angle1_metal
                custom_angle2_sio_etch = custom_angle2_metal

                width_etch_semicond = 75
                width_etch_sio = 70
                layer_etch_sio = 33





                isolation_width = 5

                bondpad_lenght = 70-31.988-15.007808-15 #this one changes the lenfth of the bodpad
                trapezoid_height = 0
                trapezoid_side1 = 50
                trapezoid_side2 = 20

                


                # width_etch_semicond = 70
                # layer_etch =2
                active_area_radius = 250
                ring_width_metallization = 15

                distance_from_edge = 7  # fixed spelling
                angle = 80
                # length_bondpad_p_metal = 100+360.25
                width_bond_pad = 25
                metal_sio_opening = 10
                rotation_angle = 0

                p_metal_position = radius - distance_from_edge - 1.2 * ring_width_metallization

                double_s_bend_length = 2*((radius)*np.sin(np.pi*custom_angle1_metal/180))
                length_bondpad_p_metal = double_s_bend_length + bondpad_lenght-p_metal_position

                # length_bondpad_p_metal = 100+360.25

                p_box_angle = 0

                            
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
                p_metal_position, active_regrowth_area_layer, isolation_regions_layer, isolation_width, p_box_angle).put(0,0,0)


                width = 50
                width_etch_semicond = 75
                width_etch_sio = 70
                

                x_n_metal = 90
                y_n_metal = 75

                length_n_contact = 57.7
                width_n_contact = width_bond_pad
                distance_semi_and_metal = 5
                ditance_sio_and_semi  =5

                n_bondpad_length = 5
                n_bondpad_width = width_n_contact

                n_bondpad_box_length = 50
                n_bondpad_box_width = 50
                n_bondpad_dist_from_mid  = 85-31.5+6.5
                n_contacts_and_bondpads(length_n_contact,
        width_n_contact,
        distance_semi_and_metal,
        ditance_sio_and_semi,
        n_meta_layer,
        n_sem_etc_layer ,
        sio_open_layer ,
                n_bondpad_length ,
        n_bondpad_width ,
        n_bondpad_box_length,
        n_bondpad_box_width).put(-126/2-41.22+73.17,-n_bondpad_dist_from_mid)
                n_contacts_and_bondpads(length_n_contact,
        width_n_contact,
        distance_semi_and_metal,
        ditance_sio_and_semi,
        n_meta_layer,
        n_sem_etc_layer ,
        sio_open_layer ,
                n_bondpad_length ,
        n_bondpad_width ,
        n_bondpad_box_length,
        n_bondpad_box_width).put(-126/2-41.22+73.17,n_bondpad_dist_from_mid)

            device_with_n_contacts.put(-20,-20)

        block_matrix.put(i*(frame_length+dicing_area),j*(frame_width+dicing_area))
        real_radius = 15 #radius -ring_width_metallization-7
        APD_area = np.power(real_radius,2)*np.pi
        frame_length= 132
        frame_width = 189.99
        tile_area = frame_length*frame_width
        ratio_areas = APD_area/tile_area*100
        nd.text("Fill Factor: {:.2f}%, for the radius of {}".format(ratio_areas,real_radius), height=500,layer = fill_factor_layer).put(+200+787+100,frame_length)
nd.export_gds(filename="test_array_v3.gds")





