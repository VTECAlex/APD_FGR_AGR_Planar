# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 15:49:16 2022

@author: aliat
"""

import nazca as nd

# =============================================================================
# length=4700
# width=2300
# cutarea=100
# frame_layer=2
# =============================================================================
def draw_frame(length, width, dicing_area,frame_layer):
    l=length
    w=width
    c=dicing_area
        
    with nd.Cell(name = 'Frame Tile') as myframe:
        nd.Polygon(layer=frame_layer, points = [(0,0),(-c,-c),(-c,w+c),(l+c,w+c),(l+c,-c),\
                                                (-c,-c),(0,0),(l,0),(l,w),(0,w),(0,0)]).put(-length/2,-width/2)
        nd.Pin("Frame Right External Pin").put(width/2+dicing_area,0)
        nd.Pin("Frame Left External Pin").put(-width/2-dicing_area,0)
        nd.Pin("Frame Bot External Pin").put(0,-width/2-dicing_area)
        nd.Pin("Frame Top External Pin").put(0,width/2+dicing_area)

        nd.Pin("Frame Right Internal Pin").put(width/2,0)
        nd.Pin("Frame Left Internal Pin").put(-width/2,0)
        nd.Pin("Frame Bot Internal Pin").put(0,-width/2)
        nd.Pin("Frame Top Internal Pin").put(0,width/2)



        nd.put_stub()
    return myframe
                
def draw_frame_no_pins(length, width, dicing_area,frame_layer):
    l=length
    w=width
    c=dicing_area
        
    with nd.Cell(name = 'Frame Tile') as myframe:
        nd.Polygon(layer=frame_layer, points = [(0,0),(-c,-c),(-c,w+c),(l+c,w+c),(l+c,-c),\
                                                (-c,-c),(0,0),(l,0),(l,w),(0,w),(0,0)]).put(-length/2,-width/2)
        nd.Pin("Frame Right External Pin").put(width/2+dicing_area,0)
        nd.Pin("Frame Left External Pin").put(-width/2-dicing_area,0)
        nd.Pin("Frame Bot External Pin").put(0,-width/2-dicing_area)
        nd.Pin("Frame Top External Pin").put(0,width/2+dicing_area)

        nd.Pin("Frame Right Internal Pin").put(width/2,0)
        nd.Pin("Frame Left Internal Pin").put(-width/2,0)
        nd.Pin("Frame Bot Internal Pin").put(0,-width/2)
        nd.Pin("Frame Top Internal Pin").put(0,width/2)



        # nd.put_stub()
    return myframe



def draw_frame_dcm_module(length, width, dicing_area,frame_layer):
    l=length
    w=width
    c=dicing_area
        
    with nd.Cell(name = 'Frame Tile') as myframe:
        nd.Polygon(layer=frame_layer, points = [(0,0),
                                                (-c,-c),
                                                (-c,w+c),
                                                (l+0,w+c),
                                                (l+0,-c),
                                                (-c,-c),
                                                (0,0),
                                                (l,0),
                                                (l,w),
                                                (0,w),
                                                (0,0)]).put(-length/2,-width/2)
        nd.Pin("Frame Right External Pin").put(width/2+dicing_area,0)
        nd.Pin("Frame Left External Pin").put(-width/2-dicing_area,0)
        nd.Pin("Frame Bot External Pin").put(0,-width/2-dicing_area)
        nd.Pin("Frame Top External Pin").put(0,width/2+dicing_area)

        nd.Pin("Frame Right Internal Pin").put(width/2,0)
        nd.Pin("Frame Left Internal Pin").put(-width/2,0)
        nd.Pin("Frame Bot Internal Pin").put(0,-width/2)
        nd.Pin("Frame Top Internal Pin").put(0,width/2)



        # nd.put_stub()
    return myframe





def draw_frame_new_for_module(length, width, dicing_area,frame_layer):
    l=length
    w=width
    c=dicing_area
        
    with nd.Cell(name = 'Frame Tile') as myframe:
        nd.Polygon(layer=frame_layer, points = [(-c,-c),
                                                (-c,w+c),
                                                (l,w+c),
                                                (l,w),
                                                (0,w),
                                                (0,0),
                                                (l,0),
                                                (l,-c),
                                                (-c,-c)]).put(-length/2,-width/2)



        # nd.put_stub()
    return myframe






if __name__ == "__main__":
    length = 500
    width  = 500
    dicing_area  = 10
    frame_layer = 1
    draw_frame(length, width, dicing_area, frame_layer).put()
    nd.export_gds(filename="test.gds")