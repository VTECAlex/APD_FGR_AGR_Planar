import nazca as nd
import math
import nazca.geometries as geom








def create_half_ring(radius, width, distance_from_mesa, layer):

    with nd.Cell(name = "Ring metallization") as Ring_metallization_n:
        #The first piece by default will have a radius 180 degrees
        default_angle = 180
        real_radius_of_the_ring = radius+distance_from_mesa # The radius of the ring is calculated again with the addition of the distnace from the mesa structure
        internal_radius = real_radius_of_the_ring - width/2

        print("The real readius of the ring is {}".format(real_radius_of_the_ring))
        main_starting_piece = nd.bend(radius=real_radius_of_the_ring, width = width, angle = default_angle, layer = layer).put(0,-internal_radius-width/2)#,-width/2-radius)
        nd.Pin("Bottom Half-ring pin").put(0,-width/2-internal_radius)
        nd.Pin("Top Half-ring pin").put(0,width/2 +internal_radius)

        print("Default angle for the main piece {}".format(default_angle))
    return Ring_metallization_n


def create_sbend(radius, width, custom_angle1,custom_angle2,layer):
    with nd.Cell(name="Custome s bend") as custom_bend:

        sbend1 = nd.bend(radius = radius, width = width, angle = custom_angle1, layer = layer).put()
        sbend1 = nd.bend(radius = radius, width = width, angle = -custom_angle2,  layer = layer).put()
        nd.Pin(name = "Pin_out_sbend").put()
    return custom_bend

def create_trapezoide(height, side1, side2,layer):
    with nd.Cell(name='Trapezoid Connection Electrodes Pads') as trapezoide:
        pipes = nd.Polygon(layer=layer, points=[(0, side1 / 2), (0, -side1 / 2),
                                                           (height, -side2 / 2 ),
                                                           (height, side2 / 2 )])
        pipes.put(0, 0)
        nd.Pin(name="Pin_Connection_Electrodes_Pads_right_side").put(height, 0)
        nd.Pin(name="Pin_Connection_Electrodes_Pads_left_side").put(0, 0)


    return trapezoide



def create_metal_layer_n_contact(radius, 
                        width, 
                        distance_from_mesa, 
                        layer_metallization,
                        custom_angle1,
                        custom_angle2,
                        bondpad_lenght,
                        trapezoide_height, 
                        trapezoide_side1, 
                        trapezoide_side2):
    half_ring = create_half_ring(radius, width, distance_from_mesa, layer_metallization).put(0,0)
    sbend_bot = create_sbend(radius, width,
                             custom_angle1,
                             custom_angle2,
                             layer_metallization).put("a0", half_ring.pin["Bottom Half-ring pin"], flop=True)
    bondpad_extension = nd.strt(length = bondpad_lenght, width  = width, layer = layer_metallization).put(sbend_bot.pin["Pin_out_sbend"])
    trapezoide = create_trapezoide(trapezoide_height, trapezoide_side1, trapezoide_side2,layer =layer_metallization).put("Pin_Connection_Electrodes_Pads_right_side",
                                                                                                            bondpad_extension.pin["b0"])
    square_pad = nd.strt(length = trapezoide_side1, width= trapezoide_side1, layer=layer_metallization ).put("b0",trapezoide.pin["Pin_Connection_Electrodes_Pads_left_side"],flop=True)
    
    sbend_top = create_sbend(radius, width, 
                            custom_angle1,
                            custom_angle2,
                            layer_metallization).put("b0", half_ring.pin["Top Half-ring pin"])
    bondpad_extension = nd.strt(length = bondpad_lenght, width  = width, layer = layer_metallization).put(sbend_top.pin["Pin_out_sbend"])
    trapezoide = create_trapezoide(trapezoide_height, trapezoide_side1, trapezoide_side2,layer =layer_metallization).put("Pin_Connection_Electrodes_Pads_right_side",
                                                                                                            bondpad_extension.pin["b0"])
    square_pad = nd.strt(length = trapezoide_side1, width= trapezoide_side1, layer=layer_metallization ).put("b0",trapezoide.pin["Pin_Connection_Electrodes_Pads_left_side"],flop=True)
    

