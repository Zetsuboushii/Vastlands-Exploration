import os
import click
from matplotlib import pyplot as plt
import decorators
import mongo_connector
import plots
import ui
from alive_progress import alive_bar
from utils import get_dataframes


def _method_is_included(name: str):
    return (name.startswith("create_") and (
            decorators.included_method_names is None or name in decorators.included_method_names))


def _method_is_in_api_included(name: str):
    return (name.startswith("create_") and (
            decorators.included_api_method_names is None or name in decorators.included_api_method_names))

@click.command("plot", help="Render the plots locally")
@click.option("--export-all", "-e", default=False, is_flag=True, help="Export all plots in the data/plots dir")
@click.option("--export-format", "--format", default="png", help="Export format for exported plots (e.g. png/svg)")
@click.option("--hide", "-h", default=False, is_flag=True, help="Hide plots when exporting")
@click.pass_context
def render_plots(ctx, export_all: bool, export_format: str, hide: bool):
    faergria_map_data_skip = ctx.obj['faergria_map_data_skip']  # Get the shared option
    data = ctx.obj["data"]
    plot_gen_methods = list(filter(_method_is_included, dir(plots)))
    faergria_map_dependend_methods = ["create_population_distribution_map"]
    with alive_bar(len(plot_gen_methods)) as bar:
        for method_name in plot_gen_methods:
            bar.text(method_name)
            if faergria_map_data_skip and method_name in faergria_map_dependend_methods:
                bar()
                continue
            method = getattr(plots, method_name)
            return_value = method(**data)
            if isinstance(return_value, plt.Figure):
                if (decorators.methods_to_export is None and export_all) or (decorators.methods_to_export is not None and method_name in decorators.methods_to_export):
                    filename = method_name.replace("create_", "") + "." + export_format
                    return_value.savefig(os.path.join("data", "plots", filename))
                if hide:
                    plt.close()
                else:
                    plt.show()
            bar()


@click.command("serve", help="Start the server that hosts the interactive UI")
@click.pass_context
def serve(ctx):
    faergria_map_data_skip = ctx.obj['faergria_map_data_skip']
    data = ctx.obj["data"]
    ui.run(data, faergria_map_data_skip)


@click.command("load", help="Load tierlists from local data/tierlists folder into mongodb")
@click.pass_context
def load_tierlists(ctx):
    mongo_connector.load_tierlists_into_db()


@click.group()
@click.option("--faergria-map-url", "-u", default="http://localhost:1338",
              help="URL to fetch the faergria map data from (default http://localhost:1338)")
@click.option("--faergria-map-data-skip", "-s", default=False, is_flag=True,
              help="Skip fetching data for the faergria map. Plots will be ignored (not rendered).")
@click.option("--force", "-f", default=False, is_flag=True,
              help="Force refresh data (bypass cache)")
@click.pass_context
def main(ctx, faergria_map_url: str, faergria_map_data_skip: bool, force: bool):
    ctx.ensure_object(dict)
    ctx.obj["faergria_map_url"] = faergria_map_url
    ctx.obj["faergria_map_data_skip"] = faergria_map_data_skip
    data, _ = get_dataframes(faergria_map_url, faergria_map_data_skip, force)
    ctx.obj["data"] = data


main.add_command(render_plots)
main.add_command(serve)
main.add_command(load_tierlists)

if __name__ == '__main__':
    main()
