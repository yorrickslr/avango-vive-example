#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import argparse

import avango
import avango.script
import avango.gua
import avango.daemon

#from lib.viewing_setup import ViewingSetup
from lib.vive_viewing_setup import ViveViewingSetup



def main():

    # Initialize scenegraph
    scenegraph = avango.gua.nodes.SceneGraph(Name = "scenegraph")

    # initialize viewing setup for vive [lib/vive_viewing_setup.py]
    viewingSetup = ViveViewingSetup(
        SCENEGRAPH = scenegraph
    )

    # create laoder for meshes
    meshloader = avango.gua.nodes.TriMeshLoader()

    # create floor object (plane.obj)
    floor = meshloader.create_geometry_from_file(
        "floor",
        "data/plane.obj",
        avango.gua.LoaderFlags.DEFAULTS
    )
    
    # create vive controller objects
    controller0 = meshloader.create_geometry_from_file(
        "controller0",
        "data/vive_controller.obj",
        avango.gua.LoaderFlags.LOAD_MATERIALS
    )

    controller1 = meshloader.create_geometry_from_file(
        "controller1",
        "data/vive_controller.obj",
        avango.gua.LoaderFlags.LOAD_MATERIALS
    )

    # create light object
    light = avango.gua.nodes.LightNode(
        Type=avango.gua.LightType.POINT,
        Name="light",
        Color=avango.gua.Color(1.0, 1.0, 1.0),
        Brightness=100.0,
        Transform=(avango.gua.make_trans_mat(0, 3, 0) *
                   avango.gua.make_scale_mat(5, 5, 5))
    )

    # connect with daemon
    device_service = avango.daemon.DeviceService()
    controller0_sensor = avango.daemon.nodes.DeviceSensor(
        DeviceService = device_service,
        Station="hmd-1"
    )

    controller0_transform = avango.gua.nodes.TransformNode(
        Name="controller0_transform", 
        Children=[controller0]
    )

    controller1_sensor = avango.daemon.nodes.DeviceSensor(
        DeviceService = device_service,
        Station="hmd-2"
    )

    controller1_transform = avango.gua.nodes.TransformNode(
        Name="controller1_transform", 
        Children=[controller1]
    )

    controller0_transform.Transform.connect_from(controller0_sensor.Matrix)
    controller1_transform.Transform.connect_from(controller1_sensor.Matrix)

    # append objects to scenegraph
    scenegraph.Root.value.Children.value.append(floor)
    scenegraph.Root.value.Children.value.append(light)
    scenegraph.Root.value.Children.value.append(controller0_transform)
    scenegraph.Root.value.Children.value.append(controller1_transform)

    # Triggers framewise evaluation of respective callback method
    # self.init_trigger = avango.script.nodes.Update(Callback = self.init_callback, Active = True)
       
    # trigger main loop and initialize GuaVE
    viewingSetup.run(locals(), globals())    

if __name__ == '__main__':
    main()
