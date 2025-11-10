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




def n_metal_ctlm():
    with nd.Cell("P metal CTLM") as p_metal_ctlm:
        etch_semi = nd.strt(length =880, width = 880, layer=n_metal_etch_semi_layer).put(139-1-10,-566.5-1.5)
        open_sio_bottom_n_metal  = nd.strt(length =860, width = 860, layer=n_metal_opening_bottom_sio_layer).put(139-1,-566.5-1.5)
        # nd.strt(length =860, width = 860, layer=p_metal_layer_opening).put(139-1,-566.5-1.5)


        CTLMs.CTLM(n_metal_deposition_layer).put(0,0)
        # frame.draw_frame_no_pins(length=860,width=860, dicing_area=50, frame_layer=EPI_1_islands_layer).put(568,-568)

    return p_metal_ctlm

n_metal_ctlm().put()
nd.export_gds(filename='n_ctlm.gds')