import nazca as nd 
from n_metal_open_v2 import n_metal_ring_process
from p_rings_metal_openings import p_metal_contact_structure
import numpy as np
from device_for_array import draw_device
from frame import draw_frame, draw_frame_no_pins





p_metal_layer = 2
p_metal_layer_opening = 3
n_metal_etch_semi_layer = 6
n_metal_deposition_layer = 4
n_metal_opening_bottom_sio_layer = 7
EPI_1_islands_layer  = 8
isolation_between_devices = 9
extra_TPA_metal_layer = 22
text_description_layer  = 11
dicing_lane_layer = 17

def one_device():
    with nd.Cell(name = "One Device") as one_device_for_array:

        frame_length = 70
        frame_width = 70
        dicing_area = 2
        frame_layer = 8

        sio_cover_for_regrowth = draw_frame_no_pins(frame_length, frame_width, dicing_area,frame_layer).put(0,0)

        #P-metal layer Ti/Pt/Au, layer number 2
        p_contact_length = 30
        p_contact_width  = frame_width
        p_contact_layer  = 2
        p_metal_contact = nd.strt(length = p_contact_length, width = p_contact_width, layer = p_contact_layer).put(-35,0)

        #P-metal layer, extra Ti/Pt/Au, layer number 22
        p_contact_length = 30
        p_contact_width  = frame_width
        p_contact_layer  = 22
        p_metal_contact = nd.strt(length = p_contact_length, width = p_contact_width, layer = p_contact_layer).put(-35,0)



        p_contact__sio_opening_length = 25
        p_contact__sio_opening_width  = frame_width-5
        p_contact__sio_opening_layer = 3
        p_metal_contact = nd.strt(length = p_contact__sio_opening_length, width = p_contact__sio_opening_width, layer = p_contact__sio_opening_layer).put(-22.5-35+25,0)


        n_contact_position = 10
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


        p_metal_contact = nd.strt(length = n_contact_semi_etch_length, width = frame_width, layer = EPI_1_islands_layer).put(27.0 +  n_contact_position,0)


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





def pd_array_1x1_device():
    with nd.Cell(name = "The 1 by 1 device") as pd_1x1:
        tota_frame_length = 100+4
        print("total frame length {}".format(tota_frame_length))
        total_frame_width = 45
        total_frame_dicing_area = 10
        array_x = 1
        array_y = array_x
        for i in range(array_x):
            for j in range(array_y):
                one_device().put(i*(84),j*(75.0))





        x_array_dimension = total_frame_width*array_y
        y_array_dimension = tota_frame_length*array_x
        print(x_array_dimension)
        print(y_array_dimension)



        active_area = 100*100

        frame_length = 114
        frame_width = 105
        fill_factor = (active_area/(frame_length*frame_width))*100
        print(fill_factor)
        layer_text = 11
        # fill_factor_letters = nd.text("ff {:.2f}%".format(fill_factor), height=300,layer=layer_text).put(0,100)

    return pd_1x1

def pd_array_2x2_device():
    with nd.Cell(name = "The 2 by 2 device") as pd_2x2:
        tota_frame_length = 69
        print("total frame length {}".format(tota_frame_length))
        total_frame_width = 45
        total_frame_dicing_area = 10
        array_x = 2
        array_y = array_x
        for i in range(array_x):
            for j in range(array_y):
                one_device().put(i*(84),j*(75.0))





        x_array_dimension = total_frame_width*array_y
        y_array_dimension = tota_frame_length*array_x
        print(x_array_dimension)
        print(y_array_dimension)



        active_area = 100*100

        frame_length = 114
        frame_width = 105
        fill_factor = (active_area/(frame_length*frame_width))*100
        print(fill_factor)
        layer_text = 11
        # fill_factor_letters = nd.text("ff {:.2f}%".format(fill_factor), height=300,layer=layer_text).put(0,100)
        dicing_lane_device = draw_frame_no_pins(length = 917-456-228-45-15, width = 845-420-210-45-15, dicing_area= 100, frame_layer=dicing_lane_layer).put(303.5+100-228-14-100-15,-15-105-210+100+267.5)


    return pd_2x2


def pd_array_4x4_device():
    with nd.Cell(name = "The 4 by 4 device") as pd_4x4:
        tota_frame_length = 100+4
        print("total frame length {}".format(tota_frame_length))
        total_frame_width = 45
        total_frame_dicing_area = 10
        array_x = 4
        array_y = array_x
        for i in range(array_x):
            for j in range(array_y):
                one_device().put(i*(84),j*(75.0))




        x_array_dimension = total_frame_width*array_y
        y_array_dimension = tota_frame_length*array_x
        print(x_array_dimension)
        print(y_array_dimension)



        active_area = 100*100

        frame_length = 114
        frame_width = 105
        fill_factor = (active_area/(frame_length*frame_width))*100
        print(fill_factor)
        layer_text = 11
        # fill_factor_letters = nd.text("ff {:.2f}%".format(fill_factor), height=300,layer=layer_text).put(0,100)
        dicing_lane_device = draw_frame_no_pins(length = 917-456-105-15, width =-105-15+ 845-420, dicing_area= 100, frame_layer=dicing_lane_layer).put(303.5+100-228-45,-45-210+100+267.5)


    return pd_4x4






def pd_array_8x8_device():
    with nd.Cell(name = "The 4 by 4 device") as pd_8x8:
        tota_frame_length = 100+4
        print("total frame length {}".format(tota_frame_length))
        total_frame_width = 45
        total_frame_dicing_area = 10
        array_x = 8
        array_y = array_x
        for i in range(array_x):
            for j in range(array_y):
                one_device().put(i*(84),j*(75.0))





        x_array_dimension = total_frame_width*array_y
        y_array_dimension = tota_frame_length*array_x
        print(x_array_dimension)
        print(y_array_dimension)



        active_area = 100*100

        frame_length = 114
        frame_width = 105
        fill_factor = (active_area/(frame_length*frame_width))*100
        print(fill_factor)
        layer_text = 11
        fill_factor_letters = nd.text("ff {:.2f}%".format(80.2), height=300,layer=layer_text).put(880,100)
        dicing_lane_device = draw_frame_no_pins(length = 917-15-225, width = 845-15-225, dicing_area= 100, frame_layer=dicing_lane_layer).put(-105+303.5+100,-105+100+267.5)


    return pd_8x8


pd_array_1x1_device().put(0,0)
pd_array_2x2_device().put(-400,0)
pd_array_4x4_device().put(-1500,0)
pd_array_8x8_device().put(-3000,0)

# pd_array_1x1_device().put(0,0)


nd.export_gds(filename="square_PD_array_70x70.gds")
