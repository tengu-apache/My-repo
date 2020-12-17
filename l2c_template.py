from jinja2 import Template

template = Template('''
                    set interfaces {{int_u}} description {{descr}}
                    set interfaces {{int_u}} encapsulation vlan-ccc
                    set interfaces {{int_u}} bandwidth {{bandwitch}}
                    set interfaces {{int_u}} vlan-id {{vlan_id}}
                    set interfaces {{int_u}} input-vlan-map pop
                    set interfaces {{int_u}} output-vlan-map push
                    set interfaces {{int_u}} family ccc filter input {{cos}}
                    set interfaces {{int_u}} family ccc policer input {{policer_in}}
                    set interfaces {{int_u}} family ccc policer output {{policer_out}}
                    set protocols l2circuit neighbor {{nei}} interface {{int_u}} virtual-circuit-id {{l2c_vc_id}}
                    set protocols l2circuit neighbor {{nei}} interface {{int_u}} description {{descr}}
                    set protocols l2circuit neighbor {{nei}} interface {{int_u}} mtu {{l2c_mtu}}
                    set protocols l2circuit neighbor {{nei}} interface {{int_u}} ignore-mtu-mismatch
                    ''')

l2c_template = {'int_u': 'ge-0/0/4.1043',
                                'descr': '"## L2C: RETN to Vladivostok ##"',
                                'bandwitch': '100m',
                                'vlan_id': '1043',
                                'cos': 'l2vpn-cos-bp',
                                'policer_in': 'lim100m',
                                'policer_out': 'lim100m',
                                'nei': '213.59.207.2',
                                'l2c_vc_id': '1043',
                                'l2c_descr': '"## L2C: RETN to Vladivostok ##"',
                                'l2c_mtu': '1540'}


#a = str(input('Enter interface type,number and unit: '))
#descr = input('Enter description: ')
#bandwitch = input('Enter bandwitch limit: ')
#vlan_id = input('Enter unit vlan-id: ')
#cos = input('Enter input CoS filter: ')
#policer_in = input('Enter policer input limit: ')
#policer_out = input('Enter policer output limit: ')
#nei = input('Enter neighbor PE IP: ')
#l2c_vc_id = input('Enter virtual-circuit-id: ')
#l2c_descr = input('Enter l2c protocol description: ')
#l2c_mtu = input('Enter MTU: ')

print(template.render(l2c_template))


