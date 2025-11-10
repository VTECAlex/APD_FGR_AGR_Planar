import nazca as nd
import nazca.geometries as geom


p_metal_layer = 2
p_metal_layer_opening = 3
n_metal_etch_semi_layer = 6
n_metal_deposition_layer = 4
n_metal_opening_bottom_sio_layer = 7
EPI_1_islands_layer  = 8
isolation_between_devices = 9
extra_TPA_metal_layer = 22
text_description_layer  = 11



diameter = 50



def circular_pin_top_illu():
    with nd.Cell("Circular PIN top illuminated") as Circular_PIN_top_illuminated:
        #### this is the metal ring

        p_metal_ring_width = 10
        active_area_radius = diameter/2+p_metal_ring_width
        polygon_points = 700
        # p_metal_ring_layer = 2
        p_metal_ring = nd.Polygon(layer=p_metal_layer, points = geom.ring(radius=active_area_radius,
                                                                        width=p_metal_ring_width,
                                                                        N=polygon_points)).put(0,0)


        #### this is the EPI_1 isolation
        epi_1_ring_width = 10
        active_area_radius = diameter/2 + epi_1_ring_width +p_metal_ring_width
        polygon_points = 700
        epi_1_ring =nd.Polygon(layer=EPI_1_islands_layer, points = geom.ring(radius=active_area_radius,
                                                                        width=epi_1_ring_width,
                                                                        N=polygon_points)).put(0,0)



        ###SiO opening

        p_metal_ring_sio_opening = 5
        active_area_radius = diameter/2+p_metal_ring_sio_opening+p_metal_ring_sio_opening/2
        polygon_points = 700
        epi_1_ring =nd.Polygon(layer=p_metal_layer_opening, points = geom.ring(radius=active_area_radius,
                                                                        width=p_metal_ring_sio_opening,
                                                                        N=polygon_points)).put(0,0)
        
        ### Ground Contact
        distance_ground_contact = -80
        with nd.Cell("Ground contact") as ground_contact_all_layers:
            metal_width = 50+20+20
            metal_length = 50
            ground_contact_metal = nd.strt(length = metal_length, width = metal_width, layer = n_metal_deposition_layer).put(-metal_length/2,0)

            metal_length = metal_length -5
            metal_width = metal_width - 5
            ground_contact_semi_etch = nd.strt(length = metal_length, width = metal_width, layer = n_metal_etch_semi_layer).put(-metal_length/2,0)

            metal_length = metal_length - 10
            metal_width = metal_width - 10
            ground_contact_bottom_sio_etch = nd.strt(length = metal_length, width = metal_width, layer = n_metal_opening_bottom_sio_layer).put(-metal_length/2,0)
        ground_contact_all_layers.put(distance_ground_contact,0)



        ### Metal Contact bond pad
        bond_pad_length = nd.strt(length = 100, width = 10, layer = p_metal_layer).put(diameter/2,0)
        circular_bondpad = nd.Polygon(layer=p_metal_layer, points = geom.circle(radius=diameter/2,
                                                                        N=polygon_points)).put()
        
    return Circular_PIN_top_illuminated



