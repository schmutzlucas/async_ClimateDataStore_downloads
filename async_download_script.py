import cdsapi
import asyncio


def background(f):
    def wrapped(*args):
        return asyncio.get_event_loop().run_in_executor(None, f, *args)

    return wrapped


@background
def cds_api_call(n, i, j, name):
    cdsapi.Client().retrieve(
        'projections-cmip6',
        {
            'temporal_resolution': 'Daily',
            'experiment': n,
            'level': 'single_levels',
            'variable': j,
            'model': i,
            'format': 'zip'
        },
        name)


# model_list = [
#     'gfdl_esm4',
#     'giss_e2_1_h',
#     'fio_esm_2_0',
#     'fgoals_f3_l',
#     'mpi_esm1_2_hr',
#     'cams_csm1_0',
#     'access_cm2',
#     'awi_cm_1_1_mr',
#     'inm_cm5_0',
#     'mpi_esm1_2_lr',
#     'miroc6',
#     'access_esm1_5',
#     'bcc_csm2_mr',
#     'kace_1_0_g',
#     'mcm_ua_1_0'
# ]
model_list = ['gfdl_esm4','giss_e2_1_h']

variable_list = [
    'near_surface_air_temperature',
    'daily_maximum_near_surface_air_temperature',
    'daily_minimum_near_surface_air_temperature',
    'precipitation',
    'sea_level_pressure',
    'near_surface_relative_humidity',
    'near_surface_specific_humidity',
    'near_surface_wind_speed'
]
# variable_list = [
#     'tas',
#     'near_surface_wind_speed'
# ]
# variable_list = ['pr', 'tas', 'huss']

scenario_list = [
    'historical',
    'ssp5_8_5'
]

for n in scenario_list:
    for i in model_list:
        for j in variable_list:
            name = j + '_Amon_' + i + '_' + n + '.zip'
            try:
                cds_api_call(n, i, j, name)
            finally:
                pass

print('download finished')
