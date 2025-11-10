import nazca as nd
import nazca.geometries as geom





def p_metal_contacts(
    active_area_radius,
    width_metallization,
    metal_layer_rings,
    distance_from_edge,
    bondpads_metal_layer,
    length_bondpad_p_metal,
    width_bond_pad,
    trapezoid_height,
    trapezoid_side1,
    trapezoid_side2,
    p_metal_position
):
    with nd.Cell(name="Top metal contact") as top_metal_contact:

        with nd.Cell(name="Metal Ring") as Metal_ring:
            polygon_points = 1000
            metal_ring = nd.Polygon(
                layer=metal_layer_rings,
                points=geom.ring(
                    radius=active_area_radius - distance_from_edge,
                    width=width_metallization,
                    N=polygon_points
                )
            ).put(0, 0)
            #p_metal_position = active_area_radius - distance_from_edge - 1.2 * width_metallization
            nd.Pin(name="Internal_Contact_Ring").put(active_area_radius - distance_from_edge-width_metallization,0)
            nd.put_stub()

        Metal_ring.put()

        with nd.Cell(name="Bondpad for {}".format(active_area_radius)) as Bondpad:
            bond_pad_straight = nd.strt(
                length=length_bondpad_p_metal,
                width=width_bond_pad,
                layer=bondpads_metal_layer
            ).put()
            height = trapezoid_height
            side1 = trapezoid_side2
            side2 = trapezoid_side1
            layer = bondpads_metal_layer
            trapezoide = Trapezoid_Electric_Pads(height, side1, side2, layer).put(bond_pad_straight.pin["b0"])
            nd.strt(length = side2, width = side2, layer= bondpads_metal_layer).put(trapezoide.pin["Pin_Connection_Electrodes_Pads_right_side"])
        metal_ring_connect = Metal_ring.put()
        Bondpad.put(metal_ring_connect.pin["Internal_Contact_Ring"])
        
    return top_metal_contact


def draw_active_region(
    active_area_radius,
    width_metallization,
    metal_layer_rings,
    distance_from_edge,
    bondpads_metal_layer,
    length_bondpad_p_metal,
    width_bond_pad,
    trapezoid_height,
    trapezoid_side1,
    trapezoid_side2,
    p_metal_position
):
    with nd.Cell(name="Active_region") as active_region:

        with nd.Cell(name="Metal Ring") as active_regrowth:
            polygon_points = 1000
            Active_region = nd.Polygon(
                layer=metal_layer_rings,
                points=geom.ring(
                    radius=active_area_radius - distance_from_edge,
                    width=width_metallization,
                    N=polygon_points
                )
            ).put(0, 0)
            #p_metal_position = active_area_radius - distance_from_edge - 1.2 * width_metallization
            # nd.Pin(name="Internal_Contact_Ring").put(active_area_radius - distance_from_edge-width_metallization,0)
            # nd.put_stub()

        active_regrowth.put()

        
    return active_region

def p_metal_contacts_matrix(
    active_area_radius,
    width_metallization,
    metal_layer_rings,
    distance_from_edge,
    bondpads_metal_layer,
    length_bondpad_p_metal,
    width_bond_pad,
    trapezoid_height,
    trapezoid_side1,
    trapezoid_side2,
    p_metal_position,
    p_box_angle
):
    with nd.Cell(name="Top metal contact") as top_metal_contact:

        with nd.Cell(name="Metal Ring") as Metal_ring:
            polygon_points = 1000
            metal_ring = nd.Polygon(
                layer=metal_layer_rings,
                points=geom.ring(
                    radius=active_area_radius - distance_from_edge,
                    width=width_metallization,
                    N=polygon_points
                )
            ).put(0, 0)
            #p_metal_position = active_area_radius - distance_from_edge - 1.2 * width_metallization
            nd.Pin(name="Internal_Contact_Ring").put(p_metal_position,0)
            nd.put_stub()

        Metal_ring.put()

        with nd.Cell(name="Bondpad for {}".format(active_area_radius)) as Bondpad:
            bond_pad_straight = nd.strt(
                length=length_bondpad_p_metal,
                width=width_bond_pad,
                layer=bondpads_metal_layer
            ).put(0,0)
            height = trapezoid_height
            side1 = trapezoid_side2
            side2 = trapezoid_side1
            layer = bondpads_metal_layer
            # trapezoide = Trapezoid_Electric_Pads(height, side1, side2, layer).put(bond_pad_straight.pin["b0"])
            with nd.Cell("bondpad_p") as bondpad_p:
                with nd.Cell("the box") as the_box:
                    p_bondpad = nd.strt(length = side2, width = side2, layer= bondpads_metal_layer).put(-side2/2,0)
                the_box.put(0,0,p_box_angle)
                nd.Pin("Center_bonpad_p").put(0,0)
                nd.put_stub()

            bondpad_p.put("Center_bonpad_p",bond_pad_straight.pin["b0"])
        metal_ring_connect = Metal_ring.put()
        Bondpad.put(metal_ring_connect.pin["Internal_Contact_Ring"])
        
    return top_metal_contact



