# -*- coding: utf-8 -*-

import pprint

import bag
#from laygo import *
import laygo
import numpy as np
import yaml

lib_name = 'clk_dis_templates'
cell_name = 'clk_dis_viadel_htree'
impl_lib = 'clk_dis_generated'

params = dict(
    lch=16e-9,
    pw=4,
    nw=4,
    m_dff=2, 
	m_inv1=6, 
	m_inv2=8, 
	m_tgate=18, 
    n_pd=4,
	m_capsw=2, 
	num_bits=5,
    num_ways=8,
    unit_cell=2,
    device_intent='fast',
    )

load_from_file=True
yamlfile_spec="adc_sar_spec.yaml"
yamlfile_size="adc_sar_size.yaml"
if load_from_file==True:
    with open(yamlfile_spec, 'r') as stream:
        specdict = yaml.load(stream)
    with open(yamlfile_size, 'r') as stream:
        sizedict = yaml.load(stream)
    params['num_ways']=specdict['n_interleave']
    params['lch']=sizedict['lch']
    params['pw']=sizedict['pw']
    params['nw']=sizedict['nw']
    params['device_intent']=sizedict['device_intent']

print('creating BAG project')
prj = bag.BagProject()

# create design module and run design method.
print('designing module')
dsn = prj.create_design_module(lib_name, cell_name)
print('design parameters:\n%s' % pprint.pformat(params))
dsn.design(**params)

# implement the design
print('implementing design with library %s' % impl_lib)
dsn.implement_design(impl_lib, top_cell_name=cell_name, erase=True)
