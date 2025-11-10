import nazca as nd


p_metal_layer = 2
p_metal_layer_opening = 3
n_metal_etch_semi_layer = 6
n_metal_deposition_layer = 4
n_metal_opening_bottom_sio_layer = 7
EPI_1_islands_layer  = 8
isolation_between_devices = 9
extra_TPA_metal_layer = 22
text_description_layer  = 11




def matrix_of_bars(layer_bars):
            with nd.Cell(name = "Matrix of bars") as matrix_of_bars:
                if layer_bars == 'Au plating ' or layer_bars == 'Metal Rings' or layer_bars == 'N Metal':
                    layerN = 200
                else:
                    layerN = 0
                for j in range(0,3):
                    with nd.Cell(name = "test cell") as test_cell:
                        column_distances = [100, 625, 1250]
                        test_width  = 5
                        distance  =  100*(j+1)
                        width_of_metal_pad = 100
                        length_of_metal_pad = 100
                        layer = layer_bars
                        with nd.Cell(name="Metal pad") as metal_pad:
                            nd.strt(width= width_of_metal_pad , length  = length_of_metal_pad , layer = layer).put()
                            
                        with nd.Cell(name = "Clumn of bars") as Column_of_bars:
                            
                            number_of_bars_variation_in_width = 4
                            nobviw = number_of_bars_variation_in_width 
                            wwv= [5,10,20,50]
                            for i in range(nobviw):
                                yy = (200+175+width_of_metal_pad)*i-layerN
                                
                                nd.text("{},{}".format(wwv[i], distance), layer = layer).put(0, yy+50,0)
    
                                metal_pad.put(-length_of_metal_pad  , yy )
                                metal_pad.put(distance, yy )
                                nd.strt(width = wwv[i], length  = distance , layer = layer).put(0, yy )
                        Column_of_bars.put()
                    # test_cell.put(100*(j+1)+(600-layerN)*j,0)
                    test_cell.put(column_distances[j],0)
                    print(100*(j+1)+(600-layerN)*j)
            
            return matrix_of_bars



def n_metal_bars():
     with nd.Cell("N metal bars") as N_metal_bars:
        nd.text("N metal bars", height=300, layer=n_metal_deposition_layer).put(0,1600)
        matrix_of_bars(n_metal_deposition_layer).put(0,0)


        return N_metal_bars

def p_metal_bars():
     with nd.Cell("N metal bars") as P_metal_bars:
        nd.text("P metal bars", height=300, layer=p_metal_layer).put(0,1600)
        matrix_of_bars(p_metal_layer).put(0,0)


        return P_metal_bars

p_metal_bars().put()
nd.export_gds(filename='metal_bars.gds')