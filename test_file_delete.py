import nazca as nd
from planar_mesa_guard_ring import fgr_agr
from p_rings_metal_openings import *
from n_contact_open_and_rings_V1 import *
import numpy as np

def planar_mesa_ground(active_area_radius,
        distance_agr_fgr,
        fgr_layer,
        agr_layer,
        agr_width,
        width_metallization,
        metal_layer,
        distance_from_edge,
        ditance_from_edge,
        metal_sio_opening,
        metal_sio_opening_layer,
        etch_ground_down_opening_layer,
        N_metal_opening_layer,
        N_metalization_layer,
        Au_plating_layer,
        radius,
        width,
        length,
        angle,
        bond_pad_size,
        trapezoid_height,
        APD_RF_length,
        RF_True,
        sbent_radius,
        sbent_angle,
        space_MESA_N_metal,
        radius_ground):
    with nd.Cell(name = "Palar Mesa and Ground Contacts, radius {}".format(radius)) as Planar_Mesa_Ground:


        #Definces MESA and FGR

        fgr_agr(active_area_radius,distance_agr_fgr,agr_width, agr_layer)


        #Defines metal openings on SiO and metal deposition ring

        #in the distance from the edge the width of the rin
        metal_rings(active_area_radius, width_metallization, metal_layer, ditance_from_edge)



        metal_sio_openings(active_area_radius, width_metallization, metal_sio_opening, metal_sio_opening_layer, ditance_from_edge)

        #rotation should be 50 because the angle of the first bend is 10
        Ground_Open_and_Metal(Au_plating_layer,
                        N_metal_opening_layer,
                        N_metalization_layer,
                        etch_ground_down_opening_layer,
                        radius_ground,
                        width,
                        length,
                        angle,
                        bond_pad_size,
                        trapezoid_height,
                        APD_RF_length,
                        RF_True,
                        sbent_angle,
                        sbent_radius).put(0,-radius_ground,0)   
    return Planar_Mesa_Ground

if __name__ == "__main__":


    active_area_radius = 250
    distance_agr_fgr  = 2
    fgr_layer  =1
    agr_layer = 1
    agr_width  = 3
    width_metallization = 15
    metal_layer = 2
    distance_from_edge = 5
    ditance_from_edge = distance_agr_fgr+distance_from_edge
    metal_sio_opening = 10
    metal_sio_opening_layer = 3
    etch_ground_down_opening_layer = 4
    N_metal_opening_layer = 5
    N_metalization_layer = 6
    Au_plating_layer = 7
    radius  = 250
    width  = 80
    length  = 300
    angle  = 80
    bond_pad_size = 200
    trapezoid_height = 100
    APD_RF_length = 0
    RF_True = True
    sbent_radius = 350
    sbent_angle = 45
    space_MESA_N_metal = 5
    radius_ground = radius + 45 + space_MESA_N_metal
    planar_mesa_ground(active_area_radius,
        distance_agr_fgr,
        fgr_layer,
        agr_layer,
        agr_width,
        width_metallization,
        metal_layer,
        distance_from_edge,
        ditance_from_edge,
        metal_sio_opening,
        metal_sio_opening_layer,
        etch_ground_down_opening_layer,
        N_metal_opening_layer,
        N_metalization_layer,
        Au_plating_layer,
        radius,
        width,
        length,
        angle,
        bond_pad_size,
        trapezoid_height,
        APD_RF_length,
        RF_True,
        sbent_radius,
        sbent_angle,
        space_MESA_N_metal,
        radius_ground).put(0,0, (180-angle)/2+90)
    

    nd.export_gds(filename="test.gds")
