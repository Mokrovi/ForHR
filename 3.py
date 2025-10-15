from pyspark.sql import DataFrame


def getProducts(products: DataFrame, categories: DataFrame, relations: DataFrame) -> DataFrame:
    result = (products
              .join(relations, "product_name", "left")
              .join(categories, "category_name", "left")
              .select("product_name", "category_name"))
    return result
