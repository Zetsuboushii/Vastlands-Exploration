import os
import click
from matplotlib import pyplot as plt
import decorators
import plots
from alive_progress import alive_bar
from utils import get_dataframes

def _method_is_included(name: str):
    return (name.startswith("create_") and (
            decorators.included_method_names is None or name in decorators.included_method_names))


@click.command()
@click.option("--export-all", "-e", default=False, is_flag=True, help="Export all plots in the data/plots dir")
@click.option("--export-format", "--format", default="png", help="Export format for exported plots (e.g. png/svg)")
@click.option("--hide", "-h", default=False, is_flag=True, help="Hide plots when exporting")
def main(export_all: bool, export_format: str, hide: bool):
    data = get_dataframes()
    plot_gen_methods = list(filter(_method_is_included, dir(plots)))
    with alive_bar(len(plot_gen_methods)) as bar:
        for method_name in plot_gen_methods:
            method = getattr(plots, method_name)
            return_value = method(**data)
            if isinstance(return_value, plt.Figure):
                if (decorators.methods_to_export is None and export_all) or (
                        decorators.methods_to_export is not None and method_name in decorators.methods_to_export):
                    filename = method_name.replace("create_", "") + "." + export_format
                    return_value.savefig(os.path.join("data", "plots", filename))
                if hide:
                    plt.close()
                else:
                    plt.show()
            bar()

if __name__ == '__main__':
    main()
