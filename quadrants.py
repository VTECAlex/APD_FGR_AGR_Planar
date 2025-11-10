import nazca as nd
from collections import defaultdict
import nazca.geometries as geom


def merge_polygons(cell, layers):
    """Merge all polygons per layer after flattening <cell>."""
    layer_nums = {lay: nd.get_layer(lay) for lay in layers}
    pgons = defaultdict(list)

    for params in nd.cell_iter(cell, flat=True):
        for pgon, xy, bbox in params.iters['polygon']:
            for lay, num in layer_nums.items():
                if pgon.layer == num:
                    pgons[lay].append(xy)

    for lay in layers:
        pgons[lay] = nd.clipper.merge_polygons(pgons[lay])

    return pgons


def remove_polygons(cell, layers):
    """Remove all polygons in <layers> from <cell>."""
    layer_nums = [nd.get_layer(lay) for lay in layers]

    for params in nd.cell_iter(cell):
        if params.cell_start:
            pgons = []
            for pgon in params.cell.polygons:
                if pgon[1].layer not in layer_nums:
                    pgons.append(pgon)
            params.cell.polygons = pgons
    return None


def Layer_Difference(Remove_layer, From_layer, cell_name):
    pgons = merge_polygons(cell=cell_name, layers=[Remove_layer, From_layer])
    remove_polygons(cell=cell_name, layers=[Remove_layer, From_layer])

    pdiff = nd.clipper.diff_polygons(pgons[From_layer], pgons[Remove_layer])
    for pol in pdiff:
        nd.Polygon(points=pol, layer=nd.get_layer(From_layer)).put(0)

    nd.netlist.pin2pin_drc_off()
    return cell_name


# def draw_quadrants(radius=200, gap=10, layer=1):
#     with nd.Cell(name="circle_cross_overlap") as quadrants:
#         nd.add_layer(name='Quadrant Layer', layer=layer, accuracy=0.001)
#         nd.add_layer(name='Gap layer', layer=layer + 1, accuracy=0.001)

#         with nd.Cell(name="Cross and circle") as cross_circle:
#             with nd.Cell(name="The circle") as circle:
#                 nd.Polygon(layer='Quadrant Layer', points=geom.circle(radius=radius, N=1000)).put()
#             circle.put()

#             with nd.Cell(name="The cross to be removed") as the_cross:
#                 nd.strt(length=2 * radius, width=gap, layer='Gap layer').put(-radius, 0)
#                 nd.strt(length=gap, width=2 * radius, layer='Gap layer').put(-gap / 2, 0)
#             the_cross.put()

#         cross_circle.put()
#         Layer_Difference("Gap layer", "Quadrant Layer", cross_circle)

#     return quadrants

def draw_quadrants(radius, gap, layer):
    with nd.Cell(name="main_cell") as main_cell:
        nd.add_layer(name='Quadrant Layer', layer=layer, accuracy=0.001)
        nd.add_layer(name='Gap layer', layer=layer + 1, accuracy=0.001)
        nd.Polygon(layer='Quadrant Layer', points=geom.circle(radius=radius, N=1000)).put()
        nd.strt(length=2 * radius, width=gap, layer='Gap layer').put(-radius, 0)
        nd.strt(length=gap, width=2 * radius, layer='Gap layer').put(-gap / 2, 0)

    # main_cell.put()
    # quadrants = Layer_Difference("Gap layer", "Quadrant Layer", main_cell)
    return main_cell

