import nazca as nd
import nazca.geometries as geom





def fgr_agr(active_area_radius,distance_agr_fgr, agr_width, agr_layer):
    if distance_agr_fgr<10:
        polygon_points = 1000
        FGR = nd.Polygon(layer=agr_layer, points=geom.ring(radius=active_area_radius, width = distance_agr_fgr, N=polygon_points)).put()
        AGR = nd.Polygon(layer=agr_layer, points=geom.ring(radius=active_area_radius+distance_agr_fgr+agr_width, width=distance_agr_fgr, N=polygon_points)).put()



    else:
        print("Error, the distance beteen the rings cannot be larger than 10um due to crystallization formation")



if __name__ == "__main__":
    #this part is for the fgr and agr
    active_area_radius = 250
    distance_agr_fgr  = 4
    fgr_layer  =1
    agr_layer = 1
    agr_width  = 3
    fgr_agr(active_area_radius,distance_agr_fgr,agr_width, agr_layer)




    nd.export_gds(filename="test.gds")