def circular_pin_bot_illu():
    with nd.Cell("Circular PIN top illuminated") as Circular_PIN_bot_illuminated:
        #### this is the metal ring

        p_metal_ring_width = 10
        active_area_radius = diameter/2+p_metal_ring_width
        polygon_points = 700
        # p_metal_ring_layer = 2
        # p_metal_ring = nd.Polygon(layer=p_metal_layer, points = geom.ring(radius=active_area_radius,
        #                                                                 width=p_metal_ring_width,
        #                                                                 N=polygon_points)).put(0,0)
        p_metal_full_circle = nd.Polygon(layer=p_metal_layer, points = geom.circle(radius=active_area_radius,
                                                                N=polygon_points)).put(0,0)


        #### this is the EPI_1 isolation
        epi_1_ring_width = 10
        active_area_radius = diameter/2 + epi_1_ring_width +p_metal_ring_width
        polygon_points = 700
        epi_1_ring =nd.Polygon(layer=EPI_1_islands_layer, points = geom.ring(radius=active_area_radius,
                                                                        width=epi_1_ring_width,
                                                                        N=polygon_points)).put(0,0)



        ###SiO opening

        p_metal_ring_sio_opening = 5
        active_area_radius = diameter/2+p_metal_ring_sio_opening+p_metal_ring_sio_opening/2
        polygon_points = 700
        epi_1_ring =nd.Polygon(layer=p_metal_layer_opening, points = geom.ring(radius=active_area_radius,
                                                                        width=p_metal_ring_sio_opening,
                                                                        N=polygon_points)).put(0,0)
        
        ### Ground Contact
        distance_ground_contact = -80
        with nd.Cell("Ground contact") as ground_contact_all_layers:
            metal_width = 50+20+20
            metal_length = 50
            ground_contact_metal = nd.strt(length = metal_length, width = metal_width, layer = n_metal_deposition_layer).put(-metal_length/2,0)

            metal_length = metal_length -5
            metal_width = metal_width - 5
            ground_contact_semi_etch = nd.strt(length = metal_length, width = metal_width, layer = n_metal_etch_semi_layer).put(-metal_length/2,0)

            metal_length = metal_length - 10
            metal_width = metal_width - 10
            ground_contact_bottom_sio_etch = nd.strt(length = metal_length, width = metal_width, layer = n_metal_opening_bottom_sio_layer).put(-metal_length/2,0)
        ground_contact_all_layers.put(distance_ground_contact,0)



        ### Metal Contact bond pad
        bond_pad_length = nd.strt(length = 100, width = 10, layer = p_metal_layer).put(diameter/2,0)
        circular_bondpad = nd.Polygon(layer=p_metal_layer, points = geom.circle(radius=diameter/2,
                                                                        N=polygon_points)).put()
        
    return Circular_PIN_bot_illuminated





def circular_pin_top_illu_no_grd():
    with nd.Cell("Circular PIN top illuminated") as Circular_PIN_top_illuminated:
        #### this is the metal ring

        p_metal_ring_width = 10
        active_area_radius = diameter/2+p_metal_ring_width
        polygon_points = 700
        # p_metal_ring_layer = 2
        p_metal_ring = nd.Polygon(layer=p_metal_layer, points = geom.ring(radius=active_area_radius,
                                                                        width=p_metal_ring_width,
                                                                        N=polygon_points)).put(0,0)


        #### this is the EPI_1 isolation
        epi_1_ring_width = 10
        active_area_radius = diameter/2 + epi_1_ring_width +p_metal_ring_width
        polygon_points = 700
        epi_1_ring =nd.Polygon(layer=EPI_1_islands_layer, points = geom.ring(radius=active_area_radius,
                                                                        width=epi_1_ring_width,
                                                                        N=polygon_points)).put(0,0)



        ###SiO opening

        p_metal_ring_sio_opening = 5
        active_area_radius = diameter/2+p_metal_ring_sio_opening+p_metal_ring_sio_opening/2
        polygon_points = 700
        epi_1_ring =nd.Polygon(layer=p_metal_layer_opening, points = geom.ring(radius=active_area_radius,
                                                                        width=p_metal_ring_sio_opening,
                                                                        N=polygon_points)).put(0,0)
        
        ### Ground Contact
        # distance_ground_contact = -80
        # with nd.Cell("Ground contact") as ground_contact_all_layers:
        #     metal_width = 50+20+20
        #     metal_length = 50
        #     ground_contact_metal = nd.strt(length = metal_length, width = metal_width, layer = n_metal_deposition_layer).put(-metal_length/2,0)

        #     metal_length = metal_length -5
        #     metal_width = metal_width - 5
        #     ground_contact_semi_etch = nd.strt(length = metal_length, width = metal_width, layer = n_metal_etch_semi_layer).put(-metal_length/2,0)

        #     metal_length = metal_length - 10
        #     metal_width = metal_width - 10
        #     ground_contact_bottom_sio_etch = nd.strt(length = metal_length, width = metal_width, layer = n_metal_opening_bottom_sio_layer).put(-metal_length/2,0)
        # ground_contact_all_layers.put(distance_ground_contact,0)



        ### Metal Contact bond pad
        bond_pad_length = nd.strt(length = 100, width = 10, layer = p_metal_layer).put(diameter/2,0)
        circular_bondpad = nd.Polygon(layer=p_metal_layer, points = geom.circle(radius=diameter/2,
                                                                        N=polygon_points)).put()
        
    return Circular_PIN_top_illuminated



