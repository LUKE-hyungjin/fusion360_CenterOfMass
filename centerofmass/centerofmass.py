#Author-Leehyungjin
#Description-change origin to center of mass

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        title = "Center of Mass"
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)
        root = design.rootComponent
        features = root.features
        allOccs = root.occurrences
        for occs in allOccs:
            prop = occs.getPhysicalProperties(adsk.fusion.CalculationAccuracy.VeryHighCalculationAccuracy)
            center_of_mass = [_/100.0 for _ in prop.centerOfMass.asArray()]
            name = occs.component.name
            ui.messageBox(f'component name : {name}\nx : {round(center_of_mass[0],5)}m, y : {round(center_of_mass[1],5)}m, z : {round(center_of_mass[2],5)}m\nx : {round(center_of_mass[0]*1000,5)}mm, y : {round(center_of_mass[1]*1000,5)}mm, z : {round(center_of_mass[2]*1000,5)}mm', title)
            try:
                for i in range(0,occs.component.bRepBodies.count):
                    selection = occs.component.bRepBodies.item(i)
                    bodies = adsk.core.ObjectCollection.create()
                    bodies.add(selection)
                    vector = adsk.core.Vector3D.create(-100*round(center_of_mass[0],5), -100*round(center_of_mass[1],5), -100*round(center_of_mass[2],5))
                    transform = adsk.core.Matrix3D.create()
                    transform.translation = vector
                    moveFeats = occs.component.features.moveFeatures
                    moveFeatureInput = moveFeats.createInput(bodies, transform)
                    moveFeats.add(moveFeatureInput)
            except:
                pass
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