def actvie_regrowth_area_matrix(
    active_area_radius,
    width_metallization,
    metal_layer_rings,
    distance_from_edge,
    bondpads_metal_layer,
    length_bondpad_p_metal,
    width_bond_pad,
    trapezoid_height,
    trapezoid_side1,
    trapezoid_side2,
    p_metal_position
):
    with nd.Cell(name="Top metal contact") as top_metal_contact:

        with nd.Cell(name="Metal Ring") as Metal_ring:
            polygon_points = 1000
            metal_ring = nd.Polygon(
                layer=metal_layer_rings,
                points=geom.ring(
                    radius=active_area_radius - distance_from_edge,
                    width=width_metallization,
                    N=polygon_points
                )
            ).put(0, 0)
            #p_metal_position = active_area_radius - distance_from_edge - 1.2 * width_metallization
            nd.Pin(name="Internal_Contact_Ring").put(p_metal_position,0)
            nd.put_stub()

        Metal_ring.put()

        # with nd.Cell(name="Bondpad for {}".format(active_area_radius)) as Bondpad:
        #     bond_pad_straight = nd.strt(
        #         length=length_bondpad_p_metal,
        #         width=width_bond_pad,
        #         layer=bondpads_metal_layer
        #     ).put(0,0)
        #     height = trapezoid_height
        #     side1 = trapezoid_side2
        #     side2 = trapezoid_side1
        #     layer = bondpads_metal_layer
        #     # trapezoide = Trapezoid_Electric_Pads(height, side1, side2, layer).put(bond_pad_straight.pin["b0"])
        #     with nd.Cell("bondpad_p") as bondpad_p:
        #         with nd.Cell("the box") as the_box:
        #             p_bondpad = nd.strt(length = side2, width = side2, layer= bondpads_metal_layer).put(-side2/2,0)
        #         the_box.put(0,0,45)
        #         nd.Pin("Center_bonpad_p").put(0,0)
        #         nd.put_stub()

        #     bondpad_p.put("Center_bonpad_p",bond_pad_straight.pin["b0"])
        # metal_ring_connect = Metal_ring.put()
        # Bondpad.put(metal_ring_connect.pin["Internal_Contact_Ring"])
        
    return top_metal_contact


def metal_sio_openings(
    active_area_radius,
    width_metallization,
    metal_sio_opening,
    metal_layer,
    distance_from_edge
):
    with nd.Cell(name="Metal Ring SiO opening") as Metal_ring_sio_opening:
        if width_metallization == metal_sio_opening:
            print("ATTENTION! The metallization has the same width as the opening at {}".format(width_metallization))
        elif width_metallization < metal_sio_opening:
            print("ATTENTION! The opening of the metallization cannot be larger than the metallization.")
        else:
            polygon_points = 1000
            to_place_in_the_middle = (width_metallization - metal_sio_opening) / 2
            metal_ring = nd.Polygon(
                layer=metal_layer,
                points=geom.ring(
                    radius=active_area_radius - distance_from_edge - to_place_in_the_middle,
                    width=metal_sio_opening,
                    N=polygon_points
                )
            ).put()
            pin_position = active_area_radius - distance_from_edge
            nd.Pin(name="Bond pad ring connection").put(pin_position, 0, 0)
            nd.put_stub()

    return Metal_ring_sio_opening


