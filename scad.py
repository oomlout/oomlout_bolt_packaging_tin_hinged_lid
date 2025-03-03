import copy
import opsc
import oobb
import oobb_base
import yaml
import os
import scad_help

def main(**kwargs):
    make_scad(**kwargs)

def make_scad(**kwargs):
    parts = []

    typ = kwargs.get("typ", "")

    if typ == "":
        #setup    
        #typ = "all"
        typ = "fast"
        #typ = "manual"

    #oomp_mode = "project"
    oomp_mode = "oobb"

    if typ == "all":
        filter = ""; save_type = "all"; navigation = True; overwrite = True; modes = ["3dpr"]; oomp_run = False
        #filter = ""; save_type = "all"; navigation = True; overwrite = True; modes = ["3dpr", "laser", "true"]
    elif typ == "fast":
        filter = ""; save_type = "none"; navigation = False; overwrite = True; modes = ["3dpr"]; oomp_run = False
    elif typ == "manual":
    #filter
        filter = ""
        #filter = "test"

    #save_type
        save_type = "none"
        #save_type = "all"
        
    #navigation        
        #navigation = False
        navigation = True    

    #overwrite
        overwrite = True
                
    #modes
        #modes = ["3dpr", "laser", "true"]
        modes = ["3dpr"]
        #modes = ["laser"]    

    #oomp_run
        oomp_run = True
        #oomp_run = False    

    #adding to kwargs
    kwargs["filter"] = filter
    kwargs["save_type"] = save_type
    kwargs["navigation"] = navigation
    kwargs["overwrite"] = overwrite
    kwargs["modes"] = modes
    kwargs["oomp_mode"] = oomp_mode
    kwargs["oomp_run"] = oomp_run
    
       
    # project_variables
    if True:
        pass
    
    # declare parts
    if True:

        directory_name = os.path.dirname(__file__) 
        directory_name = directory_name.replace("/", "\\")
        project_name = directory_name.split("\\")[-1]
        #max 60 characters
        length_max = 40
        if len(project_name) > length_max:
            project_name = project_name[:length_max]
            #if ends with a _ remove it 
            if project_name[-1] == "_":
                project_name = project_name[:-1]
                
        #defaults
        kwargs["size"] = "oobb"
        kwargs["width"] = 1
        kwargs["height"] = 1
        kwargs["thickness"] = 3
        #oomp_bits
        if oomp_mode == "project":
            kwargs["oomp_classification"] = "project"
            kwargs["oomp_type"] = "github"
            kwargs["oomp_size"] = "oomlout"
            kwargs["oomp_color"] = project_name
            kwargs["oomp_description_main"] = ""
            kwargs["oomp_description_extra"] = ""
            kwargs["oomp_manufacturer"] = ""
            kwargs["oomp_part_number"] = ""
        elif oomp_mode == "oobb":
            kwargs["oomp_classification"] = "oobb"
            kwargs["oomp_type"] = "part"
            kwargs["oomp_size"] = "liner_packaging_tin_hinged_lid"
            kwargs["oomp_color"] = ""
            kwargs["oomp_description_main"] = ""
            kwargs["oomp_description_extra"] = ""
            kwargs["oomp_manufacturer"] = ""
            kwargs["oomp_part_number"] = ""

        part_default = {} 
       
        part_default["project_name"] = project_name
        part_default["full_shift"] = [0, 0, 0]
        part_default["full_rotations"] = [0, 0, 0]
        
        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        p3["width"] = 3
        p3["height"] = 3
        #p3["thickness"] = 6
        #p3["extra"] = ""
        part["kwargs"] = p3
        nam = "liner_packaging_tin_hinged_lid"
        part["name"] = nam
        if oomp_mode == "oobb":
            p3["oomp_size"] = nam
        #parts.append(part)



        #10x14 a5
        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        #p3["thickness"] = 6
        p3["width"] = 10
        p3["height"] = 14
        part["kwargs"] = p3  
        p3["width_start"] = 161 # external_measurement
        p3["height_start"] = 221
        p3["depth_start"] = 21  #internal depth measurement      
        p3["thickness"] = p3["depth_start"]
        p3["thickness_tin"] = 0.5
        p3["thickness_bead"] = 2
        p3["diameter_bottom_bend"] = 1
        #extra = f"width_start_{p3["width_start"]}_height_start_{p3["height_start"]}_depth_start_{p3["depth_start"]}"
        extra = "packaging_tin_hinged_lid_169_mm_width_130_mm_height_18_mm_depth_350_ml_tinware_direct_t4066"
        p3["extra"] = extra
        nam = "liner_packaging_tin_hinged_lid"
        part["name"] = nam
        if oomp_mode == "oobb":
            p3["oomp_size"] = nam
        parts.append(part)


        #8x10 smaller
        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        #p3["thickness"] = 6
        p3["width"] = 8
        p3["height"] = 10
        part["kwargs"] = p3  
        p3["width_start"] = 129 # external_measurement
        p3["height_start"] = 169
        p3["depth_start"] = 18 #inside depth measurement      
        p3["thickness"] = p3["depth_start"]
        p3["thickness_tin"] = 0.5
        p3["thickness_bead"] = 1.5 #remember to remove tin thickness
        p3["diameter_bottom_bend"] = 1
        extra = "packaging_tin_hinged_lid_a5_220_mm_width_160_mm_height_25_mm_depth_450_ml_tinware_direct_t4005"
        #extra = f"width_start_{p3["width_start"]}_height_start_{p3["height_start"]}_depth_start_{p3["depth_start"]}"
        p3["extra"] = extra
        nam = "liner_packaging_tin_hinged_lid"
        part["name"] = nam
        if oomp_mode == "oobb":
            p3["oomp_size"] = nam
        parts.append(part)

    kwargs["parts"] = parts

    scad_help.make_parts(**kwargs)

    #generate navigation
    if navigation:
        sort = []
        sort.append("extra")
        sort.append("name")
        sort.append("width")
        sort.append("height")
        sort.append("thickness")
        
        scad_help.generate_navigation(sort = sort)


