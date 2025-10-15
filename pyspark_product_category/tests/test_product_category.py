import pytest
from pyspark.sql import SparkSession
from src.product_category import join_products_and_categories

@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder.master("local[*]").appName("test").getOrCreate()

def test_join_products_and_categories(spark):
    products = spark.createDataFrame([
        (1, "Phone"),
        (2, "Laptop"),
        (3, "Tablet"),
    ], ["product_id", "product_name"])

    categories = spark.createDataFrame([
        (10, "Electronics"),
        (20, "Office"),
    ], ["category_id", "category_name"])

    product_category = spark.createDataFrame([
        (1, 10),
        (2, 10),
        (2, 20),
    ], ["product_id", "category_id"])

    result = join_products_and_categories(products, categories, product_category)
    rows = [tuple(r) for r in result.collect()]

    assert ("Phone", "Electronics") in rows
    assert ("Laptop", "Electronics") in rows
    assert ("Laptop", "Office") in rows
    assert ("Tablet", None) in rows  # продукт без категории