def Trapezoid_Electric_Pads(height, side1, side2,layer):
    with nd.Cell(name='Trapezoid Connection Electrodes Pads') as Trapezoid_Connection_Electrodes_Pads:
        pipes = nd.Polygon(layer=layer, points=[(0, side1 / 2), (0, -side1 / 2),
                                                           (height, -side2 / 2 ),
                                                           (height, side2 / 2 )])
        pipes.put(0, 0)
        nd.Pin(name="Pin_Connection_Electrodes_Pads_right_side").put(height, 0)
        nd.Pin(name="Pin_Connection_Electrodes_Pads_left_side").put(0, 0)
        nd.put_stub()

    return Trapezoid_Connection_Electrodes_Pads

def p_metal_contact_structure(
    active_area_radius=250,
    ring_width_metallization=15,
    metal_layer_rings=3,
    bondpads_metal_layer=4,
    distance_from_edge=5,
    length_bondpad_p_metal=200,
    width_bond_pad=80,
    metal_sio_opening=10,
    sio_opening_layer=5,
    rotation_angle=0,
    trapezoid_height = 200,
    trapezoid_side1 = 80,
    trapezoid_side2 = 80,
    p_metal_position = 0,
    active_area_regrowth_layer=123,
    fgr_thickness = 2,
    fgr_distance=1,
    fgr_layer=123,
    isolation_layer = 12,
    isolation_width = 30):
    with nd.Cell("P Metal Process") as P_metal_process:
        # Create metal contact with bondpad
        metal_contact = p_metal_contacts(
            active_area_radius,
            ring_width_metallization,
            metal_layer_rings,
            distance_from_edge,
            bondpads_metal_layer,
            length_bondpad_p_metal,
            width_bond_pad,
            trapezoid_height,
    trapezoid_side1,
    trapezoid_side2,
    p_metal_position
        ).put(0, 0, rotation_angle)

    #     active_area_regrowth = draw_active_region(
    #         active_area_radius,
    #         ring_width_metallization,
    #         active_area_regrowth_layer,
    #         distance_from_edge,
    #         bondpads_metal_layer,
    #         length_bondpad_p_metal,
    #         width_bond_pad,
    #         trapezoid_height,
    # trapezoid_side1,
    # trapezoid_side2,
    # p_metal_position
    #     ).put(0, 0, rotation_angle)

        fgr_radius = active_area_radius+fgr_thickness+fgr_distance
    #     fgr_regorwth = draw_active_region(
    #         fgr_radius,
    #         fgr_thickness,
    #         fgr_layer,
    #         distance_from_edge,
    #         bondpads_metal_layer,
    #         length_bondpad_p_metal,
    #         width_bond_pad,
    #         trapezoid_height,
    # trapezoid_side1,
    # trapezoid_side2,
    # p_metal_position
    #     ).put(0, 0, rotation_angle)


        inner_isolation_area = draw_active_region(
            active_area_radius-ring_width_metallization,
            isolation_width,
            isolation_layer,
            distance_from_edge,
            bondpads_metal_layer,
            length_bondpad_p_metal,
            width_bond_pad,
            trapezoid_height,
    trapezoid_side1,
    trapezoid_side2,
    p_metal_position
        ).put(0, 0, rotation_angle)

        between_isolation_area = draw_active_region(
            active_area_radius+isolation_width,
            isolation_width,
            isolation_layer,
            distance_from_edge,
            bondpads_metal_layer,
            length_bondpad_p_metal,
            width_bond_pad,
            trapezoid_height,
    trapezoid_side1,
    trapezoid_side2,
    p_metal_position
        ).put(0, 0, rotation_angle)


    #     outer_isolation_area = draw_active_region(
    #         fgr_radius+isolation_width,
    #         isolation_width,
    #         isolation_layer,
    #         distance_from_edge,
    #         bondpads_metal_layer,
    #         length_bondpad_p_metal,
    #         width_bond_pad,
    #         trapezoid_height,
    # trapezoid_side1,
    # trapezoid_side2,
    # p_metal_position
    #     ).put(0, 0, rotation_angle)

        # Optional: Add SiO2 opening around metal ring (if needed)
        sio_opening = metal_sio_openings(
            active_area_radius,
            ring_width_metallization,
            metal_sio_opening,
            sio_opening_layer,
            distance_from_edge
        ).put(0, 0, rotation_angle)

    return P_metal_process


