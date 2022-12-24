import click
from utils import *

@click.command()
@click.option(  '--from',
                'source_unit_arg', 
#                default='ft', 
                help='What imperial unit to convert from', 
                required=True
)
@click.option(  '--to', 
                'target_unit_arg', 
#                default='m', 
                help='What metric unit to convert to', 
                required=True
)
@click.option(  '--precision', 
                'target_precision_arg', 
                default=2, 
                help='How many digits of the resulting value to show',
                type=int
)
@click.option(  '--log', 
                'print_log_enabled', 
                default=False,
                is_flag = True,
                show_default = True, 
                help='Should program log conversions',
                type=bool
)
def converter(  source_unit_arg, 
                target_unit_arg, 
                target_precision_arg,
                print_log_enabled
                ):
    """This program helps you to convert values from imperial units to metric and vice versa!"""
    

    result = 0.0
    universal_val = 0.0
    source_unit_valid = False
    target_unit_valid = False

    units_list = []
    units_list.append(inch_name_set)
    units_list.append(foot_name_set)
    units_list.append(yard_name_set)
    units_list.append(mile_name_set)
    units_list.append(millimetre_name_set)
    units_list.append(centimetre_name_set)
    units_list.append(metre_name_set)
    units_list.append(kilometre_name_set)

    for i, name_set in enumerate(units_list):
        if (source_unit_arg in name_set):
            source_unit_valid = True
        if (target_unit_arg in name_set):
            target_unit_valid = True
    
    if (not source_unit_valid):
        print("Invalid source unit!")
        return;

    if (not target_unit_valid):
        print("Invalid target unit!")
        return;

    print("Greetings to everbody! Welcome to the best converter in the world!")

    source_unit_val = click.prompt('Source unit', type=float)

    for i, name_set in enumerate(units_list):
        if (source_unit_arg in name_set):
            universal_val = source_unit_val * conversion_unit_list[i]
            break
    

    for i, name_set in enumerate(units_list):
        if (target_unit_arg in name_set):
            result = universal_val / conversion_unit_list[i]
            break 


    print("Target unit value: ", end = "")
    print(round(result, target_precision_arg)) 

    if (print_log_enabled):
        f = open("log.txt", "a")
        f.write("Converted " + str(source_unit_val) + " " + str(source_unit_arg) + " into " + str(round(result, target_precision_arg)) + " " + str(target_unit_arg) + "\n")
        f.close()

if __name__ == '__main__':
    converter()

