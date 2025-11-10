import nazca as nd 
from n_metal_open_v2 import n_metal_ring_process
from p_rings_metal_openings import p_metal_contact_structure
import numpy as np
from device_for_array import draw_device
from frame import draw_frame, draw_frame_no_pins
import nazca.geometries as geom



def one_device():
    with nd.Cell(name = "One Device") as one_device_for_array:

        frame_length = 100
        frame_width = 100
        dicing_area = 2
        frame_layer = 8

        sio_cover_for_regrowth = draw_frame_no_pins(frame_length, frame_width, dicing_area,frame_layer).put(0,0)

        #P-metal layer Ti/Pt/Au, layer number 2
        p_contact_length = 10
        p_contact_width  = frame_width
        p_contact_layer  = 2
        p_metal_contact = nd.strt(length = p_contact_length, width = p_contact_width+40, layer = p_contact_layer).put(-50,-20)

        #P-metal layer, extra Ti/Pt/Au, layer number 22
        p_contact_length = 10
        p_contact_width  = frame_width
        p_contact_layer  = 22
        p_metal_contact = nd.strt(length = p_contact_length, width = p_contact_width+40, layer = p_contact_layer).put(-50,-20)



        p_contact__sio_opening_length = 5
        p_contact__sio_opening_width  = frame_width-5
        p_contact__sio_opening_layer = 3
        p_metal_contact = nd.strt(length = p_contact__sio_opening_length, width = p_contact__sio_opening_width, layer = p_contact__sio_opening_layer).put(-22.5-25,0)


        n_contact_position = 25
        n_contact_length  = 22.5-14.5
        n_contact_width  = p_contact_width
        n_contact_layer = 4
        distance_p_n_contacts  = 1.5
        only_metal_contact_move_for_n = -12.0
        n_contact = nd.strt(length = n_contact_length, width = n_contact_width+40, layer = n_contact_layer).put(11.5 + n_contact_position+15,20)
        n_contact_layer = 22
        n_contact = nd.strt(length = n_contact_length, width = n_contact_width+40, layer = n_contact_layer).put(11.5 + n_contact_position+15,20)

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

        bondpad_p_contact = nd.strt(length=50, width = 50, layer = 2).put(-40-30,-80)
        bondpad_p_contact = nd.strt(length=50, width = 50, layer = 22).put(-40-30,-80)



        bondpad_n_contact = nd.strt(length=50, width = 50, layer = 2).put(-40-30+71.5+30,-80+160)
        bondpad_n_contact = nd.strt(length=50, width = 50, layer = 22).put(-40-30+71.5+30,-80+160)




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
                one_device().put(i*(64.0),j*(55.0))





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
        tota_frame_length = 100+4
        print("total frame length {}".format(tota_frame_length))
        total_frame_width = 45
        total_frame_dicing_area = 10
        array_x = 2
        array_y = array_x
        for i in range(array_x):
            for j in range(array_y):
                one_device().put(i*(222-108),j*(222-117))





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

    return pd_2x2


def pd_array_4x4_device():
    with nd.Cell(name = "The 4 by 4 device") as pd_4x4:
        tota_frame_length = 100+4
        print("total frame length {}".format(tota_frame_length))
        total_frame_width = 45
        total_frame_dicing_area = 10
        array_x = 2
        array_y = array_x
        for i in range(array_x):
            for j in range(array_y):
                one_device().put(i*(222-108),j*(222-117))





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
        fill_factor_letters = nd.text("ff {:.2f}%".format(83.5), height=300,layer=layer_text).put(0,100)

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
                one_device().put(i*(222-108),j*(222-117))





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
        fill_factor_letters = nd.text("ff {:.2f}%".format(fill_factor), height=300,layer=layer_text).put(880,100)

    return pd_8x8


def new_placement_8x8():
    with nd.Cell("New configuration") as new_8x8:
        for i in range(8):
        # pd_array_1x1_device().put(0,0)
            pd_array_1x1_device().put(40*i,-115*i)

    return new_8x8




# pd_array_1x1_device().put(0,0)
# new_placement_8x8().put(0,0)
# new_placement_8x8().put(124+17.5,50-5+55)
for i in range(8):
    new_placement_8x8().put((124+17.5)*i,(50-5+55)*i)

sun = nd.Polygon(layer=36, points=geom.circle(radius=500,N=700)).put(700,0)

active_area = 100*100*34
beam_area = np.pi*pow(500,2)
nd.export_gds(filename="square_PD_array_for_VTEC.gds")
print(active_area/beam_area)