def p_metal_contact_structure_matrix(
    active_area_radius=250,
    ring_width_metallization=15,
    metal_layer_rings=3,
    bondpads_metal_layer=4,
    distance_from_edge=5,
    length_bondpad_p_metal=200,
    width_bond_pad=80,
    metal_sio_opening=10,
    sio_opening_layer=5,
    rotation_angle=0,
    trapezoid_height = 200,
    trapezoid_side1 = 80,
    trapezoid_side2 = 80,
    p_metal_position = 0,     active_regrowth_area_layer = 11, isolation_regions_layer = 12, isolation_width = 30, p_box_angle =0 
):
    with nd.Cell("P Metal Process") as P_metal_process:
        # Create metal contact with bondpad
        metal_contact = p_metal_contacts_matrix(
            active_area_radius,
            ring_width_metallization,
            metal_layer_rings,
            distance_from_edge,
            bondpads_metal_layer,
            length_bondpad_p_metal,
            width_bond_pad,
            trapezoid_height,
    trapezoid_side1,
    trapezoid_side2,
    p_metal_position, p_box_angle
        ).put(0, 0, rotation_angle)

        active_regrowth_area = actvie_regrowth_area_matrix(
            active_area_radius,
            ring_width_metallization,
            active_regrowth_area_layer,
            distance_from_edge,
            bondpads_metal_layer,
            length_bondpad_p_metal,
            width_bond_pad,
            trapezoid_height,
    trapezoid_side1,
    trapezoid_side2,
    p_metal_position
        ).put(0, 0, rotation_angle)


        inner_isolation_region = actvie_regrowth_area_matrix(
            active_area_radius- ring_width_metallization,
            isolation_width,
            isolation_regions_layer,
            distance_from_edge,
            bondpads_metal_layer,
            length_bondpad_p_metal,
            width_bond_pad,
            trapezoid_height,
    trapezoid_side1,
    trapezoid_side2,
    p_metal_position
        ).put(0, 0, rotation_angle)

        outer_isolation_region = actvie_regrowth_area_matrix(
            active_area_radius+isolation_width,
            isolation_width,
            isolation_regions_layer,
            distance_from_edge,
            bondpads_metal_layer,
            length_bondpad_p_metal,
            width_bond_pad,
            trapezoid_height,
    trapezoid_side1,
    trapezoid_side2,
    p_metal_position
        ).put(0, 0, rotation_angle)


        

        # Optional: Add SiO2 opening around metal ring (if needed)
        sio_opening = metal_sio_openings(
            active_area_radius,
            ring_width_metallization,
            metal_sio_opening,
            sio_opening_layer,
            distance_from_edge
        ).put(0, 0, rotation_angle)

    return P_metal_process



if __name__ == "__main__":
    active_area_radius = 250
    ring_width_metallization = 15
    metal_layer_rings = 3
    bondpads_metal_layer = 4
    distance_from_edge = 5
    length_bondpad_p_metal = 100
    width_bond_pad = 80

    trapezoid_height = 200
    trapezoid_side1 = 200
    trapezoid_side2 = 80

    metal_sio_opening = 10
    sio_opening_layer = 5
    rotation_angle = 0

    p_metal_position = active_area_radius - distance_from_edge - 1.2 * ring_width_metallization

    p_metal_contact_structure_matrix(
        active_area_radius=active_area_radius,
        ring_width_metallization=ring_width_metallization,
        metal_layer_rings=metal_layer_rings,
        bondpads_metal_layer=bondpads_metal_layer,
        distance_from_edge=distance_from_edge,
        length_bondpad_p_metal=length_bondpad_p_metal,
        width_bond_pad=width_bond_pad,
        metal_sio_opening=metal_sio_opening,
        sio_opening_layer=sio_opening_layer,
        rotation_angle=rotation_angle,
        trapezoid_height=trapezoid_height,
        trapezoid_side1=trapezoid_side1,
        trapezoid_side2=trapezoid_side2,
        p_metal_position=p_metal_position
    ).put()

    nd.export_gds(filename="test.gds")




