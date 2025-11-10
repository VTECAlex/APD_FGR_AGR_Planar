import nazca as nd 
from n_metal_open_v2 import n_metal_ring_process
from p_rings_metal_openings import p_metal_contact_structure
import numpy as np
from device_for_array import draw_device
from frame import draw_frame, draw_frame_no_pins



def one_device():
    with nd.Cell(name = "One Device") as one_device_for_array:

        frame_length = 50
        frame_width = 50
        dicing_area = 2
        frame_layer = 8

        sio_cover_for_regrowth = draw_frame_no_pins(frame_length, frame_width, dicing_area,frame_layer).put(0,0)

        #P-metal layer Ti/Pt/Au, layer number 2
        p_contact_length = 30
        p_contact_width  = 50
        p_contact_layer  = 2
        p_metal_contact = nd.strt(length = p_contact_length, width = p_contact_width, layer = p_contact_layer).put(-p_contact_length/2-5-5,0)

        #P-metal layer, extra Ti/Pt/Au, layer number 22
        p_contact_length = 30
        p_contact_width  = 50
        p_contact_layer  = 22
        p_metal_contact = nd.strt(length = p_contact_length, width = p_contact_width, layer = p_contact_layer).put(-p_contact_length/2-5-5,0)



        p_contact__sio_opening_length = p_contact_length-5
        p_contact__sio_opening_width  = p_contact_width-5
        p_contact__sio_opening_layer = 3
        p_metal_contact = nd.strt(length = p_contact__sio_opening_length, width = p_contact__sio_opening_width, layer = p_contact__sio_opening_layer).put(-p_contact__sio_opening_length/2-5-5,0)



        n_contact_length  = 34.5-10-2
        n_contact_width  = p_contact_width
        n_contact_layer = 4
        distance_p_n_contacts  =2-0.5
        only_metal_contact_move_for_n = -9+2.5-1.5-3-1
        n_contact = nd.strt(length = n_contact_length, width = n_contact_width, layer = n_contact_layer).put(+frame_length/2+distance_p_n_contacts-3+only_metal_contact_move_for_n,0)
        n_contact_layer = 22
        n_contact = nd.strt(length = n_contact_length, width = n_contact_width, layer = n_contact_layer).put(+frame_length/2+distance_p_n_contacts-3+only_metal_contact_move_for_n,0)

        n_contact_semi_etch_length  = 7
        n_contact_semi_etch_width  = p_contact_width-5+2
        n_contact__semi_etch_layer = 6
        semi_etch_distance = 20-10+1.5-3
        n_contact = nd.strt(length = n_contact_semi_etch_length, width = n_contact_semi_etch_width, layer = n_contact__semi_etch_layer).put(+frame_length/2+distance_p_n_contacts+semi_etch_distance-9+1,0)

        n_contact_sio_bot_etch_length  = 5
        n_contact_sio_bot_etch_width  = p_contact_width-10+2.5+0.5+2
        n_contact_sio_bot_etch_layer = 7
        semi_etch_distance = 20.75-10+1.5+0.25-3
        n_contact = nd.strt(length = n_contact_sio_bot_etch_length, width = n_contact_sio_bot_etch_width, layer = n_contact_sio_bot_etch_layer).put(-0.25+frame_length/2+distance_p_n_contacts+semi_etch_distance-9+1.25/2-0.125-0.25+1,0)




        tota_frame_length = 75.5-1-14.5-1
        total_frame_width = 50
        total_frame_dicing_area = 5
        tota_frame_layer = 8
        total_frame = draw_frame_no_pins(tota_frame_length, total_frame_width, total_frame_dicing_area,tota_frame_layer).put(5-0.5,0)



        isolation_length = 94.5-14-2.5-1-14.5-1
        isolation_width = 52.5
        isolation_dicing_area = 2.5
        isolation_layer = 9
        isolation_region = draw_frame_no_pins(isolation_length, isolation_width, isolation_dicing_area,isolation_layer).put(5-0.5,0)

    return one_device_for_array




tota_frame_length = 89.5-14-5-1-11.5-3-1
print("total frame length {}".format(tota_frame_length))
total_frame_width = 50-5
total_frame_dicing_area = 10
array_x = 8
array_y = 8
for i in range(array_x):
    for j in range(array_y):
        one_device().put(i*(tota_frame_length+total_frame_dicing_area),j*(total_frame_width+total_frame_dicing_area))





x_array_dimension = total_frame_width*array_y
y_array_dimension = tota_frame_length*array_x
print(x_array_dimension)
print(y_array_dimension)



active_area = 50*50

frame_length = 64
frame_width = 55
fill_factor = (active_area/(frame_length*frame_width))*100
print(fill_factor)
layer_text = 11
fill_factor_letters = nd.text("fill factor {}%".format(fill_factor), height=300,layer=layer_text).put(0,100)




nd.export_gds(filename="square_PD_array_V2.gds")
