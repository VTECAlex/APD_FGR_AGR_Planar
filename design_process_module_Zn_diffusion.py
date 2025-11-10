import nazca as nd
from frame import draw_frame_dcm_module, draw_frame_new_for_module, draw_frame_no_pins







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





def dpm_single_module():
    with nd.Cell("Right side") as right_side:
        length  = 302.5
        width = 155
        frame_layer = 8
        draw_frame_new_for_module(length = length, width = width, dicing_area= 20, frame_layer=frame_layer).put()

        isolation_layer = draw_frame_new_for_module(length = length+15,
                                                     width = width+15,
                                                     dicing_area= 5,
                                                     frame_layer=isolation_between_devices).put()
        sio_metal_opening = nd.strt(length = 50, width  = 50, layer=p_metal_layer_opening).put(length/2-50-10,0)



        p_metal_deposition = nd.strt(length = length-5, width  = 70, layer=p_metal_layer).put(length/2-50-10-240,0)
        p_metal_deposition = nd.strt(length = length-5, width  = 70, layer=extra_TPA_metal_layer).put(length/2-50-10-240,0)


        p_metal_deposition = nd.strt(length = 150, width  = 150, layer=p_metal_layer).put(length/2-50-10-240,0)
        p_metal_deposition = nd.strt(length = 150, width  = 150, layer=extra_TPA_metal_layer).put(length/2-50-10-240,0)


    return right_side

def dpm_module():
    with nd.Cell("All devices") as dpm_module:
        step_size_horizontal_distance = 0.050
        veritcal_distance = 300
        total_num_modules = 16
        for i in range(total_num_modules):
            left_side = dpm_single_module().put(0,-veritcal_distance*i)

            connection_between = nd.strt(length = i*step_size_horizontal_distance,
                                          width = 195,
                                            layer=EPI_1_islands_layer).put(151.25-i*step_size_horizontal_distance/2,-veritcal_distance*i)

            right_side = dpm_single_module().put(302.5,-veritcal_distance*i, flop=True)
            nd.text("Distance {:.2f}um".format(step_size_horizontal_distance*i), layer= p_metal_layer, height=75).put(-160,-veritcal_distance*i+100)
        dicing_lane_device = draw_frame_no_pins(length = 645+20, width = 4772.5+20, dicing_area= 100, frame_layer=dicing_lane_layer).put(151.25,-2211.25)
    return dpm_module



dpm_module().put()
# dpm_single_module().put()
nd.export_gds(filename="dcm_module.gds")

isolation = nd.strt()











