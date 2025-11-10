import nazca as nd 
from n_metal_open_v2 import n_metal_ring_process
from p_rings_metal_openings import p_metal_contact_structure
import numpy as np
from device_for_array import draw_device
from frame import draw_frame, draw_frame_no_pins



def one_device():
    with nd.Cell(name = "One Device") as one_device_for_array:

        frame_length = 100
        frame_width = 100
        dicing_area = 2
        frame_layer = 8

        sio_cover_for_regrowth = draw_frame_no_pins(frame_length, frame_width, dicing_area,frame_layer).put(0,0)

        #P-metal layer Ti/Pt/Au, layer number 2
        p_contact_length = 30
        p_contact_width  = frame_width
        p_contact_layer  = 2
        p_metal_contact = nd.strt(length = p_contact_length, width = p_contact_width, layer = p_contact_layer).put(-50,0)

        #P-metal layer, extra Ti/Pt/Au, layer number 22
        p_contact_length = 30
        p_contact_width  = frame_width
        p_contact_layer  = 22
        p_metal_contact = nd.strt(length = p_contact_length, width = p_contact_width, layer = p_contact_layer).put(-50,0)



        p_contact__sio_opening_length = 25
        p_contact__sio_opening_width  = frame_width-5
        p_contact__sio_opening_layer = 3
        p_metal_contact = nd.strt(length = p_contact__sio_opening_length, width = p_contact__sio_opening_width, layer = p_contact__sio_opening_layer).put(-22.5-25,0)


        n_contact_position = 25
        n_contact_length  = 22.5
        n_contact_width  = p_contact_width
        n_contact_layer = 4
        distance_p_n_contacts  = 1.5
        only_metal_contact_move_for_n = -12.0
        n_contact = nd.strt(length = n_contact_length, width = n_contact_width, layer = n_contact_layer).put(11.5 + n_contact_position,0)
        n_contact_layer = 22
        n_contact = nd.strt(length = n_contact_length, width = n_contact_width, layer = n_contact_layer).put(11.5 + n_contact_position,0)

        n_contact_semi_etch_length  = 7
        n_contact_semi_etch_width  = frame_width-3
        n_contact__semi_etch_layer = 6
        semi_etch_distance = 8.5
        n_contact = nd.strt(length = n_contact_semi_etch_length, width = n_contact_semi_etch_width, layer = n_contact__semi_etch_layer).put(27.0 +  n_contact_position,0)

        n_contact_sio_bot_etch_length  = 5
        n_contact_sio_bot_etch_width  = frame_width-5
        n_contact_sio_bot_etch_layer = 7
        semi_etch_distance = 9.5
        n_contact = nd.strt(length = n_contact_sio_bot_etch_length, width = n_contact_sio_bot_etch_width, layer = n_contact_sio_bot_etch_layer).put(28.0 + n_contact_position,0)




        tota_frame_length = frame_width+9
        total_frame_width = frame_width
        total_frame_dicing_area = 5
        tota_frame_layer = 8
        total_frame = draw_frame_no_pins(tota_frame_length, total_frame_width, total_frame_dicing_area,tota_frame_layer).put(4.5,0)



        isolation_length = frame_width+11.5
        isolation_width = frame_width+2.5
        isolation_dicing_area = 2.5
        isolation_layer = 9
        isolation_region = draw_frame_no_pins(isolation_length, isolation_width, isolation_dicing_area,isolation_layer).put(4.5,0)

    return one_device_for_array




tota_frame_length = 100+4
print("total frame length {}".format(tota_frame_length))
total_frame_width = 45
total_frame_dicing_area = 10
array_x = 1
array_y = array_x
for i in range(array_x):
    for j in range(array_y):
        one_device().put(i*(64.0),j*(55.0))





x_array_dimension = total_frame_width*array_y
y_array_dimension = tota_frame_length*array_x
print(x_array_dimension)
print(y_array_dimension)



active_area = 100*100

frame_length = 114
frame_width = 102.5
fill_factor = (active_area/(frame_length*frame_width))*100
print(fill_factor)
layer_text = 11
fill_factor_letters = nd.text("fill factor {}%".format(fill_factor), height=300,layer=layer_text).put(0,100)




nd.export_gds(filename="square_PD_array_V4.gds")