def draw_p_metal(radius, gap, p_metal_distance_from_edge, p_metal_thickness, bondpad_width, p_bondpad_length, layer):
    radius = radius - p_metal_distance_from_edge
    with nd.Cell(name="main_p_cell") as main_cell:
        nd.add_layer(name='Quadrant p metal Layer', layer=layer, accuracy=0.001)
        nd.add_layer(name='Gap p layer', layer=layer + 1, accuracy=0.001)
        nd.Polygon(layer='Quadrant p metal Layer', points=geom.circle(radius=radius, N=1000)).put()
        nd.Polygon(layer='Gap p layer', points=geom.circle(radius=radius-p_metal_thickness, N=1000)).put()
        nd.strt(length=2 * radius, width=gap + p_metal_distance_from_edge, layer='Gap p layer').put(-radius, 0)
        nd.strt(length=gap + p_metal_distance_from_edge, width=2 * radius, layer='Gap p layer').put(-(gap+p_metal_distance_from_edge) / 2, 0)

        #Below are the bondpad layers
        for i in range(0,4):
            true_p_bondpad_legnth = radius + p_bondpad_length
            nd.strt(length=true_p_bondpad_legnth, width=bondpad_width, layer='Quadrant p metal Layer').put(0, 0,45+90*i)
            nd.strt(length = 80, width = 80, layer  ='Quadrant p metal Layer').put()

        # nd.strt(length=2 * radius, width=bondpad_width, layer='Quadrant p metal Layer').put(0, 0,45+90)
        # nd.strt(length = 80, width = 80, layer  ='Quadrant p metal Layer').put()

        # nd.strt(length=2 * radius, width=bondpad_width, layer='Quadrant p metal Layer').put(0, 0,45+180)
        # nd.strt(length = 80, width = 80, layer  ='Quadrant p metal Layer').put()

        # nd.strt(length=2 * radius, width=bondpad_width, layer='Quadrant p metal Layer').put(0, 0,45+270)
        # nd.strt(length = 80, width = 80, layer  ='Quadrant p metal Layer').put()


    # main_cell.put()
    # quadrants = Layer_Difference("Gap layer", "Quadrant Layer", main_cell)
    return main_cell


def draw_n_metal(radius, gap, layer,n_bondpad_length,n_metal_width):
    with nd.Cell(name="main_p_cell") as main_cell:
        nd.add_layer(name='Quadrant n metal Layer', layer=layer, accuracy=0.001)
        nd.add_layer(name='Gap n layer', layer=layer + 1, accuracy=0.001)
        nd.Polygon(layer='Quadrant n metal Layer', points=geom.circle(radius=radius, N=1000)).put()
        nd.Polygon(layer='Gap n layer', points=geom.circle(radius=radius-n_metal_width, N=1000)).put()
        nd.strt(length=2 * radius, width=gap, layer='Gap n layer').put(-radius, 0)
        nd.strt(length=gap, width=2 * radius, layer='Gap n layer').put(-gap / 2, 0)

        for i in range(0,4):
            true_n_bondpad_length = n_bondpad_length  + radius
            nd.strt(length=2 * radius, width=gap, layer='Gap n layer').put(0, 0,45+90*i)
            nd.strt(length=true_n_bondpad_length, width=gap, layer='Quadrant n metal Layer').put(0, 0,45 +90*i+45/2)
            nd.strt(length = 80, width = 80, layer  ='Quadrant n metal Layer').put()
            nd.strt(length=true_n_bondpad_length, width=gap, layer='Quadrant n metal Layer').put(0, 0,45 +90*i- 45/2)
            nd.strt(length = 80, width = 80, layer  ='Quadrant n metal Layer').put()





    # main_cell.put()
    # quadrants = Layer_Difference("Gap layer", "Quadrant Layer", main_cell)
    return main_cell

def quad_detector_test():
    with nd.Cell(name = "Quad detector") as quad_detector_cell:
        radius = 250
        gap = 30
        layer = 3
        
        quadrant_set = draw_quadrants(radius, gap, layer).put()
        layer = 33
        p_metal_distance_from_edge = 5
        p_metal_thickness = 30
        p_bondpad_width = 20
        p_bondpad_length = 60
        p_metal = draw_p_metal(radius, gap, p_metal_distance_from_edge, p_metal_thickness, p_bondpad_width, p_bondpad_length, layer).put()

        layer = 2
        radius = 290
        n_bondpad_length = 40
        n_metal_width  = 30
        n_metal = draw_n_metal(radius, gap, layer,n_bondpad_length,n_metal_width).put()

        Layer_Difference("Gap layer", "Quadrant Layer", quadrant_set)
        Layer_Difference("Gap p layer", "Quadrant p metal Layer", p_metal)
        Layer_Difference("Gap n layer", "Quadrant n metal Layer", n_metal)

    # quad_detector_cell.put()
    return quad_detector_cell

if __name__ == "__main__":

    quad_detector_test().put()

    nd.export_gds(filename="test_quadrant.gds")
