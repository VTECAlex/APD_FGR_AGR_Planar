import nazca as nd
from math import *
import nazca.geometries as geom




def Ground_Open_and_Metal(Au_plating_layer, N_metal_opening_layer,N_metalization_layer, etch_ground_down_opening_layer, radius, width, length, angle,bond_pad_size, trapezoid_height,APD_RF_length,RF_True,  sbent_angle, sbent_radius):

    #These coordinates have to make sure that the center of the design is th circle of the apd
    # rotational_angle =0# -90-angle/2#-angle/2
    # x_move = 0
    # y_move = 0

    rotation_angle = 0 # (180-angle)/2+90
    rot_ang_rads = (2*pi*rotation_angle)/360
    # x_move  = (radius+width/2)*sin(rot_ang_rads)
    # y_move  = -(radius-width/2)*cos(rot_ang_rads)
    x_move  = 0 #(radius+sqrt(width/2))*sin((2*pi*angle/360)/2)
    y_move  = -width/2 -radius #(radius-sqrt(width/2))*cos((2*pi*angle/360)/2)
    with nd.Cell(name  = "RF metal rings") as Rf_metal_rings:
        if RF_True:
    #with nd.Cell(name="Rf Metal Rings Up") as Rf_metal_rings_up:
            #this is a test design to check the aligment
            test_circle = nd.Polygon(layer=333, 
                                        points=geom.ring(radius=radius, 
                                                         width= width, 
                                                         N=1000)).put(0,0)
            N_contact_ring_top = nd.bend(angle=angle, radius=radius, width=width, offset=0,layer=Au_plating_layer).put(x_move, y_move, rotation_angle)
            bend_rf_top = nd.bend(radius=radius, width=width, angle=-(angle - 90) - (180 - angle) / 2,layer=Au_plating_layer).put(N_contact_ring_top.pin["a0"], flip=True)
            nd.strt(length=APD_RF_length, width=width,layer=Au_plating_layer).put()
            bend_after_strt = nd.bend(angle=sbent_angle, radius=sbent_radius, width=width, offset=0,layer=Au_plating_layer).put()
            nd.bend(angle=sbent_angle, radius=sbent_radius, width=width, offset=0,layer=Au_plating_layer).put(bend_after_strt.pin["b0"], flip=True)
            trapezoid_connection = Trapezoid_Electric_Pads(trapezoid_height, width, bond_pad_size,layer=Au_plating_layer).put()
            nd.strt(length=bond_pad_size, width=bond_pad_size, layer=Au_plating_layer).put(
            trapezoid_connection.pin["Pin_Connection_Electrodes_Pads_right_side"])
            termination_Rf_ring = nd.bend(radius=radius, width=width, angle=180 - angle,layer=Au_plating_layer).put(N_contact_ring_top.pin["b0"])


            N_contact_ring_bot = nd.bend(angle=angle, radius=radius, width=width, offset=0,layer=Au_plating_layer).put(termination_Rf_ring.pin["b0"])
            bend_rf_top = nd.bend(radius=radius, width=width, angle=-(angle - 90) - (180 - angle) / 2,layer=Au_plating_layer).put(N_contact_ring_bot.pin["b0"], flip=False)
            strt_after_ring_rf = nd.strt(length=APD_RF_length,width=width, layer=Au_plating_layer).put()
            bend_after_strt = nd.bend(angle=sbent_angle, radius=sbent_radius,width=width, offset=0, layer=Au_plating_layer).put(strt_after_ring_rf.pin["b0"], flip=True)
            nd.bend(angle=sbent_angle, radius=sbent_radius, width=width,offset=0, layer=Au_plating_layer).put(bend_after_strt.pin["b0"])
            trapezoid_connection = Trapezoid_Electric_Pads(trapezoid_height, width,bond_pad_size, Au_plating_layer).put()
            nd.strt(length=bond_pad_size, width=bond_pad_size, layer=Au_plating_layer).put(
            trapezoid_connection.pin["Pin_Connection_Electrodes_Pads_right_side"])


            metals_width = width
            #This part is for etching to the bottom to reach the ground contact
            width = 1 * metals_width-5
            N_contact_ring_top = nd.bend(angle=angle, radius=radius, width=width, offset=0, layer=etch_ground_down_opening_layer).put(x_move, y_move, rotation_angle)
            bend_rf_top = nd.bend(radius=radius, width=width, angle=-(angle - 90) - (180 - angle) / 2, layer=etch_ground_down_opening_layer).put(
                N_contact_ring_top.pin["a0"], flip=True)

            N_contact_ring_bot = nd.bend(angle=angle, radius=radius, width=width, offset=0, layer=etch_ground_down_opening_layer).put(
                termination_Rf_ring.pin["b0"])
            bend_rf_top = nd.bend(radius=radius, width=width, angle=-(angle - 90) - (180 - angle) / 2, layer=etch_ground_down_opening_layer).put(
                N_contact_ring_bot.pin["b0"], flip=False)
            termination_Rf_ring = nd.bend(radius=radius, width=width, angle=180 - angle, layer=etch_ground_down_opening_layer).put(
                N_contact_ring_top.pin["b0"])




            #This part is for making the openings on the bottom of the ground contact
            width = 1* metals_width-9
            N_contact_ring_top = nd.bend(angle=angle, radius=radius, width=width, offset=0, layer=N_metal_opening_layer).put(x_move, y_move, rotation_angle)
            bend_rf_top = nd.bend(radius=radius, width=width, angle=-(angle - 90) - (180 - angle) / 2, layer=N_metal_opening_layer).put(
                N_contact_ring_top.pin["a0"], flip=True)

            N_contact_ring_bot = nd.bend(angle=angle, radius=radius, width=width, offset=0, layer=N_metal_opening_layer).put(
                termination_Rf_ring.pin["b0"])
            bend_rf_top = nd.bend(radius=radius, width=width, angle=-(angle - 90) - (180 - angle) / 2, layer=N_metal_opening_layer).put(
                N_contact_ring_bot.pin["b0"], flip=False)
            termination_Rf_ring = nd.bend(radius=radius, width=width, angle=180 - angle, layer=N_metal_opening_layer).put(
                N_contact_ring_top.pin["b0"])


            #This part is for the metallization of the rings
            width = 1 * metals_width-3
            N_contact_ring_top = nd.bend(angle=angle, radius=radius, width=width, offset=0, layer=N_metalization_layer).put(x_move, y_move, rotation_angle)
            bend_rf_top = nd.bend(radius=radius, width=width, angle=-(angle - 90) - (180 - angle) / 2, layer=N_metalization_layer).put(
                N_contact_ring_top.pin["a0"], flip=True)

            N_contact_ring_bot = nd.bend(angle=angle, radius=radius, width=width, offset=0, layer=N_metalization_layer).put(
                termination_Rf_ring.pin["b0"])
            bend_rf_top = nd.bend(radius=radius, width=width, angle=-(angle - 90) - (180 - angle) / 2, layer=N_metalization_layer).put(
                N_contact_ring_bot.pin["b0"], flip=False)
            termination_Rf_ring = nd.bend(radius=radius, width=width, angle=180 - angle, layer=N_metalization_layer).put(
                N_contact_ring_top.pin["b0"])



    return Rf_metal_rings



