import nazca as nd
import CTLMs
import frame



p_metal_layer = 2
p_metal_layer_opening = 3
n_metal_etch_semi_layer = 6
n_metal_deposition_layer = 4
n_metal_opening_bottom_sio_layer = 7
EPI_1_islands_layer  = 8
isolation_between_devices = 9
extra_TPA_metal_layer = 22
text_description_layer  = 11




def p_metal_ctlm():
    with nd.Cell("P metal CTLM") as p_metal_ctlm:
        nd.strt(length =860, width = 860, layer=p_metal_layer_opening).put(139-1,-566.5-1.5)
        CTLMs.CTLM(p_metal_layer).put(0,0)
        frame.draw_frame_no_pins(length=860,width=860, dicing_area=50, frame_layer=EPI_1_islands_layer).put(568,-568)

    return p_metal_ctlm

p_metal_ctlm().put()
nd.export_gds(filename='p_ctlm.gds')