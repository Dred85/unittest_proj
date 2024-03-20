def get_val(collection, key, default='git'):
    """"
    Функция возвращает значение из словаря по переданному ключу,
    если ключ существует.
    В ином случае возвращается значение default
    :collection: исходный словарь
    :key: ключ.
    :default: значение по ключу или по-умолчанию.
    """

    if key in collection:
        return collection[key]
    return default