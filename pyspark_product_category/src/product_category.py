from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def join_products_and_categories(products: DataFrame, categories: DataFrame, product_category: DataFrame) -> DataFrame:
    """
    Возвращает пары «Имя продукта – Имя категории» и продукты без категорий.
    """
    result = products.join(
        product_category,
        on="product_id",
        how="left"
    ).join(
        categories,
        on="category_id",
        how="left"
    ).select(
        col("product_name"),
        col("category_name")
    )

    return result
