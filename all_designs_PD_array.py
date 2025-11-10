

from square_PD_Array_100x100 import pd_array_4x4_device, pd_array_8x8_device,pd_array_2x2_device,pd_array_1x1_device
import square_PD_Array_50x50 as fbf #import pd_array_4x4_device, pd_array_8x8_device,pd_array_2x2_device,pd_array_1x1_device
import square_PD_Array_70x70 as sbs #import pd_array_4x4_device, pd_array_8x8_device,pd_array_2x2_device,pd_array_1x1_device

from circular_PIN_bottom_top_illuminated import fifty_circular_devices_indep_grounds, fifty_circular_devices_common_grounds
import nazca as nd
from design_process_module_Zn_diffusion import dpm_module
from frame import draw_frame_no_pins
import p_layer_ctlm
import n_layer_ctlm
import metal_bars




### Square arrays
pd_array_1x1_device().put(0,0)
pd_array_2x2_device().put(0,1000)
pd_array_4x4_device().put(0,2000)
pd_array_8x8_device().put(0,3000)
nd.text("TNO PITC designs 100x100 active area, used for both bottom and top illumination", height=100,layer = 11).put(0,4000)


sbs_distance_x = 5000
sbs.pd_array_1x1_device().put(sbs_distance_x,0)
sbs.pd_array_2x2_device().put(sbs_distance_x,1000)
sbs.pd_array_4x4_device().put(sbs_distance_x,2000)
sbs.pd_array_8x8_device().put(sbs_distance_x,3000)
nd.text("TNO PITC designs 70x70 active area, used for bottom and if possible for top illumination", height=100,layer = 11).put(sbs_distance_x,4000)



ftf_distance_x = 10000
fbf.pd_array_1x1_device().put(ftf_distance_x,0)
fbf.pd_array_2x2_device().put(ftf_distance_x,1000)
fbf.pd_array_4x4_device().put(ftf_distance_x,2000)
fbf.pd_array_8x8_device().put(ftf_distance_x,3000)
nd.text("TNO PITC designs 50x50 active area, used for bottom illumination", height=100,layer = 11).put(ftf_distance_x,4000)





#### Circular detectors
tota_frame_length  = 555+20
total_frame_width = 4990+20
total_frame_dicing_area = 100
tota_frame_layer = 9
total_frame = draw_frame_no_pins(tota_frame_length, total_frame_width, total_frame_dicing_area,tota_frame_layer).put(4.5-1722-10-total_frame_dicing_area,2370+100+25-50+10-5)
circular_detectors_x_position = -2000
fifty_circular_devices_indep_grounds().put(circular_detectors_x_position,0)
total_frame = draw_frame_no_pins(tota_frame_length, total_frame_width, total_frame_dicing_area,tota_frame_layer).put(4.5-1722-10-total_frame_dicing_area-800,2370+100+25-50+10-5)
fifty_circular_devices_common_grounds().put(circular_detectors_x_position-800,0)
nd.text("Circular detectors for bottom and top illumination, 50um diameter, common and non-common grd", height=100,layer = 11).put(circular_detectors_x_position,5000)



##### Diffusion measureing modules
nd.text("Diffusion control process module", height=100).put(-3000,200-1200)
dpm_module().put(-3000,-1200)




##### CTLMs
nd.text("P and N type CTLMs", height=100).put(+3000,400-1200)

nd.text("P type CTLMs", height=100).put(+3000,200-1200)
p_layer_ctlm.p_metal_ctlm().put(+3000,-1000)

nd.text("N type CTLMs", height=100).put(+3000,-2500)
n_layer_ctlm.n_metal_ctlm().put(0+3000,-2500)





##### Metal Bars
metal_bars.p_metal_bars().put(6000,-3000)

metal_bars.n_metal_bars().put(6000,-5000)


















nd.export_gds(filename="square_PD_array_all_devices.gds")
