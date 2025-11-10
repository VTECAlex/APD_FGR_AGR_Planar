
from nazca import *



bond_pad_straight = nd.strt(
    length=30,
    width=20,
    layer=3
).put(0,0)

side2 = 80
bondpads_metal_layer =2
with nd.Cell("bondpad_p") as bondpad_p:
    with nd.Cell("the box") as the_box:
        p_bondpad = nd.strt(length = side2, width = side2, layer= bondpads_metal_layer).put(-side2/2,0)
    the_box.put(0,0,45)
    nd.Pin("Center_bonpad_p").put(0,0)
bondpad_p.put("Center_bonpad_p",bond_pad_straight.pin["b0"])
nd.export_gds()