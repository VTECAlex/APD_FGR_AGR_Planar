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


def draw_quadrants(radius=200, gap=10, layer=1):
    with nd.Cell(name="circle_cross_overlap") as quadrants:
        nd.add_layer(name='Quadrant Layer', layer=layer, accuracy=0.001)
        nd.add_layer(name='Gap layer', layer=layer + 1, accuracy=0.001)

        with nd.Cell(name="Cross and circle") as cross_circle:
            with nd.Cell(name="The circle") as circle:
                nd.Polygon(layer='Quadrant Layer', points=geom.circle(radius=radius, N=1000)).put()
            circle.put()

            with nd.Cell(name="The cross to be removed") as the_cross:
                nd.strt(length=2 * radius, width=gap, layer='Gap layer').put(-radius, 0)
                nd.strt(length=gap, width=2 * radius, layer='Gap layer').put(-gap / 2, 0)
            the_cross.put()

        cross_circle.put()
        Layer_Difference("Gap layer", "Quadrant Layer", cross_circle)

    return quadrants

def draw_quadrants(radius, gap, layer):
    with nd.Cell(name="main_cell") as main_cell:
        nd.add_layer(name='Quadrant Layer', layer=layer, accuracy=0.001)
        nd.add_layer(name='Gap layer', layer=layer + 1, accuracy=0.001)
        nd.Polygon(layer='Quadrant Layer', points=geom.circle(radius=radius, N=1000)).put()
        nd.strt(length=2 * radius, width=gap, layer='Gap layer').put(-radius, 0)
        nd.strt(length=gap, width=2 * radius, layer='Gap layer').put(-gap / 2, 0)

    # main_cell.put()
    Layer_Difference("Gap layer", "Quadrant Layer", main_cell)
    return main_cell



if __name__ == "__main__":
    radius = 250
    gap = 30
    layer = 3
    for i in range(0,1000,100):
        print(i)
        quadrant_set = draw_quadrants(radius, gap, layer)


    nd.export_gds(filename="test.gds")
