import click



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
def converter(  source_unit_arg, 
                target_unit_arg, 
                target_precision_arg
                ):
    """This program helps you to convert values from imperial units to metric and vice versa!"""
    print("Greetings to everbody! Welcome to the best converter in the world!")
    source_unit_val = click.prompt('Source unit', type=float)


    if (source_unit_arg == 'ft' and target_unit_arg == 'm'):
        print("Target unit value: ", end = "")
        print(round(source_unit_val / 3.281, target_precision_arg)) 
    elif (source_unit_arg == 'm' and target_unit_arg == 'ft'):
        print("Target unit value: ", end = "")
        print(round(source_unit_val * 3.281, target_precision_arg)) 




if __name__ == '__main__':
    converter()