def circular_pin_bot_illu_no_grd():
    with nd.Cell("Circular PIN top illuminated") as Circular_PIN_bot_illuminated:
        #### this is the metal ring

        p_metal_ring_width = 10
        active_area_radius = diameter/2+p_metal_ring_width
        polygon_points = 700
        # p_metal_ring_layer = 2
        # p_metal_ring = nd.Polygon(layer=p_metal_layer, points = geom.ring(radius=active_area_radius,
        #                                                                 width=p_metal_ring_width,
        #                                                                 N=polygon_points)).put(0,0)
        p_metal_full_circle = nd.Polygon(layer=p_metal_layer, points = geom.circle(radius=active_area_radius,
                                                                N=polygon_points)).put(0,0)


        #### this is the EPI_1 isolation
        epi_1_ring_width = 10
        active_area_radius = diameter/2 + epi_1_ring_width +p_metal_ring_width
        polygon_points = 700
        epi_1_ring =nd.Polygon(layer=EPI_1_islands_layer, points = geom.ring(radius=active_area_radius,
                                                                        width=epi_1_ring_width,
                                                                        N=polygon_points)).put(0,0)



        ###SiO opening

        p_metal_ring_sio_opening = 5
        active_area_radius = diameter/2+p_metal_ring_sio_opening+p_metal_ring_sio_opening/2
        polygon_points = 700
        epi_1_ring =nd.Polygon(layer=p_metal_layer_opening, points = geom.ring(radius=active_area_radius,
                                                                        width=p_metal_ring_sio_opening,
                                                                        N=polygon_points)).put(0,0)
        
        ### Ground Contact
        # distance_ground_contact = -80
        # with nd.Cell("Ground contact") as ground_contact_all_layers:
        #     metal_width = 50+20+20
        #     metal_length = 50
        #     ground_contact_metal = nd.strt(length = metal_length, width = metal_width, layer = n_metal_deposition_layer).put(-metal_length/2,0)

        #     metal_length = metal_length -5
        #     metal_width = metal_width - 5
        #     ground_contact_semi_etch = nd.strt(length = metal_length, width = metal_width, layer = n_metal_etch_semi_layer).put(-metal_length/2,0)

        #     metal_length = metal_length - 10
        #     metal_width = metal_width - 10
        #     ground_contact_bottom_sio_etch = nd.strt(length = metal_length, width = metal_width, layer = n_metal_opening_bottom_sio_layer).put(-metal_length/2,0)
        # ground_contact_all_layers.put(distance_ground_contact,0)



        ### Metal Contact bond pad
        bond_pad_length = nd.strt(length = 100, width = 10, layer = p_metal_layer).put(diameter/2,0)
        circular_bondpad = nd.Polygon(layer=p_metal_layer, points = geom.circle(radius=diameter/2,
                                                                        N=polygon_points)).put()
        
    return Circular_PIN_bot_illuminated






def fifty_circular_devices_indep_grounds():
    with nd.Cell("50 circular devices") as circular_devices:
        for i in range(50):
            device_dist = 100
            circular_pin_top_illu().put(0,device_dist*i)
            circular_pin_bot_illu().put(300,device_dist*i)

    return circular_devices



def fifty_circular_devices_common_grounds():
    with nd.Cell("50 circular devices") as circular_devices:
        for i in range(50):
            device_dist = 100



            ## Ground Contact
            distance_ground_contact = -80
            with nd.Cell("Ground contact") as ground_contact_all_layers:
                metal_width = 4990
                metal_length = 50
                ground_contact_metal = nd.strt(length = metal_length, width = metal_width, layer = n_metal_deposition_layer).put(-metal_length/2,metal_width/2)

                metal_length = metal_length -5
                metal_width = metal_width - 5
                ground_contact_semi_etch = nd.strt(length = metal_length, width = metal_width, layer = n_metal_etch_semi_layer).put(-metal_length/2,metal_width/2+2.5)

                metal_length = metal_length - 10
                metal_width = metal_width - 10
                ground_contact_bottom_sio_etch = nd.strt(length = metal_length, width = metal_width, layer = n_metal_opening_bottom_sio_layer).put(-metal_length/2,metal_width/2+7.5)
            ground_contact_all_layers.put(distance_ground_contact,-45)
            ground_contact_all_layers.put(distance_ground_contact+300,-45)

            circular_pin_top_illu_no_grd().put(0,device_dist*i)
            circular_pin_bot_illu_no_grd().put(300,device_dist*i)

    return circular_devices

fifty_circular_devices_indep_grounds().put()
fifty_circular_devices_common_grounds().put(+800,0)
nd.export_gds(filename="rings_PiN.gds")