def create_etch_layer(radius, 
                        width, 
                        distance_from_mesa, 
                        layer,
                        custom_angle1,
                        custom_angle2):
    half_ring = create_half_ring(radius, width, distance_from_mesa, layer).put(0,0)
    create_sbend(radius, width,
                             custom_angle1,
                             custom_angle2,
                             layer).put("a0", half_ring.pin["Bottom Half-ring pin"], flop=True)
    create_sbend(radius, width, 
                            custom_angle1,
                            custom_angle2,
                            layer).put("b0", half_ring.pin["Top Half-ring pin"])

def create_etch_sio_layer(radius, 
                        width, 
                        distance_from_mesa, 
                        layer,
                        custom_angle1,
                        custom_angle2):
    half_ring = create_half_ring(radius, width, distance_from_mesa, layer).put(0,0)
    create_sbend(radius, width,
                             custom_angle1,
                             custom_angle2,
                             layer).put("a0", half_ring.pin["Bottom Half-ring pin"], flop=True)
    create_sbend(radius, width, 
                            custom_angle1,
                            custom_angle2,
                            layer).put("b0", half_ring.pin["Top Half-ring pin"])


def n_metal_ring_process(
    radius,
    width,
    distance_from_mesa,
    layer_metallization,
    custom_angle1_metal,
    custom_angle2_metal,
    bondpad_lenght,
    trapezoide_height,
    trapezoide_side1,
    trapezoide_side2,
    width_etch_semicond,
    layer_etch,
    custom_angle1_etch_semicond,
    custom_angle2_etch_semicond,
    width_etch_sio,
    layer_etch_sio,
    custom_angle1_sio_etch,
    custom_angle2_sio_etch
):
    # radius = 250
    # width = 80
    # distance_from_mesa  = 30

    # layer_metallization =8
    # custom_angle1_metal = 45
    # custom_angle2_metal = 45
    # bondpad_lenght = 500
    # trapezoide_height = 200
    # trapezoide_side1 = 200
    # trapezoide_side2 = 80

    # width_etch_semicond = 70
    # layer_etch =2
    # custom_angle1_etch_semicond = 45
    # custom_angle2_etch_semicond = 10

    # width_etch_sio = 60
    # layer_etch_sio = 3
    # custom_angle1_sio_etch = 45
    # custom_angle2_sio_etch = 7
    with nd.Cell("N metal process") as N_metal_process:
        create_metal_layer_n_contact(radius, 
                            width, 
                            distance_from_mesa, 
                            layer_metallization,
                            custom_angle1_metal,
                            custom_angle2_metal,
                            bondpad_lenght,
                            trapezoide_height, 
                            trapezoide_side1, 
                            trapezoide_side2)
        

        create_etch_layer(radius, 
                            width_etch_semicond, 
                            distance_from_mesa, 
                            layer_etch,
                            custom_angle1_etch_semicond,
                            custom_angle2_etch_semicond)

        create_etch_sio_layer(radius, 
                        width_etch_sio, 
                        distance_from_mesa, 
                        layer_etch_sio,
                        custom_angle1_sio_etch,
                        custom_angle2_sio_etch)
    return N_metal_process




if __name__ == "__main__":
    radius = 250
    width = 80
    distance_from_mesa  = 30

    layer_metallization =8
    custom_angle1 = 45
    custom_angle2 = 45
    bondpad_lenght = 500
    rapezoide_height = 200
    trapezoide_side1 = 200
    trapezoide_side2 = 80
    create_metal_layer_n_contact(radius, 
                        width, 
                        distance_from_mesa, 
                        layer_metallization,
                        custom_angle1,
                        custom_angle2,
                        bondpad_lenght,
                        rapezoide_height, 
                        trapezoide_side1, 
                        trapezoide_side2)
    
    width_etch = 70
    layer_etch =2
    custom_angle1 = 45
    custom_angle2 = 10
    create_etch_layer(radius, 
                        width_etch, 
                        distance_from_mesa, 
                        layer_etch,
                        custom_angle1,
                        custom_angle2)
    

    width_etch = 60
    layer_etch_sio = 3
    custom_angle1 = 45
    custom_angle2 = 7
    create_etch_sio_layer(radius, 
                    width_etch, 
                    distance_from_mesa, 
                    layer_etch,
                    custom_angle1,
                    custom_angle2)


    center1 = nd.strt(length = 1000, width = 0.001, layer=1).put(0,0)
    center2 = nd.strt(length = 0.001, width = 1000, layer=1).put(0,0)
    nd.export_gds(filename="test.gds")
