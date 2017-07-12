def calcStress(intForce, area):
    return float(intForce) / float(area)

def calcStrain(change, orig):
    return float(change) / float(orig)

def listStress(forceList, area):
    stressList = []
    for thisForce in forceList:
            stressList.append(float('{0:.3f}'.format(calcStress(thisForce, area))))
    return stressList

def listStrain(changeList, orig):
    strainList = []
    for thisChange in changeList:
            strainList.append(float('{0:.3f}'.format(calcStrain(thisChange, orig))))
    return strainList

def writeToJson(thisDict, filepath):
    import json
    import os
    json_string = json.dumps(thisDict, indent=4, sort_keys=True)
    fp = open(filepath, 'w')
    fp.write(json_string)
    fp.close()
    return os.path.exists(filepath)


alu1_stress = ssc.listStress(test_dict['alu1'][0], 0.305)
alu2_stress = ssc.listStress(test_dict['alu2'][0], 0.305)
stl_stress = ssc.listStress(test_dict['stl'][0], 0.305)
plas1_stress = ssc.listStress(test_dict['plas1'][0], 1.524)
plas2_stress = ssc.listStress(test_dict['plas2'][0], 1.524)
ipw_thin_stress = ssc.listStress(test_dict['iPod-Thin'][0], 1.13)
ipw_thick_stress = ssc.listStress(test_dict['iPod-Thick'][0], 3.14)

alu1_strain = ssc.listStrain(test_dict['aluminum1'][1], 80.0)
alu2_strain = ssc.listStrain(test_dict['aluminum2'][1], 80.0)
stl_strain = ssc.listStrain(test_dict['steel'][1], 80.0)
plas1_strain = ssc.listStrain(test_dict['plastic1'][1], 80.0)
plas2_strain = ssc.listStrain(test_dict['plastic2'][1], 80.0)
ipw_thick_strain = ssc.listStrain(test_dict['iPod-Thin'][1], 70.0)
ipw_thick_strain = ssc.listStrain(test_dict['iPod-Thick'][1], 70.0)


alu1_ss = {'aluminum1':[alu1_strain, alu1_stress]}
alu2_ss = {'aluminum2':[alu2_strain, alu2_stress]}
stl_ss = {'steel':[stl_strain, stl_stress]}
plas1_ss = {'plastic1':[plas1_strain, plas1_stress]}
plas2_ss = {'plastic2':[plas2_strain, plas2_stress]}
ipw_thin_ss = {'iPod-Thin':[ipw_thin_strain, ipw_thick_stress]}
ipw_thick_ss = {'iPod-Thick':[ipw_thick_strain, ipw_thick_stress]}

alu1_path = '/Users/jparks/Desktop/xyPlot/alu1_ss.json'
alu2_path = '/Users/jparks/Desktop/xyPlot/alu2_ss.json'
stl_path = '/Users/jparks/Desktop/xyPlot/stl_ss.json'
plas1_path = '/Users/jparks/Desktop/xyPlot/plas1_ss.json'
plas2_path = '/Users/jparks/Desktop/xyPlot/plas2_ss.json'
ipw_thin_path = '/Users/jparks/Desktop/xyPlot/ipw_thin_ss.json'
ipw_thick_path = '/Users/jparks/Desktop/xyPlot/ipw_thick_ss.json'

ssc.writeToJson(alu1_ss, alu1_path)
ssc.writeToJson(alu2_ss, alu2_path)
ssc.writeToJson(stl_ss, stl_path)
ssc.writeToJson(plas1_ss, plas1_path)
ssc.writeToJson(plas2_ss, plas2_path)
ssc.writeToJson(ipw_thin_ss, ipw_thin_path)
ssc.writeToJson(ipw_thick_ss, ipw_thick_path)

stress_dict = {'aluminum1': alu1_stress, 'aluminum2': alu2_stress, 'steel': stl_stress, 'plastic1':plas1_stress, 'plastic2': plas2_stress, 'iPod-Thin': ipw_thin_stress, 'iPod-Thick': ipw_thick_stress}


