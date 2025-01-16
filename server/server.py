from io import BytesIO
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import get_dataframes
from main import _method_is_in_api_included
import plots
import matplotlib.pyplot as plt
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
CORS(app)

DATA = None
PLOT_GEN_METHODS = None


def initialize_data():
    global DATA, PLOT_GEN_METHODS
    data, _ = get_dataframes(faergria_map_url="", faergria_map_data_skip=True, force=False)
    DATA = data
    all_plot_methods = dir(plots)
    PLOT_GEN_METHODS = list(filter(_method_is_in_api_included, all_plot_methods))
    print("initialize data")


def render_plot_to_html(method_name, data):
    method = getattr(plots, method_name)
    generated_plot = method(**data)

    if isinstance(generated_plot, plt.Figure):
        # Convert the Matplotlib figure to SVG
        svg_io = BytesIO()
        generated_plot.savefig(svg_io, format='svg', bbox_inches='tight')
        svg_io.seek(0)
        svg_data = svg_io.getvalue().decode('utf-8')
        plt.close(generated_plot)
        return svg_data  # Return the raw SVG
    else:
        return f"Method '{method_name}' did not return a Matplotlib Figure."


@app.route('/plot', methods=['GET'])
def plot_endpoint():
    """
    Endpoint to generate and return a plot in SVG format.
    Example: /plot?method_name=generate_scatter_plot
    """
    method_name = request.args.get('method_name', '')

    if not method_name:
        return "No 'method_name' parameter provided.", 400

    if method_name not in PLOT_GEN_METHODS:
        return f"Method '{method_name}' is not valid. Available methods: {PLOT_GEN_METHODS}", 404

    svg_output = render_plot_to_html(method_name, DATA)
    return svg_output  # Return raw SVG directly


@app.route('/available_plots', methods=['GET'])
def available_plots():
    """
    Returns a JSON list of all valid plot methods (PLOT_GEN_METHODS).
    """
    return jsonify(PLOT_GEN_METHODS)


def main():
    initialize_data()
    start_scheduler()
    app.run(debug=True, port=5000)


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(initialize_data, 'interval', hours=1)
    scheduler.start()

if __name__ == '__main__':
    main()
