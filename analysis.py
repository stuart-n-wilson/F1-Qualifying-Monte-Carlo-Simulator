def real_results(session):
    """
    Input: session.

    Formats session results with abbreviation as index, and minimal columns.

    Output: real results dataframe.
    """

    return session.results.set_index('Abbreviation').rename(columns={'TeamName': 'Team', 'FullName':'Driver Name'}).rename_axis('Driver')[['Driver Name', 'Team', 'Position']]


def compare_grid(sim_grid, session):
    """
    Input: Simulated grid dataframe, and session.
    
    Calculates difference between simulated and true position.
    Indicates position gain in green with up arrow, and lost positions in red with down arrow.

    Output: Comparison dataframe.
    """

    # Join sim_grid and real session results on Abbreviation
    df = sim_grid.merge(real_results(session), left_index=True, right_index=True)

    df['Position change'] = df['Position'] - df['SimPosition']
    
    # Add arrows to indicate position change direction.
    df['Position change'] = df["Position change"].apply(lambda x: f"↑ {x:.0f}" if x > 0 else(f"↓ {abs(x):.0f}" if x < 0 else "0"))

    df = df.rename(columns={'SimPosition': 'Simulated position', 'Position': 'Real position'})

    # Reoder cols
    df = df[['Driver Name', 'Team', 'Simulated position', 'Real position', 'Position change']]

    # Display floats as int, and colour position changes green/red.
    df_coloured = df.style \
        .format({'Simulated position': '{:.0f}', 'Real position': '{:.0f}'}) \
        .map(
            lambda val: "color: green" if "↑" in val else ("color: red" if "↓" in val else ""),
            subset=["Position change"]
            )
    
    return df_coloured



    