def get_base(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    
    #add plate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "positive"
    p3["shape"] = f"oobb_plate"    
    p3["depth"] = depth
    #p3["holes"] = True         uncomment to include default holes
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add holes seperate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_holes"
    p3["both_holes"] = True  
    p3["depth"] = depth
    p3["holes"] = "perimeter"
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -500/2
        pos1[1] += 0
        pos1[2] += -500/2        
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_liner_packaging_tin_hinged_lid(thing, **kwargs):

    depth = kwargs.get("thickness", 4)
    prepare_print = kwargs.get("prepare_print", True)

    clearance_internal = 1

    pos = kwargs.get("pos", [0, 0, 0])
    #pos = copy.deepcopy(pos)
    #pos[2] += -20
    width = kwargs.get("width", None)
    height = kwargs.get("height", None)
    width_start =  kwargs.get("width_start", None)
    height_start = kwargs.get("height_start", None)
    depth_start = kwargs.get("depth_start", None)

    thickness_bead = kwargs.get("thickness_bead", None)
    thickness_tin = kwargs.get("thickness_tin", None)
    diameter_bottom_bend = kwargs.get("diameter_bottom_bend", None)

    clearance_width_extra = kwargs.get("clearance_width_extra", 0)    
    clearance_height_extra = kwargs.get("clearance_height_extra", 0)
    clearance_sides_extra = kwargs.get("clearance_sides_extra", 0.5) #the distance to bring in the cube sides to allow for glue or the bead lip to press up doubled so it's on each side
    clearance_depth_extra = kwargs.get("clearance_depth_extra", 0.5)

    width_total = width_start - thickness_tin - clearance_width_extra
    height_total = height_start - thickness_tin - clearance_height_extra
    depth_total = (depth_start 
                   - thickness_bead 
                   - clearance_depth_extra)
    depth_total_bead_buldge_clearance = depth_total - thickness_bead / 2
    depth_total_to_bead_top = depth_total + thickness_bead

    #add plate #inset to avoide bottom bend and add some corner clearance
    extra_clearance_corner = 1.5
    radius_inside = 9
    w = width_total - diameter_bottom_bend
    h = height_total - diameter_bottom_bend
    d = depth_total_bead_buldge_clearance 
    size_main = [w, h, d]
    size_big = copy.deepcopy(size_main)
    size_big[0] += - extra_clearance_corner*2
    size_big[1] += - extra_clearance_corner*2
    size_little = copy.deepcopy(size_main)
    size_little[0] += - thickness_bead*2
    size_little[1] += - thickness_bead*2
    size_little[2] = depth_total_to_bead_top

    
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"rounded_rectangle"       
    
    p3["size"] = size_big
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    diff = (size_big[0]-size_little[0])/2
    rad = radius_inside + diff
    p3["radius"] = rad
    oobb_base.append_full(thing,**p3)

    #above the bead piece
    p4 = copy.deepcopy(p3)
    size = copy.deepcopy(size_main)    
    p4["size"] = size_little
    p4["pos"][2] += 0
    rad = radius_inside
    p4["radius"] = rad
    #p4["m"] = "#"
    oobb_base.append_full(thing,**p4)


    #add cubes to snuck the height beyond the corner
    corner_radius_clearance = 30
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_cube"
    w = width_total - corner_radius_clearance * 2
    h = height_total - clearance_sides_extra * 2
    d = depth_total - diameter_bottom_bend
    size = [w, h, d]
    p3["size"] = size
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)
    pos1[2] += diameter_bottom_bend
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    p4 = copy.deepcopy(p3)
    w = width_total - clearance_sides_extra * 2
    h = height_total  - corner_radius_clearance * 2
    size = [w, h, d]
    p4["size"] = size
    #p4["m"] = "#"
    oobb_base.append_full(thing,**p4)
    



    

    #add cutout
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"rounded_rectangle"    
    w = width * 15 + clearance_internal
    h = height * 15 + clearance_internal
    d = depth_total + thickness_bead
    size = [w, h, d]
    p3["size"] = size
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    rad = 5 + clearance_internal / 2
    p3["radius"] = rad
    oobb_base.append_full(thing,**p3)
    

    if prepare_print:
        shift = width_total/2

        #add slice # right
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_cube"
        w = width_total
        h = height_total
        d = depth_total + thickness_bead
        size = [w, h, d]
        pos1 = copy.deepcopy(pos)
        pos1[0] += shift
        p3["pos"] = pos1
        p3["size"] = size
        #p3["m"] = "#"
        #oobb_base.append_full(thing,**p3)
        
        shift = height_total/2
        #add slice # bottom
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_cube"
        w = width_total
        h = height_total
        d = depth_total + thickness_bead
        size = [w, h, d]
        pos1 = copy.deepcopy(pos)
        pos1[1] += -shift
        p3["pos"] = pos1
        p3["size"] = size
        #p3["m"] = "#"
        #oobb_base.append_full(thing,**p3)

        

if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)