import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:

    def validate_triangle(row):
        hypotenuse = max(row['x'], row['y'], row['z'])

        return row['x'] + row['y'] + row['z'] - (2 * hypotenuse) > 0

    return (
        triangle
        .assign(
            triangle=lambda df: df.apply(validate_triangle, axis=1).map({True: 'Yes', False: 'No'})
        )
    )
