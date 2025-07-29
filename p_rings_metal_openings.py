import nazca as nd
import nazca.geometries as geom





def p_metal_contacts(
    active_area_radius,
    width_metallization,
    metal_layer_rings,
    distance_from_edge,
    bondpads_metal_layer,
    length_bondpad,
    width_bond_pad
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
            nd.Pin(name="Internal_Contact_Ring").put(
                active_area_radius - distance_from_edge - 1.2 * width_metallization,
                0
            )
        Metal_ring.put()

        with nd.Cell(name="Bondpad for {}".format(active_area_radius)) as Bondpad:
            nd.strt(
                length=length_bondpad,
                width=width_bond_pad,
                layer=bondpads_metal_layer
            ).put()
            height = 80
            side1 = 80
            side2 = 200
            layer = bondpads_metal_layer
            trapezoide = Trapezoid_Electric_Pads(height, side1, side2, layer).put()
            nd.strt(length = side2, width = side2, layer= bondpads_metal_layer).put(trapezoide.pin["Pin_Connection_Electrodes_Pads_right_side"])
        metal_ring_connect = Metal_ring.put()
        Bondpad.put(metal_ring_connect.pin["Internal_Contact_Ring"])

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
    return Trapezoid_Connection_Electrodes_Pads

def p_metal_contact_structure(
    active_area_radius=250,
    ring_width_metallization=15,
    metal_layer_rings=3,
    bondpads_metal_layer=4,
    distance_from_edge=5,
    length_bondpad=200,
    width_bond_pad=80,
    metal_sio_opening=10,
    sio_opening_layer=5,
    rotation_angle=0):
    with nd.Cell("P Metal Process") as P_metal_process:
        # Create metal contact with bondpad
        metal_contact = p_metal_contacts(
            active_area_radius,
            ring_width_metallization,
            metal_layer_rings,
            distance_from_edge,
            bondpads_metal_layer,
            length_bondpad,
            width_bond_pad
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
    distance_from_edge = 5  # fixed spelling
    angle = 80
    length_bondpad = 200
    width_bond_pad = 80

    p_metal_contact_structure(
    active_area_radius=250,
    ring_width_metallization=15,
    metal_layer_rings=3,
    bondpads_metal_layer=4,
    distance_from_edge=5,
    length_bondpad=200,
    width_bond_pad=80,
    metal_sio_opening=10,
    sio_opening_layer=5,
    rotation_angle=0).put()
    nd.export_gds(filename="test.gds")




