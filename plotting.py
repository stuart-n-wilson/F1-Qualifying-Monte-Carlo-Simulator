import matplotlib.pyplot as plt
import seaborn as sns
import fastf1 as f1
from simulator import monte_carlo_qualifying


def f1_plot_theme():
    '''
    Sets style for matplotlib plots.
    '''
    plt.style.use("dark_background")
    plt.rcParams["figure.facecolor"] = "#1b1b1b"
    plt.rcParams["axes.facecolor"] = "#1b1b1b"
    plt.rcParams["grid.color"] = "#898989"
    plt.rcParams["axes.grid.axis"] = "y"
    plt.rcParams["text.color"] = "#898989"
    plt.rcParams["axes.labelcolor"] = "#d6d6d6"
    plt.rcParams["axes.titlecolor"] = "#f2f2f2"
    plt.rcParams["xtick.color"] = "#a4a4a4"
    plt.rcParams["ytick.color"] = "#a4a4a4"

def position_probability_plot(gp, year, pos=1, n=500):
    '''
    Takes in gp, year, qualifying position (default is pole) and number of simulations.
    Returns probability distribution fig for given position.
    '''
    
    f1.set_log_level('ERROR')

    if n < 1:
        raise ValueError('n must be a positive integer.')
    
    if year < 2018:
        raise ValueError('Only years 2018 onwards are supported.')


    session = f1.get_session(year, gp, 'Q')
    session.load()

    driver_colours = {
        driver: f"#{colour}"
        for driver, colour in session.results.set_index('Abbreviation')['TeamColor'].items()
    }

    df = monte_carlo_qualifying(gp, year, n)

    data = df[pos].reset_index()
    data.columns = ["Driver", "Probability"]
    data = data.sort_values("Probability", ascending=False)
    data['Colour'] = data['Driver'].map(driver_colours)


    f1_plot_theme()

    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.bar(
        data['Driver'],
        data['Probability'],
        color=data['Colour']
    )

    sns.despine(ax=ax)

    ax.set_title(
        f"{gp} {year} P{pos} Qualifying Probability Distribution - {n} simulations",
        fontsize=16,
        weight="bold",
        pad=15
    )
    ax.set_xlabel('Driver', fontsize=12, weight="bold", labelpad=15)
    ax.set_ylabel('Probability', fontsize=12, weight="bold", labelpad=15)
    ax.set_axisbelow(True)
    ax.grid(axis='y', color="#555555", alpha=0.3, linewidth=0.8)

    return fig

def expected_position(gp, year, driver, n=500):
    '''
    Input: gp, year, driver abbreviation, number of simulations.

    Output: Driver qualifying position probability distribution fig.
    '''
    f1.set_log_level('ERROR')

    if n < 1:
        raise ValueError('n must be a positive integer.')
    
    if year < 2018:
        raise ValueError('Only years 2018 onwards are supported.')
        

    session = f1.get_session(year, gp, 'Q')
    session.load()

    driver_colours = {
        driver: f"#{colour}"
        for driver, colour in session.results.set_index('Abbreviation')['TeamColor'].items()
    }

    df = monte_carlo_qualifying(gp, year, n)

    row = df.loc[driver]
    positions = sorted(row.index.astype(int))

    probabilities = row.values

    f1_plot_theme()

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.bar(
        positions,
        probabilities,
        color = driver_colours[driver]
    )

    sns.despine(ax=ax)

    ax.set_title(f"{gp} {year} {driver} Qualifying Position Probability Distribution - {n} simulations", fontsize=16, weight="bold", pad=15)
    ax.set_xlabel('Position', fontsize=12, weight="bold", labelpad=15)
    ax.set_ylabel('Probability', fontsize=12, weight="bold", labelpad=15)
    ax.set_xticks(positions)
    ax.set_axisbelow(True)
    ax.grid(axis='y', color="#555555", alpha=0.3, linewidth=0.8)

    return fig