def Trapezoid_Electric_Pads(height, side1, side2,layer):
    with nd.Cell(name='Trapezoid Connection Electrodes Pads') as Trapezoid_Connection_Electrodes_Pads:
        pipes = nd.Polygon(layer=layer, points=[(0, side1 / 2), (0, -side1 / 2),
                                                           (height, -side2 / 2 ),
                                                           (height, side2 / 2 )])
        pipes.put(0, 0)
        nd.Pin(name="Pin_Connection_Electrodes_Pads_right_side").put(height, 0)
        nd.Pin(name="Pin_Connection_Electrodes_Pads_left_side").put(0, 0)


    return Trapezoid_Connection_Electrodes_Pads






if __name__ == "__main__":
    etch_ground_down_opening_layer = 4
    N_metal_opening_layer = 5
    N_metalization_layer = 6
    Au_plating_layer = 7
    radius  = 250
    width  = 80
    length  = 300
    angle  = 180
    bond_pad_size = 200
    trapezoid_height = 100
    APD_RF_length = 0
    RF_True = True
    sbent_radius = 350
    sbent_angle = 45

    center1 = nd.strt(length = 1000, width = 0.001, layer=1).put(0,0)
    center2 = nd.strt(length = 0.001, width = 1000, layer=1).put(0,0)

    # rotation_angle = (180-angle)/2
    # x_move  = (radius+width/2)*math.sin((2*math.pi*angle/360)/2)
    # y_move  = -(radius-width/2)*math.cos((2*math.pi*angle/360)/2)

    Ground_Open_and_Metal(Au_plating_layer,
                    N_metal_opening_layer,
                    N_metalization_layer,
                    etch_ground_down_opening_layer,
                    radius,
                    width,
                    length,
                    angle,
                    bond_pad_size,
                    trapezoid_height,
                    APD_RF_length,
                    RF_True,
                    sbent_angle,
                    sbent_radius).put(x_move=0, y_move=0, rotation_angle=0)   
                 
    nd.export_gds(filename="test.gds")
