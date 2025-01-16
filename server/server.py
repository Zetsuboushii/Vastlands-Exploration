from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import get_dataframes
from main import _method_is_included
import plots  # your custom plot file
import matplotlib.pyplot as plt
import mpld3

app = Flask(__name__)
CORS(app)  # Allow cross-origin if your HTML is served elsewhere

# Global (cached) variables
DATA = None
PLOT_GEN_METHODS = None


def initialize_data():
    global DATA, PLOT_GEN_METHODS
    data, _ = get_dataframes(faergria_map_url="", faergria_map_data_skip=True, force=False)
    DATA = data
    all_plot_methods = dir(plots)
    PLOT_GEN_METHODS = list(filter(_method_is_included, all_plot_methods))


def render_plot_to_html(method_name, data):
    method = getattr(plots, method_name)
    generated_plot = method(**data)

    if isinstance(generated_plot, plt.Figure):
        html_plot = mpld3.fig_to_html(generated_plot)
        plt.close(generated_plot)
        return html_plot
    else:
        return f"Method '{method_name}' did not return a Matplotlib Figure."


@app.route('/plot', methods=['GET'])
def plot_endpoint():
    """
    Example endpoint: /plot?method_name=generate_scatter_plot
    It will call the matching function in plots.py and return the HTML result.
    """
    method_name = request.args.get('method_name', '')

    if not method_name:
        return "No 'method_name' parameter provided.", 400

    if method_name not in PLOT_GEN_METHODS:
        return (f"Method '{method_name}' is not found in "
                f"available methods: {PLOT_GEN_METHODS}"), 404

    html_output = render_plot_to_html(method_name, DATA)
    return html_output


@app.route('/available_plots', methods=['GET'])
def available_plots():
    """
    Returns a JSON list of all valid plot methods (PLOT_GEN_METHODS),
    so you can see which method_name values are allowed.
    """
    return jsonify(PLOT_GEN_METHODS)

def main():
    initialize_data()
    app.run(debug=True, port=5000)


if __name__ == '__main__':
    main()