coffee_dict = {'countertop': [ [0,5,10,15,20,25,30,35,40,45,50,55], [204,136,123,114,105, 100,95,92,90,87, 84, 82]]}
coffee_dict['pot'] = [ [0,5,10,15,20,25,30,35,40,45,50,55], [204,139,125,113,105,98,94,90,88,86,84,82]]
coffee_dict['refrigerator'] = [ [0,5,10,15,20,25,30,35,40,45,50,55], [204,135,123,113,103,96,90,85,81,77,74,71]]

coffee_path = '/Users/jparks/Desktop/xyPlot/coffee_dict.json'
writeToJson(coffee_dict, coffee_path)

def tempDeltaList(thisGraph):
    retList = [0]
    for x in range(1,len(thisGraph[0])):
        thisDelta = (thisGraph[1][x] - thisGraph[1][0])
        retList.append(thisDelta)
    return retList

countertop_delta = tempDeltaList(coffee_dict['countertop'])
pot_delta = tempDeltaList(coffee_dict['pot'])
refrigerator_delta = tempDeltaList(coffee_dict['refrigerator'])

coffee_delta = {'countertop': [ [0,5,10,15,20,25,30,35,40,45,50,55], countertop_delta] }
coffee_delta['pot'] = [ [0,5,10,15,20,25,30,35,40,45,50,55], pot_delta] 
coffee_delta['refrigerator'] = [ [0,5,10,15,20,25,30,35,40,45,50,55], refrigerator_delta]

delta_path = '/Users/jparks/Desktop/xyPlot/coffee_delta.json'
writeToJson(coffee_delta, delta_path)

coffee_rolling = {'countertop': [[0,5,10,15,20,25,30,35,40,45,50,55], [0,-68,-13,-9,-9,-5,-5,-3,-2,-3,-3,-2] ] }
coffee_rolling['pot'] = [[0,5,10,15,20,25,30,35,40,45,50,55], [0,-65,-14,-12,-8,-7,-4,-4,-2,-2,-2,-2]]
coffee_rolling['refrigerator'] = [[0,5,10,15,20,25,30,35,40,45,50,55], [0,-69,-14,-10,-10,-7,-6,-5,-4,-4,-3,-3]]

coffee_rolling_path = '/Users/jparks/Desktop/xyPlot/coffee_rolling.json'
writeToJson(coffee_rolling, coffee_rolling_path)

water_dict = {'countertop': [[0,5,10,15,20,25,30,35,40,45,50,55], [40,41,40,39,40,41,41,42,43,44,47,48]] }
water_dict['pot'] = [[0,5,10,15,20,25,30,35,40,45,50,55], [41,36,35,35,38,37,44,49,52,54,56,58]] 
water_dict['refrigerator'] = [[0,5,10,15,20,25,30,35,40,45,50,55], [39,31,30,30,30,30,30,30,30,30,30,30]] 

water_dict_path = '/Users/jparks/Desktop/xyPlot/water_dict.json'
writeToJson(water_dict, water_dict_path)

water_ct_delta = tempDeltaList(water_dict['countertop'])
water_pot_delta = tempDeltaList(water_dict['pot'])
water_fridge_delta = tempDeltaList(water_dict['refrigerator'])

water_delta = {'countertop': [[0,5,10,15,20,25,30,35,40,45,50,55], water_ct_delta]}
water_delta['pot'] = [ [0,5,10,15,20,25,30,35,40,45,50,55], water_pot_delta]
water_delta['refrigerator'] = [ [0,5,10,15,20,25,30,35,40,45,50,55], water_fridge_delta]

water_delta_path = '/Users/jparks/Desktop/xyPlot/water_delta.json'
writeToJson(water_delta, water_delta_path)

water_rolling = {'countertop': [[0,5,10,15,20,25,30,35,40,45,50,55], [0,1,-1,-1,1,1,0,1,1,1,3,1]]}
water_rolling['pot'] = [[0,5,10,15,20,25,30,35,40,45,50,55], [0,-5,-1,0,3,-1,7,1,3,2,3,2]]
water_rolling['refrigerator'] = [[0,5,10,15,20,25,30,35,40,45,50,55], [0,-8,-1,0,0,0,0,0,0,0,0,0]]

water_rolling_path = '/Users/jparks/Desktop/xyPlot/water_rolling.json'
writeToJson(water_rolling, water_rolling_path)
